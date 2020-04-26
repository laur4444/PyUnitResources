import unittest
import calculatorTests

def main():
    runner = unittest.TextTestRunner()
    result = runner.run(calculatorTests.CalculatorTestSuite())

    print(result)
    print(result.errors)
    print(result.failures)
    print(result.wasSuccessful())
    print(result.testsRun)


if __name__ == "__main__":
    main()