#Took me about 15 mins
def fizzbuzz():
    i=1
    while i <= 100:
        fizz=(i%3==0)
        buzz=(i%5==0)
        if fizz and buzz:
            print(str(i)+": FizzBuzz")
        elif fizz:
            print(str(i)+": Fizz")
        elif buzz:
            print(str(i)+": Buzz")
        i+=1
fizzbuzz()