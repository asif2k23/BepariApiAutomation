import requests
import pytest
import json

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiMWM4MWZjMTI5ZTI1NzVhZTEwYzMyY2JmZDUzOGFmNzk1ZjI3MzllOGM1ODIxNjliOTQyMDRjNWZhYjk1YWFmM2M3MTUyMzJhNzMxMTY5MGMiLCJpYXQiOjE2OTc1MTQ0NTIsIm5iZiI6MTY5NzUxNDQ1MiwiZXhwIjoxNzI5MTM2ODUyLCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.l93ieUzT8FTQASjrLGJVEu91le2dHDTWPenFRmWTLPD6F__LJMyKKTCJqTai4ecIQpTdkfsjmQAyGEgIWruRg0LPVfbqegy-JyV14B-SmgTbrGjczAbk2ONHGjHJtHfrVevLidvE_MNsLJAw2FyWqO9p4lu637Aq2SDMBkWso1ykdg9mRZKafxz87ZRitgLmJEYJ5qlwQn2BSaGaHL_aVwgsl-9F4OqXkImyA5DbJwqCXg9V_qa1LhdUc-WMx4tlQX4FvdsRIVGlXfVs1pBq2sECPQ4JLsYl_4sGyRKcEB8-RmqXfYjZuEajTmcMztpBkNzgHlBtC0JqrAeJnV0y_tWrVSu5h2O6Ed1NbQ-79tUifJSprvLexMiUKY1RUHLeK4-yotdA5t9xBHT-OQw7OOll4jueY0_mwmRqHnx9rrXNBbu-yG_9xLwY3Z1TluUmFSknrvHyuncCd2GR79wwO5rJJjGNclGpEgK0GFm_ZRJtDf_4YxaflU9dzzfF-Idlv9Lg4zSExqVUuKsSNmfzz0kWz9zinzbmR5L8f1eW_sqW1-bc3B9HdPHc6anYxb-5J8ZOEczfq4fuUQCBT2rVy8ZuEKgCia7hG-h0QdMONS-OOcogP1evAys9KGJGfSZ0ysQ8ZWfJBZQ10ib0C7W7B7NKWrYzmOXqloDqK5k6RAg'
}

base_url = 'https://api.dev.bepari.info/demo/api/V1.1/'


# for offers on Order amount(2)
def test_discount_create_order_amount():

    payload = {

        "id": '',
        "title": "Discount Offer for order amount 1",
        "description": "<p>Discount Offer for order amount Description 1</p>",
        "platforms": [
            4
        ],
        "offers_on": [
            2
        ],
        "has_order_amount_range": 1,
        "has_selected_products": 0,
        "productData": [

        ],
        "parentProductData": [

        ],
        "order_amount_range": [
            {
                "min": 500,
                "max": 1000,
                "amount": 5,
                "discount_type": "amount",
                "key": 1
            }
        ],
        "expiry_type": 0,
        "promotion_date": [

        ],
        "discount_in": 0,
        "discount_info": '',
        "status": 1,
        "promotion_start_date": "NaN-NaN-NaN 12:NaN:NaN am",
        "promotion_end_date": "NaN-NaN-NaN 12:NaN:NaN am"
}

    response = requests.post(
        url = f'{base_url}promotion/discount-offer/create',
        headers = head,
        json = payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert 200 == response.status_code      #The response code  422 should show


# for offers on Selected target product(1)
def test_discount_create_target_product():

    payload = {
   "id":'',
   "title":"Discount Offer for target product 1",
   "description":"<p>Discount Offer for target product Description 1</p>",
   "platforms":[
      4
   ],
   "offers_on":[
      1
   ],
   "has_order_amount_range":0,
   "has_selected_products":1,
   "productData":[
      18
   ],
   "parentProductData":[

   ],
   "order_amount_range":[
      {
         "min":1,
         "max":0,
         "amount":10,
         "discount_type":"percent",
         "key":1
      }
   ],
   "expiry_type":0,
   "promotion_date":[

   ],
   "discount_in":0,
   "discount_info":'',
   "status":1,
   "promotion_start_date":"NaN-NaN-NaN 12:NaN:NaN am",
   "promotion_end_date":"NaN-NaN-NaN 12:NaN:NaN am"
}

    response = requests.post(
        url = f'{base_url}promotion/discount-offer/create',
        headers = head,
        json = payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert 200 == response.status_code      #The response code  422 should show


# offers on Order amount with same information validation check
def test_same_discount_create_order_amount_validation():
    payload = {

        "id": '',
        "title": "Discount Offer for order amount 1",
        "description": "<p>Discount Offer for order amount Description 1</p>",
        "platforms": [
            4
        ],
        "offers_on": [
            2
        ],
        "has_order_amount_range": 1,
        "has_selected_products": 0,
        "productData": [

        ],
        "parentProductData": [

        ],
        "order_amount_range": [
            {
                "min": 500,
                "max": 1000,
                "amount": 5,
                "discount_type": "amount",
                "key": 1
            }
        ],
        "expiry_type": 0,
        "promotion_date": [

        ],
        "discount_in": 0,
        "discount_info": '',
        "status": 1,
        "promotion_start_date": "NaN-NaN-NaN 12:NaN:NaN am",
        "promotion_end_date": "NaN-NaN-NaN 12:NaN:NaN am"
    }

    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert 422 == response.status_code      #The response code  422 should show


# offers on Selected target product with same information validation check
def test_same_discount_create_target_product_validation():
    payload = {
        "id": '',
        "title": "Discount Offer for target product 1",
        "description": "<p>Discount Offer for target product Description 1</p>",
        "platforms": [
            4
        ],
        "offers_on": [
            1
        ],
        "has_order_amount_range": 0,
        "has_selected_products": 1,
        "productData": [
            18
        ],
        "parentProductData": [

        ],
        "order_amount_range": [
            {
                "min": 1,
                "max": 0,
                "amount": 10,
                "discount_type": "percent",
                "key": 1
            }
        ],
        "expiry_type": 0,
        "promotion_date": [

        ],
        "discount_in": 0,
        "discount_info": '',
        "status": 1,
        "promotion_start_date": "NaN-NaN-NaN 12:NaN:NaN am",
        "promotion_end_date": "NaN-NaN-NaN 12:NaN:NaN am"
    }

    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert 422 == response.status_code      #The response code  422 should show


def test_discount_create_multiple_target_products():
    payload = {
        "id": '',
        "title": "Discount Offer for target product 2",
        "description": "<p>Discount Offer for target product Description 1</p>",
        "platforms": [
            4
        ],
        "offers_on": [
            1
        ],
        "has_order_amount_range": 0,
        "has_selected_products": 1,
        "productData": [
            18,26
        ],
        "parentProductData": [

        ],
        "order_amount_range": [
            {
                "min": 1,
                "max": 0,
                "amount": 10,
                "discount_type": "percent",
                "key": 1
            }
        ],
        "expiry_type": 0,
        "promotion_date": [

        ],
        "discount_in": 0,
        "discount_info": '',
        "status": 1,
        "promotion_start_date": "NaN-NaN-NaN 12:NaN:NaN am",
        "promotion_end_date": "NaN-NaN-NaN 12:NaN:NaN am"
    }
    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert response.status_code == 200

def test_discount_create_order_amount_different_range():
    payload = {
   "id":'',
   "title":"Discount Offer for order amount 5",
   "description":"<p>Discount Offer for order amount 5</p>",
   "platforms":[
      4,
      0,
      5
   ],
   "offers_on":[
      2
   ],
   "has_order_amount_range":1,
   "has_selected_products":0,
   "productData":[

   ],
   "parentProductData":[

   ],
   "order_amount_range":[
      {
         "min":2001,
         "max":3000,
         "amount":15,
         "discount_type":"percent",
         "key":0
      },
      {
         "key":0,
         "min":3001,
         "max":5000,
         "amount":20,
         "type":"",
         "discount_type":"percent"
      }
   ],
   "expiry_type":2,
   "promotion_date":[
      "2023-10-17T18:00:00.000Z",
      "2023-10-30T18:00:00.000Z"
   ],
   "discount_in":0,
   "discount_info":'',
   "status":1,
   "promotion_start_date":"18-10-2023 12:00:00 am",
   "promotion_end_date":"31-10-2023 12:00:00 am"
}
    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    # assert response.status_code == 200

def test_discount_create_expired_dates():
    payload = {
        "id": '',
        "title": "Discount Offer for target product 7",
        "description": "<p>Discount Offer for target product Description 7</p>",
        "platforms": [
            4
        ],
        "offers_on": [
            1
        ],
        "has_order_amount_range": 0,
        "has_selected_products": 1,
        "productData": [
            18
        ],
        "parentProductData": [

        ],
        "order_amount_range": [
            {
                "min": 1,
                "max": 0,
                "amount": 10,
                "discount_type": "percent",
                "key": 1
            }
        ],
        "expiry_type": 0,
        "promotion_date": [
            "2023-10-12T00:00:00.001Z",
            "2023-10-16T00:00:00.001Z"
        ],
        "discount_in": 0,
        "discount_info": '',
        "status": 1,
        "promotion_start_date":"12-10-2023 12:00:00 am",
        "promotion_end_date":"16-10-2023 12:00:00 am"
    }
    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert response.status_code == 422

def test_discount_create_invalid_data_validation():
    payload = {
        "id": '',
        "title": "Invalid Discount Offer for Test",
        "description": "<p>Invalid Description for Testing</p>",
        "platforms": [
            4
        ],
        "offers_on": [
            2
        ],
        "has_order_amount_range": 0,
        "has_selected_products": 0,
        "productData": [
            18
        ],
        "parentProductData": [

        ],
        "order_amount_range": [
            {
                "min": -1000,
                "max": -500,
                "amount": -10,
                "discount_type": 'percent',
                "key": 1
            }
        ],
        "expiry_type": 3,
        "promotion_date": [
            "Invalid Date"
        ],
        "discount_in": -1,
        "discount_info": "",
        "status": 1,
        "promotion_start_date": "Invalid Start Date",
        "promotion_end_date": "Invalid End Date"

    }
    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert response.status_code == 422

def test_discount_create_required_fields():
    payload = {
        # "id": '',
        # "title": "Discount Offer for target product 1",
        # "description": "<p>Discount Offer for target product Description 1</p>",
        # "platforms": [
        #     4
        # ],
        # "offers_on": [
        #     1
        # ],
        # "has_order_amount_range": 0,
        # "has_selected_products": 1,
        # "productData": [
        #     18
        # ],
        # "parentProductData": [
        #
        # ],
        # "order_amount_range": [
        #     {
        #         "min": 1,
        #         "max": 0,
        #         "amount": 10,
        #         "discount_type": "percent",
        #         "key": 1
        #     }
        # ],
        # "expiry_type": 0,
        # "promotion_date": [
        #
        # ],
        # "discount_in": 0,
        # "discount_info": '',
        # "status": 1,
        # "promotion_start_date": "NaN-NaN-NaN 12:NaN:NaN am",
        # "promotion_end_date": "NaN-NaN-NaN 12:NaN:NaN am"
    }
    response = requests.post(
        url=f'{base_url}promotion/discount-offer/create',
        headers=head,
        json=payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(response.status_code)
    print(formatted_json)
    assert response.status_code == 422