import requests
import pytest
import json

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiYjE2MjNmNjBjZWYwMmYzMzQxMzNlZDE5MjRhNjQ1ZTIxMTllZGQwY2VmZjU4NjBkZjc3Y2JiOGI2NDRlOTI2ZWIyYmE4NDNjZTIyNzNjZGMiLCJpYXQiOjE2OTc0Mjc3MzEsIm5iZiI6MTY5NzQyNzczMSwiZXhwIjoxNzI5MDUwMTMxLCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.tjvnFEduG_YgG0RkHX7u1et2Ld8kCsfxlIupECztbZ1PYPRcNjYSiJzHN_P9hhLk1Kfc_dPFlJ6il26zX_O4cphAK4JEK0G0yNhhVzESTl_61YV4WyhuuiXvIBCewTshOPRF81oTAIZtUFljUJVBsYAv1EwH-Y6pddTxyOTz3EHW1znE9s7pNtNwfH_DsqmbsOXwzcvi4GQW0dS1g7ZH-AT1OfoqVl84DhkT0w8m5_hFXfUxt0vIE7PabGzUUSdoGGkYdm-ezz4vjDbTZmsmPAlwPbzn0ET5mTmJIi897V_BDmwWsfK-bUoR9zIizcheq0krRkzf0kYY6cmA6De0EHQLXt9G1u5T521Hv37Dy-otncCBDogyoyVjF8FR0SBUD3NXW5hkIFLZ-T2k-uqngcEkBzaIIv20lbQKeAoMsU8mwArOjBXYqc7FOSe4a4Ybzgzm7v46ox9jqxceMvUh3mpbnOnbphpc8UHoa6ydx4MFc04AXFSFYtnI-FyszXi1dfqXk0vfmbwoZl3VfzbErdGQZPWyGbkkQq-MWfsjJOBskSHPOtYGZDeX7jenbvKXodw9o6aSWhGW32Af20VqTD7iQFW1zzLbFwyvBMXEN5Bv9Fj6O9kK0CgJYp52zmM1wy4nR_H_gEq3eaX3tg-W2xsBtgr--5NvlYU3mH2NqvY'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_edit_sales_return():

    payload = {
            "sales_return": {
                "invoice_id": 1042,
                "return_date": "2023-10-07T18:00:00.000Z",
                "overall_discount": "0.000",
                "sub_total": "75.000",
                "total_discount": "0.000",
                "total_before_vat": "75.000",
                "return_vat": "0.000",
                "return_amount": "75.000",
                "comment": "sad",
                "id": 37
            },
            "sales_return_details": {
                "invoice_details_id": [
                    1136
                ],
                "product_id": [
                    25
                ],
                "reason": [
                    "reason"
                ],
                "quantity": [
                    "1.000"
                ],
                "damage": [
                    0
                ],
                "unit_price": [
                    "75.000"
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
                    "0.000"
                ],
                "total_vat": [
                    "0.000"
                ],
                "total_price": [
                    "75.000"
                ],
                "total_amount": [
                    "75.000"
                ],
                "id": [
                    41
                ]
            }
    }

    sales_return_id_to_edit = 37

    respone = requests.post(
        url = f'{base_url}accounts/return/edit/{sales_return_id_to_edit}',
        headers = head,
        json = payload
    )

    API_Data = respone.json()
    formatted_json = json.dumps(API_Data, indent=4)

    print(respone.status_code)
    # print(respone.json())
    print(formatted_json)
