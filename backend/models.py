from sqlalchemy import create_engine, Column, Integer, Boolean, Float, String
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

db = create_engine(DATABASE_URL)

Base = declarative_base()

#tabela de histórico
class CashbackHistory(Base):
    __tablename__ = "cashback_history"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_ip = Column("user_ip", String(255), nullable=False)
    price = Column("price", Float, nullable=False)
    vip = Column("vip", Boolean, nullable=False)
    cashback_value = Column("cashback_value", Float, nullable=False)

    def __init__(self, user_ip, price, vip, cashback_value):
        self.user_ip = user_ip
        self.price = price
        self.vip = vip
        self.cashback_value = cashback_value