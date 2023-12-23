from functools import reduce
from typing import List


sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic",
                        "and Nory’s mother was a Catholic", "because her father was a Catholic",
                        "and her father was a Catholic", "because his mother was a Catholic",
                        "or had been"]


def check_was(a, b) -> int:
    if isinstance(a, str):
        a = int(a.count('was'))
    result = a + int(b.count('was'))
    return result


print(reduce(check_was, sentences))
