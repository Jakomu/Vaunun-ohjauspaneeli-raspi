import tkinter as tk
import customtkinter as ctk
import math

KVArvo = 40
HVArvo = 20
AkkuArvo = 12.75
OletusValonvari = "#ffffff" # voiko tähän laittaa jonkun systeemimuuttujan tms., jotta saisi sen pidettyä muistissa?
OletusValonK = 0
# try: OletusValonvari
# except NameError: OletusValonvari = "#ffffff"
    
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def vaihda_vari(t):
    temperature = t/100

#     Calculate red:

    if temperature <= 66:
        red = 255
    else:
        red = temperature - 60
        red = 329.698727446 * (red ** -0.1332047592)
        if red < 0:
            red = 0
        if red > 255:
            red = 255

#     Calculate green:

    if temperature <= 66:
        green = temperature
        green = 99.4708025861 * math.log(green) - 161.1195681661
        if green < 0:
            green = 0
        if green > 255:
            green = 255
    else:
        green = temperature - 60
        green = 288.1221695283 * (green ** -0.0755148492)
        if green < 0:
            green = 0
        if green > 255:
            green = 255

#     Calculate blue:

    if temperature >= 66:
        blue = 255
    else:
        if temperature <= 19:
            blue = 0
        else:
            blue = temperature - 10
            blue = 138.5177312231 * math.log(blue) - 305.0447927307
            if blue < 0:
                blue = 0
            if blue > 255:
                blue = 255
                
#     Change RGB-value for color_box and variable:
    color_box.configure(fg_color = rgb2hex(int(red),int(green),int(blue)))
    colorLabel.configure(text=int(t))


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("800x400")

text = ctk.CTkLabel(window, text="Ohjauspaneeli", font=("default", 20))
text.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

tilatext = ctk.CTkLabel(window, text="Vaunun tila", font=("default", 16))
tilatext.place(relx=0.2, rely=0.25, anchor=tk.CENTER)

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

slider = ctk.CTkSlider(window, from_=3000, to=10000, command=vaihda_vari)
slider.place(relx=0.7, rely=0.3)

colorLabel = ctk.CTkLabel(window, text=OletusValonK)
colorLabel.place(relx=0.7, rely=0.35)

color_box = ctk.CTkButton(window, width=100, height=100, fg_color=OletusValonvari)
color_box.place(relx=0.7, rely=0.6)


window.mainloop()