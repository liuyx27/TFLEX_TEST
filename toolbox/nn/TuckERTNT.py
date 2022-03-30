import numpy as np
import torch
import torch.nn as nn


class TuckERTNT(nn.Module):
    def __init__(self, d, de, dr, dt, device="cpu", input_dropout=0., hidden_dropout1=0., hidden_dropout2=0., **kwargs):
        super(TuckERTNT, self).__init__()

        self.device = device

        # Embeddings dimensionality
        self.de = de
        self.dr = dr
        self.dt = dt

        # Data dimensionality
        self.ne = len(d.entities)
        self.nr = len(d.relations)
        self.nt = len(d.time)

        # Embedding matrices
        self.E = nn.Embedding(self.ne, de)
        self.R = nn.Embedding(self.nr, dr)
        self.T = nn.Embedding(self.nt, dt)

        # Core tensor
        self.W = nn.Parameter(torch.tensor(np.random.uniform(-0.1, 0.1, (dr, de, dt, de)), dtype=torch.float, device=self.device, requires_grad=True))

        # "Special" Layers
        self.input_dropout = nn.Dropout(input_dropout)
        self.hidden_dropout1 = nn.Dropout(hidden_dropout1)
        self.hidden_dropout2 = nn.Dropout(hidden_dropout2)
        self.loss = nn.BCELoss()

        self.bne = nn.BatchNorm1d(de)

    def init(self):
        nn.init.xavier_normal_(self.E.weight.data)
        nn.init.xavier_normal_(self.R.weight.data)
        nn.init.xavier_normal_(self.T.weight.data)

    def forward(self, e1_idx, r_idx, t_idx):
        ### Temporal part
        # Mode 1 product with entity vector
        e1 = self.E(e1_idx)
        x = self.bne(e1)
        x = self.input_dropout(x)
        x = e1
        x = x.view(-1, 1, self.de)

        # Mode 2 product with relation vector
        r = self.R(r_idx)
        W_mat = torch.mm(r, self.W.view(r.size(1), -1))
        W_mat = W_mat.view(-1, self.de, self.de * self.dt)
        x = torch.bmm(x, W_mat)

        # Mode 4 product with entity matrix 
        x = x.view(-1, self.de)
        x = torch.mm(x, self.E.weight.transpose(1, 0))

        # Mode 3 product with time vector
        t = self.T(t_idx)
        xt = x.view(-1, self.dt, self.ne)
        xt = torch.bmm(t.view(*t.shape, -1), xt)
        xt = xt.view(-1, self.ne)

        ### Non temporal part
        # mode 3 product with identity matrix
        x = x.view(-1, self.dt)
        x = torch.mm(x, torch.ones(self.dt).view(self.dt, 1))
        x = x.view(-1, self.ne)

        # Sum of the 2 models
        x = x + xt

        # Turn results into "probabilities"
        pred = torch.sigmoid(x)
        return pred
