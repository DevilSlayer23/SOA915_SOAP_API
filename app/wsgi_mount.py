# app/wsgi_mount.py
from fastapi.middleware.wsgi import WSGIMiddleware
from soap_service import app as soap_app

# Function to mount SOAP WSGI app under /soap endpoint
def mount_soap(app):
    app.mount("/soap", WSGIMiddleware(soap_app))