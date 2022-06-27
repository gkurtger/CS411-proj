# user log in authentication check


def user_log_in_test():
    app = GUI.Safe_Word()
    with open("database/users.txt", "r") as o:
        original = o.read()
    
    with open("database/users.txt", "w") as mod:
        mod.write("test_user\\1000\\./database/user_data/test_user.txt\\test_password\n")
    with open("database/user_data/test_user.txt", "w+") as t:
        t.write("")

    print("testing GUI internal function: user_authentication() ...", end="")
    try:
        excode = app.user_authentication("test_user", "test_password", None)
        if excode == 0:
            print("success.")
        else: print(" ------- failed")
    except:
        print(" ------- failed")

    
    print("\ntesting Backend.check_password(). Expected: (True, './database/user_data/test_user.txt', 'test_password')\noutput:")
    try:
        login = GUI.Backend.check_password("test_user", "test_password")
        print(login)
        if login == (True, './database/user_data/test_user.txt', 'test_password'):
            print("Passed")
        else: print(" ------- failed")
    except:
        print(" ------- failed")

    
    
    
    print("\ntesting Backend.check_password(). Expected: (False, '', '')\noutput:")
    try:
        login = GUI.Backend.check_password("test_user", "lmao")
        print(login)
        if login == (False, '', ''):
            print("Passed")
        else: print(" ------- failed")
    except:
        print(" ------- failed")
    

    with open("database/users.txt", "w+") as o:
        o.write(original)
    
    


if __name__ != "__main__":
    import GUI
    print("--------------------------------------- TEST CASE: user log in\n")
    user_log_in_test()

if __name__ == "__main__":
    print("########## do not run thi file directly. Run ./run_test_cases.py")