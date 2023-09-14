from django.shortcuts import render
from weather_app.forms import PlaceForm 
import requests

api_key = "API_KEY"

def index(request):
    error = ""
    data = None

    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = request.POST['place'].capitalize()

            response_cords = requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=5&appid={api_key}").json()
            
            if response_cords:

                lat = response_cords[0].get('lat')
                lon = response_cords[0].get('lon')
                
                response_weather = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}").json()
                temp = round(response_weather["main"]["temp"] - 273.15)

                image_id = response_weather["weather"][0]["icon"]
                image = f"https://openweathermap.org/img/wn/{image_id}@4x.png"

                description = response_weather["weather"][0]["main"]

                humidity = str(response_weather["main"]["humidity"]) + "%"

                wind = str(round(response_weather["wind"]["speed"])) + " m/s"

                data = {
                    "place": place,
                    "temp": temp,
                    "image": image,
                    "description": description,
                    "humidity": humidity,
                    "wind": wind,
                }

            else:
                error = 'Unknown location'
   
    form = PlaceForm()    

    context = {
                "form": form,
                "data": data,
                "error": error,
            }

    return render(request, "weather_app/index.html", context=context)