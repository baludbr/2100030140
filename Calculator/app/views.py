import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from collections import deque
import time
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)




windows = {
    'p': deque(maxlen=10),
    'f': deque(maxlen=10),
    'e': deque(maxlen=10),
    'r': deque(maxlen=10)
}

TEST_SERVER={
    'p': 'http://20.244.56.144/test/primes',
    'f': 'http://20.244.56.144/test/fibo',
    'e': 'http://20.244.56.144/test/even',
    'r': 'http://20.244.56.144/test/rand',
}

BEARER_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MjYyNjI2LCJpYXQiOjE3MTgyNjIzMjYsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjdlODM5YzIwLTJjZmItNDNiZS05Nzg3LTg0NDZjNzdiYjFjZSIsInN1YiI6ImR3YXJhbXB1ZGliYWxhamlyZWRkeUBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJLTCBVTklWRVJTSVRZIiwiY2xpZW50SUQiOiI3ZTgzOWMyMC0yY2ZiLTQzYmUtOTc4Ny04NDQ2Yzc3YmIxY2UiLCJjbGllbnRTZWNyZXQiOiJJWEdxZlVpd2Rpa2FsbU5wIiwib3duZXJOYW1lIjoiRFdBUkFNUFVESSBCQUxBSkkgUkVERFkiLCJvd25lckVtYWlsIjoiZHdhcmFtcHVkaWJhbGFqaXJlZGR5QGdtYWlsLmNvbSIsInJvbGxObyI6IjIxMDAwMzAxNDAifQ.sOcTU1pN9ulvNO-SsSogR4uDnzbfhSsv97yKPAwu5RM'


class Calc(APIView):
    def get(self, request, number_type):
        if numberid not in TEST_SERVER:
            return JsonResponse({'error': 'Invalid number type'}, status=400)

        start_time = time.time()
        url = TEST_SERVER[number_type]

        try:
            headers = {
                'Authorization': f'Bearer {BEARER_TOKEN}'
            }
            response = requests.get(url, headers=headers, timeout=0.5)
            fetched= response.json().get('numbers', [])
        except requests.Exception as e:
            return JsonResponse({'error': 'Failed to fetch'}, status=500)


        prev = list(windows[number_type])
        for i in fetched:
            if i not in windows[number_type]:
                windows[number_type].append(i)

        response_data = {
            "numbers": fetched,
            "windowPrevState": prev,
            "windowCurrState": list(windows[numberid]),
            "avg": sum(curr_window_state) / len(curr_window_state) if curr_window_state else 0
        }

        if time.time() - start_time > 0.5:
            return JsonResponse({'error': 'Response time exceeded 500 milli Seconds'}, status=500)

        return JsonResponse(response_data)