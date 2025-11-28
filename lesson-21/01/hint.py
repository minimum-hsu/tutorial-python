#!/usr/bin/env python3

from typing import Any
from typing import Mapping
from typing import Sequence

def dict_keys(d: Mapping[str, Any]) -> Sequence[str]:
    return list(d.keys())

if __name__ == '__main__':
    sample_dict: dict[str, int | str] = {'a': 1, 'b': '2', 'c': 3}
    keys = dict_keys(sample_dict)
    print(f"Keys: {keys}")