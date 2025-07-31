# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    new_s = []
    
    for item in s:
        if item.isalpha():
            if item.islower():
                new_s.append(item.upper())
            else:
                new_s.append(item.lower())
        else:
            new_s.append(item)
    return ''.join(new_s)

if __name__ == '__main__':
    s = input("Enter a string to swap cases: ")
    result = swap_case(s)
    print("Result: ", result)