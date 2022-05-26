import complex
import rational
import ui

ans = 'y'
while ans != 'n':
    x = ui.get_x()
    op = ui.get_op()
    y = ui.get_y()

    if op == '*':
        if x[-1] == 'j' or y[-1] == 'j':
            res = complex.mult(x, y)
        else:
            res = rational.mult(x, y)
    elif op == '/':
        if x[-1] == 'j' or y[-1] == 'j':
            res = complex.div(x, y)
        else:
            res = rational.div(x, y)
    elif op == '+':
        if x[-1] == 'j' or y[-1] == 'j':
            res = complex.sum(x, y)
        else:
            res = rational.sum(x, y)
    elif op == '-':
        if x[-1] == 'j' or y[-1] == 'j':
            res = complex.sub(x, y)
        else:
            res = rational.sub(x, y)

    ui.print_result(res)
    ans = ui.get_ans()
