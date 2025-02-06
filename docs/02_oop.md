# OOP
The difference between object-oriented programming (OOP) and procedural programming?

Object-Oriented Programming (OOP) organizes code around **objects** that represent real-world entities, whereas procedural programming structures code as **a sequence of instructions (functions).**

- **OOP Advantage**: Code is more **modular, reusable, easy to maintain**.

- **Procedural** (C style): each function is organized in `function`, all data is stored globally.

- **Object Oriented** (Python/Java): data is organized in `class`, data and behavior are bound together.
## **1. The four main features of OOP**

| Characterization  | Explanation                        | Code example           |
|-------------------| ---------------------------- |------------------------|
| **Encapsulation** | Encapsulate data and methods inside the class    | `self.__private_var`   |
| **Inheritance**   | Subclasses can inherit methods and attributes from the parent class | `class Child(Parent):` |
| **Polymorphism**  | Same interface, different implementation          | `method overriding`    |
| **Abstraction**   | Expose only necessary information and hide implementation details | `ABC` Module           |

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Can only be accessed via methods

account = BankAccount(100)
print(account.get_balance())  # ✅ 100
# print(account.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'
```

## 2. Design Patterns

### **2.1 Singleton**

> "A Singleton ensures that **only one instance** of a class is created. There are several ways to implement it in Python."

**Method 1：Use `__new__()`**

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # ✅ True
```

**Method 2：Use decorator**

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton:
    pass
```

✅ **Applicable scenarios:**

- **Database connection management** (prevents creation of multiple connection objects)
- **Global configuration management**
- **Logging system**


### 2.2 Factory


> "Factory pattern provides an **interface to create objects without specifying the exact class**. This makes it easier to extend and modify."

**Example: Create different types of database connections**

```python
class DatabaseFactory:
    @staticmethod
    def get_database(db_type):
        if db_type == "mysql":
            return MySQLDatabase()
        elif db_type == "sqlite":
            return SQLiteDatabase()
        else:
            raise ValueError("Unknown database type")

class MySQLDatabase:
    def connect(self): print("Connecting to MySQL...")

class SQLiteDatabase:
    def connect(self): print("Connecting to SQLite...")

db = DatabaseFactory.get_database("mysql")
db.connect()  # ✅ "Connecting to MySQL..."
```

✅ **Applicable Scenarios:**

- **Dependency Injection (DI)**
- **Plugin System**
- **Different Data Sources (SQL, NoSQL, File) Handling**



### **2.3 Observer**

> "Observer pattern is used when multiple objects need to react to state changes in another object."

**Example: Event Listener**

```python
class Observer:
    def update(self, message): pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received update: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Use example
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject = Subject()
subject.attach(observer1)
subject.attach(observer2)

subject.notify("Event happened!")  # ✅ Both observers are notified
```

✅ **Applicable Scenarios:**

- **GUI event listener**
- **Message subscription system**
- **Data synchronization (e.g., Stock Market monitoring)**



## 3. Summary

| Design Patterns | Functions                                     | Example Scenarios |
| ------------- |-----------------------------------------------| -------------------------- |
| **Singleton** | Only one instance                             | **Database connection, logging system** |
| **Factory** | Unified object creation                       | **Database management, plug-in systems** |
| **Observer** | Listening for events, automatic notifications | **Event-driven architecture, message subscription** |

