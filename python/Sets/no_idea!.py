# There is an array of n integers. There are also 2 sets, A and B, each containing m integers.
# You like all the integers in set A and dislike all the integers in set B.
# Your initial happiness is 0. For each integer in the array, if i is in A,
# you add 1 to your happiness. If i is in B, you subtract 1 from your happiness.
# Otherwise, your happiness does not change. Output your final happiness at the end.

n, m = list(map(int, input().split()))
my_arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

def calculate_happiness(n, m, my_arr, set_a, set_b):
    happiness = 0
    for num in my_arr:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
    
    return happiness     
    
print(calculate_happiness(n, m, my_arr, set_a, set_b))   