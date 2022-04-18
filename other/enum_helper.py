from typing import Any


inc_holder = {}


def inc(context: Any) -> int:
    key = None
    if isinstance(context, type):
        key = context.__name__
    if isinstance(context, str):
        key = context
    if not key: raise Exception("Unknown context in `inc` function")

    if key not in inc_holder.keys():
        inc_holder[key] = 0
        return 0
    else:
        inc_holder[key] += 1
        return inc_holder[key]
