from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import CashbackHistory

router = APIRouter(prefix="/cashback", tags=["cashback"])

def get_real_ip(request: Request):

    forwarded = request.headers.get("X-Forwarded-For")

    if forwarded:
        return forwarded.split(",")[0]
    return request.client.host

@router.get("/")
async def calculate_cashback(request: Request, price:float, vip:bool, discount:int = 0, db: Session = Depends(get_db)):
    """
    Rota padrão para calcular o cashback da compra do cliente
    """
    user_ip = get_real_ip(request) #get the user IP

    if price < 0 or discount < 0:
        raise HTTPException(status_code=400, detail="Valores não podem ser negativos")

    normalCashback = 0.05
    vipCashback = 0.1

    if discount > 0:
        discount /= 100
        price -= discount * price

    cashbackValue = price * normalCashback

    if vip == True:
        cashbackValue = cashbackValue * vipCashback + cashbackValue

    if price > 500:
        cashbackValue *= 2

    cashbackValue = round(cashbackValue, 2)

    #create an object and add the values
    registration = CashbackHistory(
        user_ip=user_ip,
        price=price,
        vip=vip,
        cashback_value=cashbackValue
    )

    db.add(registration)
    db.commit()
    db.refresh(registration) 
    
    return {"cashback_value": cashbackValue, "id": registration.id}

@router.get("/history")
async def get_history(request: Request, db: Session = Depends(get_db)):
    """
    Rota para pegar o histórico do cashback baseado no IP do usuário
    """
    user_ip = get_real_ip(request)
    
    query = db.query(CashbackHistory).filter(CashbackHistory.user_ip == user_ip).all()
    
    return query