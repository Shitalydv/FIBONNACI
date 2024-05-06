'''Fibonacci  starts starts with 0 1 1  2 3 4 8 13 21 34 55 .... etc
0: invalid input
1:[0]
2:[0,1]
3:[0,1,1]
4:[0,1,,1,2]
5:[0,1,1,2,3]





'''

def get_fibonacci_series(num):
    if not isinstance(num, int):
        print('Invalid input type')
        return None
    if num<=0:
        print("Invalid  input number. The number must be positive integer")
        return None
    if num ==1:
        return[0]
    
    fibonacci_series=[0,1]
    
    for i in range (num-2):
        next_item =fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_item)
        
        
    return fibonacci_series        