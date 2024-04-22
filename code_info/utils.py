from opcode import *
import inspect


def disassemble(co):
    """ Disassemble a code object.
        And return opcode list.
        modify from dis.disassemble

        >>> def test(a):
        ...    a += 1
        ...    return a


        >>> disassemble(test.__code__)
        [['LOAD_FAST', 0, 'a'], ['LOAD_CONST', 1, 1], ['INPLACE_ADD'], ['STORE_FAST', 0, 'a'], ['LOAD_FAST', 0, 'a'], ['RETURN_VALUE']]
    """
    code = co.co_code
    # code = co.co_code_adaptive
    n = len(code)
    i = -1
    extended_arg = 0
    statement_list = list()
    free = None
    while i+1 +1 < n: #i+1 надо делать после...
        c = code[i]
        op = c #ord(c)
        statement = list()
        statement.append(opname[op])
        i += 1
        if op >= HAVE_ARGUMENT:
            # oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
            oparg = code[i] + code[i+1]*256 + extended_arg
            extended_arg = 0
            i += 2
            if op == EXTENDED_ARG:
                extended_arg = oparg*65536
            # print(oparg)
            statement.append(oparg)
            try:
                if op in hasconst:
                    statement.append(co.co_consts[oparg])
                elif op in hasname:
                    statement.append(co.co_names[oparg])
                elif op in hasjrel:
                    statement.append(i + oparg)
                elif op in haslocal:
                    statement.append(co.co_varnames[oparg])
                elif op in hascompare:
                    statement.append(cmp_op[oparg])
                elif op in hasfree:
                    if free is None:
                        free = co.co_cellvars + co.co_freevars
                    statement.append(free[oparg])
            except Exception as e:
                # print(e)
                pass

        statement_list.append(statement)
    return statement_list


def generate_space(num):
    """ generate_space
        And return opcode list.

    """
    return ' ' * num


def is_module_or_class(obj):
    ''' return true if obj is module or class.
    '''
    return inspect.isclass(obj) or inspect.ismodule(obj)


if __name__ == '__main__':
    import doctest
    doctest.testmod()