
def register():
    account_name = input("Enter Account Name:")
    while True:
        pin = int(input("Enter 4 digit pin:"))
        if pin not in range (1000,10000):
            print("invalid pin")
         print(f'Please try again!')
    else:
        print("Registration successfull")
        process = False
        return account_name, pin
    

    name, pin = register()
    print(name)
    print (pin)
    
         name =input("Enter your student name:")
gender = input("Enter student gender:")
age = int(input("Enter student age:"))
phone_num = input("Enter your student phone number:")
email_address = input("Enter your student email address:")



# print(f'student Name: {name}')
# print{f'student Gender:{gender}'}
# print{f'student Age:{age}'}
# print{f'student CEll Number:{phone_num}'}
# print{f'studentMail:{email_address}'}



 student_file ={
     "name":name,
     "gender": gender,
     "age":age,
     "phone_num":phone_num,
     "mail":email_address 
 }
    

    return student_file