""" Тесты для функции нахождения обратной польской нотации от введенного числа"""
import unittest
from ddz import rpn
from ddz import Calc


class TestRpn(unittest.TestCase):
    """ Тесты для функции нахождения обратной польской нотации от введенного числа"""

    def test_rpn_error(self):
        """Тесты с ошибочными исходными данными"""
        self.assertRaises(IndexError, Calc.count, rpn('+'))
        self.assertRaises(IndexError, Calc.count, rpn('2 +'))
        self.assertRaises(ValueError, Calc.count, rpn("2 2"))
        self.assertRaises(ValueError, Calc.count, rpn('+ 2 2'))
        self.assertRaises(ValueError, rpn, 'a 2 -')
        self.assertRaises(ValueError, rpn, "2 2 +-")

    def test_rpn(self):
        """Тесты с корректными исходными данными"""
        self.assertEqual('666', rpn("666"))
        self.assertEqual('2 3 * 4 +', rpn('2 * 3 + 4'))
        self.assertEqual('2 3 4 + *', rpn('2 * ( 3 + 4 )'))
        self.assertEqual('7 2 / 4 ^', rpn('( 7 / 2 ) ^ ( 4 )'))
        self.assertEqual('2 3 ^ 4 ^', rpn('( 2 ^ 3 ) ^ 4'))
        self.assertEqual('5 1 2 + 4 * + 3 -', rpn('5 + ( ( 1 + 2 ) * 4 ) - 3'))
