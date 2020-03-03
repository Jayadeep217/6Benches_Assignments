import sys

def highestSetBit(num):
    n=0
    order = -1
    num_size = sys.getsizeof(num)* 8 #Integer size in bits
    while (n < num_size):
        if((num>>n) & 1):
            order = n
        n = n+1

    if (order != -1):
        print("Highest set bit number is", order)
    else :
        print("0 has no set bits.")

num = int(input("Enter a number"))
highestSetBit(num)
