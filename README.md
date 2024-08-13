# table-in-SPA-format

Таблица в формате Single Page Application, которая отображает данные из базы данных
и обеспечивает пользователю функциональность для сортировки, фильтрации и пагинации данных.
Таблица работает без перезагрузки страницы.

### Технологии и инструменты:
#### Backend:
- Python 3.11
- Django REST Framework
- PostgreSQL
- Django ORM
#### Frontend:
- Vue.js
- Axios
- CSS
#### Проксирование:
- Nginx

### Инструкция по развертыванию:

- установить [Docker](https://docs.docker.com/engine/install/)
- для сборки и запуска приложения:

```text
docker-compose up -d --build
cd path\to\project\client\
npm i
npm run dev
```

- перейти по [ссылке](http://localhost:5173/) с фронтовой частью приложения: http://localhost:5173/
