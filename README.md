# Тестовое задание

### Возможности
Получение информации о погоде по названию населеного пункта. Для получения координат используется Геокодер Яндекса. Интерфейс собран на фреймворке Gradio.

### Установка

```sh
git clone https://github.com/buvanenko/test-weather.git
cd test-weather
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Запуск
Перед запуском необходимо получить API ключ для геокодера здесь: https://developer.tech.yandex.ru/services

Затем создайте файл .env со следующим содержимым:
```
GEOCODER_API_KEY=ВАШ КЛЮЧ АПИ
```

Запускайте из окружения:
```
. venv/bin/activate
python main.py
```