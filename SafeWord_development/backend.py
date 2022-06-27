import cryptographic_algorithms as crypt



class Backend():

    list_of_encryptions = dict()
    for cls in crypt.Enc_algorithm.__subclasses__():
        list_of_encryptions[cls.name] = cls

    def read_database(path):
        with open(path, 'r') as ul:
            items = ul.readlines()
            items = [x[:-1].split("\\") if x[-1]=="\n" else x.split("\\") for x in items]
        
        return items

    def check_password(username, password):
        # hasher = crypt.Enc_Fernet()

        users = []
        users = Backend.read_database("./database/users.txt")
        for u in users:
            if u[0] != username: continue
            try:
                #result = hasher.encrypt(username, bytes(password, 'utf-8'))
                assert password == u[3]
                return (True, u[2], password)
            except: return (False, "", "")
        
        return (False, "", "")

    def edit_password(user_data_path: str,
            old_password_item: (list or tuple),
            new_password_item: (list or tuple)=None):
        # old_password_item expectd to be a list or tuple (website, username, encryption)
        pw_list = Backend.read_database(user_data_path)
        
        if old_password_item != None:
            # this means only add new password
            item = " ".join(old_password_item)
            for pw in pw_list:
                if " ".join(pw[:3]) == item:
                    pw_list.pop(pw_list.index(pw))
                    break
        
        if new_password_item != None:
            algo = Backend.list_of_encryptions[new_password_item[3]]()
            encrypted_password = algo.encrypt(new_password_item[2], "user key")
            pw_list.append(list(new_password_item[:2])+[new_password_item[3]]+[encrypted_password])
        pw_list.sort()
        with open(user_data_path, "w") as updated:
            for i in pw_list:
                updated.write("\\".join(i)+"\n")
        return