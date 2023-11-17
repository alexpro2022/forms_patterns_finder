# Forms' patterns finder

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

[![Python](https://img.shields.io/badge/Python-v3.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![aiohttp](https://img.shields.io/badge/-aiohttp-464646?logo=aiohttp)](https://docs.aiohttp.org/en/stable/index.html)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/)
[![MongoDB](https://img.shields.io/badge/-MongoDB-464646?logo=MongoDB)](https://www.mongodb.com/)
[![Motor](https://img.shields.io/badge/-Motor-464646?logo=Python)](https://motor.readthedocs.io/en/3.3.1/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-asyncio](https://img.shields.io/badge/-Pytest--asyncio-464646?logo=Pytest-asyncio)](https://pypi.org/project/pytest-asyncio/)
[![Pytest-aiohttp](https://img.shields.io/badge/-Pytest--aiohttp-464646?logo=Pytest-aiohttp)](https://pypi.org/project/pytest-aiohttp/)
[![deepdiff](https://img.shields.io/badge/-deepdiff-464646?logo=deepdiff)](https://zepworks.com/deepdiff/6.3.1/diff.html)


[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

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
git clone https://github.com/alexpro2022/.git
cd 
cp env_example .env
nano .env
```

2. Из корневой директории проекта выполните команды запуска тестов:
```bash
docker compose -f docker/test.docker-compose.yml up --build --abort-on-container-exit
clear
docker logs tests
docker rm mongo
docker rm tests
```
После прохождения тестов в консоль будет выведен отчет pytest.

<br>

## Запуск приложения:
1. Из корневой директории проекта выполните команду:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```
Проект будет развернут в docker-контейнерах:
  - приложение можно протестировать Postman по адресу: http://localhost:8080
  - Доступ к БД осуществляется по адресу: http://localhost:8081, учетные данные "admin:pass"

2. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f docker/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f docker/docker-compose.yml down -v
```

[⬆️Оглавление](#оглавление)

<br>

## Удаление:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr 
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#salaries_counter)
