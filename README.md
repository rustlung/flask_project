# Flask Resume Showcase

Минималистичный Flask-проект, который демонстрирует backend-навыки junior-разработчика: модели опыта и таймлайна, публичные и админские API, валидация через Marshmallow и авторизация по токену.

## Структура и компоненты
- `app/` — фабрика приложения, модели, схемы, маршруты, расширения.
- `docs/` — архитектурные заметки и контракты данных.
- `tests/` — автоматические тесты, которые проверяют публичные и админские эндпоинты.
- `requirements.txt` — зависимости проекта.

## Быстрый старт

1. Создай виртуальное окружение и установи зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows PowerShell
   pip install -r requirements.txt
   ```
2. Скопируй `.env.example` в `.env` и укажи значения:
   ```
   FLASK_ENV=development
   SECRET_KEY=любое_слово
   ADMIN_TOKEN=секрет
   DATABASE_URL=sqlite:///dev.db
   ```
3. Инициализируй и примени миграции:
   ```bash
   flask db init
   flask db migrate -m "init"
   flask db upgrade
   ```
4. Запусти сервер:
   ```bash
   flask run
   ```

## API

### Публичные эндпоинты
- `GET /api/v1/experience` — список публичных записей (опционально фильтруется по `category` и `tag`).
- `GET /api/v1/timeline` — хронология событий (`limit`, `offset`, `order=asc|desc`).

Пример запроса (PowerShell):
```powershell
Invoke-WebRequest `
  -Uri http://127.0.0.1:5000/api/v1/experience `
  -Method GET
```

### Админские эндпоинты
Все запросы требуют заголовка `X-Admin-Token` с токеном из `.env`.

- `POST /api/v1/admin/experience` — добавляет запись.
- `PUT /api/v1/admin/experience/<id>` — частично обновляет (можно передавать `public`, `highlights` и др.).
- `DELETE /api/v1/admin/experience/<id>` — удаляет запись.
- Аналогично: `/api/v1/admin/timeline`.

Пример создания (`curl`):
```bash
curl -X POST http://127.0.0.1:5000/api/v1/admin/experience \
  -H "Content-Type: application/json" \
  -H "X-Admin-Token: secret" \
  -d '{"title":"Project","category":"project","description":"Desc","start_date":"2024-01-01","link":"https://example.com"}'
```

### Ошибки
- `400` — ошибка валидации (`details` показывает поля).
- `401` — неверный токен.
- `404` — запись не найдена.

## Тесты

1. Установи зависимости (включены в `requirements.txt`).  
2. Перед запуском экспортируй переменные окружения или добавь их к команде:
   ```bash
   set FLASK_ENV=testing
   set ADMIN_TOKEN=test-token
   pytest
   ```
   (_Windows PowerShell_: ` $env:FLASK_ENV="testing" ; $env:ADMIN_TOKEN="test-token" ; pytest`).
3. Тесты используют in-memory SQLite и проверяют публичные маршруты, админские CRUD и авторизацию через `X-Admin-Token`.

## Следующие шаги

- Написать документацию Swagger/OpenAPI.
- Добавить логирование действий админа.
- Развернуть проект на любому облаке и прикрепить ссылку к резюме.

