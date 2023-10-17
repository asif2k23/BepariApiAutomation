import requests
import json
import pytest
head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiMWM4MWZjMTI5ZTI1NzVhZTEwYzMyY2JmZDUzOGFmNzk1ZjI3MzllOGM1ODIxNjliOTQyMDRjNWZhYjk1YWFmM2M3MTUyMzJhNzMxMTY5MGMiLCJpYXQiOjE2OTc1MTQ0NTIsIm5iZiI6MTY5NzUxNDQ1MiwiZXhwIjoxNzI5MTM2ODUyLCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.l93ieUzT8FTQASjrLGJVEu91le2dHDTWPenFRmWTLPD6F__LJMyKKTCJqTai4ecIQpTdkfsjmQAyGEgIWruRg0LPVfbqegy-JyV14B-SmgTbrGjczAbk2ONHGjHJtHfrVevLidvE_MNsLJAw2FyWqO9p4lu637Aq2SDMBkWso1ykdg9mRZKafxz87ZRitgLmJEYJ5qlwQn2BSaGaHL_aVwgsl-9F4OqXkImyA5DbJwqCXg9V_qa1LhdUc-WMx4tlQX4FvdsRIVGlXfVs1pBq2sECPQ4JLsYl_4sGyRKcEB8-RmqXfYjZuEajTmcMztpBkNzgHlBtC0JqrAeJnV0y_tWrVSu5h2O6Ed1NbQ-79tUifJSprvLexMiUKY1RUHLeK4-yotdA5t9xBHT-OQw7OOll4jueY0_mwmRqHnx9rrXNBbu-yG_9xLwY3Z1TluUmFSknrvHyuncCd2GR79wwO5rJJjGNclGpEgK0GFm_ZRJtDf_4YxaflU9dzzfF-Idlv9Lg4zSExqVUuKsSNmfzz0kWz9zinzbmR5L8f1eW_sqW1-bc3B9HdPHc6anYxb-5J8ZOEczfq4fuUQCBT2rVy8ZuEKgCia7hG-h0QdMONS-OOcogP1evAys9KGJGfSZ0ysQ8ZWfJBZQ10ib0C7W7B7NKWrYzmOXqloDqK5k6RAg'
}

base_url = 'https://api.dev.bepari.info/demo/api/V1.1/'

params = {
    'keyword': 'a',
    'sell': 'true',
    'branch_id': '1',
    'show_del_charge': '',
    'product_price_category_id': '1',
    'inventory_type[]': ['0', '1', '2']
}

def test_discount_list_invoice():

    response = requests.get(
        url = f'{base_url}product-catalog/product/dropdown-product-discount-transaction?{params}',
        headers = head,
        params = params
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent = 4)

    print(response.status_code)
    print(formatted_json)