#Тестовое задание  
###Описание

[***stripe.com/docs***](https://www.stripe.com/docs/) -
платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей.
С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции.

Мы предлагаем вам познакомиться с этой прекрасной платежной системой, реализовав простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров.
Для решения нужно использовать Django.
###Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price)
- API с двумя методами:
- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)


- Бонусные задачи: 
  - Запуск используя Docker
  - Использование environment variables

  - Просмотр Django Моделей в Django Admin панели


## Как запустить демонстрационную версию сайта

1. Установите [Docker](https://www.docker.com/).
2. Создайте учетную запись в [Stripe](https://dashboard.stripe.com/register).  
3. Скачайте код и перейдите в каталог проекта:
```sh
git clone https://github.com/MeshkovD/payment_system_api_test_task.git
cd stripe_pay
```
4. Проект настроен на работу с переменными окружения. Для их использования, в каталоге содержащем settings.py создайте файл .env

Примерное содержимое файла .env:
```sh
SECRET_KEY=ikzst-5&i6x(9gg(example)0bfghtf4ggDFG455thyhwfjqgdg45
ALLOWED_HOSTS=127.0.0.1,localhost
DEBUG=True
STRIPE_API_KEY=sk_test_51Lhn3QJTt1K7QeHmW3RbjREHoLBdYoLdcxmdu...
```

**Нестандартные переменные окруженя**:  
STRIPE_API_KEY - секретный ключ API Stripe. Необходимо получить, на сайте [Secret key](https://dashboard.stripe.com/test/apikeys).  

5. Соберите образ:  
```sh
docker build -t strip_example .
```
6. Создайте и запустите контейнер:  
```sh
docker run --rm -it --env-file stripe_pay\.env -p 8000:8000 strip_example
```
*Где "stripe_pay\.env" - это путь к ранее созданному файлу .env*

*Автоматически будет создана база данных, проведены миграции.  
В демонстрационных целях, будет создан суперпользователь(login: ***admin***, password: ***admin***), а так же 1 Item.*
7. Сайт доступен в браузере по адресу http://localhost:8000/  
