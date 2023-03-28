# Handling APIs (Application programming interface) which allows us to interact with other systems.
# API Endpoints:
# The Location where API exists is called API Endpoint.
# Example:
# This URL 'http://api.open-notify.org/iss-now.json' is endpoint of ISS (International Space Station).

import requests  # use to interact with APIs.

# My locations longitude and latitude.
# use this https://www.latlong.net/ to find.
MY_LONG = 69.345116
MY_LAT = 30.666121

response = requests.get("http://api.open-notify.org/iss-now.json")
# Print response:
# print(response)  # It will give <Response [200]> output.

# Now, question here is that what is 200:
# This is code which are too much, but we can categorize it as:

# XX means any number here.

#           Code      Meaning
#           1XX       Hold on.
#           2XX       Here You go.
#           3XX       Go away.
#           4XX       You screwed up. i.e 404
#           5XX       I screwed up.

print(response.json())  # It will give all data.

# Exception handling:
response.raise_for_status()

# Current location of ISS.
location = response.json()['iss_position']
# ISS Longitude:
iss_long = location['longitude']
# ISS Latitude:
iss_lat = location['latitude']

# Check if ISS is +5 or -5 to your location.

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get('https://www.latlong.net/', params=parameters)
response.raise_for_status()
print(response.json())
