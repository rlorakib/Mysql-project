from Dbhelper import dbhelper

def main():
    db = dbhelper()
    while True :
        print('************************WELCOME***************************')
        print()
        print('Press 1 to insert new user')
        print('Press 2 to display all user')
        print('PRESS 3 to delete user')
        print('PRESS 4 to update user')
        print('PRESS 5 to exit program')

        try:

            choice = int(input())
            if (choice==1):
                uid = int(input('Enter user id :'))
                username = input("Enter username:")
                phone = input('Enter phone number:')
                db.insert_user(input(uid,username,phone))
                
            elif (choice ==2):
                db.fetch_all()
                pass
            elif (choice==3):
                userid = int(input('Enter user id which on you want to delete '))
                db.delete_user(userid)
      
            elif (choice==4):
                userid = int(input('Enter user id :'))
                newName = input("Enter new username:")
                newPhone = input('Enter new phone number:')
                db.update_user(userid,newName,newPhone)
               
            elif (choice==5):
                break
            else:
                print('Invalid number ! Please try again')

        except Exception as e:
            print(e)
            print('Invalid Number ! Please try again')

if __name__=="__main__":
    main()