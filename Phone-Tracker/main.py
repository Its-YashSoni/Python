import phonenumbers
from phonenumbers import geocoder
import folium as fol 
from test import number
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import webbrowser
from phonenumbers import timezone
import os

key = "e4e03a35044049fa884de7da6f5c2d1f"

check_number= phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)


service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
print(timezone.time_zones_for_number(service_provider))



map_loc = fol.Map(location=[lat,lng], zoom_start=1)
fol.Marker([lat,lng],popup=number_location).add_to(map_loc)


map_loc.save("location.html")


webbrowser.open('file://' + os.path.realpath('location.html'))