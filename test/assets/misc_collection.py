import random
from datetime import date

from veho.matrix import init

from test.assets.classes import Message, Point

basics = {
    'none': None,
    'bool': bool(random.randint(0, 1)),
    'string': 'shakes',
    'number': 128,
    'date': date.today(),
    'tuple': ('left', 'centre', 'right')
}

vectors = {
    'void_vec': [],
    'void_matrix': [[]],
    'nested_vec:': [[[[[[[[[]]]]]]]]],
    'simple_vec': [1, 2, 3, 'foo', 'bar', 'zen'],
    'alphabetical': init(4, 7, lambda x, y: chr(63 + (x * 7) + y)),
}

dicts = {
    'void_dict': {},
    'simple_dict': {'foo': 1, 'bar': 2}
}

misc = {
    'lambda': lambda x: str(x)
}

objects = {
    'point': Point(3, 4, 'initial_point'),
    'message': Message('ford', 'ferrary', 'daytona')
}

misc_candidates = {
    **basics,
    **vectors,
    **dicts,
    **misc,
    **objects
}
