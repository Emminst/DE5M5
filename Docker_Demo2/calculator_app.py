class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_sum(self):
        return self.a + self.b

    def do_product(self):
        return self.a * self.b

    def do_subtract(self):
        return self.a - self.b

    def do_divide(self):
        return self.a / self.b
    
    def times_table(self):  
        """Generate the multiplication table for 'a' up to 'b'."""
        for i in range(1, self.b + 1):
            print(f"{self.a} × {i} = {self.a * i}")

#myCalc = Calculator(11,6)
#print("the answer is...", myCalc.do_sum())

