def c1(x):
    """
    Returns x ** 2.
    :param x: int.
    :return: int square of x.
    """
    return x ** 2

def c2(word):
    """
    Prints word.
    :param word: string.
    :print: string word.
    """
    word = str(word)
    print(word)

def c3(x, y = 10):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return int sum of x and y.
    """
    return x + y

def c4_1(x):
    """
    Returns x / 2.
    :param x: int.
    :return int x divided by 2.
    """
    x = x / 2
    x = int(x)
    return x

def c4_2(x):
    """
    Returns x *4.
    :param x: int.
    :return int x multiplied by 4.
    """
    x = x * 4
    x = int(x)
    return x

def c5(num):
    """
    Return num.
    :param num: int.
    :return float num.
    """
    try:
        num1 = float(num)
        return num1
    except(ValueError):
        print("数字を入力してください。")

print(c1(2))

c2("aaa")

print(c3(4))

chl4_1 = c4_1(5)
print(c4_2(chl4_1))
    
print(c5(5))
