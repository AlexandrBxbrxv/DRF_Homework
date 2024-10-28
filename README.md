# **Домашняя работа курса DRF**


Создайте базу данных в PostgreSQL

Заполните ".env.sample" своими данными и переименуйте его в ".env"

Фикстуры: python manage.py loaddata fixtures\приложение_data.json

Кастомные команды: python manage.py create_payment

Для запуска сайта: python manage.py runserver

DevBlog

`v.3`
1. Добавлена библиотека djangorestframework-simplejwt, внесена в INSTALLED_APPS
2. Добавлен CRUD для User, все контроллеры защищены авторизацией кроме создания пользователя и токенов

`v.2`
1. Добавлена библиотека django-filter и внесена в INSTALLED_APPS
2. Модель Payments переименована в Payment
3. Добавлен контроллер для просмотра списка Payment с фильтрацией
4. Добавлен контроллер для просмотра списка User с выводом истории платежей

`v.1.1`
1. Переопределён сериализатор для retrieve в CourseViewSet для вывода кол-ва уроков курса
2. Добавлена модель Payments и команда создания объекта этой модели
3. для CourseDetailSerializer добавлено поле lessons выводящее уроки курса

`v.1`
1. Добавлены модели Course и Lesson
2. Контроллер для Course через ViewSet
3. CRUD для Lesson
4. Контроллер для изменения User

`v.0`
1. Установлены базовые библиотеки для работы сайта
2. Все чувствительные данные засекречены
3. Добавлена модель User
