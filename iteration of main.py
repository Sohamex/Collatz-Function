from main_function import Clz

while True:
    
    x = float(input('Enter the number: '))
    n = int(input("Enter number of iteration:  "))

    def Clzi(x,n):
        result = x

        for i in range (n):
            result = Clz(result)

        return result
    print(Clzi(x,n))
