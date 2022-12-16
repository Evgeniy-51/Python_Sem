from decimal import Decimal

def is_valid(expr: str) -> bool:
    allowable = ['-', '+', '=', '*', '/', '(', ')', ' ']
    return all([x.isdigit() or x in allowable for x in expr])

def run_calc(expr: str) -> str:
    def get_lst(expr):
        lst = []
        tmp = ''
        for i in range(len(expr)):
            if expr[i] in '+-*/()':
                lst.append(expr[i])
            elif expr[i].isdigit() or expr[i] == '.':
                if i == len(expr) - 1:
                    tmp += expr[i]
                    lst.append(Decimal(tmp))
                elif expr[i + 1].isdigit() or expr[i + 1] == '.':
                    tmp += expr[i]
                else:
                    tmp += expr[i]
                    lst.append(Decimal(tmp))
                    tmp = ''
            else:
                continue

        if lst[0] == '-':
            lst[0] = -1
            lst.insert(1, '*')

        return lst

    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def normalize_fraction(res):
        normalized = res.normalize()
        sign, digit, exponent = normalized.as_tuple()
        return normalized if exponent <= 0 else normalized.quantize(1)

    def run(op):
        if op == '+':
            a = n_stack.pop()
            b = n_stack.pop()
            n_stack.append(b + a)
        elif op == '-':
            a = n_stack.pop()
            b = n_stack.pop()
            n_stack.append(b - a)
        elif op == '*':
            a = n_stack.pop()
            b = n_stack.pop()
            n_stack.append(b * a)
        elif op == '/':
            a = n_stack.pop()
            b = n_stack.pop()
            if a != 0:
                n_stack.append(b / a)
            else:
                n_stack.clear()
                n_stack.append(False)
                return



    def calculator(exp):
        i = 0
        while i < len(exp):
            if is_number(str(exp[i])):
                n_stack.append(exp[i])

            elif exp[i] in ('+', '-'):
                if op_stack[-1] in (0, '('):
                    op_stack.append(exp[i])
                elif op_stack[-1] in ('*', '/', '-', '+'):
                    run(op_stack[-1])
                    op_stack.pop()
                    continue

            elif exp[i] in ('*', '/'):
                if op_stack[-1] in (0, '+', '-', '('):
                    op_stack.append(exp[i])
                elif op_stack[-1] in ('*', '/'):
                    run(op_stack[-1])
                    op_stack.pop()
                    continue

            elif exp[i] == '(':
                op_stack.append(exp[i])

            elif exp[i] == ')':
                if op_stack[-1] == '(':
                    op_stack.pop()
                else:
                    run(op_stack[-1])
                    op_stack.pop()
                    continue

            if i == len(exp) - 1 and op_stack:
                while op_stack:
                    run(op_stack[-1])
                    op_stack.pop()
            i += 1

    n_stack = [0]
    op_stack = [0]
    ex_lst = get_lst(expr)
    calculator(ex_lst)
    return str(normalize_fraction(n_stack[-1])) if n_stack[-1] else "Ошибка, деление на ноль!"
