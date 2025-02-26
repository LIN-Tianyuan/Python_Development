# Django
## 1. Django ORM

**Django ORM Query Optimization**

**❓ Q: How can we reduce the N+1 query problem?** 

👉 Use `select_related()` or `prefetch_related()`

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Inefficient queries (N+1 query problem)
books = Book.objects.all()
for book in books:
    print(book.author.name)  # An additional query is performed each time the author is accessed

# Efficient queries (select_related, load all data in one query)
books = Book.objects.select_related('author').all()
for book in books:
    print(book.author.name)  # No additional queries will be generated

# In the case of a ManyToMany relationship, prefetch_related can be used.
```

- **`select_related()`**: for **ForeignKey** relationships, JOIN preloading to reduce queries.
- **`prefetch_related()`**: for **ManyToMany** relationships, use **separate query + Python processing** to improve performance.

**Transaction management**

**❓ Q: How do we ensure data consistency?** 

👉 Use `@transaction.atomic` to ensure that the operation **all succeeds** or **all rolls back**.

```python
from django.db import transaction

@transaction.atomic
def create_order():
    user = User.objects.create(username="test_user")
    Order.objects.create(user=user, amount=100)  # If this fails, user will not be created.
```
- `@transaction.atomic` applies to **multi-table operations**.
- `select_for_update()` applies to **row level locks to prevent concurrent write problems**.

## 2. Django Serializer

**ModelSerializer vs Serializer**

**❓ Q: When to use `ModelSerializer` and when to use `Serializer`?**

👉 `ModelSerializer` automatically maps Django Models, while `Serializer` requires fields to be defined manually.

```python
# Using the ModelSerializer (Automatically Mapping Models)
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']  # Only some of the fields are returned
```

```python
# Custom Serializer (for complex logic such as data format conversion)
class CustomBookSerializer(serializers.Serializer):
    title = serializers.CharField()
    author_name = serializers.CharField(source='author.name')  # Direct mapping of foreign key data
```
- `ModelSerializer` **Applicable to mapping database fields directly**, reducing duplicate code.
- `Serializer` **Suitable for custom formatting/combining multiple model data**.

**Nested serialization**

**❓ Q: How do we return nested objects?** 

👉 `AuthorSerializer` nested `BookSerializer`
```python
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serialization

    class Meta:
        model = Book
        fields = ['title', 'author']
```

## 3. Django ViewSets

**ModelViewSet**

**❓ Q: When to use `ViewSet` and when to use `APIView`?**

👉 `ViewSet` for **standard CRUD operations** and `APIView` for **custom API logic**.

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Customize the create method
    def create(self, request, *args, **kwargs):
        data = request.data
        if 'author' not in data:
            return Response({"error": "Author is required"}, status=400)
        return super().create(request, *args, **kwargs)
```

- `ViewSet` for **Standard CRUD**
- `APIView` for **complex API logic**
- `get_queryset()` **Dynamic querying**

## 4. Authentication & Permission

**JWT Certification**

**❓ Q: How do we use the JWT Authentication API?**

👉 DRF combines `SimpleJWT` with `JWT`.

```bash
pip install djangorestframework-simplejwt
```

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```
- JWT applies **Separation of front and back ends**
- `refresh_token` **prevents frequent re-logins**

**Customized Privileges**

**❓ Q: How do we control that only administrators have access?** 

👉 **Customized Permission Class**

```python
from rest_framework.permissions import BasePermission

class IsAdminUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff  # Only administrators can access
```

```python
class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOnly]
```

- `BasePermission` is suitable for **complex permission control**.
- **Permission can be controlled dynamically (e.g., `has_object_permission()` restricts access to specific objects)**

## 5. **Optimized database queries**
**N+1 query problem**

**❓ Q: What is N+1 query? How to optimize?**

👉 The N+1 query problem refers to querying one object at a time and then additionally querying the associated objects, resulting in **large number of SQL queries**。

```python
# Model: An Author has more than one Book
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

```python
# Inefficient queries (N+1 issues)
books = Book.objects.all()
for book in books:
    print(book.author.name)  # Here a query is triggered every time book.author is accessed
```

**🔥 Solution:`select_related()`**

```python
# Efficient queries (JOIN queries, get all data at once)
books = Book.objects.select_related('author').all()
for book in books:
    print(book.author.name)  # Only one SQL query will be triggered
```

✅ **applies to ForeignKey and OneToOne relationships**

**prefetch_related()**

**❓ Q: How can we optimize if it's a ManyToMany relationship?** 

👉 `prefetch_related()` for **ManyToMany** relationship

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
```

```python
# Inefficient queries (N+1 issues)
books = Book.objects.all()
for book in books:
    for author in book.authors.all():  # Each visit to authors results in an additional query
        print(author.name)
```

**🔥 Solution: `prefetch_related()`**

```python
books = Book.objects.prefetch_related('authors').all()
for book in books:
    for author in book.authors.all():  # No additional queries will be made here
        print(author.name)
```

✅ **Applicable to ManyToMany and Reverse ForeignKey relationships**

**Using Indexes to Optimize Queries**

**❓Q: How can we speed up my query?**

👉 Add indexes to fields with high-frequency queries

```python
class Book(models.Model):
    title = models.CharField(max_length=100, db_index=True)  # 添加索引
```

✅ **Indexes are applied to search fields, filtered fields**

✅ Checking query performance using `EXPLAIN ANALYZE`