print("Привет, введи два числа, каждое с новой строки!")
a=int(input())
b=int(input())
print("Молодец, Ты справился с этим!!!")
print(a-b)
print("Хочешь узнать число больше нуля? (да/нет)")
da=str(input())
if da=="да":
    print((a-b)>0)
else:
    print("Ну и пока!")