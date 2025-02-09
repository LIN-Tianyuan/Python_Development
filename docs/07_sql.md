# SQL
## 1. Multi-table query
```sql
SELECT users.id, users.name, orders.id AS order_id, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

- `INNER JOIN`: **Both tables will return** only if they have matching data.
- `LEFT JOIN`: **Even if there are no matches in the `orders` table, `users` will still be displayed**.
- `RIGHT JOIN`: **The opposite of `LEFT JOIN`, returns all data from the `orders` table**.
## 2. Group By
```sql
SELECT user_id, SUM(amount) AS total_spent
FROM orders
GROUP BY user_id
HAVING SUM(amount) > 100;
```
- `GROUP BY` Used to group by `user_id`.
- `SUM(amount)` Calculates the total amount of the order for each user.
- `HAVING` filters **aggregated data** (`WHERE` cannot be used with `SUM()`).
## 3. Window Functions
**Window Functions** are advanced functions in SQL that **are used to perform calculations** within a subset of the query results (the window), but instead of merging rows like `GROUP BY`, they **keep the data for each row** and add the results of the calculations to it.

```sql
FunctionName() OVER (
    PARTITION BY column name -- optional, group by a column
    ORDER BY column name -- specify the order of the window
)
```
 - OVER(): the core of the window function, indicates the range of the calculation.

 - PARTITION BY: optional, specifies how the window is grouped (similar to GROUP BY).

 - ORDER BY: specifies the sorting method for calculations within the window.
```sql
SELECT user_id, order_id, amount,
       RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS rank,
       DENSE_RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS dense_rank,
       ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY amount DESC) AS row_number
FROM orders;
```

| Functions | Allow Skipping of Rankings | Whether to rank consecutively |
| -------------- | ------------ | ---------------- |
| `RANK()` | ✅ Allow skipping | ❌ May have ranking intervals |
| `DENSE_RANK()` | ❌ No skipping | ✅ Continuous ranking |
| `ROW_NUMBER()` | ✅ Unique numbering | ✅ No relation to same amount |

## 4. Indexing optimization (Indexes & EXPLAIN analysis)
```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
```
```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 1;
```
**Query analysis**

- **`Seq Scan`** (Full Table Scan): ❌ Slow
- **`Index Scan`**: ✅ Fast
- **`Index Only Scan`** (Index Coverage Query): 🔥 Faster
## 5. Transaction & ACID
```sql
BEGIN;  -- Begin transaction
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
COMMIT;  -- Commit transaction
```
 - If the second UPDATE fails, the transaction does not commit.
```sql
BEGIN;
UPDATE orders SET status = 'shipped' WHERE order_id = 123;
ROLLBACK;  -- Cancel the operation, the data will not be changed.

```
 - ROLLBACK can undo all changes if the transaction is not completed.