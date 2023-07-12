# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:07:52 2023

@author: Obaid
"""

import tkinter as tk
import requests
import json

class Weather_App:
    def __init__(self):
    
        self.window = tk.Tk()
        self.window.title("Weather App")
        self.window.geometry("500x500")
        
        city_label = tk.Label(self.window, text='Type City', bd=8, width=30)
        city_label.place(x=20, y=30)
        city_text = tk.StringVar()
        city_text.set('')
        city_entry = tk.Entry(self.window, bd=8, width=30, textvariable=city_text)
        city_entry.place(x=20, y=70)
        
        country_label = tk.Label(self.window, bd=8, width=30, text='Type Country')
        country_label.place(x=250, y = 30)
        country_text = tk.StringVar()
        country_text.set("")
        country_entry = tk.Entry(self.window, bd=8, width=30, textvariable=country_text)
        country_entry.place(x=250, y=70)
        
        enter_button = tk.Button(self.window, text='Confirm', bg='lime', bd=8, width=30, command=lambda: self.display(city_text, country_text))
        enter_button.place(x=100, y=150)
        self.window.mainloop()

    def display(self, city_text, country_text):
        # Set the API endpoint URL
        url = "https://api.openweathermap.org/data/2.5/weather"
        
        # Set the location and API key as parameters
        params = {
            "q": city_text.get() +", " + country_text.get(),
            "appid": "3077029f1f6ed92b27d129b191bd7cfd"
        }
        
        # Send the GET request to the API
        response = requests.get(url, params=params)
        
        # Retrieve the API response and parse it as JSON
        data = response.json()
        # Process the weather data
        if response.status_code == 404:  # Check if the request was successful
            # Access the weather information from the response data
            display = tk.Label(self.window, bd=60, width =60, text= "Incorrect Country or City Please Type again")
            display.place(x=20, y=220)
        else:
            # Access the weather information from the response data
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_description = data["weather"][0]["description"]
        
            # Convert temperature from Kelvin to Celsius
            temperature_celsius = temperature - 273.15
        
            # Display the weather information
            display_temp = tk.Label(self.window, bd=30, width=60, text="Temperature:  "+ str(temperature_celsius) + "°C")
            display_temp.place(x=20, y = 200)
            display_humidity = tk.Label(self.window, bd=30, width=60, text ="Humidity: "+ str(humidity)+ "%")
            display_humidity.place(x=20, y = 250)
            display_description = tk.Label(self.window, bd=30, width=60, text="Weather Description: "+ str(weather_description))
            display_description.place(x=20, y = 300)
    
            print("Temperature:", temperature_celsius, "°C")
            print("Humidity:", humidity, "%")
            print("Weather Description:", weather_description)
    
wapp = Weather_App()
