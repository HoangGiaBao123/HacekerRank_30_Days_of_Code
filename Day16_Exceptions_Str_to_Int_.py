def convert_str_to_int(string):
    try:
        int_str = int(string)
        print(int_str)
    except ValueError:
        print('Bad String')
        
s = input().strip()
convert_str_to_int(s)
