## Контракты данных

### Experience
| Поле        | Тип                              | Обязательно              | Описание                                | Пример                          |
| ----------- | -------------------------------- | ------------------------ | ---------------------------------------- | ------------------------------- |
| id          | int                              | да                       | Уникальный идентификатор                 | 1                               |
| title       | str                              | да                       | Название записи (проект, роль и т.п.)    | «Личный сайт-витрина»           |
| category    | enum [project, role, certificate] | да                       | Тип опыта, нужен для фильтрации          | project                         |
| description | str                              | да                       | Краткое описание, зачем служит запись    | «Сайт-портфолио на Flask…»      |
| start_date  | date                             | да                       | Дата начала (ISO)                        | 2023-05-01                      |
| end_date    | date                             | нет                      | Дата завершения или null                 | 2023-08-01                      |
| highlights  | list[str]                        | нет                      | Ключевые достижения                      | [«API», «Docker»]               |
| tags       | list[str]                        | нет                      | Теги / технологии                        | [«Flask», «REST»]               |
| public      | bool                             | да (по умолчанию true)   | Видимость на витрине                     | true                            |
| link        | str                              | нет                      | Ссылка (GitHub, кейс, демо)              | https://github.com/...          |
| created_at  | datetime                         | да                       | Время создания                           | 2025-12-17T12:00:00Z            |
| updated_at  | datetime                         | да                       | Время последнего обновления              | 2025-12-18T09:30:00Z            |

### Timeline
| Поле        | Тип     | Обязательно | Описание                                   | Пример                       |
| ----------- | ------- | ----------- | ------------------------------------------ | ---------------------------- |
| id          | int     | да          | Уникальный идентификатор события           | 1                            |
| date        | date    | да          | Дата события или этап                       | 2023-01-01                   |
| title       | str     | да          | Название события                            | «Начал изучать Flask»         |
| description | str     | да          | Что произошло / чему научился              | «Сделал первый API»          |
| category    | str     | нет         | Классификация (для UI/фильтров)            | learning                     |
| order       | int     | нет         | Порядок вывода (если нужен)                 | 10                           |
| highlight   | bool    | нет         | Подсветить событие как ключевое             | true                         |

### Шаблон ответа Timeline
```
{
  "events": [
    {
      "id": 1,
      "date": "2023-01-01",
      "title": "Начал изучать Flask",
      "description": "Собрал первый API и понял, как работает маршрут.",
      "category": "learning",
      "highlight": true
    },
    {
      "id": 2,
      "date": "2023-03-15",
      "title": "Проектная работа",
      "description": "Собрал мини-сервис уведомлений с SQLite и cron.",
      "category": "project",
      "highlight": false
    }
  ]
}
```

### Админские ответы
```
# POST /api/v1/admin/experience
{
  "id": 5,
  "title": "Автоматизация отчетности",
  ...
}

# PUT /api/v1/admin/experience/5
{
  "id": 5,
  "updated_at": "2025-12-18T13:15:00Z",
  "changes": {
    "public": false
  }
}

# DELETE /api/v1/admin/experience/5
204 No Content

# POST /api/v1/admin/timeline
{
  "id": 3,
  "date": "2025-12-01",
  "title": "Менторство",
  "description": "Провёл 3 ревью равноценных pet-проектов.",
  "category": "learning",
  "highlight": true
}
```

### Ошибки и коды ответа
| Код | Где | Описание | Пример тела |
| --- | --- | --- | --- |
| `400 Bad Request` | Любой POST/PUT | Неправильный JSON, пропущены обязательные поля или формат даты | `{ "error": "validation failed", "details": { "title": "обязательно" } }` |
| `401 Unauthorized` | Админские маршруты | Токен не передан или не совпадает с `ADMIN_TOKEN` | `{ "error": "Unauthorized", "message": "Invalid admin token" }` |
| `404 Not Found` | GET/PUT/DELETE по id | Запись не найдена или не публична (в случае публичных маршрутов). | `{ "error": "Experience not found" }` |
| `409 Conflict` | POST experience | Дублирование уникальных данных (например, `title` + `start_date`) | `{ "error": "Experience already exists" }` |
| `500 Internal Server Error` | любые | Что-то пошло не так на сервере; логирование подскажет, где. | `{ "error": "Internal Server Error" }` |

### Шаблон для JSON-ответа
```
{
  "id": 1,
  "title": "Личный сайт-витрина",
  "category": "project",
  "description": "Сайт-портфолио на Flask с API и админкой",
  "start_date": "2024-09-01",
  "end_date": null,
  "highlights": [
    "REST API",
    "SQLite + SQLAlchemy",
    "Документация"
  ],
  "tags": [
    "Flask",
    "Backend",
    "Junior"
  ],
  "public": true,
  "link": "https://github.com/...",
  "created_at": "2025-12-17T12:00:00Z",
  "updated_at": "2025-12-18T09:30:00Z"
}
```

