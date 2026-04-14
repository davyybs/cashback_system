from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import CashbackHistory

router = APIRouter(prefix="/cashback", tags=["cashback"])

@router.get("/")
async def calculate_cashback(request: Request, price:float, vip:bool, discount:int = 0, db: Session = Depends(get_db)):
    """
    Rota padrão para calcular o cashback da compra do cliente
    """
    user_ip = request.client.host #get the user IP

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

    #create an object and add the values
    registration = CashbackHistory(
        user_ip=user_ip,
        price=price,
        discount=discount,
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
    user_ip = request.client.host
    
    query = db.query(CashbackHistory).filter(CashbackHistory.user_ip == user_ip).all()
    
    return query