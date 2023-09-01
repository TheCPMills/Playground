import string
import enum

# ==========================================================================
# int to char practice
# ==========================================================================
def createList(numbers):
    lst = []
    for char in numbers:
        lst.append(int(char.strip(string.ascii_letters)))
    return lst

list = createList("135")
print("Values in list: ", end="")
for num in list:
    print(num, end=" ")
print("")

# ==========================================================================
# enum practice
# ==========================================================================
class fruit(enum.Enum):
    apple = 1
    banana = 2
    grape = 3

print("The first fruit is " + fruit(1).name)

# ==========================================================================
# while loop practice
# ==========================================================================
def ah():
    i = 0
    while((i := i + 1) < 5):
        print("a", end="")
    print("h")

print("I'm going to scream with five letters: ", end="")
ah()

# ==========================================================================
# list practice
# ==========================================================================
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("The list is " + x.__str__())
print("Removed the second element of the list: " + x.pop(1).__str__())
print("Every other element of the list is " + x[::2].__str__())
print("Every other element of the list from the third to the fifth element is " + x[2:5:2].__str__())  # start:end:skip_every
print("The odd elements of the list are " + (x := [n for n in x if n % 2 != 0]).__str__())
print("The first occurance of 5 between indices 0 and 3 is at index" + x.index(5, 0, 3).__str__())

# ==========================================================================
# string practice
# ==========================================================================
def replace(str, index, item):
    return str[:index] + item + str[index+1:]
    
def incrementChar(strings):
    for i in range(0, len(strings), 1):
        strings = replace(strings, i, chr(ord(strings[i]) + 2))
    return strings

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

print("5030 backwards is " + change(5030).__str__())
print("5030 backwards is " + fn(5030).__str__())

# ==========================================================================
# dictionary practice
# ==========================================================================
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
