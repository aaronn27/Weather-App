import tkinter as tk
import requests
import time

# Function to get weather data
def getWeather(canvas):
    city = textfield.get()  # Get the city name from the text field
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=Enter you API Id"  # API URL with city and API key
    json_data = requests.get(api).json()  # Get the JSON data from the API
    condition = json_data['weather'][0]['main']  # Extract weather condition
    curr_temp = int(json_data['main']['temp'] - 273.15)  # Convert temperature from Kelvin to Celsius
    min_temp = int(json_data['main']['temp_min'] - 273.15)  # Convert minimum temperature from Kelvin to Celsius
    max_temp = int(json_data['main']['temp_max'] - 273.15)  # Convert maximum temperature from Kelvin to Celsius
    pressure = json_data['main']['pressure']  # Extract pressure
    humidity = json_data['main']['humidity']  # Extract humidity
    wind = json_data['wind']['speed']  # Extract wind speed
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))  # Convert sunrise time to readable format
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))  # Convert sunset time to readable format

    # Prepare the final information strings
    final_info = condition + "\n" + str(curr_temp) + "°C"
    final_data = "\n" + "Maximum Temperature: " + str(max_temp) + "\n" + "Minimum Temperature: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    
    # Update the labels with the weather information
    label1.config(text=final_info)
    label2.config(text=final_data)

# Create the main window
canvas = tk.Tk()
canvas.geometry("600x500")  # Set the window size
canvas.title("Weather App")  # Set the window title

# Define font styles
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Create and pack the text field
textfield = tk.Entry(canvas, justify='center', font = t)
textfield.pack(pady = 20)
textfield.focus()  # Set focus to the text field
textfield.bind('<Return>', getWeather)  # Bind the Enter key to the getWeather function

# Create and pack the labels
label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

# Run the main loop
canvas.mainloop()
