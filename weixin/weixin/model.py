from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    # print('uri',get_project_settings().get("SQL_CONNECT_STRING"))
    return create_engine(get_project_settings().get("SQL_CONNECT_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class WeiXinData(Base):
    __tablename__ = 'weixin_data'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))
    # processed_marker = Column(String(64))

class WeiXinOilCross(Base):
    __tablename__ = 'weixin_oil_cross'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))

class WeiXinLngCon(Base):
    __tablename__ = 'weixin_lng_con'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))

class WeiXinCnpcNews(Base):
    __tablename__ = 'weixin_cnpc_news'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))



class WeiXinPetroTrading(Base):
    __tablename__ = 'weixin_petro_trading'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))

class WeiXinEnergyExpress(Base):
    __tablename__ = 'weixin_energy_express'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))


class WeiXinHaiBei(Base):
    __tablename__ = 'weixin_hai_bei'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))


class WeiXinOffshoreEnergy(Base):
    __tablename__ = 'weixin_offshore_energy'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))


class WeiXinHaiBo(Base):
    __tablename__ = 'weixin_hai_bo'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))


class WeiXinCRSL(Base):
    __tablename__ = 'weixin_crsl'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))


class WeiXinOilCubic(Base):
    __tablename__ = 'weixin_oil_cubic'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))


class WeiXinOilLink(Base):
    __tablename__ = 'weixin_oil_link'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    pre_title = Column(String(255))
    author = Column(String(255))
    pub_time = Column(String(255))
    preview_img_link = Column(String(255))
    content = Column(Text)
    categories = Column(String(255))
    crawl_time = Column(String(255))
    url = Column(String(255))
    images_url = Column(String(2048))
    images = Column(String(4096))

