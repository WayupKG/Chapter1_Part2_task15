def age_func():
    age = int(input("Сколько вам лет - "))
    if age % 2 == 0:
        for i in range(0, age + 1):
            if i % 2 == 0:
                print(i)
            i += 1
    elif age % 2 != 0:
        for i in range(1, age+1):
            if i % 2:
                print(i)
age_func()
