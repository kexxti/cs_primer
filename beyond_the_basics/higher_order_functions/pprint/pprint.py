from collections.abc import Iterable

test_list = [1, 2, 3, [4, "inner", ["super inner", ['mega inner'], 5], "less inner than super"], 6]


def is_nested(obj):
    if not isinstance(obj, Iterable) or isinstance(obj, (str, bytes)):
        return False

    items = obj.values() if isinstance(obj, dict) else obj

    return any(
        isinstance(item, Iterable) and not isinstance(item, (str, bytes))
        for item in items
    )


def fmt(ds, depth=1):
    parts = []
    for elem in ds:
        if is_nested(elem):
            parts.append(fmt(elem, depth + 1))
        else:
            parts.append(repr(elem))
    ret = '[' + (',\n' + ' ' * depth).join(parts) + ']'
    return ret

print(fmt(test_list))