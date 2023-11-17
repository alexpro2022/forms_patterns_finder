# Forms patterns finder

[Тестовое задание](https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit#heading=h.pieurecv5l1j)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск тестов](#установка-и-запуск-тестов)
- [Запуск приложения](#запуск-приложения)
- [Удаление приложения](#удаление-приложения)
- [Автор](#автор)

<br>

## Технологии:

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![aiohttp](https://img.shields.io/badge/-aiohttp-464646?logo=aiohttp)](https://docs.aiohttp.org/en/stable/index.html)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/)
[![MongoDB](https://img.shields.io/badge/-MongoDB-464646?logo=MongoDB)](https://www.mongodb.com/)
[![Motor](https://img.shields.io/badge/-Motor-464646?logo=Python)](https://motor.readthedocs.io/en/3.3.1/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-asyncio](https://img.shields.io/badge/-Pytest--asyncio-464646?logo=Pytest-asyncio)](https://pypi.org/project/pytest-asyncio/)
[![Pytest-aiohttp](https://img.shields.io/badge/-Pytest--aiohttp-464646?logo=Pytest-aiohttp)](https://pypi.org/project/pytest-aiohttp/)
[![coverage](https://img.shields.io/badge/-coverage-464646?logo=coverage)](https://coverage.readthedocs.io/en/latest/index.html)
[![deepdiff](https://img.shields.io/badge/-deepdiff-464646?logo=deepdiff)](https://zepworks.com/deepdiff/6.3.1/diff.html)


[⬆️Оглавление](#оглавление)

<br>

## Описание работы:
Приложение принимает список полей формы со значениями в теле POST запроса. Возвращает имя шаблона, наиболее подходящего данному списку полей формы, а при отсутствии совпадений с известными шаблонами производит типизацию полей принятой формы на лету и возвращает список полей с их типами. При нахождении более одного подходящего шаблона, алгоритм вычисляет **наиболее** подходящий (фактически выбирает шаблон с максимальным кол-вом полей из всех найденных шаблонов). Чтобы найти подходящий шаблон нужно выбрать тот, поля которого совпали с полями в присланной форме. Совпадающими считаются поля, у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим. Самое главное, чтобы все поля шаблона присутствовали в форме.

[⬆️Оглавление](#оглавление)

<br>

## Установка и запуск тестов: 
#### Docker Compose
<details><summary>Предварительные условия:</summary>

Предполагается, что пользователь:
 - установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине. Проверить наличие можно выполнив команды:
 
    ```bash
    docker --version && docker-compose --version
    ```
<h1></h1>
</details>
<br>

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (тестовые данные уже введены):

```bash
git clone https://github.com/alexpro2022/forms_patterns_finder.git
cd forms_patterns_finder
cp env_example .env
nano .env
```

2. Из корневой директории проекта выполните команды запуска тестов:
```bash
docker compose -f docker/test.docker-compose.yml up --build --abort-on-container-exit
docker logs tests && docker rm mongo && docker rm tests
```
После прохождения тестов в консоль будет выведен отчет pytest и coverage.

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:
1. Из корневой директории проекта выполните команду:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```
Проект будет развернут в docker-контейнерах:
  - приложение можно протестировать Postman по адресу: http://localhost:8080
  - Доступ к БД осуществляется по адресу: http://localhost:8081, учетные данные "admin:pass", коллекция шаблонов `patterns_collection`

2. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f docker/docker-compose.yml down
```
3. Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f docker/docker-compose.yml down -v
```

[⬆️Оглавление](#оглавление)

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr forms_patterns_finder
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#forms-patterns-finder)

