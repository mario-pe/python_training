def fizzBuzz(number):
    if number%3 == 0 and number%5 == 0:
        return 'fizz buzz'
    elif number%3 == 0:
        return 'fizz'
    elif number%5 == 0:
        return 'buzz'
    return 'No no'


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)