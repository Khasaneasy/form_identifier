# Form Identifier

Проект для идентификации форм с использованием FastAPI и TinyDB. Этот сервис позволяет сохранять шаблоны форм и искать их на основе переданных данных через API.

## Описание

Этот проект предоставляет API для создания шаблонов форм и поиска шаблонов на основе переданных данных. Шаблоны хранятся в базе данных **TinyDB**. Приложение использует **FastAPI** для создания API, которое принимает данные и находит соответствующие шаблоны в базе данных.

## Функциональность

- **Создание шаблонов**: Шаблоны форм могут быть созданы и сохранены в базе данных.
- **Поиск шаблонов**: При отправке данных через API, сервис ищет шаблон, соответствующий этим данным.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/form_identifier.git
```
2. Перейдите в директорию проекта:

```bash
cd form_identifier
```
3. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск проекта

```bash
uvicorn main:app --reload
```


### API
1. Создание шаблона
POST /create_template

Пример запроса:

```json
{
  "name": "Шаблон 1",
  "fields": {
    "field1": "email",
    "field2": "phone"
  }
}
```
Ответ:

```json
{
  "message": "Шаблон успешно создан"
}
```

2. Получение формы
POST /get_form

Пример запроса:

```json
{
  "name": "Шаблон 1",
  "fields": {
    "field1": "email",
    "field2": "phone"
  }
}
```

Ответ:

```json
{
  "template_name": "Шаблон 1"
}
```