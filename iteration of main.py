import math
import cmath
from main_function import Clz

while True:
    
    x = float(input('Enter the number of choice: '))
    n = 3 #int(input("Enter number of iteration:  "))

    def Clzi(x,n):
        result = x

        for index in range (n):
            result = Clz(result)

        return result
    print(Clzi(x,n))
