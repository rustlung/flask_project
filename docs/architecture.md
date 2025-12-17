## Структура проекта

app/
├── __init__.py               # factory: собирает Flask, configs, extensions (DB, Migrate)
├── config.py                 # окружения (development, production, testing)
├── extensions.py             # init SQLAlchemy, Migrate и др.
├── models/
│   ├── experience.py          # модель опыта
│   ├── timeline.py            # модель истории
│   └── __init__.py
├── routes/
│   ├── public.py              # публичные API/витрина
│   ├── admin.py               # админские CRUD
│   └── __init__.py            # регистрирует blueprint’ы
├── services/
│   ├── experience_service.py  # бизнес-логика (поиск, фильтрация, агрегаты)
│   ├── timeline_service.py    # логика timeline
│   └── auth.py                # простой ключ/токен
├── schemas/
│   ├── experience_schema.py   # сериализация/валидация input/output
│   ├── timeline_schema.py
│   └── __init__.py
├── utils/
│   └── helpers.py             # общие функции (например, конвертация дат)
run.py                         # точка входа / точка запуска приложения
requirements.txt
README.md                       # описание, скрипт запуска
.env.example                   # примеры переменных (SECRET_KEY, ADMIN_TOKEN и т.п.)
docs/
├── architecture.md             # текущая структура + решения
└── maybe_more.md
tests/
└── test_public_endpoints.py