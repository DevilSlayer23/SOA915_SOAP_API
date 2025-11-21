Here are ready-to-use SOAP XML payloads for all four CRUD operations that you can paste into Postman (POST to http://localhost:5000/soap, header Content-Type: text/xml).

## 1. Create User
```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <create_user>
      <name>Michael Scott</name>
      <age>45</age>
    </create_user>
  </soap:Body>
</soap:Envelope>
```


## Response Example:

```<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <create_userResponse>
      <result>User 3 created</result>
    </create_userResponse>
  </soap:Body>
</soap:Envelope>
```

## 2. Get User Details
```<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <get_user_details>
      <user_id>3</user_id>
    </get_user_details>
  </soap:Body>
</soap:Envelope>
```

## Response Example:

``` <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <get_user_detailsResponse>
      <result>Name: Michael Scott, Age: 45</result>
    </get_user_detailsResponse>
  </soap:Body>
</soap:Envelope>
```

## 3. Update User Name
```<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <update_user_details>
      <user_id>3</user_id>
      <new_name>Michael S.</new_name>
    </update_user_details>
  </soap:Body>
</soap:Envelope>
```

## Response Example:
```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <update_user_detailsResponse>
      <result>User 3 updated to Michael S.</result>
    </update_user_detailsResponse>
  </soap:Body>
</soap:Envelope>
```

## 4. Delete User
```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <delete_user>
      <user_id>3</user_id>
    </delete_user>
  </soap:Body>
</soap:Envelope>
```

## Response Example:
```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <delete_userResponse>
      <result>User 3 deleted</result>
    </delete_userResponse>
  </soap:Body>
</soap:Envelope>
```

## How to use in Postman

````
Create a POST request: http://localhost:5000/soap

Add header: Content-Type: text/xml

Paste one of the payloads above into Body → raw

Click Send

You can do Create → Read → Update → Read → Delete → Read in sequence to demonstrate full CRUD.

```