# Flask Showcase Cheat Sheet

Эта шпаргалка — последовательность шагов, которые мы прошли в проекте. Она помогает быстро вспомнить, как строить аккуратный Flask-проект с моделями, схемами, маршрутами, админкой и тестами.

## 1. Окружение и конфигурация
- Создай `venv` и установи зависимости из `requirements.txt`.  
- Добавь `.env.example` с переменными (`FLASK_ENV`, `SECRET_KEY`, `ADMIN_TOKEN`, `DATABASE_URL`).  
- `app/config.py` содержит `BaseConfig`, `DevelopmentConfig`, `ProductionConfig`, `TestingConfig`. Используй `get_config(env)` для фабрики.
- Разгрузи чувствительные значения через `load_dotenv()` и `os.environ`.
- `.gitignore`: `venv/`, `.env`, `__pycache__/`, `*.pyc`.

## 2. Структура приложения
```
app/
├── __init__.py        # factory + регистрация блюпринтов
├── config.py          # конфигурации
├── extensions.py      # db, migrate и т.п.
├── models/            # SQLAlchemy
├── schemas/           # Marshmallow
├── routes/            # public и admin blueprints
├── services/          # бизнес-логика (по желанию)
└── utils/             # вспомогательные функции
```
- `run.py` или `flask run` запускает factory.
- `docs/` хранит архитектуру, контракты, шпаргалки.
- `tests/` содержат `conftest.py`, фикстуры, и тесты (pytest).

## 3. Модели
- SQLAlchemy, соединённый через `app/extensions.py` (`db = SQLAlchemy()`, `migrate = Migrate()`).
- Миксины для общих колонок (`created_at`, `updated_at`).
- Порядок:
  1. `class TimestampMixin`: `created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)` и `updated_at`.
  2. Наследуй модели от `TimestampMixin` и `db.Model`.
  3. Колонки: `String`, `Enum`, `JSON`, `Boolean`, `Date`.
  4. Сохраняй списки (`tags`, `highlights`) через `db.JSON`.

## 4. Схемы (Marshmallow)
- Для `POST/PUT`/`GET` описывают поля (`fields.Str`, `fields.Date`, `fields.List`, `fields.Bool`), валидацию `validate.OneOf`, `validate.Length`.
- Используй `load_default` вместо `missing`.
- `@post_load` только для полной загрузки (при `partial=True` возвращай dict).
- `dump_only` для `id`, `created_at`, `updated_at`.

## 5. Маршруты
- **Blueprints** (`public`, `admin`) в `app/routes/`. Регистрируй оба через `register_blueprints` в `app/__init__.py`.
- **Публичные**: GET `/api/v1/experience`, `/api/v1/timeline`, фильтры, пагинация и сортировка. Возвращай JSON через схемы.
- **Админские**: POST/PUT/DELETE endpoints. Проверяй `X-Admin-Token` против `current_app.config["ADMIN_TOKEN"]`. Используй `ValidationError` для 400.
- Вынеси логигу в `services/` при росте проекта.

## 6. Документация и контракты
- `docs/contracts.md`: таблицы полей + шаблоны JSON + ошибки.
- `docs/architecture.md`: структура проекта.
- Дополни `README.md` по шагам: установка, миграции, API, тесты, CI.

## 7. Тесты
- `tests/conftest.py`: добавь фикстуры `app`, `client`, `admin_headers`. Вставь `sys.path` при необходимости.
- Используй `app.app_context()` чтобы создавать записи перед запросами.
- Тесты должны проверять публичные GET и админские CRUD.
- Запуск: `python -m pytest`.

## 8. CI и деплой
- `.github/workflows/ci.yml`: установи Python, install deps, `python -m pytest`, передай `FLASK_ENV=testing`, `ADMIN_TOKEN`, `DATABASE_URL`.
- В будущем можно добавить шаги миграции/деплоя.

## 9. Фронтенд (опционально)
- Шаблоны Jinja + статические файлы (`app/templates`, `app/static/css`).
- Блюпринт может возвращать `render_template("index.html", experiences=..., timeline=...)`.
- Подключай Bootstrap/Vanilla JS для интерактивности.

## 10. Полезные команды
- `flask shell` (с `@app.shell_context_processor` для `db`, `models`).
- `flask db init/migrate/upgrade`.
- `pytest`.
- `python -m pytest` или `.\venv\Scripts\python.exe -m pytest` на Windows.

## 11. Полезные ресурсы
- [Flask official docs](https://flask.palletsprojects.com/) — основная документация.
- [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial.html).
- [Marshmallow quickstart](https://marshmallow.readthedocs.io/en/stable/quickstart.html).
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/).
- [GitHub Actions docs](https://docs.github.com/actions).
- [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html).

Хочешь, дополнить раздел шаблонами или ссылками на документацию?  

