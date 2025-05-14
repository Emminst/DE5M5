from calculator_app import Calculator
import pandas as pd

calculation=Calculator(364,97)  

print("The answer is... " ,calculation.do_product())


calc = Calculator(3, 10)  # Create an instance for the 3 times table up to 10
answer_list = calc.times_table()

print(pd.DataFrame(answer_list))


