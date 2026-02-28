def factorial(n):
    num = int(n)
    
    for i in range(1, num):
        num *= i
        
    return num

if __name__ == '__main__':
  print(factorial(8))   # Output: 40320
  print(factorial(5))   # Output: 120
  print(factorial(0))   # Output: 1
