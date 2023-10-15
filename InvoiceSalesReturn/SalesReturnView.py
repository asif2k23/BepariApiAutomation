import requests
import json
import pytest

head = {
        'accept': 'application/json, text/plain',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNDc2ZDQ0NTc2ZDZmNWNmNzRmMTMwNTg5OTBmOWU2ODg0OWM4MzYzM2JmZjdjMDllN2ZlNWRkZDEyNDQ0MDM1NzgwYjAwZTJkNDg5NTcwYjQiLCJpYXQiOjE2OTcwODE4NzUsIm5iZiI6MTY5NzA4MTg3NSwiZXhwIjoxNzI4NzA0Mjc1LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.JRkqcC1s0k2Kz3pTg2Hnnsk6HchcoCTJ9965r1yNtxdGZN1Vkk-cL6WfWcq_kLLA5iPBB1hvGAF6kIZO1_zpdEnSiHaoP8AV1OQOCL5YGiHfWizYmRNX_042vIYxW3VAGEykfyXfLdDSADqmYW3ALdI5nL78gkJ_h2oNCkyXG4Dum76vspVcz_ouPsfHYCFsqQewMXk-CHe2LXXMgtYsp4P-yl7YfG6iM7qd5-OJzsTqj2rOBxcNRAbB9CuqgFd-Ty2TwBg13wK3dp7XtTKlTA_KBJ__XAO-olX1wjILs_qgdJ9A_tKAX793D3Cck_-jdhOFgSFtl-M5CNZu73kWjftC6-bPI5-84GYzTnakCn-vZzO8mjMPsg7CcGY5TLgHuTLyT40GpbgJFKl1017fIUoAzcCCIykZ2OqBaQ909LHh3oNw7Igm3Xnlz5jON22GDH4AAXGl8sJd83M87-STGYjObyl4AT4a8uSwSmO6S9TNj0UMLo1aFb3C3Fh5ZfrSSy4je7ARmljzsG6IiKoKjQXXG_hnBmXU0oQ8L8IoVOxElOrjEGU2AcSOxj06O0uo0EcYCvJpL5wY9O1-Iw9VVnEPerkn8M-PYfXT3L_MVDpHAl9s440hHq7G7n2so11Z4-zLDcslWG28nOQyvQ1rKBmPXrIiDjnCadZTG99tHis'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_test_invoice_return_view():

    salesreturn_id_to_return_view = 51

    response = requests.get(
        url = f'{base_url}accounts/return/view/{salesreturn_id_to_return_view}',
        headers = head
    )

    print(response.status_code)
    print(response.text)