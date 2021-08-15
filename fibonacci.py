import time

x = 0
y = 1
z = x+y

def fibonacci():
    global x
    global y
    global z
    print(x)
    print(y)
    print(z)
    while __name__ == '__main__':
        x = y
        y = z
        z = x+y

        print(z)
        time.sleep(1)


def fibonacciEven():
    global x
    global y
    global z

    while __name__ == '__main__':
        x = y
        y = z
        z = x+y
        if z % 2 == 0:
            print(z)

        time.sleep(1)

def fibonacciOdd():
    global x
    global y
    global z
    print(y)
    print(z)


    while __name__ == '__main__':
        x = y
        y = z
        z = x+y
        if z % 2 != 0:
            print(z)

        time.sleep(1)



chooseSequence = input("Which of these would you like to execute?\n1. Fibonacci Sequence.\n2. Fibonacci Sequence (Even Numbers).\n3. Fibonacci Sequence (Odd Numbers)\n\n")

if chooseSequence == "1":
    print("")
    fibonacci()
elif chooseSequence == "2":
    print("")
    fibonacciEven()
elif chooseSequence == "3":
    print("")
    fibonacciOdd()