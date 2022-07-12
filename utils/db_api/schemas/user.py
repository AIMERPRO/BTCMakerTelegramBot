from sqlalchemy import Integer, Column, BigInteger, String, sql, Float, Boolean, ARRAY

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)

    name = Column(String(100))
    balance = Column(Float)
    withdraw = Column(Float)
    earn = Column(Float)
    earn_easy = Column(Float)

    percent = Column(Float)

    verification = Column(Boolean)

    cryptos = Column(String)

    BTC_balance = Column(Float)
    ETH_balance = Column(Float)
    USDT_balance = Column(Float)
    USDC_balance = Column(Float)
    DAI_balance = Column(Float)

    BTC_hours = Column(Integer)
    ETH_hours = Column(Integer)
    USDT_hours = Column(Integer)
    USDC_hours = Column(Integer)
    DAI_hours = Column(Integer)

    BTC_balance_Z = Column(Float)
    ETH_balance_Z = Column(Float)
    USDT_balance_Z = Column(Float)
    USDC_balance_Z = Column(Float)
    DAI_balance_Z = Column(Float)

    lang = Column(String(100))

    referral = Column(BigInteger)

    query: sql.Select
