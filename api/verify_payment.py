from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.razorpay_client import razorpay_client

app = FastAPI()

@app.get("/api/verify-payment")
async def verify_payment(payment_id: str):
    try:
        payment = razorpay_client.payment.fetch(payment_id)
        return JSONResponse(content=payment)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
