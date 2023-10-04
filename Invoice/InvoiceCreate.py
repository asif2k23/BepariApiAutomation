import requests
import pytest
import json

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiOWRlZGU4Y2VlYTA2NjdiYmViZGQxNmVmNDY2ZmFhNDYxN2Y3NjM5ZDgxZWY2ZjBmNTkyYmY4NWU3ZDEzMzE4MGY3NmY1NGNiMDk3MzJhYTQiLCJpYXQiOjE2OTYzOTIyNTgsIm5iZiI6MTY5NjM5MjI1OCwiZXhwIjoxNzI4MDE0NjU4LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.lq4JDcpPKPSD6G8CRvwpLvs2WVLpaJHa9ylTIyk3ne-AD_H6rdhL8ipDcEpaA3gc2o_38nVnC6ODVtsctiUSvPYYcpwTzAf7DM60V4j6G-6cYWWmDWmCjTmR6j5q5eF0I6eUe3gtJLZMt-irHZViGdGxrIAZToKlJYDFmOlZzYuuInOuNUDn-j2Qllj-qMygPaV19UqK92zAOJCSE9cY0yDwmP8k9BNDCu0BD7SDw7jEUsFjmCm-FQGWVfLJvTGBoBFmjrDMuVkaV4tzY81TR78VdVEddxre5E74YeNmjNfGURBW5AG6wbXYH1-piETKEU0p_GzqHZ3gPIO5w1kqb9HcQUwSja6jvNcnZKzq6u8xE9csOm-dMQIQgJNhqPIrNKVUPLXXRymV6oEGX8aLLL1Iy2Dvdl7ewSY13qaAf4bq90kjnut09VQMi8b3Ds2TuWFpmxBJ3sz5HQKrUSIgaYXFsej-OGbnD-JazC__CJtnhjYrWmLQRfJnfFzKvf7EBL0j43DAhFf6pW4CSDMGjAxQlAuI_kBAr0-GiLMfq_SuMpRTiu5jHFXE6AZuiZarMpE7k6qzeGW_jbvwE3iJDRzq6klUdIFF7PFAKEvGXGfvrpoIVZ2MRjq9cijZUjfajRMjniuAXeIIRGvq2mq4M6yuUVK2VYsBtQY7DdIHDPQ'
       }

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_postrequest_validation():
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

    response = requests.post(url=str(base_url+'accounts/invoice/create'),headers = head, json = payload)
    assert 200 == response.status_code
    print(response.status_code)
    print(response.json())

def test_missing_required_fields():
    payload = {

    }
    response = requests.post(url=str(base_url+'accounts/invoice/create'), headers=head, json=payload)
    assert 400 == response.status_code
    print(response.status_code)

def test_invalid_data_types():
    payload = {
        "delivery_vendor_name": 123,  # Should be a string
        "customer_id": "invalid_id",  # Should be an integer
    }
    response = requests.post(url=str(base_url+'accounts/invoice/create'), headers=head, json=payload)
    assert 400 == response.status_code  # Expecting a 400 Bad Request response
    print(response.status_code)

def test_unauthorized_access():
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer auifhdhjkhkhuieruihuihsauidhfcinuinuiahfuihauisnufer.erfjeuirhuierh'
    }
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
    response = requests.post(url=str(base_url+'accounts/invoice/create'), headers=headers, json=payload)
    assert 401 == response.status_code  # Expecting a 401 Unauthorized response
    print(response.status_code)

def test_server_errors():
    # Simulate a server error by providing an invalid URL
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
    assert 404 == response.status_code  # Expecting a 404 Internal Server Error response
    print(response.status_code)


