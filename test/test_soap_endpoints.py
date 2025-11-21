import requests


SOAP_ENDPOINT = "http://localhost:8000/soap"


SOAP_GET = '''<?xml version='1.0'?>
<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
<soap:Body>
<get_user_details>
<user_id>1</user_id>
</get_user_details>
</soap:Body>
</soap:Envelope>'''


SOAP_UPDATE = '''<?xml version='1.0'?>
<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
<soap:Body>
<update_user_details>
<user_id>1</user_id>
<new_name>New Name</new_name>
</update_user_details>
</soap:Body>
</soap:Envelope>'''


SOAP_DELETE = '''<?xml version='1.0'?>
<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
<soap:Body>
<delete_user>
<user_id>2</user_id>
</delete_user>
</soap:Body>
</soap:Envelope>'''




def test_get_user_details():
    r = requests.post(SOAP_ENDPOINT, data=SOAP_GET, headers={"Content-Type": "text/xml"})
    assert r.status_code == 200
    assert b"John Doe" in r.content




def test_update_user_details():
    r = requests.post(SOAP_ENDPOINT, data=SOAP_UPDATE, headers={"Content-Type": "text/xml"})
    assert r.status_code == 200
    assert b"updated to New Name" in r.content




def test_delete_user():
    r = requests.post(SOAP_ENDPOINT, data=SOAP_DELETE, headers={"Content-Type": "text/xml"})
    assert r.status_code == 200
    assert b"deleted" in r.content

