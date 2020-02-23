import requests

headers = {
    'x-version': '1.3.14562',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36',
    'sec-fetch-mode': 'cors',
    'content-type': 'application/json',
    'accept': 'application/json',
    'referer': 'https://www.thetrainline.com/book/results?origin=dfa822c7546111f40356479a6bd7a60d&destination=8ad03cfded18966635d0b4c821fc8e62&outwardDate=2019-10-21T14%3A00%3A00&outwardDateType=departAfter&journeySearchType=single&passengers%5B%5D=1989-10-20&selectedOutward=2qG%2BdvAJf3o%3D%3ACt5SUu4aii8%3D&temporalDirection=next&transitDefinitionDirection=outward&searchId=9c755bdc-3ba8-4112-8c92-15f8855a314b',
    'authority': 'www.thetrainline.com',
    'cookie': 'reset_currency=1; wasabiId=57b27eda-7fa6-4284-b0bf-2dbad801ddb7; currency_code=GBP; AMCVS_5D570C3A53DB50FA0A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C62974749092022106353101875068247214066; _ga=GA1.2.1499674015.1571047534; TANGO-371=true; temp_basket_id=d8209a53-b3d8-4c4a-a516-e7c26ff7dd85; basket_id=f1e58b16-a2d4-41f4-a332-8bebf1a95381; eu_cookies_visi={%22version%22:3%2C%22feature%22:%22%22}; ab.storage.sessionId.ed8871ee-f4e9-4188-bf1c-3499e423fa02=%7B%22g%22%3A%228404fcef-79ed-2525-a9ab-66a890f5e481%22%2C%22e%22%3A1571049343188%2C%22c%22%3A1571047543190%2C%22l%22%3A1571047543190%7D; ab.storage.deviceId.ed8871ee-f4e9-4188-bf1c-3499e423fa02=%7B%22g%22%3A%2234bf441b-3c90-a331-6b3b-f0c661940a6c%22%2C%22c%22%3A1571047543209%2C%22l%22%3A1571047543209%7D; ravelinSessionUuid=2a12d765-b27f-45b4-9ea7-7b9a707dca9f; ravelinUuid=382ba06d-86cc-42d0-a53d-d62c98a0e740; ravelinDeviceId=382ba06d-86cc-42d0-a53d-d62c98a0e740; _gcl_au=1.1.1725438725.1571047549; s_cc=true; _fbp=fb.1.1571047553557.1086642220; RT="z=1&dm=www.thetrainline.com&si=ade12e0e-ff52-45b3-ae0f-37dce6a95950&ss=k1qbp4rj&sl=0&tt=0&hd=1qoz&bcn=%2F%2F0211c83e.akstat.io%2F"; TANGO-EDGE=0; _gid=GA1.2.1863864999.1571477836; pinned_results_message_hidden=false; wExperienced=OPTI-491-3=1,OPTI-493-4=0,OPTI-504-4=1; context_id=dd204098-1ff3-46d9-aa36-9e363bdcc031; context_alias_id=31f927fe-5c86-4fe6-8598-0ba791b1717d; login=0; AMCV_5D570C3A53DB50FA0A490D4D%40AdobeOrg=-330454231%7CMCIDTS%7C18189%7CMCMID%7C62974749092022106353101875068247214066%7CMCAAMLH-1572192246%7C6%7CMCAAMB-1572192246%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1571594646s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; SSID=CABuQR2WAQAAAABpSKRdcIZCFWlIpF0IAAAAAAAAAAAARpGsXQCB4Oy8AAEMLRkARpGsXQEAq7kAAWiOGABGkaxdAQDiswABjnEXAEaRrF0BAIG7AAGO5hgARpGsXQEA97sAAeQAGQBGkaxdAQDbuwABb_cYAEaRrF0BAIS4AAPiVBgAaUikXQgAJ7EAATzgFgBGkaxdAQAWvAABJgUZAEaRrF0BACe8AAFiCBkARpGsXQEAHbsAAXfXGABGkaxdAQCgugABnrgYAEaRrF0BAM66AAEWvxgARpGsXQEAM7wAARIJGQBGkaxdAQBJuAAB5UoYAEaRrF0BADW8AAEyCRkARpGsXQEAFbwAARwFGQBGkaxdAQC5vAABSCIZAEaRrF0BABy7AAFs1xgARpGsXQEAj7cAAespGABGkaxdAQBwuwABIOIYAEaRrF0BAKOlAANYehQAMZ6rXQUAS7gAARBLGABGkaxdAQAouAADZkIYAELZql0GAAe7AAEW0BgARpGsXQEAWLkAARx7GABGkaxdAQA7sQAB3uIWAEaRrF0BADK8AAEICRkARpGsXQEAWLIAAxUeFwBpSKRdCAA; SSSC=266.G6747597757873292912.8|42403.1342040:45351.1499196:45371.1499870:45656.1515029:46050.1536398:46991.1583595:47144.1589862:47177.1592037:47179.1592080:47236.1594594:47448.1604380:47531.1609320:47776.1620126:47822.1621782:47879.1626134:47900.1628012:47901.1628023:47984.1630752:48001.1631886:48091.1636207:48119.1638628:48149.1639708:48150.1639718:48167.1640546:48178.1640712:48179.1640722:48181.1640754:48313.1647176:48364.1649932; wSession=703-6Z696-6Z491-3A492-4A493-4Z495-4A499-4A500-4A504-4A494-2Z501-1A505-1Z721-5A; AKA_A2=A; analyticsSessionId=1571590477038.t9w21hq7; s_lv_s=Less%20than%201%20day; SSRT=c5KsXQADAA; s_nr=1571592237109-Repeat; s_lv=1571592237113; _tq_id.TV-544536-1.8433=ae8fce999340eb29.1571047553.0.1571592244..; _gat_trainlineGATracker=1; _gat_1c2a5c4a9563fa50f39c8fa2e8ff4296=1; RT="z=1&dm=thetrainline.com&si=ade12e0e-ff52-45b3-ae0f-37dce6a95950&ss=k1zaclsv&sl=1&tt=1&hd=1qoz&bcn=%2F%2F5f651e6f.akstat.io%2F"; s_sq=tlntrainlineprod%3D%2526pid%253Dresults%2526pidt%253D1%2526oid%253Dfunctionhr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
    'sec-fetch-site': 'same-origin',
}

response = requests.get('https://www.thetrainline.com/api/journey-search-leg-calling-points/ad9188d1-1fdd-4b0a-82b3-4fd102860d59/a62f053d-4092-425d-8764-c0b9bcb326d5/64b41635-6327-4b3b-8d91-0fc9e864143a', headers=headers)
response_json = response.json()

stops = response_json["service"]["stops"]
locations = response_json["locations"]

departure_stop = "474f3248-6d78-4f31-a875-67fe11a39799"
arrival_stop = "42e64d15-5093-4891-844b-1de91f02562f"
departure_stop_idx = 0
arrival_stop_idx = len(stops) - 1

for idx, stop in enumerate(stops):
    # print(stop)
    if stop["location"] == departure_stop:
        departure_stop_idx = idx
        continue

    if stop["location"] == arrival_stop:
        arrival_stop_idx = idx
        break

stops = stops[departure_stop_idx:arrival_stop_idx+1]

for stop in stops:
    print(locations[stop["location"]]["name"])
    # break