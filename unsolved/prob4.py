# problem 4 from project euler

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is   .

Find the largest palindrome made from the product of two -digit numbers."""


def isPalindrome(x: int):
    "Check to see if number is palindrome"
    xs = str(x)
    i = 0
    t = True
    while i < len(xs) / 2:
        breakpoint()  # not done yet


def main():
    a = 999
    b = 999
    x = 0
    done = False
    while a > 100:
        while b > 100:
            x = a * b
            done = isPalindrome(x)
            if done:
                break
            b = b - 1
        if done:
            break
        a = a - 1
    print(x, " is a product of", a, " x ", b)


if __name__ == "__main__":
    main()
