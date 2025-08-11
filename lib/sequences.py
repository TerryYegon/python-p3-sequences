#!/usr/bin/env python3

def print_fibonacci(n):

    if n <= 0:
        print([])
        return
    elif n == 1:
        print([0])
        return

    
    fib_list = [0, 1]

    
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]  
        fib_list.append(next_num)

    print(fib_list)
