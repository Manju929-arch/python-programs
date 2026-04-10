if __name__ == '__main__':
    # a = 12
    # b = 18
    # while a!= b:
    #     if a>b:
    #         a = a-b
    #     else :
    #         b = b -a
    #
    # print(a)
    a = 12
    b = 24
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:
            b= b%a

    if a!=0:
        print(a)
    else:
        print(b)

