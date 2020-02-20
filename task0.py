for i in range(100):
    num = i + 1
    if num % 3 == 0 and num % 5 == 0: #multiples of both three and five
        print("FizzBuzz")
    elif num % 3 == 0: #multiples of three
        print("Fizz")
    elif num % 5 == 0: #multiples of five
        print("Buzz")
    else:
        print(num)