from lxml import etree
from serivces.user_service import get_user_summary, update_user_name, delete_user


NS_SOAP = "http://schemas.xmlsoap.org/soap/envelope/"




def _parse_body(xml_bytes):
    root = etree.fromstring(xml_bytes)
    body = root.find(f"{{{NS_SOAP}}}Body")
    if body is None or len(body) == 0:
        raise ValueError("No SOAP body")
    method_el = body[0]
    method = etree.QName(method_el).localname
    return method, method_el




def _wrap_response(localname, result_text):
    nsmap = {"soap": NS_SOAP}
    envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", nsmap=nsmap)
    body = etree.SubElement(envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
    resp = etree.SubElement(body, localname)
    result = etree.SubElement(resp, "result")
    result.text = result_text
    return etree.tostring(envelope, xml_declaration=True, encoding="utf-8")




def handle_soap_request(xml_bytes):
    method, el = _parse_body(xml_bytes)

    if method == "get_user_details":
        uid_el = el.find("user_id")
        if uid_el is None or not uid_el.text:
            raise ValueError("user_id missing")
        user_id = int(uid_el.text)
        result = get_user_summary(user_id)
        return _wrap_response("get_user_detailsResponse", result)

    if method == "update_user_details":
        user_id = int(el.findtext("user_id"))
        new_name = el.findtext("new_name")
        result = update_user_name(user_id, new_name)
        return _wrap_response("update_user_detailsResponse", result)


    if method == "delete_user":
        user_id = int(el.findtext("user_id"))
        result = delete_user(user_id)
        return _wrap_response("delete_userResponse", result)

    raise ValueError(f"Unknown SOAP operation: {method}")