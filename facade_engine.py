class A(object):
    def __init__(self, name):
        print(name)
        self.name = name


class B(object):
    def __init__(self, name):
        print(name)
        self.name = name


class C(object):
    def __init__(self, name):
        print(name)
        self.name = name


class D(object):
    def __init__(self, name):
        print(name)
        self.name = name


class E(object):
    def __init__(self, name):
        print(name)
        self.name = name


class RunFunction(object):
    def __init__(self):
        self.functions_list = []
        self.functions_list.append(self.function_a)
        self.functions_list.append(self.function_b)
        self.functions_list.append(self.function_c)
        self.functions_list.append(self.function_d)
        self.functions_list.append(self.function_e)

        self.function_dict = dict()
        self.function_dict['a'] = self.function_a
        self.function_dict['b'] = self.function_b
        self.function_dict['c'] = self.function_c
        self.function_dict['d'] = self.function_d
        self.function_dict['e'] = self.function_e

        self.name_dict = dict()
        self.name_dict['a'] = 'A("Class A")'
        self.name_dict['b'] = 'B("Class B")'
        self.name_dict['c'] = 'C("Class C")'
        self.name_dict['d'] = 'D("Class D")'
        self.name_dict['e'] = 'E("Class E")'

    @staticmethod
    def run(func):
        func()

    @staticmethod
    def function_a():
        print('Function A is called.')
        a = A('Name = Class A')

    @staticmethod
    def function_b():
        print('Function B is called.')
        b = B('Name = Class B')

    @staticmethod
    def function_c():
        print('Function C is called.')
        c = C('Name = Class C')

    @staticmethod
    def function_d():
        print('Function D is called.')
        d = D('Name = Class D')

    @staticmethod
    def function_e():
        print('Function E is called.')
        e = E('Name = Class E')

    def run_function_1(self, func_id: str):
        if func_id == 'a':
            self.run(self.functions_list[0])
        elif func_id == 'b':
            self.run(self.functions_list[1])
        elif func_id == 'c':
            self.run(self.functions_list[2])
        elif func_id == 'd':
            self.run(self.functions_list[3])
        elif func_id == 'e':
            self.run(self.functions_list[4])
        else:
            print('Function with ID ' + func_id + ' does not exist.')

    def run_function_2(self, func_id: str):
        try:
            _func = self.function_dict[func_id]
            self.run(_func)
        except KeyError:
            print('Function with ID ' + func_id + ' does not exist.')

    def eval_function(self, func_id: str):
        try:
            _c = eval(self.name_dict[func_id])
        except KeyError:
            print('Function with ID ' + func_id + ' does not exist.')


if __name__ == '__main__':
    rf = RunFunction()
    print('*** Function_1 ***')
    rf.run_function_1('a')
    rf.run_function_1('b')
    rf.run_function_1('c')
    rf.run_function_1('d')
    rf.run_function_1('e')
    rf.run_function_1('f')

    print('*** Function_2 ***')
    rf.run_function_2('a')
    rf.run_function_2('b')
    rf.run_function_2('c')
    rf.run_function_2('d')
    rf.run_function_2('e')
    rf.run_function_2('f')

    print('*** eval_function ***')
    rf.eval_function('a')
    rf.eval_function('b')
    rf.eval_function('c')
    rf.eval_function('d')
    rf.eval_function('e')
    rf.eval_function('f')
