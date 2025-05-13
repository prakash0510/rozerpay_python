from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import hmac
import hashlib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend origin in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

@app.post("/api/verify-signature")
async def verify_signature(request: Request):
    data = await request.json()
    order_id = data.get("razorpay_order_id")
    payment_id = data.get("razorpay_payment_id")
    signature = data.get("razorpay_signature")

    generated_signature = hmac.new(
        RAZORPAY_KEY_SECRET.encode(),
        f"{order_id}|{payment_id}".encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(generated_signature, signature):
        return JSONResponse(content={"status": "Signature valid"}, status_code=200)
    else:
        return JSONResponse(content={"error": "Invalid signature"}, status_code=400)
