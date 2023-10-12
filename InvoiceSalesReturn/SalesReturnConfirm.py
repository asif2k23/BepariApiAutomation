import requests
import pytest
import json

head = {
        'accept': 'application/json, text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNzQ1YzIxZTQzNTNjZGE4ODljZDFjNDcxNjRiYmRjNzMxYjVmNjg3NjE2Y2U5MzJjYjg4ZmUxYjJkZDQ3Mzc5NGY4OTE2NmU3OWFmZWRlZTMiLCJpYXQiOjE2OTY5MjgyMTQsIm5iZiI6MTY5NjkyODIxNCwiZXhwIjoxNzI4NTUwNjE0LCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.TO_P15SW-eFBUjIkAL-KvTJXLy8K-2MJjXM3tcZG7sPT3rc-nOpPMJpMpKiIrGr2__tFHkSsgRP3GljhaGpesPNonjE7Dyp_z9nKtd4fxLyUAUW89NWy1rQMKAzjoGjLZb-mjl3b1-0TdPstVOcaxwUbhw1bQin_5-xxZYipXZEV4JTS28JHnJGwKmnMa27yzOcrmt9GWJ5XuYq8J84oQdhhivjbNFTETFr9a-vm8hLQCQroWFUH8-pU6QvqJmHUVdnzJif0Soqe5RGKvqbgvP46a3oSLdiB2EqAhx3xPXekLnqqeTOLT6_WqHDpgiOHGROgvBpkMfVUc9TRJCBDcV3vEo_yaxK5S3QSUi53Ffi7h3_A606gLD1J1JZCPT_rO6iujlxJg1ELtULqfjmx8BYEZrHAwaEq4viXTMt40itUectW4nysOOerCopqDdBXdaQhkMFYzkumFJOiQXte4bVhj8HrRG1VEBUisv4qdz_vXw4Xvy1NsIhFpgGH6VR00OP3RuiaON9CFSEWI4m01yH6uv1fpsxqetkVAq7A9H80jwuVUsgbV7Eh2EROYm-qx32ixgQAYlc3KbzGPebVDFYCvYn2RLxFZKDDU_tkuEP8k0tUgUsRxkoWgxbYej_xOz7nWxZnKz2r_oQZ2dBUuXiUSmLCdas9FPvSnL8u_D0'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_invoice_return_confirm():

    salesreturn_id_to_return_confirm = 1231

    response = requests.post(
        url = f'{base_url}accounts/return/confirm/{salesreturn_id_to_return_confirm}',
        headers = head
    )

    print(response.status_code)
    print(response.json())