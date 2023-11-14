from pydash import *
from maps import functions


def define_env(env):
    tuples = []
    for fun in functions:
        title = fun.function.__name__
        description = fun.description
        example = fun.test_case
        result = eval(example)
        docstring = fun.function.__doc__
        tuples.append((title, description, example, result, docstring))
    env.variables.functions = tuples
