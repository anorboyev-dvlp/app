# app.py
if body.code != otp.code:
otp.tries_left -= 1
db.commit()
raise HTTPException(400, "Invalid code")


# Success → delete OTP
db.delete(otp)
db.commit()


user = find_user_by_phone(db, phone)
token = make_jwt({"sub": user.phone})
return TokenOut(access_token=8286040355:AAHLVrUsrF456ppe-GMapQeexaGRMgZRtGE)


# ------------------ PROTECTED ------------------
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()




def current_user(creds: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> User:
try:
payload = jwt.decode(creds.credentials, JWT_SECRET, algorithms=["HS256"])
phone = payload.get("sub")
user = find_user_by_phone(db, phone)
if not user:
raise HTTPException(401, "User not found")
return user
except jwt.ExpiredSignatureError:
raise HTTPException(401, "Token expired")
except Exception:
raise HTTPException(401, "Invalid token")


@app.get("/me/status", response_model=StatusOut)
def me_status(u: User = Depends(current_user)):
now = datetime.utcnow()
if u.subscription_end:
delta = (u.subscription_end - now).days
days_left = max(delta, 0)
status = "active" if u.subscription_end > now else "inactive"
next_payment = (u.subscription_end + timedelta(days=1)).strftime("%Y-%m-%d") if status == "active" else None
else:
status = "inactive"
days_left = 0
next_payment = None


return StatusOut(status=status, days_left=days_left, next_payment=next_payment)


# Mock tests
CATEGORIES = [
{"key": "ona", "title": "Ona tili", "count": 12},
{"key": "adb", "title": "Adabiyot", "count": 8},
{"key": "multi", "title": "Multilevel", "count": 5},
{"key": "ielts", "title": "IELTS", "count": 6},
]


@app.get("/tests/categories", response_model=List[TestCategory])
def categories():
return CATEGORIES


@app.get("/tests/list")
def tests_list(category: str):
# Mock list
return [{"id": f"{category}-{i}", "title": f"{category.upper()} Test #{i+1}", "questions": 30} for i in range(5)]


# Healthcheck
@app.get("/")
def root():
return {"ok": True, "service": "test-platform-api", "time": datetime.utcnow().isoformat()}


# Run: uvicorn app:app --host 0.0.0.0 --port 8000
