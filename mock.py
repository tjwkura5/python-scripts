import requests

def flights():
    url = "https://api.travelpayouts.com/v2/prices/month-matrix"

    querystring = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"LAX"}

    headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f'An error occured: {e}')




flight_data = flights()
response = flight_data.json()
date = '2024-10-21'

new_list = [flight for flight in response['data'] if flight['depart_date'] == date]

# print(new_list)
first_item = new_list[0]

print(f'There is a flight from {first_item['origin']} to {first_item['destination']} scheduled on {date} with a duration of {first_item['duration']} min.')