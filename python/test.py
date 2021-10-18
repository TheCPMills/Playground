import string
import enum


def createList(numbers):
    lst = []
    for char in numbers:
        lst.append(int(char.strip(string.ascii_letters)))
    return lst


def line(x, y, z):
    return (x**2 + y**2 + z**2)**0.5


list = createList("135")
for n in list:
    print(n)


class fruit(enum.Enum):
    apple = 1
    banana = 2
    grape = 3


print(fruit(1).name)


def ah():
    i = 0
    while((i := i + 1) < 5):
        print("a", end="")
    print("h")


def incrementChar(strings):
    for i in range(0, len(strings), 1):
        strings = replace(strings, i, chr(ord(strings[i]) + 2))
    return strings


def replace(str, index, item):
    return str[:index] + item + str[index+1:]


ah()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(x)
print(x.pop(1))
print(x[::2])
print(x[2:5:2])  # start:end:skip_every
print(x)
print((x := [n for n in x if n % 2 != 0]))
print(x.index(5, 0, 3))

print("uIo yh aetveo ly oIu"[1::2])
print("uIo yh aetveo ly oIu"[18::-2])
print(incrementChar("KMLMNMJW"))


def change(num):
    s = ""
    while(num > 0):
        s += str(num % 10)
        num //= 10
        change(num)
    return s


def fn(num):
    reversed = 0
    while(num > 0):
        reversed = (reversed * 10) + (num % 10)
        num //= 10
    return reversed


print(change(5030))
print(fn(5030))


def wordsOfFrequency(words, freq):
    newWords = [x.lower() for x in words]
    result = []
    indicies = []
    for num in range(len(newWords)):
        if(not num in indicies and newWords.count(newWords[num]) == freq):
            index = [i for i, x in enumerate(newWords) if x == newWords[num]]
            indicies.extend(index)
            for n in index:
                result.append(words[n])
    return result


userInputStr = str(input())
userWords = userInputStr.split(' ')
userInputNum = int(input())
print(wordsOfFrequency(userWords, userInputNum))
