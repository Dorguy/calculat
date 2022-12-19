import unittest

import test_calculator


class Test_0(unittest.TestCase):
    def test_1(self):
        self.assertEqual(test_calculator.Delete_0(-1), (None))
        self.assertEqual(test_calculator.Delete_0('T'), (None))
        self.assertEqual(test_calculator.Delete_0(0), (None))

    def test_2(self):
        self.assertEqual(test_calculator.validate_e(-1), (True))
        self.assertEqual(test_calculator.validate_e('T'), (False))
        self.assertEqual(test_calculator.validate_e('-'), (True))

    

    def test_3(self):
        self.assertEqual(test_calculator.add_pl(10.0, 45.0), ('55.0'))
        self.assertEqual(test_calculator.add_pl(4565.0, 23466.0), ('28031.0'))
        self.assertRaises(TypeError, test_calculator.add_pl, '534', 45)

    def test_4(self):
        self.assertEqual(test_calculator.add_mi(55.0, 45.0), ('10.0'))
        self.assertEqual(test_calculator.add_mi(436346.0, 23466.0), ('412880.0'))
        self.assertRaises(TypeError, test_calculator.add_mi, '534', 45)

    def test_5(self):
        self.assertEqual(test_calculator.add_um(55.0, 45.0), ('2475.0'))
        self.assertEqual(test_calculator.add_um(436346.0, 23466.0), ('10239295236.0'))
        self.assertRaises(TypeError, test_calculator.add_um, '534', 45)

    def test_6(self):
        self.assertEqual(test_calculator.add_de(55.0, 55.0), ('1.0'))
        self.assertEqual(test_calculator.add_de(486.0, 6.0), ('81.0'))
        self.assertRaises(TypeError, test_calculator.add_de, '534', 45.0)
        self.assertEqual(test_calculator.add_de(66.0, 0.0), 0)

    def test_7(self):
        self.assertEqual(test_calculator.add_calculation_1('×', 10.0, 11.0), '110.0')
        self.assertEqual(test_calculator.add_calculation_1('-', 10.0, 11.0), '-1.0')
        self.assertEqual(test_calculator.add_calculation_1('+', 10.0, 11.0), '21.0')
        self.assertRaises(TypeError, test_calculator.add_calculation_1, 60.0, 'y', 11.0)

    def test_8(self):
        self.assertEqual(test_calculator.add_calculation_0('5+6'), ('11'))
        self.assertEqual(test_calculator.add_calculation_0('5×10'), ('50'))
        self.assertEqual(test_calculator.add_calculation_0('5-6'), ('-1'))
        self.assertRaises(TypeError, test_calculator.add_calculation_0, '_-_')

    

    def test_9(self):
        self.assertEqual(test_calculator.game(), True)
    def test_10(self):
        self.assertEqual(test_calculator.sq(0.0), '0')
    def test_11(self):
        self.assertEqual(test_calculator.sq_r(0.0), '0')

if __name__ == "__main__":
    unittest.main()
