# Consider the following:
# * A string, s, of length n where s = c0c1...cn-1
# * An integer, k, where k is a factor of n.
# We can split s into n/k substrings where each substring, ti, consists of a contigious block
# of k characters in s. Then, use each ti to create string ui such that:
# * The characters in ui are a subsequence of the characters in ti.
# * Any repeat occurence of a character is removed from the string such that each character at
#   some index j in ti occurs at a previous index < j in ti, then do not include the character
#   in string ui. 
# Given s and k, print n/k lines where each line i denotes string ui. 

def merge_the_tools(string, k):
    start = 0
    end = k
    
    while end <= len(string):
        temp = string[start:end]
        chunk = list(set(list(temp)))
        print(''.join(chunk))
        
        start += k
        end += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)