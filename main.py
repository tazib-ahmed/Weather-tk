import tkinter as tk
import datetime as dt
import requests
import pandas as pd
from PIL import ImageTk, Image
import customtkinter as ctk


codes = pd.read_csv("codes.csv")

canvas = tk.Tk()
canvas.geometry("650x500")
canvas.title("Weather")
canvas.iconbitmap("icons/sunny.ico")

f = ("Birch Std", 20, "bold")
t = ("Birch Std", 30, "bold")

def getweather(canvas):
    BASEURL = "https://api.weatherapi.com/v1/"
    KW = "current.json?"
    KEY = open("api", mode="r").read()
    CITY = textfield.get()

    url = BASEURL + KW + "key=" + KEY + "&q=" + CITY

    response = requests.get(url).json()

    tempc = response['current']['temp_c']
    feels_like = response['current']['feelslike_c']
    wind = response['current']['wind_kph']
    condition = response['current']['condition']['text']
    humidity = response['current']['humidity']
    date = dt.datetime.strptime(response['location']['localtime'], "%Y-%m-%d %H:%M")
    time = date.time()
    code = response['current']['condition']['code']
    status = "night" if time.hour < 6 or time.hour < 18 else "day"

    imgcode = codes.icon[codes.code == code].values[0]
    imgst = codes[status][codes.code == code].values[0]
    path = "weathericons" + "/" + status + "/" + str(imgcode) + ".png"
    image = ctk.CTkImage(
        dark_image=Image.open(path),
        size = (100,100))
    final_info =  condition + "\n" + str(tempc) + chr(176) +"C\n"
    final_data =  "Feels Like " + str(feels_like) + chr(176) + "C" "\n" + "Wind " + str(wind) + " km/h" + "\n" + "Humidity " + str(humidity) + "%" + "\n"

    label.configure(image=image, text="")
    label1.config(text=final_info)
    label2.config(text=final_data)

textfield = tk.Entry(canvas, font= t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", getweather)

label = ctk.CTkLabel(canvas)
label.pack( )
label1 = tk.Label(canvas, font= t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()



canvas.mainloop()