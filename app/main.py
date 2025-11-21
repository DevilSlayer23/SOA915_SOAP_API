# app/main.py
from fastapi import FastAPI
from app.wsgi_mount import mount_soap
from app.api.routes import router as rest_router

app = FastAPI(title="Gateway API")

# Mount SOAP WSGI app at /soap
mount_soap(app)

# Include REST API routes
app.include_router(rest_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FastAPI gateway up and running"}