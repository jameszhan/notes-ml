# -*- coding: utf-8 -*-


def solve(f, guess, epsilon=1e-8):
    i = 0
    while True:
        new_guess = f(guess)
        if abs(guess - new_guess) > epsilon:
            guess = new_guess
        else:
            break
        print '[ Epoch {0} ] guess = {1}'.format(i, guess)
        i += 1
    return guess


print solve(lambda x: (x + 5 / x) / 2.0, 10.0)
print solve(lambda x: (x + 8 / (x ** 2)) / 2.0, 10.0)




