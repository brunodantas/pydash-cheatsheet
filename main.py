from dataclasses import dataclass
from typing import Callable

from pydash import *


@dataclass
class Map:
    function: Callable
    description: str
    test_case: str


functions = [
    Map(
        get,
        "Easy access to properties at any level",
        "get({'a': {'b': 1}, 'c': 2}, 'a.b')",
    ),
    Map(
        set_,
        "Set property at any level\n\nVariants: set_with",
        "set_({'a': 2}, 'b.c', 3)",
    ),
    Map(
        has,
        "Check if property exists at any level",
        "has({'a': {'b': 1}, 'c': 2}, 'a.d')",
    ),
    Map(
        find,
        "Find first element that passes a criterion function\n\nVariants: find_index, find_last, find_last_index",
        "find([1, 2, 3, 4], lambda n: n > 2)",
    ),
    Map(
        index_of,
        "Find the index of an element\n\nVariants: last_index_of",
        "index_of([1, 2, 3, 2], 2)",
    ),
    Map(
        pluck,
        "Retrieve property values from collections",
        "pluck([{'a': 1}, {'a': 2, 'b': 3}, {'a': 4}, {}], 'a')",
    ),
    Map(
        pull,
        "Removes specific elements from array\n\nVariants: pull_all_by, pull_all_with, pull_at, remove, take, without",
        "pull([1, 2, 3, 4, 3, 2], 2, 3)",
    ),
    Map(
        rename_keys,
        "New dict with renamed keys",
        "rename_keys({'a': 1, 'b': 2}, {'a': 'A', 'b': 'B'})",
    ),
    Map(
        flatten,
        "Flatten an array by one level\n\nVariants: flatten_deep, flatten_depth",
        "flatten([1, [2, [3, [4]], 5]])",
    ),
    Map(count_by, "Count occurences of values in sequence", "count_by('mississipi')"),
    Map(
        camel_case,
        "Text to camel case\n\nVariants: kebab_case, human_case, snake_case, slugify etc",
        "camel_case('Foo Bar')",
    ),
    Map(
        sample_size,
        "Retrieve random sample of elements",
        "sample_size([1, 2, 3, 4], 2)",
    ),
    Map(
        chunk,
        "Separate elements into chunks",
        "chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)",
    ),
    Map(compact, "Take falsey values out", "compact([0, 1, False, 2, '', 3])"),
    Map(
        difference,
        "Return elements that are in the first array but not in the others\n\nVariants: difference_by, difference_with",
        "difference([1, 2], [2, 3], [4, 5])",
    ),
    Map(
        take_while,
        "Conditional slice\n\nVariants: drop_right_while, drop_while, drop_right_while",
        "take_while([1, 2, 3, 4], lambda n: n < 3)",
    ),
    Map(duplicates, "Returns duplicate values", "duplicates([1, 2, 3, 4, 2, 3])"),
    Map(
        attempt, "Return function result or caught exception", "attempt(lambda: 1 / 0)"
    ),
    Map(memoize, "Cache function results", "memoize(sum).cache"),
    Map(
        debounce,
        "Delay execution of a function\n\nVariants: delay",
        "debounce(lambda: print('Hello'), 1000)()",
    ),
    Map(
        curry,
        "Partial application of functions",
        "curry(lambda a, b, c: a + b + c)(1)(2)(3)",
    ),
    Map(
        xor,
        "Exclusive or of sequences\n\nVariants: xor_by, xor_with",
        "xor([1, 2], [2, 3], [3, 4])",
    ),
]


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
