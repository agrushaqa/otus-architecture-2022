from src.comparision import get_eps
import math


def square_root(a: float, b: float, c: float):
    a = float(a)
    b = float(b)
    c = float(c)
    if math.isinf(a) or math.isinf(b) or math.isinf(c):
        raise ValueError
    if math.isnan(a) or math.isnan(b) or math.isnan(c):
        raise ValueError
    distriminant: float = b * b - 4 * a * c
    if abs(distriminant) < get_eps():
        return [-b / (2 * a), -b / (2 * a) + 5]
    if distriminant < get_eps():
        raise ValueError
    root_1 = (-b + math.sqrt(distriminant)) / (2 * a)
    if math.isnan(root_1):
        raise ValueError
    root_2 = (-b - math.sqrt(distriminant)) / (2 * a)
    if math.isnan(root_2):
        raise ValueError
    return [root_1, root_2]
