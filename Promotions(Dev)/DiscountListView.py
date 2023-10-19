import requests
import pytest
import json

head = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiODQyYjUxZTQyNDJiN2U1ZWUzZDNmZWE5NWE3ZmQ0NDQ4NWRjNDU1MDJlNGQ1YmQzNDI4ZDBlYjExMjQ0YjJmMDc0NzFlNDRhYmM0YmVkZDUiLCJpYXQiOjE2OTc2ODY5OTgsIm5iZiI6MTY5NzY4Njk5OCwiZXhwIjoxNzI5MzA5Mzk4LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.hndzWp-Mo7niI0l81eqx_iWkMDvqp1X_lMgXysZHLufwDsZER-s-RdjHcvtGeTxm7ue3t89X3oIbBcx7JZpwlfVLk_zKE-SJikGV1n893b3uN0d4LQyzjglhSMPquoD46Maq0QI5gjPWCGzQxr0pM1wWACOAmLzwv6JXnmykkGJTX8oJxSbqm5HGvxHrL7Bpq9f-QBGNliy-AO4tNFEVftMfxFruz1E8qa2eSbcqnqnWbsQPXOr5m_O9y_OiWuFPKiN8oAUmGFuBkNqt9FCrUQ2P7U3gHUX0PukmTVnogta1rpIw5j8_nwROvTPgWDLvN6t40lm-Hz7BwRoxF6pQ9YgLbvYHCXBY6jjwePRzcPk7eB4zZ7psOq-mB8I3cTosvlE2ERx8XZFrVW5e7rkC5hK2updlkiyDBUKm4ITgjVDTJzgiQh1QQ5uZu8TGkCuPSuklwT0NHOetage_aKscptGGDCzuo6f9WcUFWE0f-UZaGJ4HROWeERXc6HpF_mxFcHiK_PfIyVB8cuD7IFBKw-w5UgY1z8tKOLBrnADvaEg-Y5PWcadbelUBmlbsOSoSfDXUdEBQy8X_mCNSaFkJvuCDEm0N_mj8yAGmoYww_bDIPYLidMM_0Lp-BvD6EPgy35mFUxHLCRMEobqsnDvRnXtvU46i4CyZiW7tRiykCzk'
}

base_url = 'https://api.dev.bepari.info/demo/api/V1.1/'

params = {
    'page': 1,
    'page_size': 20
}

def test_discount_list_view():


    response = requests.get(
        url = f'{base_url}promotion/discount-offer/list?',
        params = params,
        headers = head
    )

    API_Data = response.json()
    formatted_json = json.dumps(API_Data, indent = 4)

    print(response.status_code)
    print(formatted_json)
