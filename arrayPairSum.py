# Find all unique pairs in an array whose currentSum is equal to a value k
__author__='https://github.com/dhillonfarms'

def pair_sum(list1, sum1):
    # Declare an empty list for output
    output_list = []
    # Simple case -- if number to be compared is even, see if more than 1 occurences of num/2 exist
    if sum1%2 ==0 and list1.count(sum1/2) > 1:
        output_list.append((int(sum1/2), int(sum1/2)))
    # Once above case is handled, remove any non-unique values
    set_list1 = set(list1)
    if sum1%2==0:
        set_list1.discard(int(sum1/2))
    # Go thru the list to see if currentNumber and (sum - currentNumber) pair exists
    for n in set_list1.copy():
        if (sum1-n) in set_list1:
            output_list.append((n, sum1-n))
            set_list1.discard(n)
            set_list1.discard(sum1-n)
            continue
        if n > sum1 and (n-sum1) in set_list1:
            output_list.append((n, n-sum1))
            set_list1.discard(n)
            set_list1.discard(n-sum1)
            continue
    # Return final list
    return output_list

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))
print(pair_sum([1,3,2,2],4))