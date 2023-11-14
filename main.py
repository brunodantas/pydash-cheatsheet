from pydash import *
import maps


def define_env(env):
    function_map = maps.functions
    functions = []
    for fun in function_map:
        title = fun.function.__name__
        description = fun.description
        example = fun.test_case
        result = eval(example)
        docstring = fun.function.__doc__
        functions.append((title, description, example, result, docstring))
    env.variables.functions = functions
