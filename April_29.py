import Fibonacci
def main():
    print('Starting main,,,,')
    number=int(input("Enter the length of bibonacci_series: "))
    
    
    series= Fibonacci.get_fibonacci_series(number)
    
    print(series)
    
    
    
main()    