import http.client
import json

check_time = ['11:00', '11:30', '12:00', '12:30']
how_many_ppl = 7

booking_host= 'inline.app'
booking_url = '/api/booking-capacities?companyId=-KO9-zyZTRpTH7LNAe99&branchId=-LOcon_dHjl7H4_PR39w'

conn = http.client.HTTPSConnection(booking_host)
conn.request('GET', booking_url)
resp = conn.getresponse()

available_time = resp.read()
conn.close()

all_time = json.loads(available_time)['default']

result = []
for date, time in all_time.items():
    for t in check_time:
        if t in time:
            try:
                time[t].index(how_many_ppl)
                result.append(f'{date} has {how_many_ppl} people seats on {t}.')
            except ValueError:
                pass

if result:
    print('\n'.join(result))
else:
    print(f'No seats available for {how_many_ppl} people now')
