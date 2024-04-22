
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

