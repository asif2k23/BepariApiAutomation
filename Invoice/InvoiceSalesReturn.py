import requests
import pytest
import json

head = {
        'accept': 'application/json, text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiOTI3MTA5NTkyYzA5MDMwMmQ5MTRiZDE1ZDkxOTU1ZjRjZWMxNTc1ZTk3MDhhNWFkN2JlMzg2NDNhZjBlODQ4OThjNDdlNDgwMzZlMmQ2YjMiLCJpYXQiOjE2OTczNDE3MDAsIm5iZiI6MTY5NzM0MTcwMCwiZXhwIjoxNzI4OTY0MDk5LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.T4eXxoPmmKNZ-va9mjuVXzcb0L5ln1rO3QZh4XrxOunJ2K_c8B9Kc4_WoQ_ZQlkfHnlldZ8sl7OZ3V-tJK-1YqZmRo8D0-UALb9r0cF-y2d7cg_VIF3B_82pe5VeSjAEBc4m32IxPJXRIDRBPi5p-ZZz5MGC1bUTuwGgGHwPSQUu4IMZZX-JxzQ6E3u4-Gl-GxQMvgbAbWVl34VabzyK2ahy59-igkmVEIk8BkBMwdO3nrTFO5ZjcXUyQYPgHWW28CPF5jFUHHctGgRLL-rGwe597QoCO2o5W1V-MZY7ZorDBcIXawX8BIMESX_xRKSWw2bcGP0CQmGc7NkDbnFAe06UEIwmQGAic-iX9xWpNngf2fu4JE9VIKMHJgFOxr7l3_Qs-OBSrWUv47m0ZmMjAI_wbcJ_TVvppzyxy6c-rmr3j-tQxwWhk57yi3F6PZpfJFuss7Ks_JRTj5ooXP_DHZoc2OPJicl1Ne7O2r7-ul2is_iVHTNpr7jwE24XJx3OYQVkxB1N-GMyD-czlJ68utstKB-f1-hNe3zrmLUhiB1CBj6Eld3uylU5ezy2TAQze9OTbElkm2GCAB9-wwebU-oIIuVvWjqrLtLGgZOQcKBVn6HWBiXKtMvgUCaQ79kLug4C7KV6OlsX9CT9inN2fUKtF4-37PkpzxCrgxnsfM4'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'


def test_invoice_sales_return():

    payload = {
   "sales_return":{
      "invoice_id":1231,
      "return_date":"2023-10-10T11:08:26.717Z",
      "overall_discount":"0.000",
      "sub_total":"300.000",
      "total_discount":"0.000",
      "total_before_vat":"300.000",
      "return_vat":"15.000",
      "return_amount":"315.000",
      "comment":"a"
   },
   "sales_return_details":{
      "invoice_details_id":[
         2313
      ],
      "product_id":[
         18
      ],
      "reason":[
         "a"
      ],
      "quantity":[
         4
      ],
      "damage":[
         0
      ],
      "unit_price":[
         75
      ],
      "per_unit_discount":[
         "0.000"
      ],
      "overall_discount":[
         0
      ],
      "item_total_discount":[
         0
      ],
      "discount_type":[
         "amount"
      ],
      "vat_rate":[
         "5.000"
      ],
      "total_vat":[
         "37.500"
      ],
      "total_price":[
         300
      ],
      "total_amount":[
         "315.000"
      ],
      "id":[
         ""
      ]
   }
}

    invoice_id_to_sales_return = 1231

    response = requests.post(
        url = f'{base_url}accounts/return/create/{invoice_id_to_sales_return}',
        headers = head,
        json = payload
    )

    print(response.status_code)
    print(response.text)
    # print(response.json())
    # assert 200 == response.status_code


def test_invoice_sales_return_required_fields():
   payload = {
      #required fields validation check
   }

   invoice_id_to_sales_return = 1231

   response = requests.post(
      url=f'{base_url}accounts/return/create/{invoice_id_to_sales_return}',
      headers=head,
      json=payload
   )

   print(response.status_code)
   print(response.text)
   # print(response.json())
   # assert 200 == response.status_code


def test_sales_return_method_validation():

   invoice_id_to_sales_return = 1231

   payload = {
      "sales_return": {
         "invoice_id": 1231,
         "return_date": "2023-10-10T11:08:26.717Z",
         "overall_discount": "0.000",
         "sub_total": "300.000",
         "total_discount": "0.000",
         "total_before_vat": "300.000",
         "return_vat": "15.000",
         "return_amount": "315.000",
         "comment": "a"
      },
      "sales_return_details": {
         "invoice_details_id": [
            2313
         ],
         "product_id": [
            18
         ],
         "reason": [
            "a"
         ],
         "quantity": [
            4
         ],
         "damage": [
            0
         ],
         "unit_price": [
            75
         ],
         "per_unit_discount": [
            "0.000"
         ],
         "overall_discount": [
            0
         ],
         "item_total_discount": [
            0
         ],
         "discount_type": [
            "amount"
         ],
         "vat_rate": [
            "5.000"
         ],
         "total_vat": [
            "37.500"
         ],
         "total_price": [
            300
         ],
         "total_amount": [
            "315.000"
         ],
         "id": [
            ""
         ]
      }
   }

   response = requests.delete(
      url=f'{base_url}accounts/return/create/{invoice_id_to_sales_return}',
      headers=head,
      json = payload
   )
   print(response.status_code)
   print(response.json())

def test_with_invalid_auth_token():
   payload = {
      "sales_return": {
         "invoice_id": 1231,
         "return_date": "2023-10-10T11:08:26.717Z",
         "overall_discount": "0.000",
         "sub_total": "300.000",
         "total_discount": "0.000",
         "total_before_vat": "300.000",
         "return_vat": "15.000",
         "return_amount": "315.000",
         "comment": "a"
      },
      "sales_return_details": {
         "invoice_details_id": [
            2313
         ],
         "product_id": [
            18
         ],
         "reason": [
            "a"
         ],
         "quantity": [
            4
         ],
         "damage": [
            0
         ],
         "unit_price": [
            75
         ],
         "per_unit_discount": [
            "0.000"
         ],
         "overall_discount": [
            0
         ],
         "item_total_discount": [
            0
         ],
         "discount_type": [
            "amount"
         ],
         "vat_rate": [
            "5.000"
         ],
         "total_vat": [
            "37.500"
         ],
         "total_price": [
            300
         ],
         "total_amount": [
            "315.000"
         ],
         "id": [
            ""
         ]
      }
   }

   invalid_token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'

   invoice_id_to_sales_return = 1231

   response = requests.post(
      url=f'{base_url}accounts/return/create/{invoice_id_to_sales_return}',
      headers={'Authorization': invalid_token},
      json=payload
   )

   print(response.status_code)
   print(response.text)