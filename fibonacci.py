import time

x = 0
y = 1
z = x+y
print(z)

def fibonacci():
    global x
    global y
    global z

    x = y
    y = z
    z = x+y

    print(z)
    time.sleep(1)
    fibonacci()

fibonacci()