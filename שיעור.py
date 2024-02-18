# אופציה א'

names = ["avi", "itzik", "kobi"]
for name in names:
    print("my friend", name)






# אופציה ב'


names = ["avi", "itzik", "kobi"]
for i in range(3):
    print("my friend", names[i])


# נחלק כל מספר זוגי במערך ב 2

numbers = [1, 4, 7, 6, 9, 34]
for h in numbers:
    if h % 2 == 0:
        print(h // 2)
    else:
        print(h)

# אותו דבר עם הדפסה של מערך חדש עם המספרים הזוגים מחולקים ל2

numbers = [1, 4, 7, 6, 9, 34]
for a in range(6):
    if numbers[a] % 2 == 0:
        numbers[a] = numbers[a] // 2
print(numbers)

# break - ברגע שמגיע למה שהגדרנו שיפסיק את הריצה ויעבור לשלב הבא
# מציאת האות c

letters = ["a", "b", "c", "d", "e", "f", "g"]
for letter in letters:
    if letter == "c":
        print("found c")
        break
    print("still searching for c")
print("search ended")


# continue - ברגע שהתנאי התקיים תדלג על הפעולה הבאה שמתחת ותמשיך להריץ את התנאי

for number in range(10):
    if number % 2 > 0:
        continue
    print("this is an even number")
    print(number)
