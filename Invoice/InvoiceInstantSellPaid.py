import requests
import pytest
import json

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiYmRkMTVlNzU4YTM1NDdiZTc4YmQzNzM4NTQ2YWYwMmI2MTE4ZTY4OTIxOTgzOWM1NDgzNjU1YWM0MzI3MzkwODNmNjJjOTRiMTNlMDg1OTIiLCJpYXQiOjE2OTY3Mzc5MDcsIm5iZiI6MTY5NjczNzkwNywiZXhwIjoxNzI4MzYwMzA3LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.ZnwlbQdBYmh-Rw3LXAMKjuEFi3_GdTCixcnf1QWWgcaOL56Q6Y0Ymqfv2xWKZgKAlg-OXbL_nBlo9dIOXo0KjfQQt4VdLgRHHxCrRGJ8K_tafDAERHswqcotoTinHF3upHF__uNWcCYkWuqJrXyh5X6SrlH3fP1UdZEEwgjnI2jMmcjouZgdEvchiykklGZEroV5x36yPQV89BEsODsPjeJZH5xyzfJ7cDgPB9v8NcfepbzHeszODwGdrEdJFI_IDTlWGWXGAO5fHfKFJycfvhohRcqFDaxGQ1Pm0DsMGd6PTLnCXvHgupFlZJFGL9mAHA0KZl_-83FxnT3bZjkrd36TGzt4JFFO_WBUMoAD9YOGOyC4LY7KoHH1mDu7XJ4vcpVHr0fiGAejmaad9dn1SNs95XP9HvoYm4WDUGcRqok8Zyuh2WDTcHpQcqoLDU-p0HrCd7F3zE-SBTs6T8ojGWqL3wzDy4637iN7uVMYN5WJGSJ-xguDkC5_1Eg8t3E3pkDWZDsLy9RcFujfAjcbKRhXLPuTMkvpJPpQh80IMoYV5GOEhv3ZKImK2XR8EfTE2w_ZQzD8Uvetp2FrOsBrA-EDCbLr8n4RpdRkHh8zpa4DdUu1rY6ICTl4cYonbk4J-qrfVS44U5qAL9p8We7aQkgqJjPtCjzF1O-5HF3nlQI'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_invoice_sell_paid():

    invoice_id_to_sell_paid = 1137

    response = requests.post(
        url = f'{base_url}accounts/invoice/instant-sell-paid/{invoice_id_to_sell_paid}',
        headers = head
    )

    print(response.status_code)
    print(response.json())
    assert 200 == response.status_code

def test_delivered_invoice_sell_paid():

    invoice_id_to_sell_paid = 1042

    response = requests.post(
        url=f"{base_url}accounts/invoice/instant-sell-paid/{invoice_id_to_sell_paid}",
        headers=head
    )

    print(response.status_code)
    print(response.json())
    # assert 404 == response.status_code