from tinydb import TinyDB, Query

db = TinyDB('template.json')
Template = Query()


def init_db():
    db.truncate()  # Очистка базы перед добавлением данных
    db.insert_multiple([
        {
            "name": "ContactForm",
            "email": "email",
            "phone": "phone"
        },
        {
            "name": "OrderForm",
            "order_date": "date",
            "customer_name": "text"
        }
    ])


# Инициализация базы данных
init_db()
print(f"Инициализация базы данных завершена! Файл базы данных: {'template.json'}")
