#
#Seuraavat jutut:
#- Napeille funktionaalisuus,
#  joka säätää preset arvojen mukaan kirkkauden ja värin
#- Sensoreiden yms. säädöt
#
#
#

import tkinter as tk
import customtkinter as ctk
import math

KVArvo = 40
HVArvo = 20
AkkuArvo = 12.75
SLampo = 22
ULampo = 3
OletusValonvari = "#ffffff" # voiko tähän laittaa jonkun systeemimuuttujan tms., jotta saisi sen pidettyä muistissa?
OletusKelvin = 6500 # ja sama tähän?
OletusKirkkaus = 50 # ja vielä tähän?
    
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def vaihdaVari(t):
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
    KelvinLabel.configure(text=str(int(t)) + " K")
    #tähän tulee funktio, joka säätää värin oikeasti
    
def vaihdaKirkkaus(kirkkaus):
    print(str(kirkkaus))
    #tähän tulee funktio joka säätää kirkkauden oikeasti


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

UlkoLampo = ctk.CTkLabel(window, text="Ulkolämpötila:")
UlkoLampo.place(relx=0.1, rely=0.65)
ULampoArvo = ctk.CTkLabel(window, text=str(ULampo) + " °C")
ULampoArvo.place(relx=0.25, rely=0.65)

SisaLampo = ctk.CTkLabel(window, text="Sisälämpötila:")
SisaLampo.place(relx=0.1, rely=0.75)
SLampoArvo = ctk.CTkLabel(window, text=str(SLampo) + " °C")
SLampoArvo.place(relx=0.25, rely=0.75)

valotext = ctk.CTkLabel(window, text="Valot", font=("default", 16))
valotext.place(relx=0.68, rely=0.25, anchor=tk.CENTER)

ValotVirta = ctk.CTkButton(window, text="OFF", height=60, width=80)
ValotVirta.place(relx=0.5, rely=0.40, anchor=tk.CENTER)

ValotVirta = ctk.CTkButton(window, text="Lämmin", height=60, width=80)
ValotVirta.place(relx=0.62, rely=0.40, anchor=tk.CENTER)

ValotVirta = ctk.CTkButton(window, text="Perus", height=60, width=80)
ValotVirta.place(relx=0.74, rely=0.40, anchor=tk.CENTER)

ValotVirta = ctk.CTkButton(window, text="Kylmä", height=60, width=80)
ValotVirta.place(relx=0.86, rely=0.40, anchor=tk.CENTER)

KelvinSlider = ctk.CTkSlider(window, from_=3000, to=10000, command=vaihdaVari, width=350)
KelvinSlider.set(OletusKelvin)
KelvinSlider.place(relx=0.68, rely=0.6, anchor=tk.CENTER)

KelvinLabel = ctk.CTkLabel(window, text=str(OletusKelvin) + " K", height=8)
KelvinLabel.place(relx=0.68, rely=0.65, anchor=tk.CENTER)

KirkkausSlider = ctk.CTkSlider(window, from_=0, to=100, command=vaihdaKirkkaus, width=350)
KirkkausSlider.set(OletusKirkkaus)
KirkkausSlider.place(relx=0.68, rely=0.75, anchor=tk.CENTER)

KirkkausLabel = ctk.CTkLabel(window, text=str(OletusKirkkaus) + " %", height=8)
KirkkausLabel.place(relx=0.68, rely=0.8, anchor=tk.CENTER)

color_box = ctk.CTkButton(window, width=100, height=50, fg_color=OletusValonvari, text="Valojen testiboxi")
color_box.place(relx=0.9, rely=0.1, anchor=tk.CENTER)


window.mainloop()