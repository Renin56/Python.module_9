from random import randint


a = randint(1, 1000)
b = randint(1, 1000)
c = randint(1, 1000)


def is_prime(func):
    def wrapper(*args, **kwargs):
        simple = False

        res = func(*args, **kwargs)

        for i in range(2, res):
            # print(f'{res} // {i} = {res // i}')
            if res % i == 0:
                simple = True
                break

        if simple:
            return 'Составное\n' + str(res)
        else:
            return 'Простое\n' + str(res)

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


print(sum_three(2, 3, 6))

# print(sum_three(a, b, c))
