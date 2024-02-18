# כתוב תוכנית הקולטת מספר טבעי num וספרה k. התוכנית תדפיס את מספר הספרות בnum המתחלקות
# ב-k ללא שארית


num = input("הכנס מספר שלם\n")
k = float(input("הכנס כל מספר\n"))
x = 0
for i in num:
    i = int(i)
    if i % k == 0:
        if i == 0:
            continue
        x += 1
print(x)
