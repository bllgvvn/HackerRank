def mutate_string(string, position, character):
    new_list = list(string)
    new_list[position] = f"{character}"
    string = ''.join(new_list)
    return string

if __name__ == '__main__':
    s = input("Enter the string: ")
    i, c = input("Enter the position and character: ").split()
    s_new = mutate_string(s, int(i), c)
    print("Mutated string:", s_new)