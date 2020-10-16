# login simulation
def login(username, pwd):
    for i in range(3):
        user_name_str = input("please input your username:\n")
        if user_name_str == username:
            break
        else:
            print('wrong username, input again!\n')
            if i == 2:
                print('username wrong 3 times. login exit')
                return

    for i in range(3):
        passwd_str = input("please input your passwd:\n")
        if passwd_str == pwd:
            print("login successfully")
            return
        else:
            print("wrong passwd input again!\n")
    print("passwd wrong 3 times .Login Exit")


if __name__ == "__main__":
    name = 'kamisama'
    passwd = '123'
    login(name, passwd)
