import unittest
import calculatorTests

def main():
    runner = unittest.TextTestRunner()
    runner.run(calculatorTests.CalculatorTestSuite())

if __name__ == "__main__":
    main()