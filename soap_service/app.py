# from flask import Flask, request, Response, send_file
# from lxml import etree
# from .handlers import handle_soap_request
# import os


# app = Flask(__name__)


# WSDL_PATH = os.path.join(os.path.dirname(__file__), "wsdl", "user_service.wsdl")


# @app.route("/soap", methods=["POST", "GET"])
# def soap_root():
#     if request.method == "GET":
#         # serve WSDL
#         return send_file(WSDL_PATH, mimetype="text/xml")


#     # POST -> SOAP envelope
#     xml = request.data
#     try:
#         response_xml = handle_soap_request(xml)
#         return Response(response_xml, mimetype="text/xml")
#     except Exception as e:
#     # Return a SOAP Fault
#         fault = ("<?xml version='1.0'?>"
#         "<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>"
#         "<soap:Body><soap:Fault><faultcode>Server</faultcode>"
#         f"<faultstring>{str(e)}</faultstring></soap:Fault></soap:Body></soap:Envelope>")
#     return Response(fault, status=500, mimetype="text/xml")

from flask import Flask, request, Response, send_file
from lxml import etree
import os

app = Flask(__name__)

# In-memory user store
users = {
    1: {"name": "John Doe", "age": 30},
    2: {"name": "Jane Smith", "age": 28}
}
next_user_id = 3  # auto-increment for new users

WSDL_PATH = os.path.join(os.path.dirname(__file__), "wsdl", "user_service.wsdl")


def soap_response(body_content):
    """Wrap the response in a SOAP envelope"""
    return f"""<?xml version='1.0'?>
                <soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
                    <soap:Body>
                        {body_content}
                    </soap:Body>
                </soap:Envelope>"""


@app.route("/", methods=["POST", 'GET'])
def soap_root():
    global next_user_id

    if request.method == "GET":
        # serve WSDL
        return send_file(WSDL_PATH, mimetype="text/xml")

    # POST -> handle SOAP envelope
    xml = request.data.decode()

    try:
        # CREATE
        if "<create_user>" in xml:
            name = xml.split("<name>")[1].split("</name>")[0]
            age = int(xml.split("<age>")[1].split("</age>")[0])
            user_id = next_user_id
            users[user_id] = {"name": name, "age": age}
            next_user_id += 1
            body = f"<create_userResponse><result>User {user_id} created</result></create_userResponse>"
            return Response(soap_response(body), mimetype="text/xml")

        # READ
        elif "<get_user_details>" in xml:
            user_id = int(xml.split("<user_id>")[1].split("</user_id>")[0])
            user = users.get(user_id)
            if user:
                body = f"<get_user_detailsResponse><result>Name: {user['name']}, Age: {user['age']}</result></get_user_detailsResponse>"
            else:
                body = f"<get_user_detailsResponse><result>User not found</result></get_user_detailsResponse>"
            return Response(soap_response(body), mimetype="text/xml")

        # UPDATE
        elif "<update_user_details>" in xml:
            user_id = int(xml.split("<user_id>")[1].split("</user_id>")[0])
            new_name = xml.split("<new_name>")[1].split("</new_name>")[0]
            if user_id in users:
                users[user_id]["name"] = new_name
                body = f"<update_user_detailsResponse><result>User {user_id} updated to {new_name}</result></update_user_detailsResponse>"
            else:
                body = f"<update_user_detailsResponse><result>User not found</result></update_user_detailsResponse>"
            return Response(soap_response(body), mimetype="text/xml")

        # DELETE
        elif "<delete_user>" in xml:
            user_id = int(xml.split("<user_id>")[1].split("</user_id>")[0])
            if user_id in users:
                del users[user_id]
                body = f"<delete_userResponse><result>User {user_id} deleted</result></delete_userResponse>"
            else:
                body = f"<delete_userResponse><result>User not found</result></delete_userResponse>"
            return Response(soap_response(body), mimetype="text/xml")

        else:
            # Unknown operation
            body = "<soap:Fault><faultcode>Client</faultcode><faultstring>Unknown operation</faultstring></soap:Fault>"
            return Response(soap_response(body), status=400, mimetype="text/xml")

    except Exception as e:
        # Return SOAP Fault for any exception
        fault = f"""<?xml version='1.0'?>
                    <soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
                    <soap:Body>
                        <soap:Fault>
                        <faultcode>Server</faultcode>
                        <faultstring>{str(e)}</faultstring>
                        </soap:Fault>
                    </soap:Body>
                    </soap:Envelope>"""
        return Response(fault, status=500, mimetype="text/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)