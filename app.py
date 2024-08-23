import requests
import logging
import time
from flask import Flask

#  logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Define the function to send a request
def send_request(session, url, headers, json_data, i):
    try:
        response = session.post(url, headers=headers, json=json_data)
        logger.info(f"Response {i + 1}: {response.text}")
    except Exception as e:
        logger.error(f"Request {i + 1} failed: {str(e)}")

def main():
    url = "https://agicoinbot.com/game_tokens"
    headers = {
        "Accept": "/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjU5NzI4MTA1NDZ9.lbQW1VX40adF_fpn2HovhF-5RTSybxIWj-ecuvqC1Rk",
        "Origin": "https://agicoinbot.com",
        "Referer": "https://agicoinbot.com/game",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"'
    }
    json_data = {
        "init_data": "query_id=AAEy2wFkAgAAADLbAWRKsp38&user=%7B%22id%22%3A5972810546%2C%22first_name%22%3A%22TEMMY%22%2C%22last_name%22%3A%22PRO%22%2C%22username%22%3A%22TEMMY_PRO%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1724411602&hash=6807c1b88e45d14e20005178858d8b7400067969702eca160e2fb101fa977beb",
        "tokens": 10
    }

    number_of_requests = 1000000
    requests_per_minute = 80
    delay_between_requests = 60 / requests_per_minute  # Calculate delay in seconds

    # Create a session object
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"
    })
    session.cookies.set("token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjU5NzI4MTA1NDZ9.lbQW1VX40adF_fpn2HovhF-5RTSybxIWj-ecuvqC1Rk", domain="agicoinbot.com")

    for i in range(number_of_requests):
        send_request(session, url, headers, json_data, i)
        time.sleep(delay_between_requests)  # Rate limiting

@app.route('/')
def home():
    return "Server is running. Check logs for request status."

if __name__ == "__main__":
    from threading import Thread
    # Start the Flask app in a separate thread
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    # Run the main function
    main()