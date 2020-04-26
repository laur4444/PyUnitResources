import unittest
import calculator

class CalculatorTestFixture(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()
        self.calculator.launch()

    def tearDown(self):
        self.calculator.destroy()

class CalculatorTests(CalculatorTestFixture):
    def testFactorial_5(self):
        assert self.calculator.factorial(5) == 120, 'Incorrect factorial of 5'

    def testFactorial_invalid(self):
        assert self.calculator.factorial(-1) == None, 'Incorrect factorial of -1'
    def testFail(self):
        assert self.calculator.factorial(0) == 0, 'Factorial of 0 is not 0'

class CalculatorTestSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self, map(CalculatorTests,
                                        ["testFactorial_5",
                                        "testFactorial_invalid",
                                        "testFail"]))
