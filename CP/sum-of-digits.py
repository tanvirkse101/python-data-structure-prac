def sumOfDigits(no):
    return 0 if no == 0 else int(no % 10) + sumOfDigits(int(no/10))


if __name__ == '__main__':
    print(sumOfDigits(999))
