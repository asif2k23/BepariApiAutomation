import requests
import json
import pytest

head = {
        'accept': 'application/json, text/plain',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiOTI3MTA5NTkyYzA5MDMwMmQ5MTRiZDE1ZDkxOTU1ZjRjZWMxNTc1ZTk3MDhhNWFkN2JlMzg2NDNhZjBlODQ4OThjNDdlNDgwMzZlMmQ2YjMiLCJpYXQiOjE2OTczNDE3MDAsIm5iZiI6MTY5NzM0MTcwMCwiZXhwIjoxNzI4OTY0MDk5LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.T4eXxoPmmKNZ-va9mjuVXzcb0L5ln1rO3QZh4XrxOunJ2K_c8B9Kc4_WoQ_ZQlkfHnlldZ8sl7OZ3V-tJK-1YqZmRo8D0-UALb9r0cF-y2d7cg_VIF3B_82pe5VeSjAEBc4m32IxPJXRIDRBPi5p-ZZz5MGC1bUTuwGgGHwPSQUu4IMZZX-JxzQ6E3u4-Gl-GxQMvgbAbWVl34VabzyK2ahy59-igkmVEIk8BkBMwdO3nrTFO5ZjcXUyQYPgHWW28CPF5jFUHHctGgRLL-rGwe597QoCO2o5W1V-MZY7ZorDBcIXawX8BIMESX_xRKSWw2bcGP0CQmGc7NkDbnFAe06UEIwmQGAic-iX9xWpNngf2fu4JE9VIKMHJgFOxr7l3_Qs-OBSrWUv47m0ZmMjAI_wbcJ_TVvppzyxy6c-rmr3j-tQxwWhk57yi3F6PZpfJFuss7Ks_JRTj5ooXP_DHZoc2OPJicl1Ne7O2r7-ul2is_iVHTNpr7jwE24XJx3OYQVkxB1N-GMyD-czlJ68utstKB-f1-hNe3zrmLUhiB1CBj6Eld3uylU5ezy2TAQze9OTbElkm2GCAB9-wwebU-oIIuVvWjqrLtLGgZOQcKBVn6HWBiXKtMvgUCaQ79kLug4C7KV6OlsX9CT9inN2fUKtF4-37PkpzxCrgxnsfM4'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_sales_return_cancelation():

    sales_return_id_to_cancel = 69

    response = requests.post(
        url=f'{base_url}accounts/return/cancel/{sales_return_id_to_cancel}',
        headers=head
    )
    print(response.status_code)
    print(response.json())

def test_canceled_return_cancel_validation():

    sales_return_id_to_cancel = 68

    response = requests.post(
        url=f'{base_url}accounts/return/cancel/{sales_return_id_to_cancel}',
        headers=head
    )
    print(response.status_code)
    print(response.json())

def test_invalid_return_id_cancel():

    sales_return_id_to_cancel = 490

    response = requests.post(
        url=f'{base_url}accounts/return/cancel/{sales_return_id_to_cancel}',
        headers=head
    )
    print(response.status_code)
    print(response.json())

def test_sales_return_cancel_method_validation():

    sales_return_id_to_cancel = 500

    response = requests.get(
        url=f'{base_url}accounts/return/cancel/{sales_return_id_to_cancel}',
        headers=head
    )
    print(response.status_code)
    print(response.json())