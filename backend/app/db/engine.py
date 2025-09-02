from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, echo=True)