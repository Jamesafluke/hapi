import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


url = "http://192.168.1.101:8123/api/webhook/webhooktest"

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(3)

        curl_command = ["curl", "-X", "POST", url]

        request = requests.Request(method='POST', url=url)
        prepared_request = request.prepare()


        prepared_request.headers['User-Agent'] = 'curl/7.68.0'
        prepared_request.headers['Accept'] = '*/*'
        prepared_request.headers['Connection'] = 'keep-alive'


        response = requests.Session().send(prepared_request)

        print(response.content)

#curl -X POST http://jamesfluke.duckdns.com:8123/api/webhook/testid
#    -H 'Content-type: application/json'
#    -d '{ "key": "value" }'
