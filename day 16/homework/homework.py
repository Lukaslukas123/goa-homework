x = 1
i= 1
while  i  != 11:
    x = x * i
    i = i + 1
print(x)
 



x=1

for i in range (1, 10):
    x= x * i
print(x)



#4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:   10 % 2 = 0;    5 % 2 = 1)
num1=int(input("enter you namber"))

if num1 % 2 == 0:
    print("the number is even")
else:
    print("is number is odd")





score=int(input("enter you namber" ))
if 90 <= score <= 100:
    print("you get greade is A")
elif 80 <= score <= 89:
    print("you grade is B")

else:
    print("your score is not in the 80-100 range ")
