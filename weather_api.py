  
import tkinter as tk
import requests
from PIL import Image, ImageTk

app = tk.Tk()

HEIGHT = 500
WIDTH = 600

def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
    except:
        final_str = 'There was a problem retrieving that information'
    #final_str = 'hello'
    return final_str


def get_weather(city):
    weather_key = '#####################'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': '##############', 'q': city, 'units':'imperial'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())



C = tk.Canvas(app, height=HEIGHT, width=WIDTH)


C.pack()

frame = tk.Frame(app,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
#frame_window = C.create_window(100, 40, window=frame)

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(textbox.get()))
#submit.config(font=)
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)
app.mainloop()


