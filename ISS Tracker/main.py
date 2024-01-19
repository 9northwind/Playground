import requests
from datetime import datetime
import smtplib as smt
import time

MY_LAT = 12.815330
MY_LONG = 80.041618


def distance():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    iss_position = data['iss_position']
    print(iss_position)

    latitude = float(iss_position['latitude'])
    longitude = float(iss_position['longitude'])

    location = (latitude, longitude)

    if MY_LAT+5 >= latitude >= MY_LAT-5 and MY_LONG+5 >= longitude >= MY_LONG-5:
        # print("The ISS is with your range")
        return True
    else:
        # print('The ISS is not in range')
        return False


def night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }

    sun_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sun_response.raise_for_status()

    sun_data = sun_response.json()
    print(sun_data)

    sunrise = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])
    # print(sunrise)
    ist_sunrise = sunrise+6
    ist_sunset = sunset+6
    print(ist_sunset)

    present = datetime.now()
    present_hour = present.hour
    print(present_hour)

    if present_hour >= ist_sunset or present_hour<= ist_sunrise:
        print("It's Night")
        # return True
    else:
        print("It's Day")
        # return False


while True:
    time.sleep(60)
    if distance() and night():
        EMAIL = 'email.id'
        PASS = 'app password'
        with smt.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASS)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg='Subject:ISS Tracker\n\nLook Up!\nISS is overhead')

