username = "informatika"
password = "12345678"

for i in range(3):

    input_username = input("Username anda : ")
    input_password = input("Password anda : ")
    if input_username == username and input_password == password:
        print("Berhasil Login!")
        break
    else:
        print("Username atau password salah coba lagi")
else:
    print("Akun Anda Diblokir")