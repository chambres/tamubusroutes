import requests
from fetchCookies import fetch_token_and_cookies

def getBaseData(TSESSIONID, MyRideRequestVerificationToken, requestVerificationToken):
    cookies = {
        '.MyRide.cookiePolicy': 'a=1',
        '.MyRide.RequestVerificationToken': MyRideRequestVerificationToken,
        'TSSESSIONID': TSESSIONID
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://aggiespirit.ts.tamu.edu',
        'Referer': 'https://aggiespirit.ts.tamu.edu/RouteMap',
        'RequestVerificationToken': requestVerificationToken,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    response = requests.post('https://aggiespirit.ts.tamu.edu/RouteMap/GetBaseData/', cookies=cookies, headers=headers)
    return response.json()

def getPatternPaths(TSESSIONID, MyRideRequestVerificationToken, requestVerificationToken, routeKeys):
    cookies = {
        '.MyRide.cookiePolicy': 'a=1',
        '.MyRide.RequestVerificationToken': MyRideRequestVerificationToken,
        'TSSESSIONID': TSESSIONID
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://aggiespirit.ts.tamu.edu',
        'Referer': 'https://aggiespirit.ts.tamu.edu/RouteMap',
        'RequestVerificationToken': requestVerificationToken,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }

    data = {
        'routeKeys[]': routeKeys,
    }

    response = requests.post('https://aggiespirit.ts.tamu.edu/RouteMap/GetPatternPaths/', cookies=cookies, headers=headers, data=data)
    print(response.text)
    print("hi")
    print(routeKeys)
    return response.json()

def getVehicles(TSESSIONID, MyRideRequestVerificationToken, requestVerificationToken, routeKeys):
    cookies = {
        '.MyRide.cookiePolicy': 'a=1',
        '.MyRide.RequestVerificationToken': MyRideRequestVerificationToken,
        'TSSESSIONID': TSESSIONID
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://aggiespirit.ts.tamu.edu',
        'Referer': 'https://aggiespirit.ts.tamu.edu/RouteMap',
        'RequestVerificationToken': requestVerificationToken,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = {
        'routeKeys[]': routeKeys,
    }

    response = requests.post('https://aggiespirit.ts.tamu.edu/RouteMap/GetVehicles/', cookies=cookies, headers=headers, data=data)
    return (response.json())