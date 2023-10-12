import requests
import pytest
import json

head = {
        'accept': 'application/json, text/plain',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiZGE5MmYxYzllM2NlNTc5OGIxNWQ4NzIyYmEzN2IyNDAwNzNjNjQ3MzQ2YTc1NmU2MTE2ZmVjNTZlZjZjMWEyMzUxOTA2Y2NjZDI1YmZiMGYiLCJpYXQiOjE2OTY4MjIxODIsIm5iZiI6MTY5NjgyMjE4MiwiZXhwIjoxNzI4NDQ0NTgyLCJzdWIiOiIxMSIsInNjb3BlcyI6WyIqIl19.UM5LdptKozp-aEcZxFzC48j0U4Mnv91pMoCl7JUvGE5JzyXiCEZdomrE0rf3b-DZaI4nhFygjJmCdTEXOH6WPxFKTIcV1vee78pQOT4HXzeL-PYrQIM2vI6CZ9dHpbQ4aiq0FMKQI6WY1LcwhiXR3iLh4A2PwpvoIZe3B32rAi2BNohcScsZltU8TjaWvHRsQAWUvNSZveutC0quKdqZhaLDg5JAAvUsBNgml0zo7vujtdsPNapX4pilDfdj3kb2poGJwyO2464nJvSbaSiswrY1tc25e2plTJbmtJWDhHbpbpBe8GeUGqu8aTjA9GO5R81bi3Lvrpyk53-Y5qZtV_CmVstX3Bm0FYjOSFqojk173Mse4ZkIrsP6JJ1DN2g9lRwCS_IJLIuDRq2nDFKqpT-5GZOntkd9uLUVuP8qYQePHiPD36r1GO-QdqQ4vGRiZVYhM_7SOR4TiE_TRuMv0M2VxArFi9EA4HV86gmbKE8U6IAi5rV6Mz5e_s18YIVjWDEhQQKudD9S8x4rMMebIcqFeaAae31V9bZOb3Gv1pNBNvO_Jq3jMZG3sWrXbFRjsBhWey6mVQaPPJPIy9sdcg-hbbQ-vKTU1TfXwvd9oIM19M_6OhUqTernTq3oeyhsvvpOhV-Xf9Su1I7ohcvsHync6xcGiH9_ZKRWXxSOHFs'
}

base_url = 'https://api.staging.bepari.info/demo/api/V1.1/'

def test_invoice_view_valid_invoiceid():

    invoice_id_to_view = 1042

    response = requests.get(
        url=f"{base_url}accounts/invoice/view/{invoice_id_to_view}",
        headers=head
    )

    print(response.status_code)
    print(response.json())
    assert 200 == response.status_code

def test_invoice_view_invalid_invoiceid():

    invoice_id_to_view = 1050

    response = requests.get(
        url=f"{base_url}accounts/invoice/view/{invoice_id_to_view}",
        headers=head
    )

    print(response.status_code)
    print(response.json())
    assert 404 == response.status_code

# if __name__ == "__main__":
    # pytest.main(["-v", "InvoiceView.py", "--html=report.html"])