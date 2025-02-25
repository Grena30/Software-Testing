from behave import given, when, then
from factorial import factorial

@given('the number {num:d}')
def given_number(context, num):
    context.num = num

@when('I calculate the factorial')
def when_calculate_factorial(context):
    context.result = factorial(context.num)

@then('the result should be {expected:d}')
def then_check_result(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"
