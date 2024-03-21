import unittest
from random import randint, random
from numpy import prod
from mathOperations import add, multiply, divide


class TestCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Testing all modules in the mathOperations package")
        cls.listInt = [randint(-125, 125) for i in range(10)]
        cls.listFloats = [random() * (-1) ** i for i in range(10)]
        cls.listFloatsNoZeros = [(1 - random()) * (-1) ** i for i in range(10)]
        cls.listIntNoZeros = [int(flt * 100) for flt in cls.listFloatsNoZeros]
        cls.listStr = ["poulet", "bateau", "cucurbitacee", "osé les accents !"]

    def testAddInts(self):
        """Testing add function with +/- ints"""
        valuetotest = add.addlist(self.listInt)
        correctvalue = sum(self.listInt)
        self.assertEqual(valuetotest, correctvalue, "addlist doesn't work with ints")

    def testAddfloats(self):
        """Testing add function with +/- floats"""
        valuetotest = add.addlist(self.listFloats)
        correctvalue = sum(self.listFloats)
        self.assertEqual(valuetotest, correctvalue, "addlist doesn't work with floats")

    def testAddStr(self):
        """Testing add function with strings"""
        valuetotest = add.addlist(self.listStr)
        self.assertIsNone(valuetotest, "addlist doesn't handle wrong data type")

    def testMultiplyInts(self):
        """Testing multiply function with +/-ints"""
        valuetotest = multiply.multiplylist(self.listInt)
        correctvalue = 1
        for item in self.listInt:
            correctvalue *= float(item)
        self.assertEqual(
            valuetotest, correctvalue, "multiplylist doesn't work with ints"
        )

    def testMultiplyfloats(self):
        """Testing multiply function with +/-floats"""
        valuetotest = multiply.multiplylist(self.listFloats)
        correctvalue = 1
        for item in self.listFloats:
            correctvalue *= float(item)
        self.assertEqual(
            valuetotest, correctvalue, "multiplylist doesn't work with floats"
        )

    def testMultiplyStr(self):
        """Testing add function with strings"""
        valuetotest = multiply.multiplylist(self.listStr)
        self.assertIsNone(valuetotest, "multiplylist doesn't handle wrong data type")

    def testDivideIntsNoZeros(self):
        """Testing divide function with +/-ints but no 0"""
        liste = [self.listIntNoZeros[0], self.listIntNoZeros[1]]
        valuetotest = divide.divideList(liste)
        correctvalue = liste[0] / liste[1]
        self.assertEqual(valuetotest, correctvalue, "dividelist doesn't work with ints")

    def testDivideFloatsNoZeros(self):
        """Testing divide function with +/-floats but no 0"""
        liste = (self.listFloatsNoZeros[0], self.listFloatsNoZeros[1])
        valuetotest = divide.divideList(liste)
        correctvalue = liste[0] / liste[1]
        self.assertEqual(
            valuetotest, correctvalue, "dividelist doesn't work with floats"
        )

    def testDivideWithZeros(self):
        """Testing divide function with 0"""
        liste = [1, 0]
        valuetotest = divide.divideList(liste)
        self.assertIsNone(valuetotest, "dividelist doesn't handle zeros")

    def testDivideWithTooManyParmeters(self):
        """Testing divide function with too many parameters"""
        liste = [1, 1, 1, 1, 1, 1]
        valuetotest = divide.divideList(liste)
        self.assertIsNone(
            valuetotest, "dividelist doesn't handle being given too many parameters"
        )

    def testDivideWithTooFewParmeters(self):
        """Testing divide function with too many parameters"""
        liste = [1]
        valuetotest = divide.divideList(liste)
        self.assertIsNone(
            valuetotest, "dividelist doesn't handle being given too few parameters"
        )

    def testDivideStr(self):
        """Testing add function with strings"""
        valuetotest = divide.divideList(self.listStr)
        self.assertIsNone(valuetotest, "dividelist doesn't handle wrong data type")


if __name__ == "__main__":
    unittest.main()
