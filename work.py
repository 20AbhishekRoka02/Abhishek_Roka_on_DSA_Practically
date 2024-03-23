import sqlparse
# from sqlparse.sql import Statement, Token, TokenList, Where
import sqlvalidator 

sql = 'select * where id in (select id from bar) from foo;'
# sql = """select * 
# from foo 
# where id in (select id from bar);
# select * 
# from foo 
# where id in (select id from bar);"""

# sql = """
# SELECT
#     c.customer_id,
#     c.first_name,
#     c.last_name,
#     COUNT(o.order_id) AS num_orders,
#     SUM(oi.quantity * oi.unit_price) AS total_spent
# FROM
#     customers c
# JOIN
#     orders o ON c.customer_id = o.customer_id
# JOIN
#     order_items oi ON o.order_id = oi.order_id
# JOIN
#     products p ON oi.product_id = p.product_id
# WHERE
#     c.country = 'USA'
#     AND o.order_date >= '2023-01-01'
#     AND o.order_date < '2024-01-01'
# GROUP BY
#     c.customer_id,
#     c.first_name,
#     c.last_name
# HAVING
#     COUNT(o.order_id) >= 3
# ORDER BY
#     total_spent DESC
# LIMIT
#     10;

# """

formatted_sql = sqlvalidator.parse(sql)
print(formatted_sql.sql_query)
print(formatted_sql.is_valid())



# sql = 'select * from foo where id in (select id from bar);select * from foo where id in (select id from bar);'
# sql = 'create database hello;'
# print(sqlparse.format(sql,reindent=True, keyword_case='upper'))
# a = sqlparse.parse(sql)

# state = a[0]
# print(a)
# print(state.token_index())

# print(where.)
# m = Statement(a[0])
# print(m.get_type())


# from tabulate import tabulate

# # Example table data
# data = [
#     ["ID", "Name", "Age"],
#     [1, "Alice Works in San Fransisco", 25],
#     [2, "Bob", 30],
#     [3, "Charlie", 35]
# ]

# # Display table
# print(tabulate(data, headers="firstrow", tablefmt="grid"))
