
import cryptographic_algorithms as crypt


def check_password(username, password):
    hasher = crypt.Enc_Fernet()

    users = []
    with open("./database/users.txt") as ul:
        users = ul.readlines()
        users = [x[:-1].split("\\") for x in users]
    
    for u in users:
        if u[0] != username: continue
        try:
            #result = hasher.encrypt(username, bytes(password, 'utf-8'))
            assert password == u[3]
            return (True, password)
        except: return (False, "")
    
    return (False, "")



result = check_password("user1", "password")

print(result)