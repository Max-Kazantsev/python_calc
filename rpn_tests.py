""" Тесты для функции нахождения обратной польской нотации"""
import unittest
from ddz import Calc
from ddz import rpn


class TestCalc(unittest.TestCase):
    """ Тесты для функции нахождения обратной польской нотации """

    def test_calc(self):
        """Тесты с корректными исходными данными"""
        tests = {'1 + 2 + 3': 6,
                 '3 - 2 - 1': 0,
                 '1 * 2 * 3': 6,
                 '3 / 2 / 1': 1.5,
                 '1 + 2 - 3 * 4 / 5': 0.6000000000000001,
                 '1 + ( 2 - 3 ) * 4 / 5': 0.19999999999999996,
                 '( 1 + ( 2 - 3 ) ) * 4 / 5': 0}

        for test_case in tests:
            self.assertEqual(tests[test_case], Calc.count(test_case))


class TestRpn(unittest.TestCase):
    """ Тесты для функции нахождения обратной польской нотации """

    def test_rpn_error(self):
        """Тесты с ошибочными исходными данными"""
        type_error_tests = ['+', '2 +', '2 2', '+ 2 2']
        value_error_tests = ['a 2 -', '2 2 +-']

        for test in type_error_tests:
            self.assertRaises(TypeError, rpn(test))
        for test in value_error_tests:
            self.assertRaises(ValueError, rpn, test)

    def test_rpn(self):
        """Тесты с корректными исходными данными"""
        tests = {'123': '123',
                 '1 * 2 + 3': '1 2 * 3 +',
                 '( 7 / 2 ) ^ ( 4 )': '7 2 / 4 ^',
                 '( 2 ^ 3 ) ^ 4': '2 3 ^ 4 ^',
                 '5 + ( ( 1 + 2 ) * 4 ) - 3': '5 1 2 + 4 * + 3 -'}

        for test in tests:
            self.assertEqual(tests[test], rpn(test))
