dict = {'sajal' : 60 , 'mishra' : 89 , 'raj' : 98 , 'juhu' :99}
name = input("Enter  name of the 'student' : ")


if name in dict:
    print(f"{name} marks is : {dict[name]}")
else:
    print("Student not found")