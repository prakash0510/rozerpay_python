# Razorpay FastAPI Backend for Vercel (No Webhook)

## Features
- ✅ Create Razorpay order
- ✅ Verify Razorpay signature from frontend
- ✅ Fetch Razorpay payment details

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env` file
```
RAZORPAY_KEY_ID=your_key_id_here
RAZORPAY_KEY_SECRET=your_key_secret_here
```

### 3. Run locally using Uvicorn
```bash
uvicorn api.create_order:app --reload
```
```bash
uvicorn api.verify_payment:app --reload
```
```bash
uvicorn api.verify_signature:app --reload
```

---

## API Endpoints

### `POST /api/create-order`
Create an order with amount

### `POST /api/verify-signature`
Verify Razorpay signature sent from frontend

### `GET /api/verify-payment?payment_id=<id>`
Fetch payment details by Razorpay `payment_id`
