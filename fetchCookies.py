from playwright.sync_api import sync_playwright

def fetch_token_and_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Intercept network requests to find the token
        token_holder = {}

        def capture_request(request):
            if "GetBaseData" in request.url and request.method == "POST":
                token_holder["headers"] = request.headers

        page.on("request", capture_request)
        page.goto("https://aggiespirit.ts.tamu.edu/RouteMap")
        page.wait_for_timeout(5000)

        # Trigger whatever JS triggers GetBaseData (maybe click or wait long enough)
        page.evaluate("window.dispatchEvent(new Event('load'))")  # Trigger load if needed

        # Wait for requests
        page.wait_for_timeout(5000)

        cookies = context.cookies()
        browser.close()


        return {
            ".MyRide.RequestVerificationToken": cookies[0]['value'],
            "TSSESSIONID": cookies[1]['value'],
            "RequestVerificationToken": token_holder.get("headers", {}).get("requestverificationtoken")
        }

