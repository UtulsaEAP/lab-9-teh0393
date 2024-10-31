def int_to_reverse_binary(num1):
    if num1==0:
        return(str(0))
    binary_val = ''
    while num1 > 0:
        binary_val+=str(num1%2)
        num1=num1//2
    print(binary_val)
    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    for i in input_string[::-1]:
        reverse_input += i
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)