def odd_even_index_str (string):
    str_list = list(string)
    odd_str_list = []
    even_str_list = []
    
    for strs, char in enumerate(str_list):
        if strs % 2 == 0:
            even_str_list.append(char)
        else:
            odd_str_list.append(char)
    
    final_str = str("".join(even_str_list)) + " " + str("".join(odd_str_list))
    
    return final_str

if __name__ == '__main__':
    n = int(input())
    
    for i in range (n):
        s = input()
        print(odd_even_index_str(s))
