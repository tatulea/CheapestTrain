import requests
import json
from datetime import datetime, timedelta
from dateutil import parser as dp
from operator import itemgetter


headers = {
    'authority': 'www.thetrainline.com',
    'x-version': '1.3.15228',
    'origin': 'https://www.thetrainline.com',
    'accept-language': 'en-GB',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'sec-fetch-dest': 'empty',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    # 'referer': 'https://www.thetrainline.com/book/results?origin=dfa822c7546111f40356479a6bd7a60d&destination=8ad03cfded18966635d0b4c821fc8e62&outwardDate=2020-02-23T18%3A30%3A00&outwardDateType=departAfter&journeySearchType=single&passengers%5B%5D=1990-02-23',
    'cookie': 'acid=4691a07b-994e-4d75-b308-4efa155cd223; reset_currency=1; TANGO-EDGE=0; AMCVS_5D570C3A53DB50FA0A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C62974749092022106353101875068247214066; _ga=GA1.2.454261820.1581939179; TANGO-371=true; eu_cookies_visi={%22version%22:3%2C%22feature%22:%22%22}; ab.storage.sessionId.ed8871ee-f4e9-4188-bf1c-3499e423fa02=%7B%22g%22%3A%22ea05a0d3-3097-e59f-63f5-c572c0e25b27%22%2C%22e%22%3A1581940983721%2C%22c%22%3A1581939183724%2C%22l%22%3A1581939183724%7D; _abck=A75E4BC6FAA702CE06028C885FA9ED2F~0~YAAQdxdlX1mOdkBwAQAAAmDsUgMLJdYNu2kH8agYtPYA4+ciJ96yTGiIJU6WXO1wP2xXKg2/KAeCBYE6BYlLIEBylTT1dtXY7xrhTX7pr44lUjQPGbSbWkh/WP8t+HmWOWwnIHbkmf+6f7ewVAhwXwx+Y8H5D0puPb3FOQDGyQvwbY5gz1c1bkfkqfSe++33FIFP2QrIGO9f3KqfNDPA/pjYE2PRmm1LdmI2yHMAUxtiZfbn6I6ENhSa/kXYis7sws9wjC7AxpAJ1HDFJzz9bJwSCVdZhr3XG+d8DcX4LICIdijVYTojQB9qS77xbTJ95hFx44zdcl2AwsZCNA==~-1~-1~-1; ravelinSessionUuid=84cc6bdd-3b66-4057-9800-3c3abf2b8453; ravelinDeviceId=8371e3e5-297c-485d-9bdd-5b32209018dd; s_cc=true; _gcl_au=1.1.1270014935.1581939194; AMCV_5D570C3A53DB50FA0A490D4D%40AdobeOrg=-330454231%7CMCIDTS%7C18312%7CMCMID%7C62974749092022106353101875068247214066%7CMCAAMLH-1582706461%7C6%7CMCAAMB-1582706461%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1582108861s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; currency_code=GBP; pref_lang=en; s_nr=1582101733694-Repeat; s_lv=1582101733697; s_sq=%5B%5BB%5D%5D; context_alias_id=35a4556c-7c58-46b2-977f-fc407071b4a4; context_id=b1eef471-0710-4c27-8535-892ddf25b81d; passive_basket_id=1020f848-845e-4e08-a21d-0d6cf6b525d1; temp_basket_id=eab5df12-fc8c-42b1-a9b9-592830473021; basket_id=8dd1e723-cd28-4be2-b152-336794ff6ba1; RMROCKET-1248=1; OPTI-810=1; OPTI-922=1; SSID=CAA5lx0YAQQAAADneUpes6PBDOd5Sl4GAAAAAAAAAAAA6r5SXgCB4CLIAAFvfxsA6r5SXgEAGsgAAZN-GwDqvlJeAQC2vAAB-CEZAOq-Ul4BABnIAAGQfhsA6r5SXgEAO8YAA586GwDneUpeBgAgyAABE38bAOq-Ul4BAIbIAAE_ixsA6r5SXgEAiMgAAZ6LGwDqvlJeAQBeygABQtMbAOq-Ul4BAGXIAANHhhsA53lKXgYAacQAA0DoGgDneUpeBgAgxgABZzQbAOq-Ul4BAMbEAAHO-RoA6r5SXgEAfsgAAyyKGwC1-UteBQBUyAABtoQbAOq-Ul4BALrGAAFxSRsA6r5SXgEAhMYAAc1DGwDqvlJeAQDexQABrCsbAOq-Ul4BAAbHAAG8UhsA6r5SXgEAY8gAAz2GGwDneUpeBgBJxwAA; SSSC=266.G6794377021100237747.6|48310.1647096:50281.1763392:50374.1767886:50654.1780652:50720.1782887:50747.1784479:50820.1786829:50874.1788273:50950.1790652:51225.1801872:51226.1801875:51232.1802003:51234.1802095:51284.1803446:51299.1803837:51301.1803847:51326.1804844:51334.1805119:51336.1805214:51806.1823554; SSRT=6r5SXgADAA; login=0; AKA_A2=A; bm_sz=89D891B2711C0E6FB8194B4AFA46957A~YAAQ1IFlX43bP1pwAQAA4cQ5cwaOlMV9kk+oq4vjNpRGnzqYn+r8l9T/fz9l38XZHhdf6lVcyZuUP3/nbTe7EFVsUfjB/+4jBphZVmEwk+1WeyuxbICNgnFGStklca5/0UKMUFbHnZ8cN4UaSxyLjTfl1TQWEJwWJaSsPNUWDg4enQcdkO6AvstAMNehgdMTQspsNm1h; _gid=GA1.2.298837650.1582481136; ravelinCanFingerprint=1; _tq_id.TV-544536-1.8433=ab52b2387f29ff60.1581939196.0.1582481149..; RT="z=1&dm=thetrainline.com&si=1d940e44-aa0b-4213-a4ac-9816a744f952&ss=k6zceo46&sl=1&tt=buf&bcn=%2F%2F684dd304.akstat.io%2F&ld=ctl&nu=31gkdd5o&cl=1wc0"; pinned_results_message_hidden=false',
}

data = {
    "passengers": [{
        "dateOfBirth": "1989-10-19"
    }],
    "isEurope": False,
    "cards": [],
    "transitDefinitions": [{
        "direction": "outward",
        "origin": "dfa822c7546111f40356479a6bd7a60d",
        "destination": "8ad03cfded18966635d0b4c821fc8e62",
        "journeyDate": {
            "type": "departAfter",
            "time": "2020-01-17T00:00:00"
        }
    }],
    "type": "single",
    "maximumJourneys": 15,
    "includeTravelTogetherFares": True,
    "includeRealtime": False,
    "requestedCurrencyCode": "GBP"
}

# Glasgow:  8ad03cfded18966635d0b4c821fc8e62
# Coventry: dfa822c7546111f40356479a6bd7a60d

starting_date = datetime(year=2020, month=2, day=27, hour=15, minute=30)
ending_date = datetime(year=2020, month=3, day=30, hour=0, minute=0)
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
            # ValueError: min() arg is an empty sequence
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
