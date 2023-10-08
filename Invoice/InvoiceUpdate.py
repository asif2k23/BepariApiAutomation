import requests
import json
import pytest

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiYmRkMTVlNzU4YTM1NDdiZTc4YmQzNzM4NTQ2YWYwMmI2MTE4ZTY4OTIxOTgzOWM1NDgzNjU1YWM0MzI3MzkwODNmNjJjOTRiMTNlMDg1OTIiLCJpYXQiOjE2OTY3Mzc5MDcsIm5iZiI6MTY5NjczNzkwNywiZXhwIjoxNzI4MzYwMzA3LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.ZnwlbQdBYmh-Rw3LXAMKjuEFi3_GdTCixcnf1QWWgcaOL56Q6Y0Ymqfv2xWKZgKAlg-OXbL_nBlo9dIOXo0KjfQQt4VdLgRHHxCrRGJ8K_tafDAERHswqcotoTinHF3upHF__uNWcCYkWuqJrXyh5X6SrlH3fP1UdZEEwgjnI2jMmcjouZgdEvchiykklGZEroV5x36yPQV89BEsODsPjeJZH5xyzfJ7cDgPB9v8NcfepbzHeszODwGdrEdJFI_IDTlWGWXGAO5fHfKFJycfvhohRcqFDaxGQ1Pm0DsMGd6PTLnCXvHgupFlZJFGL9mAHA0KZl_-83FxnT3bZjkrd36TGzt4JFFO_WBUMoAD9YOGOyC4LY7KoHH1mDu7XJ4vcpVHr0fiGAejmaad9dn1SNs95XP9HvoYm4WDUGcRqok8Zyuh2WDTcHpQcqoLDU-p0HrCd7F3zE-SBTs6T8ojGWqL3wzDy4637iN7uVMYN5WJGSJ-xguDkC5_1Eg8t3E3pkDWZDsLy9RcFujfAjcbKRhXLPuTMkvpJPpQh80IMoYV5GOEhv3ZKImK2XR8EfTE2w_ZQzD8Uvetp2FrOsBrA-EDCbLr8n4RpdRkHh8zpa4DdUu1rY6ICTl4cYonbk4J-qrfVS44U5qAL9p8We7aQkgqJjPtCjzF1O-5HF3nlQI'
       }

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_updaterequest_validation():

    payload = {
       "delivery_vendor_name":'',
       "delivery_tracking_number":'',
       "comment":'',
       "invoice_id":1002,
       "customer_id":33,
       "branch_id":1,
       "ship_to_customer_address":1,
       "sales_source":6,
       "salesperson_id":"",
       "sub_total":"135.00",
       "invoice_amount":"135.00",
       "invoice_vat":"0.00",
       "total_before_vat":"135.00",
       "total_discount":"0.00",
       "delivery_date":"2023-10-04",
       "delivery_slot_start":"16:00:00",
       "delivery_slot_end":"16:59:00",
       "due_date":"2023-10-03T18:00:00.000Z",
       "invoice_date":"2023-10-03T18:00:00.000Z",
       "overall_discount":"0.000",
       "total_amount":[
          "70.000",
          "65.000"
       ],
       "product_id":[
          26,
          17
       ],
       "accounts_group_id":[
          26,
          17
       ],
       "total_price":[
          70,
          65
       ],
       "vat_rate":[
          0,
          0
       ],
       "total_vat":[
          0,
          0
       ],
       "quantity":[
          2,
          2
       ],
       "inventory_type":[
          1,
          1
       ],
       "quantity_left":[
          "196.00",
          "95.00"
       ],
       "item_total_discount":[
          "0.000",
          "0.000"
       ],
       "discount_id":[
          0,
          0
       ],
       "per_unit_discount":[
          "0.000",
          "0.000"
       ],
       "unit_price":[
          70,
          65
       ],
       "average_unit_cost":[
          "10.000",
          "20.000"
       ],
       "discount_type":[
          "amount",
          "amount"
       ],
       "invoice_detail_id":[
          1095,
          1096
       ],
       "productwise_overall_discount":[
          "0.000",
          "0.000"
       ],
       "note":[
          "",
          ""
       ],
       "product_identity":[
           (
             {
                "label":"SL",
                "value":''
             },
             {
                "label":"IMEI",
                "value":''
             },
             {
                "label":"WARRANTY",
                "value":'',
                "day_type":"DAYS"
             }
           ),
           (
             {
                "label":"SL",
                "value":''
             },
             {
                "label":"IMEI",
                "value":''
             },
             {
                "label":"WARRANTY",
                "value":'',
                "day_type":"DAYS"
             }
           )
       ],
       "overall_discount_percent":0
}

    invoice_id_to_update = 1002

    response = requests.post(
        url=str(base_url + f'accounts/invoice/edit/{invoice_id_to_update}'),
        headers=head,
        json=payload
    )

    assert 200 == response.status_code
    print(response.status_code)
    # print("Response Text:\n", response.text)
    # assert "Invoice updated successfully!" in response.text

def test_update_invoice_with_invalid_data():
    payload = {
        "delivery_vendor_name": '',
        "delivery_tracking_number": '',
        "comment": '',
        "invoice_id": 'ygyrf',
        "customer_id": 'we',
        "branch_id": 's',
        "ship_to_customer_address": 'rhyhsd',
        "sales_source": 'shdbv',
        "salesperson_id": 'hsdb',
        "sub_total": "135.00",
        "invoice_amount": "135.00",
        "invoice_vat": "0.00",
        "total_before_vat": "135.00",
        "total_discount": "0.00",
        "delivery_date": "2023-10-04",
        "delivery_slot_start": "16:00:00",
        "delivery_slot_end": "16:59:00",
        "due_date": "2023-10-03T18:00:00.000Z",
        "invoice_date": "2023-10-03T18:00:00.000Z",
        "overall_discount": "0.000",
        "total_amount": [
            "70.000",
            "65.000"
        ],
        "product_id": [
            26,
            17
        ],
        "accounts_group_id": [
            26,
            17
        ],
        "total_price": [
            70,
            65
        ],
        "vat_rate": [
            0,
            0
        ],
        "total_vat": [
            0,
            0
        ],
        "quantity": [
            2,
            2
        ],
        "inventory_type": [
            1,
            1
        ],
        "quantity_left": [
            "196.00",
            "95.00"
        ],
        "item_total_discount": [
            "0.000",
            "0.000"
        ],
        "discount_id": [
            0,
            0
        ],
        "per_unit_discount": [
            "0.000",
            "0.000"
        ],
        "unit_price": [
            70,
            65
        ],
        "average_unit_cost": [
            "10.000",
            "20.000"
        ],
        "discount_type": [
            "amount",
            "amount"
        ],
        "invoice_detail_id": [
            1095,
            1096
        ],
        "productwise_overall_discount": [
            "0.000",
            "0.000"
        ],
        "note": [
            "",
            ""
        ],
        "product_identity": [
            (
                {
                    "label": "SL",
                    "value": ''
                },
                {
                    "label": "IMEI",
                    "value": ''
                },
                {
                    "label": "WARRANTY",
                    "value": '',
                    "day_type": "DAYS"
                }
            ),
            (
                {
                    "label": "SL",
                    "value": ''
                },
                {
                    "label": "IMEI",
                    "value": ''
                },
                {
                    "label": "WARRANTY",
                    "value": '',
                    "day_type": "DAYS"
                }
            )
        ],
        "overall_discount_percent": 0
    }

    invoice_id_to_update = 1002

    response = requests.post(
        url=str(base_url + f'accounts/invoice/edit/{invoice_id_to_update}'),
        headers=head,
        json=payload
    )
    assert 422 == response.status_code
    print(response.status_code)
    print(response.json())

def test_update_invalid_invoiceID():
    payload = {
        "delivery_vendor_name": '',
        "delivery_tracking_number": '',
        "comment": '',
        "invoice_id": 1002,
        "customer_id": 33,
        "branch_id": 1,
        "ship_to_customer_address": 1,
        "sales_source": 6,
        "salesperson_id": "",
        "sub_total": "135.00",
        "invoice_amount": "135.00",
        "invoice_vat": "0.00",
        "total_before_vat": "135.00",
        "total_discount": "0.00",
        "delivery_date": "2023-10-04",
        "delivery_slot_start": "16:00:00",
        "delivery_slot_end": "16:59:00",
        "due_date": "2023-10-03T18:00:00.000Z",
        "invoice_date": "2023-10-03T18:00:00.000Z",
        "overall_discount": "0.000",
        "total_amount": [
            "70.000",
            "65.000"
        ],
        "product_id": [
            26,
            17
        ],
        "accounts_group_id": [
            26,
            17
        ],
        "total_price": [
            70,
            65
        ],
        "vat_rate": [
            0,
            0
        ],
        "total_vat": [
            0,
            0
        ],
        "quantity": [
            2,
            2
        ],
        "inventory_type": [
            1,
            1
        ],
        "quantity_left": [
            "196.00",
            "95.00"
        ],
        "item_total_discount": [
            "0.000",
            "0.000"
        ],
        "discount_id": [
            0,
            0
        ],
        "per_unit_discount": [
            "0.000",
            "0.000"
        ],
        "unit_price": [
            70,
            65
        ],
        "average_unit_cost": [
            "10.000",
            "20.000"
        ],
        "discount_type": [
            "amount",
            "amount"
        ],
        "invoice_detail_id": [
            1095,
            1096
        ],
        "productwise_overall_discount": [
            "0.000",
            "0.000"
        ],
        "note": [
            "",
            ""
        ],
        "product_identity": [
            (
                {
                    "label": "SL",
                    "value": ''
                },
                {
                    "label": "IMEI",
                    "value": ''
                },
                {
                    "label": "WARRANTY",
                    "value": '',
                    "day_type": "DAYS"
                }
            ),
            (
                {
                    "label": "SL",
                    "value": ''
                },
                {
                    "label": "IMEI",
                    "value": ''
                },
                {
                    "label": "WARRANTY",
                    "value": '',
                    "day_type": "DAYS"
                }
            )
        ],
        "overall_discount_percent": 0
    }

    invoice_id_to_update = 9999

    response = requests.post(
        url=str(base_url + f'accounts/invoice/edit/{invoice_id_to_update}'),
        headers=head,
        json=payload
    )
    assert 404 == response.status_code
    print(response.status_code)
    print(response.json())

def test_invalid_auth_token():
    invalid_token = 'Bearer invalid_token_here''Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiYmRkMTVlNzU4YTM1NDdiZTc4YmQzNzM4NTQ2YWYwMmI2MTE4ZTY4OTIxOTgzOWM1NDgzNjU1YWM0MzI3MzkwODNmNjJjOTRiMTNlMDg1OTIiLCJpYXQiOjE2OTY3Mzc5MDcsIm5iZiI6MTY5NjczNzkwNywiZXhwIjoxNzI4MzYwMzA3LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.ZnwlbQdBYmh-Rw3LXAMKjuEFi3_GdTCixcnf1QWWgcaOL56Q6Y0Ymqfv2xWKZgKAlg-OXbL_nBlo9dIOXo0KjfQQt4VdLgRHHxCrRGJ8K_tafDAERHswqcotoTinHF3upHF__uNWcCYkWuqJrXyh5X6SrlH3fP1UdZEEwgjnI2jMmcjouZgdEvchiykklGZEroV5x36yPQV89BEsODsPjeJZH5xyzfJ7cDgPB9v8NcfepbzHeszODwGdrEdJFI_IDTlWGWXGAO5fHfKFJycfvhohRcqFDaxGQ1Pm0DsMGd6PTLnCXvHgupFlZJFGL9mAHA0KZl_-83FxnT3bZjkrd36TGzt4JFFO_WBUMoAD9YOGOyC4LY7KoHH1mDu7XJ4vcpVHr0fiGAejmaad9dn1SNs95XP9HvoYm4WDUGcRqok8Zyuh2WDTcHpQcqoLDU-p0HrCd7F3zE-SBTs6T8ojGWqL3wzDy4637iN7uVMYN5WJGSJ-xguDkC5_1Eg8t3E3pkDWZDsLy9RcFujfAjcbKRhXLPuTMkvpJPpQh80IMoYV5GOEhv3ZKImK2XR8EfTE2w_ZQzD8Uvetp2FrOsBrA-EDCbLr8n4RpdRkHh8zpa4DdUu1rY6ICTl4cYonbk4J-qrfVS44U5qAL9p8We7aQkgqJjPtCjzF1O-5HF3nlQI'
    payload = {
        "delivery_vendor_name": '',
        "delivery_tracking_number": '',
        "comment": '',
        "invoice_id": 1002,
        "customer_id": 33,
        "branch_id": 1,
        "ship_to_customer_address": 1,
        "sales_source": 6,
        "salesperson_id": "",
        "sub_total": "135.00",
        "invoice_amount": "135.00",
        "invoice_vat": "0.00",
        "total_before_vat": "135.00",
        "total_discount": "0.00",
        "delivery_date": "2023-10-04",
        "delivery_slot_start": "16:00:00",
        "delivery_slot_end": "16:59:00",
        "due_date": "2023-10-03T18:00:00.000Z",
        "invoice_date": "2023-10-03T18:00:00.000Z",
        "overall_discount": "0.000",
        "total_amount": [
            "70.000",
            "65.000"
        ],
        "product_id": [
            26,
            17
        ],
        "accounts_group_id": [
            26,
            17
        ],
        "total_price": [
            70,
            65
        ],
        "vat_rate": [
            0,
            0
        ],
        "total_vat": [
            0,
            0
        ],
        "quantity": [
            2,
            2
        ],
        "inventory_type": [
            1,
            1
        ],
        "quantity_left": [
            "196.00",
            "95.00"
        ],
        "item_total_discount": [
            "0.000",
            "0.000"
        ],
        "discount_id": [
            0,
            0
        ],
        "per_unit_discount": [
            "0.000",
            "0.000"
        ],
        "unit_price": [
            70,
            65
        ],
        "average_unit_cost": [
            "10.000",
            "20.000"
        ],
        "discount_type": [
            "amount",
            "amount"
        ],
        "invoice_detail_id": [
            1095,
            1096
        ],
        "productwise_overall_discount": [
            "0.000",
            "0.000"
        ],
        "note": [
            "",
            ""
        ],
        "product_identity": [
            (
                {
                    "label": "SL",
                    "value": ''
                },
                {
                    "label": "IMEI",
                    "value": ''
                },
                {
                    "label": "WARRANTY",
                    "value": '',
                    "day_type": "DAYS"
                }
            ),
            (
                {
                    "label": "SL",
                    "value": ''
                },
                {
                    "label": "IMEI",
                    "value": ''
                },
                {
                    "label": "WARRANTY",
                    "value": '',
                    "day_type": "DAYS"
                }
            )
        ],
        "overall_discount_percent": 0
    }
    invoice_id_to_update = 1002

    response = requests.post(
        url=str(base_url + f'accounts/invoice/edit/{invoice_id_to_update}'),
        headers={'Authorization': invalid_token},
        json=payload
    )
    assert 401 == response.status_code
    print(response.status_code)
    print(response.json())

def test_missing_required_fields():
    payload = {

    }
    invoice_id_to_update = 1002
    response = requests.post(
        url=str(base_url + f'accounts/invoice/edit/{invoice_id_to_update}'),
        headers=head,
        json=payload
    )
    assert 422 == response.status_code
    print(response.status_code)
    print(response.json())

def test_server_errors():
    invalid_url = 'https://example.com/invalid_endpoint'
    payload = {
        "delivery_vendor_name": "",
        "delivery_tracking_number": "",
        "comment": "",
        "invoice_note": "",
        "customer_id": 33,
        "branch_id": 1,
        "ship_to_customer_address": 1,
        "sales_source": "6",
        "sub_total": "75.00",
        "invoice_amount": "75.00",
        "invoice_vat": "0.00",
        "total_before_vat": "75.00",
        "total_discount": "0.00",
        "overall_discount": "0.000",
        "overall_discount_percent": 0,
        "delivery_date": "2023-10-04",
        "delivery_slot_start": "16:00",
        "delivery_slot_end": "16:59",
        "due_date": "2023-10-04T04:22:04.512Z",
        "invoice_date": "2023-10-04T04:22:04.512Z",
        "total_amount": [
            "75.000"
        ],
        "product_id": [
            25
        ],
        "accounts_group_id": [
            25
        ],
        "total_price": [
            75
        ],
        "vat_rate": [
            0
        ],
        "total_vat": [
            0
        ],
        "quantity": [
            1
        ],
        "inventory_type": [
            1
        ],
        "quantity_left": [
            "234.00"
        ],
        "item_total_discount": [
            "0.000"
        ],
        "discount_id": [
            0
        ],
        "per_unit_discount": [
            0
        ],
        "unit_price": [
            75
        ],
        "discount_type": [
            "amount"
        ],
        "productwise_overall_discount": [
            "0.000"
        ],
        "note": [
            ""
        ],
        "average_unit_cost": [
            52.336
        ],
        "product_identity": [
            (
                {
                    "label": "SL",
                    "value": ""
                },
                {
                    "label": "IMEI",
                    "value": ""
                },
                {
                    "label": "WARRANTY",
                    "value": "",
                    "day_type": "DAYS"
                }
            )
        ]
    }
    response = requests.post(url=invalid_url, headers=head, json=payload)
    assert 404 == response.status_code
    print(response.status_code)
    print(response.text)
