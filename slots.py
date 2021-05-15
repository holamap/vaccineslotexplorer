# set in 1 minutes loop or deploy in cron 
# can use python 3
# you can creare replica of codes with different pin and dates by changing params  or improve the code or simply incorporating input params in the code

import requests
import json

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'
headers = requests.utils.default_headers()

young_age_group = 18
old_age_group = 45

## can create multiple pin and date ranges

pincode = "201301"
date = "16-05-2021"

params = {'pincode':pincode,'date':date}

headers.update(
    {
        'User-Agent': 'Chrome/90.0.4430.93',
    }
)
response = requests.get(url=url, params= params, headers=headers)

for doc in response.json()["centers"]:
	for session in doc['sessions']:
		if session['min_age_limit'] == young_age_group and session['available_capacity_dose1'] > 0:
			print(session['available_capacity_dose1'])
			print('\a')	
			## This ^^ print will give you small ding-ding system default ping sound make speakers up before deployment

