from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:1234@localhost/pizza_delivery',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()
