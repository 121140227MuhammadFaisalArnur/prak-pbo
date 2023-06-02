import tkinter as tk
from PIL import Image, ImageTk
import random

# inisialisasi window
root = tk.Tk()
root.geometry("1080x720")
root.title("Game suit Indonesia")

# definisi frame tombol
frame_bawah = tk.Frame(root)
frame_bawah.pack(side="bottom", pady=100)
frame_atas = tk.Frame(root)
frame_atas.pack(side="top", pady=10)

#definisi skor
skor_user = 0
skor_komputer = 0

# definisi gambar
gambar_kelingking = Image.open("kelingking.jpg")
gambar_kelingking = gambar_kelingking.resize((100, 100))
gambar_kelingking = ImageTk.PhotoImage(gambar_kelingking)

gambar_telunjuk = Image.open("telunjuk.jpg")
gambar_telunjuk = gambar_telunjuk.resize((100, 100))
gambar_telunjuk = ImageTk.PhotoImage(gambar_telunjuk)

gambar_jempol = Image.open("jempol.jpg")
gambar_jempol = gambar_jempol.resize((100, 100))
gambar_jempol = ImageTk.PhotoImage(gambar_jempol)

# definisi label
user_label = tk.Label(root, text="kamu", font=("Segoe UI", 16))
computer_label = tk.Label(root, text="komputer", font=("Segoe UI", 16))
hasil_komputer = tk.Label(root, font=("Segoe UI", 16), pady=20)
hasil_pertandingan = tk.Label(root, font=("Segoe UI", 20), pady=20)
hasil_user = tk.Label(root, font=("Segoe UI", 16), pady=20)


# definisikan tombol
tombol_kelingking = tk.Button(frame_bawah, image=gambar_kelingking, command=lambda: main("kelingking"))
tombol_telunjuk = tk.Button(frame_bawah, image=gambar_telunjuk, command=lambda: main("telunjuk"))
tombol_jempol = tk.Button(frame_bawah, image=gambar_jempol, command=lambda: main("jempol"))
restart_btn = tk.Button(frame_atas, text="Mulai Ulang", font=("Segoe UI", 12), command=lambda: restart())
quit_btn = tk.Button(frame_atas, text="Keluar", font=("Segoe UI", 12), command=root.quit)

# penempatan tombol jempol kelingking telunjuk
tombol_kelingking.pack(side="left", padx=20)
tombol_telunjuk.pack(side="left", padx=20)
tombol_jempol.pack(side="left", padx=20)


# penempatan gambar
user_label.pack(side="left")
hasil_user.pack(side="left")
computer_label.pack(side="right")
hasil_komputer.pack(side="right")
hasil_pertandingan.pack(side="bottom")

#penempatan tombol mulai ulang dan restart
quit_btn.pack(side="left", padx=10, pady=10)
restart_btn.pack(side="right", padx=10, pady=10)



# Game
def main(user_choice):

    #skor diambil dari variable global
    global skor_komputer, skor_user

    # pemilihan random komputer
    pilih = ["kelingking", "telunjuk", "jempol"]
    pilihan_komputer = random.choice(pilih)

    # menentukan pemenang
    if user_choice == pilihan_komputer:
        hasil_pertandingan.config(text="seri")
    elif (user_choice == "kelingking" and pilihan_komputer == "jempol") or (user_choice == "telunjuk" and pilihan_komputer == "kelingking") or (user_choice == "jempol" and pilihan_komputer == "telunjuk"):
        hasil_pertandingan.config(text="kamu menang!")
        skor_user += 1
    else:
        hasil_pertandingan.config(text="kamu kalah!")
        skor_komputer += 1


    # update gambar
    if user_choice == "kelingking":
        user_label.config(image=gambar_kelingking)
        hasil_komputer.config(text=f"skor komputer {skor_komputer}")
        hasil_user.config(text=f"skor kamu {skor_user}")
    elif user_choice == "telunjuk":
        user_label.config(image=gambar_telunjuk)
        hasil_komputer.config(text=f"skor komputer {skor_komputer}")
        hasil_user.config(text=f"skor kamu {skor_user}")
    else:
        user_label.config(image=gambar_jempol)
        hasil_komputer.config(text=f"skor komputer {skor_komputer}")
        hasil_user.config(text=f"skor kamu {skor_user}")

    if pilihan_komputer == "kelingking":
        computer_label.config(image=gambar_kelingking)
        hasil_komputer.config(text=f"skor komputer {skor_komputer}")
        hasil_user.config(text=f"skor kamu {skor_user}")
    elif pilihan_komputer == "telunjuk":
        computer_label.config(image=gambar_telunjuk)
        hasil_komputer.config(text=f"skor komputer {skor_komputer}")
        hasil_user.config(text=f"skor kamu {skor_user}")
    else:
        computer_label.config(image=gambar_jempol)
        hasil_komputer.config(text=f"skor komputer {skor_komputer}")
        hasil_user.config(text=f"skor kamu {skor_user}")

    #menentukan akhir permainan
    if skor_komputer >= 5:
        hasil_pertandingan.config(text="game selesai, kamu kalah!")
    elif skor_user >= 5:
        hasil_pertandingan.config(text="game selesai, kamu menang!")
    
    if skor_komputer > 4 or skor_user > 4:
        tombol_kelingking.config(state="disabled")
        tombol_telunjuk.config(state="disabled")
        tombol_jempol.config(state="disabled")
 

#fungsi untuk memulai game dari awal
def restart():
    global skor_user, skor_komputer

    skor_user = 0
    skor_komputer = 0

    user_label.config(image="")
    computer_label.config(image="")
    hasil_user.config(text="")
    hasil_komputer.config(text="")
    hasil_pertandingan.config(text="")

    tombol_kelingking.config(state="normal")
    tombol_telunjuk.config(state="normal")
    tombol_jempol.config(state="normal")


#menjalankan program
root.mainloop()
