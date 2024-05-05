import radon.metrics as rm
import radon.complexity as rc
import radon.raw as rw
import dis
from code_info import *

def countComplexity(obj1, count, modificator = 1):
    if (type(obj1[4]) != type([])):
        return count + modificator*obj1[-1]
    else:
        count += 2
        count += obj1[-1]
        for cc in obj1[4]:
            # print('cc in def:', cc)
            count = countComplexity(cc, count, modificator = -1)
    return count

def analyzeCode(text_code):
    returnedJSON = {}

    # print( rc.cc_visit(text_code) )                 # 3. Цикломатик комплексити
    count = 0
    len_cc = 0
    for cc in rc.cc_visit(text_code):
        count = countComplexity(cc, count)
        len_cc += 1
    if len_cc == 0:
        returnedJSON['v_g'] =           0 # 2.
    else:
        returnedJSON['v_g'] =           count/len_cc # 2.
    returnedJSON['ev_g'] =              2 # 3.
    returnedJSON['iv_g'] =              3 # 4.

    # print( rm.mi_parameters(text_code) )            # Совсем не нужно

    # print( rm.h_visit(text_code) )  # 1. Хольстееед
    hola_hola = rm.h_visit(text_code)
    # Программирование для radon-6.0.1
    returnedJSON['length'] =            hola_hola[0][5] # 5.
    returnedJSON['volume'] =            hola_hola[0][7] # 6.
    returnedJSON['calculated_length'] = hola_hola[0][6] # 7.
    returnedJSON['difficulty'] =        hola_hola[0][8] # 8.
    if returnedJSON['difficulty'] == 0:
        returnedJSON['intelligence'] =  0 # 9. 1/difficulty
    else:
        returnedJSON['intelligence'] =  1/hola_hola[0][8] # 9. 1/difficulty
    returnedJSON['effort'] =            hola_hola[0][9] # 10.
    returnedJSON['bugs'] =              hola_hola[0][11] # 11.
    returnedJSON['time'] =              hola_hola[0][10] # 12.
    returnedJSON['h1'] =                hola_hola[0][0] # 17.
    returnedJSON['h2'] =                hola_hola[0][1] # 18.
    returnedJSON['N1'] =                hola_hola[0][2] # 19.
    returnedJSON['N2'] =                hola_hola[0][3] # 20.

    # print( rw.analyze(text_code) )                  # 2. Роу (строка)
    raw_raw = rw.analyze(text_code)
    # Программирование для radon-6.0.1
    returnedJSON['LOC'] =               raw_raw[0] # 1.
    returnedJSON['SLOC'] =              raw_raw[2] # 13.
    returnedJSON['single_comments'] =   raw_raw[6] # 14.
    returnedJSON['blank'] =             raw_raw[5] # 15.
    returnedJSON['multi'] =             raw_raw[4] # 16.



    # ######### 4*. Количество брэнчЕй
    bytecode = dis.Bytecode(text_code)

    opcode_list = []
    for instr in bytecode:
        # print(instr.opname)
        opcode_list.append(instr.opname)
    # print( opcode_list )

    # print( count_branch(opcode_list) )
    returnedJSON['count_branch'] =      count_branch(opcode_list) # 21.
    print( returnedJSON )

    return returnedJSON