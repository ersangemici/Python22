phone_book= {}
while True :
    x = int(input("Select the action you want to do ..... 1) Add person 2) delete contact 3)Log out\n"))
    if x == 1 :
        name = input("enter contact name\n")
        num = int(input("enter the person's number\n"))
        temporary = {name : num }
        phone_book.update(temporary)
        print(phone_book)
        print("--------------------------------")
    elif  x ==  2 :
        print(phone_book)
        del1 = input("select the contact you want to delete\n")

        phone_book.pop(del1) 
        print(phone_book)
        print("--------------------------------")
    elif x == 3:
        print("Checking Out")
        break
    else:
        print("Checking Out")
        break
