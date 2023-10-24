import requests
import pytest
import json

head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiMGRlNTJhMmM2NjM3ZTU1MzA1YjhlZGFhNjMwYTRlZTBhOWQ2ZDA4Mzk2OTFhNDlmNGI2ZGU0N2M0ZmI1ZTIwNTFhY2ZiZWIxODg3MzBjZGEiLCJpYXQiOjE2OTgxMTcxMDgsIm5iZiI6MTY5ODExNzEwOCwiZXhwIjoxNzI5NzM5NTA4LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.pWpTUHFsIefHMmBtDP3FFd-cCi6eX8l3EcfBrxkaHxZ_iiqENEUvqBYzQ8AkfnXCDH8DjMxHWqqbxX077o_Oda_S9n3z82vZr7adWZnDKUdMoeiRjdYAacYQkrip6l51-X-12wV0he9gMP-U02dKP7Z0xxGjjlzXpziwqBbLxVh2REF2cSU1Zcjc-xWZewKH_Ksp4NSKeMOapIHr2gYBI2_bFYtrXOkC6Ata-oYncu39Wv4-0VktaDCHyEhLIMT_SOnhFYU9MZLsyYCyDqXZ7LzsFqgyrqx06utivC87_UcU3m5-Pb9gYN2QEb_yfpFGdiDN6moplL8wODS5hJAzuUmcjnqgeR_acWyUzcsocm6qyZUCoUhQw5CRWo9txRp6XFdm08VpzykH-shY6siqE8C9ryk6RJdPRnVFBkdYKeRsT0cL1kXNmdFsoG4qsUihOxioFFx4w5D34oX_CgimP0NV9J8QzL2n5l_1WHl3AAVTogkS7B8RYnpJAtb2om8e1KCZ_l3eG6eCJ5uRiv7HlazrWBHpEYuRhrMc8H3Qj5RNruPH_-MhWk-BEEu99XQG4wjJzmvAsLDfMfakO7omF59IJrQMnRyUO8q0FgseDRAG86VFKDCxfQ_Bsc97rz86oxo8Tln-lhnSaHiEZ9FLswaUtYOc6XQHPvwE-XYvLa0'
}

base_url = 'https://api.dev.bepari.info/demo/api/V1.1/'

def test_pos_product_list():
    params = {
        "branch_id": 1,
        "customer_id": 12,
        "customer_data": {
            "id": 12,
            "name": "Sabbir",
            "mobile": "01706967855",
            "product_price_category_id": 1
        },
        "searchProduct": "",
        "product_price_category_id": 1,
        "category_ids": [88, 2, 83, 15, 18, 16, 86, 9, 13, 47, 14, 17, 82, 48, 11],
        "page": 1
    }

    response = requests.get(
        url=f'{base_url}product-catalog/product/pos-category-product-list?{params}',
        headers=head,
        params=params
    )

    api_data = response.json()
    formatted_json = json.dumps(api_data, indent=4)

    print(response.status_code)
    print(formatted_json)

    assert 200 == response.status_code

# test_pos_product_list()

def test_pos_product_list_parameter_validation():
    params = {
        # "branch_id": 1,
        # "customer_id": 12,
        # "customer_data": {
        #     "id": 12,
        #     "name": "Sabbir",
        #     "mobile": "01706967855",
        #     "product_price_category_id": 1
        # },
        # "searchProduct": "",
        # "product_price_category_id": 1,
        # "category_ids": [88, 2, 83, 15, 18, 16, 86, 9, 13, 47, 14, 17, 82, 48, 11],
        # "page": 1
    }

    response = requests.get(
        url=f'{base_url}product-catalog/product/pos-category-product-list?{params}',
        headers=head,
        params=params
    )

    api_data = response.json()
    formatted_json = json.dumps(api_data, indent=4)

    print(response.status_code)
    print(formatted_json)

    assert 400 == response.status_code  # It should response 400 and show required feilds


def test_pos_product_search_validation():
    params = {
        "branch_id": 1,
        "customer_id": 12,
        "customer_data": {
            "id": 12,
            "name": "Sabbir",
            "mobile": "01706967855",
            "product_price_category_id": 1
        },
        "searchProduct": '',
        "product_price_category_id": 1,
        "category_ids": [88, 2, 83, 15, 18, 16, 86, 9, 13, 47, 14, 17, 82, 48, 11],
        "page": 1
    }

    response = requests.get(
        url=f'{base_url}product-catalog/product/pos-category-product-list?',
        headers=head,
        params=params
    )

    api_data = response.json()
    formatted_json = json.dumps(api_data, indent=4)

    print(response.status_code)
    print(formatted_json)

    assert 200 == response.status_code  #It should response 200


def test_pos_product_list_invalid_data_validation():
    params = {
        "branch_id": -1,
        "customer_id": -12,
        "customer_data": {
            "id": -12,
            "name": -9,
            "mobile": -9,
            "product_price_category_id": 'ghj'
        },
        "searchProduct": '',
        "product_price_category_id": 1,
        "category_ids": [88, 2, 83, 15, 18, 16, 86, 9, 13, 47, 14, 17, 82, 48, 11],
        "page": -1
    }

    response = requests.get(
        url=f'{base_url}product-catalog/product/pos-category-product-list?',
        headers=head,
        params=params
    )

    api_data = response.json()
    formatted_json = json.dumps(api_data, indent=4)

    print(response.status_code)
    print(formatted_json)

    assert 400 == response.status_code  #It should response 400 for invalid data


