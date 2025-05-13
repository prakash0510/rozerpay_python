from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.razorpay_client import razorpay_client

app = FastAPI()

@app.post("/api/create-order")
async def create_order(request: Request):
    value = True
    if request.method == "OPTIONS":
        value = True

    if value:
        data = await request.json()
        amount = data.get("amount")
        currency = "INR"
        payment_capture = 1

        try:
            razorpay_order = razorpay_client.order.create({
                "amount": int(float(amount) * 100),
                "currency": currency,
                "payment_capture": payment_capture
            })
            return JSONResponse(content={
                "order_id": razorpay_order['id'],
                "amount": razorpay_order['amount'],
                "currency": razorpay_order['currency']
            })
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/api/test")
async def create_order(request: Request):
    try:
        return JSONResponse(content={
                "message": "Hello from Razorpay API"
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})