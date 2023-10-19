import requests
import pytest
import json
import uuid

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiODQyYjUxZTQyNDJiN2U1ZWUzZDNmZWE5NWE3ZmQ0NDQ4NWRjNDU1MDJlNGQ1YmQzNDI4ZDBlYjExMjQ0YjJmMDc0NzFlNDRhYmM0YmVkZDUiLCJpYXQiOjE2OTc2ODY5OTgsIm5iZiI6MTY5NzY4Njk5OCwiZXhwIjoxNzI5MzA5Mzk4LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.hndzWp-Mo7niI0l81eqx_iWkMDvqp1X_lMgXysZHLufwDsZER-s-RdjHcvtGeTxm7ue3t89X3oIbBcx7JZpwlfVLk_zKE-SJikGV1n893b3uN0d4LQyzjglhSMPquoD46Maq0QI5gjPWCGzQxr0pM1wWACOAmLzwv6JXnmykkGJTX8oJxSbqm5HGvxHrL7Bpq9f-QBGNliy-AO4tNFEVftMfxFruz1E8qa2eSbcqnqnWbsQPXOr5m_O9y_OiWuFPKiN8oAUmGFuBkNqt9FCrUQ2P7U3gHUX0PukmTVnogta1rpIw5j8_nwROvTPgWDLvN6t40lm-Hz7BwRoxF6pQ9YgLbvYHCXBY6jjwePRzcPk7eB4zZ7psOq-mB8I3cTosvlE2ERx8XZFrVW5e7rkC5hK2updlkiyDBUKm4ITgjVDTJzgiQh1QQ5uZu8TGkCuPSuklwT0NHOetage_aKscptGGDCzuo6f9WcUFWE0f-UZaGJ4HROWeERXc6HpF_mxFcHiK_PfIyVB8cuD7IFBKw-w5UgY1z8tKOLBrnADvaEg-Y5PWcadbelUBmlbsOSoSfDXUdEBQy8X_mCNSaFkJvuCDEm0N_mj8yAGmoYww_bDIPYLidMM_0Lp-BvD6EPgy35mFUxHLCRMEobqsnDvRnXtvU46i4CyZiW7tRiykCzk'
}

base_url = 'https://api.dev.bepari.info/demo/api/V1.1/'

def generate_unique_key():
    return str(uuid.uuid4())

def test_discount_update():

    discount_id_to_update = 30

    payload = {
           "id":30,
           "title":"Updated Discount",
           "description":"<p>Updated Discount Description</p>",
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
           "expiry_type":2,
           "promotion_start_date":"19-10-2023 12:00:00 am",
           "promotion_end_date":"18-11-2023 12:00:00 am",
           "discount_in":0,
           "status":1,
           "discount_info":{
              "order_amount_range":[
                 {
                    "min":300,
                    "max":500,
                    "amount":5,
                    "discount_type":"percent",
                    "key":generate_unique_key()
                 },
                 {
                    "key":generate_unique_key(),
                    "min":501,
                    "max":1000,
                    "amount":10,
                    "type":'',
                    "discount_type":"percent"
                 },
                 {
                    "key":generate_unique_key(),
                    "min":1001,
                    "max":2000,
                    "amount":15,
                    "type":"",
                    "discount_type":"percent"
                 }
              ]
           },
           "created_by":11,
           "updated_by":11,
           "deleted_at":'',
           "created_at":"2023-10-18T08:05:23.000000Z",
           "updated_at":"2023-10-18T08:05:23.000000Z",
           "selected_products_promotional_discounts":[

           ],
           "promotion_date":[
              "2023-10-18T18:00:00.000Z",
              "2023-11-17T18:00:00.000Z"
           ],
           "order_amount_range":[
              {
                 "min":300,
                 "max":500,
                 "amount":5,
                 "discount_type":"percent",
                 "key":generate_unique_key()
              },
              {
                 "key":generate_unique_key(),
                 "min":501,
                 "max":1000,
                 "amount":10,
                 "type":'',
                 "discount_type":"percent"
              },
              {
                 "key":generate_unique_key(),
                 "min":1001,
                 "max":2000,
                 "amount":15,
                 "type":"",
                 "discount_type":"percent"
              }
           ],
           "parentProductData":[

           ],
           "productData":[

           ]
        }

    response = requests.post(
        url = f'{base_url}promotion/discount-offer/edit/{discount_id_to_update}',
        headers = head,
        json = payload
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent = 4)

    print(response.status_code)
    print(formatted_json)
