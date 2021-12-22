from main import *
from behave import *


@given('I have {a}*x**4 + {b}*x**2 + {c} = 0')
def step_impl(context, a, b, c):
    context.a = float(a)
    context.b = float(b)
    context.c = float(c)


@when('I solve the equation')
def step_impl(context):
    context.roots = check_coef(context.a, context.b, context.c)


@then('I expect 3 roots: {x_1}, {x_2}, {x_3}')
def step_impl(context, x_1, x_2, x_3):
    res = [float(x_1), float(x_2), float(x_3)]
    assert context.roots == res
