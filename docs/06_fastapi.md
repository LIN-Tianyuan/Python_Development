# FastAPI
```python
from fastapi import FastAPI

app = FastAPI()

# 1. Path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# 2. Query parameters
@app.get("/users/")
def read_user(name: str, age: int = 18):  # age Default value 18
    return {"name": name, "age": age}

# 3. Request body（POST）
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/items/")
def create_item(item: Item):
    return {"message": f"Item {item.name} created", "price": item.price}
```
Difference between path parameters and query parameters?

- Path parameters are **URL mandatory** for `/items/{item_id}`.
- Query parameters are **optional** such as `/users?name=John&age=30`.

How do we set default parameters for the API?
```python
@app.get("/products/")
def get_products(limit: int = 10):
    return {"limit": limit}
```
## 1. Dependency Injection
Dependency Injection is a mechanism provided by FastAPI to automatically manage and pass dependency objects to avoid creating the same resources (e.g., database connections, permission checks, logging systems, etc.) across multiple API endpoints.

In FastAPI, dependency injection uses Depends() to automatically execute a function and pass its return value to the API endpoint.

```python
from fastapi import Depends

def common_params(q: str = "", limit: int = 10):
    return {"query": q, "limit": limit}

@app.get("/search/")
def search(params: dict = Depends(common_params)):
    return params
```
The role of dependency injection?
- The code is clearer and avoids duplicate logic (e.g. **database connection, permission validation, logging**).

How to use Dependency Injection in database operations?
- We can create a `get_db()` dependency to pass the database connection automatically:
```python
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```
Detailed analysis of the yield mechanism
 - Normal functions vs. yield generators
 - Python's yield turns a function into a “generator” that doesn't execute immediately, but pauses and resumes when next() is called.
```python
def my_generator():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")

gen = my_generator()
print(next(gen))  # "Start" -> output 10
print(next(gen))  # "Middle" -> output 20
"""
Start
10
Middle
20
End
"""
```
 - The first time next(gen) is executed, it pauses after yield 10 and returns 10.
 - The second time next(gen) is executed, it continues after yield 10, executes yield 20, and then pauses again.
## 2. JWT authentication (identity verification)
```python
from fastapi import Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return {"error": "Invalid token"}

@app.get("/protected/")
def protected_route(payload: dict = Depends(verify_token)):
    return {"message": "Access granted", "user": payload}

```
What is the basic flow of JWT authentication?
 - User logs in → server returns JWT (access token) → client stores JWT → JWT is attached when accessing protected APIs → server validates JWT and returns data.

Difference between JWT authentication and OAuth2?

 - **OAuth2** is mainly used for authorization (e.g. Google/Facebook login).
 - **JWT** is a stateless authentication mechanism that can be used in APIs.
## 3. FastAPI Interaction with PostgreSQL
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Create a database model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Dependency Injection - Get Database Sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User search
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```
How to create database tables?
```python
Base.metadata.create_all(bind=engine)
```
How to use ORM for database insertion?
```python
@app.post("/users/")
def create_user(name: str, db: Session = Depends(get_db)):
    new_user = User(name=name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```
## 4. FastAPI Performance Optimization
 - Using the `async` keyword
```python
@app.get("/data/")
async def fetch_data():
    return {"data": "This is async"}
```
 - Run FastAPI with Uvicorn
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```
 - Cache Query Results with Redis
```python
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.get("/cache/")
def get_cached_data():
    cached_data = redis_client.get("my_key")
    if cached_data:
        return {"data": cached_data.decode("utf-8")}
    result = "Expensive computation result"
    redis_client.set("my_key", result, ex=60)  # 60 seconds cache
    return {"data": result}
```