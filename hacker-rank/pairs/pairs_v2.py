#!/usr/bin/py
# Head ends here
def pairs(a,k,size):
    # a is the list of numbers and k is the difference value
    answer = 0 
    x = 0
    j = 1

    while (j < size):
        diff = a[j] - a[x]
        if (diff == k):
            answer+=1
            j+=1
        elif (diff > k):
            x+=1
        elif (diff < k):
            j+=1

    return answer
# Tail starts here




if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    nums = sorted(b)
    print(pairs(nums,_k,_a_size))