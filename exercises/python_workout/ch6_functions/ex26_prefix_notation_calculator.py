# Problem: using the operator module, calculate a prefix math string.  Limit 2 numbers and the six basic operators.
#          Can use if statements or defining our own functions.  Function dispatch table (well... dict) is nicer.
# Input: math string in prefix notation
# Output: number result

import operator


def prefix_calculation(math_equation: str):
    """ Calculate the result of the input prefix math string """

    operator_dispatch = {'+': operator.add,
                         '-': operator.sub,
                         '*': operator.mul,
                         '/': operator.truediv,
                         '**': operator.pow,
                         '%': operator.mod}

    operation, left_side, right_side = math_equation.split(maxsplit=2)
    left_side = int(left_side)
    right_side = int(right_side)

    return operator_dispatch[operation](left_side, right_side)


print(prefix_calculation('+ 1 2'))
