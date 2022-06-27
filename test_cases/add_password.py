# user log in authentication check

def add_pw_test():
    app = GUI.Safe_Word()
    with open("database/users.txt", "r") as o:
        original = o.read()
    
    with open("database/users.txt", "w") as mod:
        mod.write("test_user\\1000\\./database/user_data/test_user.txt\\test_password\n")
    with open("database/user_data/test_user.txt", "w+") as t:
        t.write("")

    print("\ntesting GUI internal function: add_password().\nExpected: site\\name\\Plain-text\\pw\nresult:")


    app.user_key = "test_password"
    app.user_data_path = "./database/user_data/test_user.txt"
    app.add_password("site", "name", "pw", "Plain-text", [Treeview()], None)
    with open(app.user_data_path, "r") as k:
        file_content = k.read()
    print(file_content)
    if file_content == "site\\name\\Plain-text\\pw\n": print("passed")
    else: print(" ------- failed")
    try: ...
    except:
        print(" ------- failed")

    

    with open("database/users.txt", "w+") as o:
        o.write(original)
    
    


if __name__ != "__main__":
    from tkinter.ttk import Treeview
    import GUI
    print("--------------------------------------- TEST CASE: add password\n")
    add_pw_test()

if __name__ == "__main__":
    print("########## do not run thi file directly. Run ./run_test_cases.py")