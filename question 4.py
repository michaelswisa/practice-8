# כתבו תוכנית הקולטת מהמשתמש סדרה של מספרים שלמים אי- שליליים המסתיימת ב - (-1).
# בסוף הקליטה עליכם להציג:
# - המספר המקסימלי
# - המספר המינימלי
# - ממוצע המספרים
# - כמות המספרים
# - כמות המספרים הזוגיים
# - כמו המספרים האי זוגיים
# אם הסדרה ריקה יש להודיע על כך.


my_list = [int(input("enter number - "))]
for i in my_list:
    if i == -1:
        break
    my_list.append(int(input("enter number - ")))
my_list.remove(-1)
if len(my_list) == 0:
    print("The series is empty")
else:
    print("The resulting string", my_list)
    maximum = 0
    for i in my_list:
        if i > maximum:
            maximum = i
    print("the maximum number", maximum)
    minimal = my_list[0]
    for i in my_list:
        if minimal > i != -1:
            minimal = i
    print("Minimum number", minimal)
    sum = 0
    for i in my_list:
        sum += i
    average = sum / len(my_list)
    print("Total sum of the string numbers", sum)
    print("average", average)
    double = 0
    for i in my_list:
        if i % 2 == 0:
            double += 1
    print("the sum of the even numbers", double)
    odd = 0
    for i in my_list:
        if i % 2 != 0:
            odd += 1
    print("The sum of the odd numbers", odd)
