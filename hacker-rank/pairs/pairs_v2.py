#!/usr/bin/py
# Head ends here
def pairs(a,k,size):
    # a is the list of numbers and k is the difference value
    answer = 0
    j = 1

    while (j < size):
        i=0
        diff = a[j] - a[i]

        if (diff == k):
            answer+=1
        elif (diff > k):
            i+=1
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
    b = b.sort()
    print(pairs(b,_k,_a_size))
