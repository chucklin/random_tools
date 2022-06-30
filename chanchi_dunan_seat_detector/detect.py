import http.client
import json

from typing import List

check_time = ['11:00', '11:30', '12:00', '12:30']
how_many_ppl = 7

def main(check_time: List[str], how_many_ppl: int):
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
            if t in time and how_many_ppl in time[t]:
                result.append(f'{date} has {how_many_ppl} people seats on {t}.')

    if result:
        print('\n'.join(result))
    else:
        print(f'No seats available for {how_many_ppl} people now')

if __name__ == '__main__':
    main(check_time, how_many_ppl)
