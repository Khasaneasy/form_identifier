from tinydb import TinyDB, Query

db = TinyDB('template.json')
Template = Query()

# Пример для тестирования
if not db.all():
    db.insert({
        "name": "Contact Form",
        "fields": {
            "user_email": "email",
            "user_phone": "phone"
        }
    })
    db.insert({
        "name": "Order Form",
        "fields": {
            "order_date": "date",
            "user_email": "email"
        }
    })
