# About 23 mins
def fibonacci(num):
    x=0
    y=1
    count=2
    while count<num:
        z=x+y
        x=y
        y=z
        count+=1
        if(count==num):
            print(z)
fibonacci(7)