
from lightautoml.automl.presets.tabular_presets import TabularAutoML
from lightautoml.tasks import Task
import dill
import pandas as pd
# print(test_pred)
# import joblib
with open('model.pkl', 'rb') as f:
    automl = dill.load(f) #, pickle_module=dill)


text_json = {'v_g': 2.0, 'ev_g': 2, 'iv_g': 3, 'length': 4, 'volume': 6.339850002884625, 'calculated_length': 2.0, 'difficulty': 0.5, 'intelligence': 2.0, 'effort': 3.1699250014423126, 'bugs': 0.002113283334294875, 'time': 0.17610694452457293, 'h1': 1, 'h2': 2, 'N1': 2, 'N2': 2, 'LOC': 81, 'SLOC': 61, 'single_comments': 10, 'blank': 10, 'multi': 0, 'count_branch': 0}
text_json['loc'] = text_json['LOC']
text_json['v(g)'] = text_json['v_g']
text_json['ev(g)'] = text_json['ev_g']
text_json['iv(g)'] = text_json['iv_g']
text_json['n'] = text_json['length']
text_json['v'] = text_json['volume']
text_json['l'] = text_json['calculated_length']
text_json['d'] = text_json['difficulty']
text_json['i'] = text_json['intelligence']
text_json['e'] = text_json['effort']
text_json['b'] = text_json['bugs']
text_json['t'] = text_json['time']
text_json['lOCode'] = text_json['SLOC']
text_json['lOComment'] = text_json['single_comments']
text_json['lOBlank'] = text_json['blank']
text_json['locCodeAndComment'] = text_json['multi']
text_json['uniq_Op'] = text_json['h1']
text_json['uniq_Opnd'] = text_json['h2']
text_json['total_Op'] = text_json['N1']
text_json['total_Opnd'] = text_json['N2']
text_json['branchCount'] = text_json['count_branch']

del text_json['LOC']
del text_json['v_g']
del text_json['ev_g']
del text_json['iv_g']
del text_json['length']
del text_json['volume']
del text_json['calculated_length']
del text_json['difficulty']
del text_json['intelligence']
del text_json['effort']
del text_json['bugs']
del text_json['time']
del text_json['SLOC']
del text_json['single_comments']
del text_json['blank']
del text_json['multi']
del text_json['h1']
del text_json['h2']
del text_json['N1']
del text_json['N2']
del text_json['count_branch']

# v(g)
# ev(g)
# iv(g)
# n
# v
# l
# d
# i
# e
# b
# t
# lOCode
# lOComment
# lOBlank
# locCodeAndComment
# uniq_Op
# uniq_Opnd
# total_Op
# total_Opnd
# branchCount

for k, v in text_json.items():
  text_json[k] = [v]
text_json_pd = pd.DataFrame(text_json)
text_json_pd
pred = automl.predict(text_json_pd)
pred = pred.to_numpy()

print( float(str(pred[0, 'WeightedBlend_0'])) )
# print( pred['WeightedBlend_0', 0] )
# np.array(pred,np.float32)
# for i in pred:
#     print(i)
#     np.array(i,np.float32)
#     for j in i:
#         print(np.array(j,np.float32))
print( pred._hstack )
print( pred[0].features )
print( type(pred) )
# n1 = np.array(pred)
# print(n1)
# print( pred.dtype )
# print( float(str(pred[0][0])) ) #.astype(float) )

exit()
import analyze_code as ac

with open("mainwindow.py", 'r', encoding="utf-8") as f:
    code = f.read()
# code = '''print("Hello world")
# '''

print( ac.analyzeCode(code)['loc'] )


# import radon.complexity as rс
# print( rс.cc_visit(code) )
# print( ac.analyzeCode(code) )

exit()
listFilesAndTexts = {}
fileName = 'C:/dilpom/analyze_code.py'
listFilesAndTexts[str(fileName)]={'123':123}
print(listFilesAndTexts[str(fileName)]['123'])
# тонкости листов в Питоне

exit()

import analyze_code as ac

with open("C:/dilpom/analyze_code.py", 'r', encoding="utf-8") as f:
    code = f.read()

print( ac.analyzeCode(code) )

# def countComplexity(obj1, count, modificator = 1):
#     if (type(obj1[4]) != 'list'):
#     # if (obj1[4] == True):
#         return count + modificator*obj1[-1]
#     else:
#         count += 2
#         count += obj1[-1]
#         for cc in obj1[4]:
#             # print('cc in def:', cc)
#             count = countComplexity(cc, count, modificator = -1)
#     return count

# import radon.complexity as rс
# print( rс.cc_visit(code) )
# count = 0

# for cc in rс.cc_visit(code):
#     count = countComplexity(cc, count)
#     print(cc)
#     print(count)
    
# print( 'count' )
# print( count )
# print( len( rс.cc_visit(code) ) )
# print( count/len( rс.cc_visit(code) ) )
# cyclo_cyclo = rс.cc_visit(code)
# for k in cyclo_cyclo:
#     print( k )  # 2. Цикломатическая 

# import radon.raw as rw
# raw_raw = rw.analyze(code)
# for k in raw_raw:
#     print( k )  # 2. Рооооу

# import radon.metrics as rm
# hola_hola = rm.h_visit(code)
# for k in hola_hola[0]:
#     print( k )  # 1. Хольстееед


exit()

import radon.metrics as rm
import radon.complexity as rc


with open("C:\minifi\minifi_Sec_Elektra_Energia_v1_1.yml", 'r', encoding="utf-8") as f:
    # mainwindow.py
    code = f.read()

# print( rm.h_visit(code) )
# print( rm.h_visit_ast(rm.h_visit(code)) )
print( rc.cc_visit(code) )
print( rm.mi_parameters(code) )
# print( rc.cc_visit_ast(rc.cc_visit(code)) )

exit()

# Дока по radon
# proga (top): https://radon.readthedocs.io/en/latest/api.html#module-radon.metrics
# cli        : https://radon.readthedocs.io/en/latest/commandline.html
# чел. опис. : https://habr.com/ru/companies/intel/articles/106082/

import dis
import mainwindow
from code_info import *



with open("C:\minifi\minifi_Sec_Elektra_Energia_v1_1.yml", 'r', encoding="utf-8") as f:
    code = f.read()


# print( dis.show_code(code) ) #, file=f) #, depth=0)
# к dis'у
# https://stackoverflow.com/questions/31989893/how-to-fully-disassemble-python-source
# https://pythobyte.com/dis-50619/

bytecode = dis.Bytecode(code)
# dis.show_code(bytecode.codeobj) #it works

opcode_list = []
for instr in bytecode:
    # print(instr.opname)
    opcode_list.append(instr.opname)
print( opcode_list )

# opcode_list = dis.code_info(code) #it works
# # opcode_list = dis.get_instructions(mainwindow)
# with open("opcode_list.txt", 'w', encoding="utf-8") as f:
#     opcode_list = dis.dis(mainwindow, file=f) #, depth=0)


print( count_branch(opcode_list) )

exit()

from code_info import count_branch_in_model
import mainwindow

# with open("mainwindow.py", 'r', encoding="utf-8") as f:
#     code = f.read()

print( count_branch_in_model( mainwindow ) )#, module_list=['mainwindow'] ) )

exit()

# https://webdevblog.ru/uproshhenie-koda-prilozhenij-python-s-pomoshhju-refaktoringa-chast-1/
# обзор инструмента wily для ci/cd

import radon.complexity as rc

with open("mainwindow.py", 'r', encoding="utf-8") as f:
    code = f.read()

print( rc.cc_rank(2.5) )
# как считается average и analyzed cc: 
# https://programtalk.com/python-examples/radon.complexity.cc_rank/

exit()

#импортируем нужный модуль
from staticfg import CFGBuilder
#создаем объект класса CFGBuilder
cfg = CFGBuilder().build_from_file('mainwindow','mainwindow.py')
#сохраняем визуализацию
cfg.build_visual('mainwindow','png')

