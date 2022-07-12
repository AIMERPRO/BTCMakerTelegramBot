from sqlalchemy import Integer, Column, BigInteger, String, sql, Float

from utils.db_api.db_gino import TimedBaseModel


class Crypto(TimedBaseModel):
    __tablename__ = 'crypto'
    id = Column(BigInteger, primary_key=True)

    name = Column(String(10))
    price = Column(Float)

    query: sql.Select