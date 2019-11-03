def jiujiu_No_1():
    for i in range(0,10):
        for j in range(1,i+1):
            print('{}*{}={:<6}'.format(j,i,i*j),end="")
        print()

def jiujiu_No_2():
    for i in range(9,0,-1):
        for j in range(1,i+1,+1):
            print('{}*{}={:<6}'.format(j,i,i*j),end="")
        print()

def jiujiu_No_3():
    for i in range(1,10):
        for j in range(9,0,-1):
            if j>i:
                print("{:<6}".format(" "),end="    ")
            else:
                print('{}*{}={:<6}'.format(j,i,i*j),end="")
        print()

def jiujiu_No_4():
    for i in range(9,0,-1):
        for j in range(9,0,-1):
            if j > i:
                print("{:<6}".format(" "), end="    ")
            else:
                print('{}*{}={:<6}'.format(j, i, i * j), end="")
        print()

def jiujiu_No_5():
    i=1
    while i<10:
        j=1
        while j<i+1:
            print('{}*{}={:<6}'.format(j, i, i * j), end="")
            j+=1
        print()
        i+=1
def jiujiu_No_6():
    i = 9
    while i > 0:
        j = 1
        while j < i + 1:
            print('{}*{}={:<6}'.format(j, i, i * j), end="")
            j += 1
        print()
        i -= 1

def jiujiu_No_7():
    i = 1
    j = 9
    while i < 10:
        j=9
        while j >0:
            if j > i:
                print("{:<6}".format(" "), end="    ")
            else:
                print('{}*{}={:<6}'.format(j, i, i * j), end="")
            j-=1
        print()
        i += 1

def jiujiu_No_8():
    i=9
    j=9
    while i>0:
        j=9
        while j>0:
            if j>i:
                print("{:<10}".format(""),end="")
            else:
                print("{}*{}={:<6}".format(j,i,i*j),end="")
            j-=1
        i-=1
        print()
def main():
    jiujiu_No_1()
    jiujiu_No_2()
    jiujiu_No_3()
    jiujiu_No_4()
    jiujiu_No_5()
    jiujiu_No_6()
    jiujiu_No_7()
    jiujiu_No_8()
main()