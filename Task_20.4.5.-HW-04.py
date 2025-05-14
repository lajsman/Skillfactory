import json

with open(r"C:\Users\lajsm\Desktop\orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

max_price = 0
max_price_order = ''

max_quantity = 0
max_quantity_order = ''

orders_per_day = {}
orders_per_user = {}
user_total_spent = {}

total_order_price = 0
order_count = 0

total_quantity = 0  # общее количество товаров
total_price = 0     # суммарная цена всех заказов

for order_num, data in orders.items():
    price = data.get("price", 0)
    quantity = data.get("quantity", 0)
    user_id = data.get("user_id", "unknown")
    date = data.get("date", "")

    # 1. Самый дорогой заказ
    if price > max_price:
        max_price = price
        max_price_order = order_num

    # 2. Заказ с наибольшим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order = order_num

    # 3. Заказы по дням (только июль)
    if date.startswith("2023-07"):
        if date not in orders_per_day:
            orders_per_day[date] = 0
        orders_per_day[date] += 1

    # 4. Кол-во заказов по пользователям
    if user_id not in orders_per_user:
        orders_per_user[user_id] = 0
    orders_per_user[user_id] += 1

    # 5. Суммарная стоимость по пользователям
    if user_id not in user_total_spent:
        user_total_spent[user_id] = 0
    user_total_spent[user_id] += price

    # 6. Средняя стоимость заказа
    total_order_price += price
    order_count += 1

    # 7. Средняя стоимость товаров (по цене за заказ и кол-ву товаров)
    total_quantity += quantity
    total_price += price

# 3. День с наибольшим количеством заказов
most_active_day = max(orders_per_day, key=orders_per_day.get)

# 4. Пользователь с наибольшим числом заказов
most_orders_user = max(orders_per_user, key=orders_per_user.get)

# 5. Пользователь с самой большой суммой заказов
top_spender = max(user_total_spent, key=user_total_spent.get)

# 6. Средняя стоимость заказа
avg_order_price = round(total_order_price / order_count, 2) if order_count else 0

# 7. Средняя стоимость товаров (общая стоимость / общее количество)
avg_item_price = round(total_price / total_quantity, 2) if total_quantity else 0

# Вывод
print(f"1. Номер самого дорогого заказа: {max_price_order}, стоимость: {max_price}")
print(f"2. Номер заказа с наибольшим количеством товаров: {max_quantity_order}, количество: {max_quantity}")
print(f"3. День с наибольшим количеством заказов: {most_active_day}, количество: {orders_per_day[most_active_day]}")
print(f"4. Пользователь с наибольшим числом заказов: {most_orders_user}, заказов: {orders_per_user[most_orders_user]}")
print(f"5. Пользователь с самой большой суммой заказов: {top_spender}, сумма: {user_total_spent[top_spender]}")
print(f"6. Средняя стоимость заказа: {avg_order_price}")
print(f"7. Средняя стоимость товаров: {avg_item_price}")