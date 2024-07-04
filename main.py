from tkinter import *
import requests
from threading import Thread


# -----------------------------SPLASH SCREEN , API REQUESTING AND CURRENT DATA------------------------------#
def splash_screen():
    popup = Toplevel()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    window_width = 400
    window_height = 200

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # hide the title bar
    popup.overrideredirect(True)
    popup_label = Label(popup, text='Loading, please wait......', font=('Arial', 10, 'bold'))
    popup_label.pack(padx=50, pady=80)
    window.after(5000, popup.destroy)


def api_call():

    value = str(city.get())

    headers = {
        "X-RapidAPI-Key": "79b3f45fd3msha0b643199a5e363p195fc9jsn9fedfa50cdb5",
        "X-RapidAPI-Host": "the-weather-api.p.rapidapi.com"
    }

    p = {
        "cityName": value,
    }
    response = requests.get(f"https://the-weather-api.p.rapidapi.com/api/weather/{p['cityName']}", headers=headers)
    record = (response.json()['data'])

    cw.insert(0, record['current_weather'])
    t.insert(0, record['temp'])
    w.insert(0, record['wind'])
    h.insert(0, record['humidity'])
    if record['insight_description'] == '':
        d.insert(0, record['aqi_description'])
    else:
        d.insert(0, record['insight_description'])


def search():
    splash_screen()
    api_thread = Thread(target=api_call)
    api_thread.start()


# -----------------------------CLOSING THE WINDOW------------------------------#
def close_window():
    window.destroy()


# -----------------------------DELETING DATA------------------------------#
def delete():
    city.delete(0, END)
    cw.delete(0, END)
    t.delete(0, END)
    w.delete(0, END)
    h.delete(0, END)
    d.delete(0, END)


# ---------------------------------UI SETUP--------------------------------------------#

window = Tk()
window.title('WEATHER FORECAST')
window.config(bg="#8ECDDD")
window.state('zoomed')

logo = PhotoImage(file='icon.png')
canvas = Canvas(width=360, height=300, bg="#8ECDDD", highlightthickness=0)
a = canvas.create_image(180, 150, image=logo)
canvas.grid(row=0, column=0, columnspan=2)

label = Label(text='Write Your City / Country : ', font=('Arial', 20, 'bold'), bg="#8ECDDD",
              highlightthickness=0)
label.grid(row=1, column=0)

entry_frame = Frame(relief='ridge', bd=0)
entry_frame.grid(row=1, column=1)

city = Entry(entry_frame, width=20, font=('Arial', 20, 'italic'))
city.focus()
city.grid()

button = Button(text='Search', width=10, height=2, font=('Arial', 10, 'bold'), command=search)
button.grid(row=1, column=2, padx=20)

curr_weather = Label(text='Current Weather :', font=('Arial', 15, 'bold'), bg="#8ECDDD", highlightthickness=0)
curr_weather.grid(row=2, column=0, padx=10, pady=10)

cw_frame = Frame(width=2, relief='ridge', bd=0)
cw_frame.grid(row=2, column=1)

cw = Entry(cw_frame, width=30, font=('Arial', 10, 'italic'))
cw.grid()

temp = Label(text='Temperature :', font=('Arial', 15, 'bold'), bg="#8ECDDD", highlightthickness=0)
temp.grid(row=3, column=0, padx=10, pady=10)

temp_frame = Frame(relief='ridge', bd=0)
temp_frame.grid(row=3, column=1)

t = Entry(temp_frame, width=10, font=('Arial', 10, 'italic'))
t.grid()

wind = Label(text='Wind Speed :', font=('Arial', 15, 'bold'), bg="#8ECDDD", highlightthickness=0)
wind.grid(row=4, column=0, padx=10, pady=10)

w_frame = Frame(borderwidth=5, relief='ridge', bd=0)
w_frame.grid(row=4, column=1)

w = Entry(w_frame, width=10, font=('Arial', 10, 'italic'))
w.grid()

humidity = Label(text='Humidity :', font=('Arial', 15, 'bold'), bg="#8ECDDD", highlightthickness=0)
humidity.grid(row=5, column=0, padx=10, pady=10)

h_frame = Frame(borderwidth=5, relief='ridge', bd=0)
h_frame.grid(row=5, column=1)

h = Entry(h_frame, width=10, font=('Arial', 10, 'italic'))
h.grid()

des = Label(text='Description :', font=('Arial', 15, 'bold'), bg="#8ECDDD", highlightthickness=0)
des.grid(row=6, column=0, padx=10, pady=10)

d_frame = Frame(borderwidth=5, relief='ridge', bd=0)
d_frame.grid(row=6, column=1)

d = Entry(d_frame, width=50, font=('Arial', 10, 'italic'))
d.grid()

close = Button(text='OKAY, I AM DONE.', font=('Arial', 10, 'bold'), command=close_window)
close.grid(row=7, column=0, padx=10, pady=10)

clear = Button(text='CLEAR ALL', font=('Arial', 10, 'bold'), command=delete)
clear.grid(row=7, column=1, padx=10, pady=10)

window.mainloop()
