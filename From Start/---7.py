#For gym admission V.001
#How old is he
age=float(input("age="))
#What is his height
hgh=float(input("height(cm)="))
#Is his health good or no
hlg=input("healthy(True/False)=")
#Conditions
A=(18<=age<=40)
B=(hgh>=155)
C=(hlg=="True" or hlg=="true")
#Check for accepting
if A and B and C:
    print("You are accepted")
else:
    print("You are rejected")
#For window still be open
input("For exit press enter")
