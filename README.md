# Y_Lab

## Задание 1

Написать проект на FastAPI с использованием PostgreSQL в качестве БД. В проекте следует реализовать
REST API по работе с меню ресторана, все CRUD операции. Для проверки задания, к презентаций будет
приложена Postman коллекция с тестами. Задание выполнено, если все тесты проходят успешно.

Даны 3 сущности: Меню, Подменю, Блюдо.

Зависимости:
- У меню есть подменю, которые к ней привязаны.
- У подменю есть блюда.

Условия:
- Блюдо не может быть привязано напрямую к меню, минуя подменю.
- Блюдо не может находиться в 2-х подменю одновременно.
- Подменю не может находиться в 2-х меню одновременно.
- Если удалить меню, должны удалиться все подменю и блюда этого меню.
- Если удалить подменю, должны удалиться все блюда этого подменю.
- Цены блюд выводить с округлением до 2 знаков после запятой.
- Во время выдачи списка меню, для каждого меню добавлять кол-во подменю и блюд в этом меню.
- Во время выдачи списка подменю, для каждого подменю добавлять кол-во блюд в этом подменю.
- Во время запуска тестового сценария БД должна быть пуста.

## Задание 2

- Обернуть программные компоненты в контейнеры. 
- Контейнеры должны запускаться по одной команде “docker-compose up -d”.
- Образы для Docker:
-- python:3.10-slim
-- postgres:15.1-alpine
- Написать CRUD тесты для ранее разработанного API с помощью библиотеки pytest.
- Подготовить отдельный контейнер для запуска тестов.

### Запуск приложения с базой данных

`sudo docker-compose up --build -d`

### Запуск базы данных и приложения для тестов

`sudo docker-compose -f docker-compose_test up --build -d`

### Запуск тестов

`sudo docker-compose -f docker-compose_test run test`
