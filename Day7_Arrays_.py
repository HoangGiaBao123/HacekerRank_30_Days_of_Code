if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    if len(arr) == n:
        for a in reversed(arr):
            a = str(a) + " "
            print(a, end="")
