def def_cashback (price, vip, discount=0):
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
    
    return cashbackValue

print(def_cashback(600, True, 15))