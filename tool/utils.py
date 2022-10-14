from typing import TypeVar

T = TypeVar("T")


def get_2d(arr: list[list[T]], x: int, y: int, *, fallback=None) -> T | None:
    if 0 <= x < len(arr):
        second = arr[x]
        if 0 <= y < len(second):
            return second[y]
        else:
            return fallback
    else:
        return fallback
