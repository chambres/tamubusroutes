import json
import requests

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
    print("Response Text:\n", response.text)
    return response.json()

def load_cookies():
    with open('cookies.json', 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    # Load cookies from the file
    cookies = load_cookies()

    # Example route key
    test_route_keys = ['754c0a41-6779-44f1-84d2-2401706e4cf0']

    # Call the API
    result = getPatternPaths(
        cookies['TSSESSIONID'],
        cookies['.MyRide.RequestVerificationToken'],
        cookies['RequestVerificationToken'],
        test_route_keys
    )

    print("Result:\n", json.dumps(result, indent=4))
