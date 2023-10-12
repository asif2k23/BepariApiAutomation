import requests
import pytest
import json

head = {
        'accept': 'application/json, text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNzQ1YzIxZTQzNTNjZGE4ODljZDFjNDcxNjRiYmRjNzMxYjVmNjg3NjE2Y2U5MzJjYjg4ZmUxYjJkZDQ3Mzc5NGY4OTE2NmU3OWFmZWRlZTMiLCJpYXQiOjE2OTY5MjgyMTQsIm5iZiI6MTY5NjkyODIxNCwiZXhwIjoxNzI4NTUwNjE0LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.TO_P15SW-eFBUjIkAL-KvTJXLy8K-2MJjXM3tcZG7sPT3rc-nOpPMJpMpKiIrGr2__tFHkSsgRP3GljhaGpesPNonjE7Dyp_z9nKtd4fxLyUAUW89NWy1rQMKAzjoGjLZb-mjl3b1-0TdPstVOcaxwUbhw1bQin_5-xxZYipXZEV4JTS28JHnJGwKmnMa27yzOcrmt9GWJ5XuYq8J84oQdhhivjbNFTETFr9a-vm8hLQCQroWFUH8-pU6QvqJmHUVdnzJif0Soqe5RGKvqbgvP46a3oSLdiB2EqAhx3xPXekLnqqeTOLT6_WqHDpgiOHGROgvBpkMfVUc9TRJCBDcV3vEo_yaxK5S3QSUi53Ffi7h3_A606gLD1J1JZCPT_rO6iujlxJg1ELtULqfjmx8BYEZrHAwaEq4viXTMt40itUectW4nysOOerCopqDdBXdaQhkMFYzkumFJOiQXte4bVhj8HrRG1VEBUisv4qdz_vXw4Xvy1NsIhFpgGH6VR00OP3RuiaON9CFSEWI4m01yH6uv1fpsxqetkVAq7A9H80jwuVUsgbV7Eh2EROYm-qx32ixgQAYlc3KbzGPebVDFYCvYn2RLxFZKDDU_tkuEP8k0tUgUsRxkoWgxbYej_xOz7nWxZnKz2r_oQZ2dBUuXiUSmLCdas9FPvSnL8u_D0'
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