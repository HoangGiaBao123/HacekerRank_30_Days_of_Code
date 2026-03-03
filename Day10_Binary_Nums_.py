if __name__ == '__main__':
    n = int(input().strip())
    
    binary = str(bin(n))
    
    repeat_count = 0
    max_repeat = 0
    
    for letter in binary:
        if letter == "1":
            repeat_count += 1
            
            if repeat_count > max_repeat:
                max_repeat = repeat_count
            
        else:
            repeat_count = 0
            
    print(max_repeat)
