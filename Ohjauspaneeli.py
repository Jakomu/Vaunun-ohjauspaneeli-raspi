import tkinter as tk
import customtkinter as ctk

KVArvo = 40
HVArvo = 20
AkkuArvo = 12.75

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("800x400")

text = ctk.CTkLabel(window, text="Ohjauspaneeli", font=("default", 20))
text.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

tilaText = ctk.CTkLabel(window, text="Vaunun tila", font=("default", 16))
tilaText.place(relx=0.2, rely=0.25, anchor=tk.CENTER)

KirkasVesi = ctk.CTkLabel(window, text="Kirkas vesi:")
KirkasVesi.place(relx=0.1, rely=0.35)
KVArvo = ctk.CTkLabel(window, text=str(KVArvo) + " %")
KVArvo.place(relx=0.25, rely=0.35)

HarmaaVesi = ctk.CTkLabel(window, text="Harmaa vesi:")
HarmaaVesi.place(relx=0.1, rely=0.45)
HVArvo = ctk.CTkLabel(window, text=str(HVArvo) + " %")
HVArvo.place(relx=0.25, rely=0.45)

AkkuV = ctk.CTkLabel(window, text="Akun jännite:")
AkkuV.place(relx=0.1, rely=0.55)
AkkuArvo = ctk.CTkLabel(window, text=str(AkkuArvo) + " V")
AkkuArvo.place(relx=0.25, rely=0.55)

window.mainloop()