from fastapi import APIRouter

router = APIRouter(prefix="/cashback", tags=["cashback"])

@router.get("/")
async def calculate_cashback(price:float, vip:bool, discount:int = 0):
    """
    Rota padrão para calcular o cashback da compra do cliente
    """
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
    
    return {"Valor do Cashback:": cashbackValue}