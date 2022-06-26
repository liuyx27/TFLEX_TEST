"""
@author: lxy
@email:
@date: 2022/3/26
@description: null
"""
from pathlib import Path

from toolbox.utils.LaTeXSotre import result_dict_to_dataframe, save_dataframe_to_latex_by_path

result = {'Test    ': ['avg', 'Pe', 'Pe2', 'Pe3', 'Pe_Pt', 'Pe_aPt', 'Pe_at2i', 'Pe_bPt', 'Pe_bt2i', 'Pe_e2i', 'Pe_e2i_Pe_NPe', 'Pe_e2u', 'Pe_e2u_DM', 'Pe_nPt', 'Pe_nt2i', 'Pe_t2i', 'Pe_t2i_PtPe_NPt',
                       'Pe_t2u', 'Pe_t2u_DM', 'Pt', 'Pt_lPe', 'Pt_le2i', 'Pt_rPe', 'Pt_re2i', 'between', 'e2i', 'e2i_N', 'e2i_NPe', 'e2i_Pe', 'e2i_PeN', 'e2u', 'e2u_DM', 'e3i', 'e3i_N', 't2i',
                       't2i_N', 't2i_NPt', 't2i_Pe', 't2i_PtN', 't2u', 't2u_DM', 't3i', 't3i_N'],
          'num_queries': [160713, 8848, 4037, 4083, 3638, 4733, 5338, 4565, 5386, 2913, 3012, 2913, 2913, 3108, 5308, 2913, 3127, 2913, 2913, 7419, 5608, 3466, 3621, 3485, 2913, 3655, 2975, 3192,
                          2913, 3031, 2913, 2913, 3023, 2914, 6631, 3328,
                          5464, 2913, 3609, 2913, 2913, 3296, 2944],
          'MRR': [0.0030855130773222834, 0.0002737671311479062, 0.0003708905423991382, 0.0003859089338220656, 0.00036551355151459575, 0.0002949332119897008, 0.0002571190125308931,
                  0.00033468464971520007, 0.00023883258108980954, 0.00046915002167224884, 0.0004722067678812891, 0.0005176254198886454, 0.0005233862902969122, 0.00038025446701794863,
                  0.0002626487985253334, 1.6274422875994787e-07, 0.0004053183947689831, 0.0004123782564420253, 0.00042002490954473615, 0.004794704727828503, 0.004948691464960575,
                  0.0073967971839010715, 0.008296769112348557, 0.007632172666490078, 0.005165413022041321,
                  0.0004925596294924617, 0.0010105501860380173, 0.0026386240497231483, 0.0004946666886098683, 0.0004992787726223469, 0.00039558319258503616, 0.0004454601148609072,
                  0.0006029927753843367, 0.000704441627021879, 0.005021926015615463, 0.009879080578684807, 0.004737935960292816, 0.008284383453428745, 0.00725273322314024, 0.011514361947774887,
                  0.011547524482011795, 0.008881663903594017, 0.010568428784608841],
          'hits@1': [0.0003107704615104012, 0.0, 0.0, 0.00012245897960383445, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0005147996125742793, 0.0016800324665382504, 0.0009917200077325106, 0.0009028024505823851, 0.0006216655601747334, 0.0, 0.0, 0.00033613445702940226,
                     0.001409774413332343, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001017838018015027,
                     0.00028485135408118367, 0.0013109270948916674, 0.00045771829900331795, 0.0012267435668036342, 0.0003718961088452488, 0.0003718961088452488, 0.0007517530466429889,
                     0.0006793478387407959],
          'hits@3': [0.0016568293023218367, 0.0, 0.0, 0.00012245897960383445, 0.0, 0.0, 0.0, 3.6509674828266725e-05, 3.094442581641488e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 5.337854599929415e-05, 0.0, 0.0,
                     0.0, 0.0, 0.0019660284742712975, 0.0034000230953097343, 0.00218477426096797, 0.0036314032040536404, 0.001432402990758419, 9.614485315978527e-05, 0.0, 0.00033613445702940226,
                     0.0031328320037573576, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0006863417802378535, 0.003412781748920679, 0.007499684579670429, 0.004105699714273214, 0.002288591116666794,
                     0.001549388631246984, 0.01177235133945942, 0.01177235133945942, 0.006849703378975391, 0.0032269021030515432],
          'hits@10': [0.00667382614561315, 0.0003955696302000433, 0.0, 0.00012245897960383445, 9.162543574348092e-05, 0.00027818858507089317, 0.0005073685315437615, 0.0009085930068977177,
                      0.0004713130765594542, 0.0, 0.00016600266098976135, 0.0, 0.0, 0.0003217503253836185, 5.337854599929415e-05, 0.0, 0.0, 0.0, 0.00011442957475082949, 0.009499570354819298,
                      0.012788079679012299, 0.020120922476053238, 0.020416593179106712, 0.018762867897748947, 0.001368302502669394, 0.0, 0.0015126049984246492, 0.00558688398450613, 0.0,
                      0.0007698229746893048, 0.0, 0.0, 0.00016539861098863184, 0.0008007321739569306, 0.010361090302467346, 0.026688721030950546, 0.014097942970693111, 0.013073577545583248,
                      0.018806764855980873, 0.03283106908202171, 0.03283106908202171, 0.017196429893374443, 0.019191576167941093]}
df = result_dict_to_dataframe(result)
print(df)
# save_dataframe_to_latex(df, "a.tex")
save_dataframe_to_latex_by_path(df, Path(".") / "a.tex")
