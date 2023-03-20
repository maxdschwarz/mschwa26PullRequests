#df bugs
a, b = 0, 1
sum_even = 0
# swapped > to < to enter the while loop
while b < 4000000:
    # added == instead of = to resolve a runtime error
    if b % 2 == 0:
        sum_even += b
        
    a, b = b, a+b
    

print(sum_even)

# answer should be 4613732
