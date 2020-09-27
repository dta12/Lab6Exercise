def splitStr(any_String):
    return [char for char in any_String]


def roundScore(score):
    return round(score, 2)


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetList = splitStr(alphabet)
name = str(input("enter your name: "))
name.lower()
name.strip()
name.replace(' ', '')
nameLetters = splitStr(name)
nameLength = int(input("how many letters are in your name? "))
sumScore = 0
for letter in nameLetters:
    sumScore = sumScore + (int(alphabetList.index(letter))+1)


avg = sumScore/nameLength
print("your name score is: ", roundScore(avg))
