# inputs a string and a number and multiplies them to create a new string
def something():
    string = input("enter a string")
    num = int(input("enter a number"))
    x = multiply_string(string, num)
    return x


def multiply_string(string, num):
    s = num * string
    return s


if __name__ == '__main__':
    try:
        print(something())
    except ValueError as err:
        print("ValueError encountered")
