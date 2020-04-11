class Calculator:
    def launch(self):
        print("Calculator launched!")

    def factorial(self, n):
        if n < 0:
            return None
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def destroy(self):
        print("Calculator destroyed")