from parameterized import parameterized
import unittest
from src.comparision import approximately_equal
from src.comparision import approximately_equal_with_eps
from src.equation import square_root
import sys


# поиск тестов в папке tests
#  python -m unittest discover -s tests -p "*" -v -b
# запускать в папке module_tests
class TestSolutionOfQuadraticEquation(unittest.TestCase):

    @parameterized.expand([
        (0, 0, 0),
        (0, 5, 0),
        (0, 1, 1),
        (2, 0, 1),
        (1, 1, "Ы"),
        (1, "V", 1),
        ("!", 1, 1),
        (1, 1, '习'),
        (float("inf"), 1, 1),
        (1, float("nan"), 1),
        (4, 1, float("-inf")),
        (-1e+100000000000000, 1, 2)
    ])
    def test_square_root_expected_exception(self, a, b, c):
        self.assertRaises(Exception, square_root, a, b, c)

    @parameterized.expand([
        (1, -2, 1, 1, 1),
        (1, 4, 4, -2, -2),
        (0.001, 0.0049, 0.0051, -2.4499999999999997, -2.4499999999999997),
        (1, 0, -1, 1, -1),
        ("1", "0", "-1", 1, -1),
        (99999999, 100000000, 0, -1.0000000100000002, 0),
        (99999999, -10, 0, 1.0000000100000001e-07, 0),
        (1, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1,
         -1e+101, 0),
        (1, 100000000, 1, -100000000.0, -7.450580596923828e-09),
        (1, 100000, 1, -99999.99999, -1.0000003385357559e-05)
    ])
    def test_square_root_expected_two(self, a, b, c, root_1, root_2):
        generate_result_list = sorted(square_root(a, b, c))
        expected_result_list = sorted([root_1, root_2])
        assert len(generate_result_list) == len(expected_result_list)
        print(generate_result_list)
        print(expected_result_list)
        for index in range(len(expected_result_list)):
            assert approximately_equal(generate_result_list[index], expected_result_list[index]) is True

    @parameterized.expand([
        (1, -2, 1),
        (2, 4, 0),
        (1, 10000, 1),
        (9999, 40000, 0),
        (99999999, 100000000, 0),
        (1, 100000, 1)
    ])
    def test_quadratic_equation(self, a, b, c):
        generate_result_list = square_root(a, b, c)
        for i_value in generate_result_list:
            result = a * i_value * i_value + b * i_value + c
            print(generate_result_list)
            print(f"result:{result}")
            assert approximately_equal(result, 0)

    @parameterized.expand([
        (1, -2, 1, 1, 1, 0.00000001),
        (1, 0, -1, 1, -1, 0.00000001),
        (1, 4, 4, -2, -2, 0.00000001),
        (99999999, 100000000, 0, -1.0000000100000002, 0, 0.00000001),
        (99999999, -10, 0, 1.0000000100000001e-07, 0, 0.00000001),
        (1, 100000, 1, -99999.99999, -1.0000003385357559e-05, 0.000001),
        (1, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1,
         -1e+101, 0, 2),
        (1, 100000000, 1, -100000000.0, -7.450580596923828e-09, 2),
        (0.001, 0.0049, 0.0051, -2.4499999999999997, -2.4499999999999997, 0.001)
    ])
    def test_expected_result(self, a, b, c, root1, root_2, eps):
        result = a * root1 * root1 + b * root1 + c
        assert approximately_equal_with_eps(result, 0, eps), f"result:{result}"
        result = a * root_2 * root_2 + b * root_2 + c
        assert approximately_equal_with_eps(result, 0, eps), f"result:{result}"
