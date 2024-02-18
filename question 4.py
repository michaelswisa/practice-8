# כתבו תוכנית הקולטת מהמשתמש סדרה של מספרים שלמים אי- שליליים המסתיימת ב - (-1).
# בסוף הקליטה עליכם להציג:
# - המספר המקסימלי
# - המספר המינימלי
# - ממוצע המספרים
# - כמות המספרים
# - כמות המספרים הזוגיים
# - כמו המספרים האי זוגיים
# אם הסדרה ריקה יש להודיע על כך.


my_str = [int(input("הכנס מספר - "))]
for i in my_str:
    if i == -1:
        break
    my_str.append(int(input("הכנס מספר - ")))
if my_str[0] == -1:
    my_str.pop(0)
    print("הסדרה ריקה")
new_str = my_str
new_str.remove(-1)
print("המחרוזת שהתקבלה", new_str)
maximum = 0
for i in new_str:
    if i > maximum:
        maximum = i
print("המספר המקסימלי", maximum)
minimal = new_str[0]
for i in new_str:
    if minimal > i != -1:
        minimal = i
print("מספר מינימלי", minimal)
sum = 0
for i in new_str:
    sum += i
average = sum / len(my_str)
print("סכום כולל של מספרי המחרוזת", sum)
print("ממוצע", average)
double = 0
for i in new_str:
    if i % 2 == 0:
        double += 1
print("סכום המספרים הזוגים", double)
odd = 0
for i in new_str:
    if i % 2 != 0:
        odd += 1
print("סכום המספרים האי זוגים", odd)
