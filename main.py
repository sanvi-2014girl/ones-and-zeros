def numberofbits(bit):
    ones_count = 0
    zero_count = 0
    while(bit):
        if bit&1  ==1:
             ones_count = ones_count + 1
        else:
            zero_count = zero_count + 1
        bit >>= 1
    print("Ones:",ones_count)
    print("Zeros:",zero_count)
bit = int(input("Enter number: "))
numberofbits(bit)