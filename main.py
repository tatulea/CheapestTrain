import requests
import json
from datetime import datetime, timedelta
from dateutil import parser as dp
from operator import itemgetter


headers = {
    'x-version': '1.3.14562',
    'origin': 'https://www.thetrainline.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB',
    'sec-fetch-mode': 'cors',
    'cookie': 'reset_currency=1; wasabiId=57b27eda-7fa6-4284-b0bf-2dbad801ddb7; currency_code=GBP; AMCVS_5D570C3A53DB50FA0A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C62974749092022106353101875068247214066; _ga=GA1.2.1499674015.1571047534; TANGO-371=true; temp_basket_id=d8209a53-b3d8-4c4a-a516-e7c26ff7dd85; basket_id=f1e58b16-a2d4-41f4-a332-8bebf1a95381; eu_cookies_visi={%22version%22:3%2C%22feature%22:%22%22}; ab.storage.sessionId.ed8871ee-f4e9-4188-bf1c-3499e423fa02=%7B%22g%22%3A%228404fcef-79ed-2525-a9ab-66a890f5e481%22%2C%22e%22%3A1571049343188%2C%22c%22%3A1571047543190%2C%22l%22%3A1571047543190%7D; ab.storage.deviceId.ed8871ee-f4e9-4188-bf1c-3499e423fa02=%7B%22g%22%3A%2234bf441b-3c90-a331-6b3b-f0c661940a6c%22%2C%22c%22%3A1571047543209%2C%22l%22%3A1571047543209%7D; ravelinSessionUuid=2a12d765-b27f-45b4-9ea7-7b9a707dca9f; ravelinUuid=382ba06d-86cc-42d0-a53d-d62c98a0e740; ravelinDeviceId=382ba06d-86cc-42d0-a53d-d62c98a0e740; _gcl_au=1.1.1725438725.1571047549; s_cc=true; _fbp=fb.1.1571047553557.1086642220; RT="z=1&dm=www.thetrainline.com&si=ade12e0e-ff52-45b3-ae0f-37dce6a95950&ss=k1qbp4rj&sl=0&tt=0&hd=1qoz&bcn=%2F%2F0211c83e.akstat.io%2F"; EUCRO-234=1; RMROCKET-1248=1; DWEB-8052=2; SDDM-292=1; OPTI-707=1; SDDM-1119=0; OPTI-826=0; EUCRO-413=0; UC-91=1; EUCRO-288=1; EUCRO-555=1; OPTI-862=0; SSSC=266.G6747597757873292912.3|42403.1342040:45351.1499196:45371.1499870:45656.1515029:46050.1536398:46991.1583596:47144.1589862:47177.1592036:47179.1592080:47236.1594594:47448.1604381:47531.1609320:47776.1620126:47822.1621783:47879.1626134:47900.1628012:47901.1628022:47984.1630752:48001.1631885:48091.1636206:48119.1638627:48149.1639708:48150.1639717:48167.1640545:48178.1640712:48179.1640722:48181.1640754:48313.1647176:48364.1649932; wSession=703-6Z696-6Z491-3A492-4A493-4Z495-4A499-4A500-4A504-4A494-2Z501-1A505-1Z721-5A; TANGO-EDGE=0; AKA_A2=A; AMCV_5D570C3A53DB50FA0A490D4D%40AdobeOrg=-330454231%7CMCIDTS%7C18189%7CMCMID%7C62974749092022106353101875068247214066%7CMCAAMLH-1572082634%7C6%7CMCAAMB-1572082634%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1571485034s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; _gid=GA1.2.1863864999.1571477836; analyticsSessionId=1571477835881.ieio19; login=0; s_lv_s=Less%20than%207%20days; SSID=CACIXB2WAQAAAABpSKRdcIZCFWlIpF0DAAAAAAAAAAAAQtmqXQCB4Em4AAHkShgAQtmqXQEAcLsAASDiGABC2apdAQA7sQAB3uIWAELZql0BABW8AAEcBRkAQtmqXQEAj7cAAewpGABC2apdAQCjpQABWHoUAELZql0BAEu4AAEQSxgAQtmqXQEAgbsAAY3mGABC2apdAQD3uwAB4wAZAELZql0BAAe7AAEW0BgAQtmqXQEAhLgAA-JUGABpSKRdAwAcuwABbNcYAELZql0BAKC6AAGeuBgAQtmqXQEAHbsAAXbXGABC2apdAQDiswABjnEXAELZql0BABa8AAElBRkAQtmqXQEA27sAAW73GABC2apdAQA1vAABMgkZAELZql0BAM66AAEXvxgAQtmqXQEAMrwAAQgJGQBC2apdAQBYuQABHXsYAELZql0BACexAAE84BYAQtmqXQEAM7wAARIJGQBC2apdAQDsvAABDC0ZAELZql0BALm8AAFIIhkAQtmqXQEAKLgAA2ZCGABC2apdAQBYsgADFR4XAGlIpF0DAKu5AAFojhgAQtmqXQEAJ7wAAWEIGQBC2apdAQA; pinned_results_message_hidden=false; wExperienced=OPTI-491-3=1,OPTI-493-4=0,OPTI-504-4=1; s_sq=%5B%5BB%5D%5D; context_alias_id=d12c907d-932b-4540-9462-87dc10edabb6; context_id=a84bd86f-8127-45ce-908d-ac8ab0b7c0ce; SSRT=UN6qXQADAA; s_nr=1571479127485-Repeat; s_lv=1571479127491; _tq_id.TV-544536-1.8433=ae8fce999340eb29.1571047553.0.1571479139..; _gat_trainlineGATracker=1; _gat_1c2a5c4a9563fa50f39c8fa2e8ff4296=1; ravelinCanFingerprint=1; RT="z=1&dm=thetrainline.com&si=ade12e0e-ff52-45b3-ae0f-37dce6a95950&ss=k1xe3d72&sl=0&tt=0&hd=yzu&bcn=%2F%2F684dd307.akstat.io%2F"',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36',
    'content-type': 'text/plain;charset=UTF-8',
    'accept': 'application/json',
    # 'referer': 'https://www.thetrainline.com/book/results?origin=dfa822c7546111f40356479a6bd7a60d&destination=8ad03cfded18966635d0b4c821fc8e62&outwardDate=2019-12-05T10%3A45%3A00&outwardDateType=departAfter&journeySearchType=single&passengers%5B%5D=1989-10-19&selectedOutward=Di8Tj7fYcRk%3D%3AFUp5sRsbGyg%3D',
    'authority': 'www.thetrainline.com',
    'sec-fetch-site': 'same-origin',
}

data = {
    "passengers": [{
        "dateOfBirth": "1989-10-19"
    }],
    "isEurope": False,
    "cards": [],
    "transitDefinitions": [{
        "direction": "outward",
        "origin": "8ad03cfded18966635d0b4c821fc8e62",
        "destination": "dfa822c7546111f40356479a6bd7a60d",
        "journeyDate": {
            "type": "departAfter",
            "time": "2019-12-05T00:00:00"
        }
    }],
    "type": "single",
    "maximumJourneys": 15,
    "includeTravelTogetherFares": True,
    "includeRealtime": False,
    "requestedCurrencyCode": "GBP"
}

starting_date = datetime(year=2019, month=12, day=12, hour=0, minute=0)
ending_date = datetime(year=2019, month=12, day=15, hour=0, minute=0)
journeys_set = set()

while (starting_date < ending_date):
    data["transitDefinitions"][0]["journeyDate"]["time"] = starting_date.isoformat()

    response = requests.post('https://www.thetrainline.com/api/journey-search/', headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        print(response.text)
        break
    else:
        response_json = response.json()["data"]["journeySearch"]
        journeys = response_json['journeys']
        # print("Found", len(journeys), "journeys")

        last_journey = None
        for id, journey in journeys.items():
            depart_at = dp.isoparse(journey["departAt"])
            if depart_at.day > starting_date.day:
                # Next day
                cheapest_journey = min(journeys_set, key=itemgetter(1))
                cheapest_journeys = filter(lambda x: x[1] == cheapest_journey[1], journeys_set)
                cheapest_journeys = sorted(cheapest_journeys, key=itemgetter(0))
                
                print("-->", starting_date.strftime("%d/%m/%Y"))
                for cheapest_journey in cheapest_journeys:
                    print("    {DATE} - {PRICE}".format(
                        DATE=cheapest_journey[0],
                        PRICE=cheapest_journey[1],
                    ))

                starting_date = (starting_date + timedelta(days=1)).replace(hour=0, minute=0)
                last_journey = None
                journeys_set = set()
                print("\r\n")
                break

            last_journey = journey
            section = journey["sections"][0] # Can be more than 1?

            prices = []
            for alternative in response_json["sections"][section]["alternatives"]:
                price = response_json["alternatives"][alternative]["price"]["amount"]
                prices.append(price)
            
            journeys_set.add((
                depart_at,      # departure time
                min(prices)     # the price for this journey
            ))
        
        if last_journey != None:
            starting_date = dp.isoparse(last_journey["departAt"]) + timedelta(minutes=1)
            starting_date = starting_date.replace(tzinfo=None)