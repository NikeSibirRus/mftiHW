# mftiHW | ДЗ - Портал новостей для браузера Google Chrome
## Данный проект построен на базе материалов учебного курса по Django Python.

Домашнее задание выполнено в приложении "home01"
Шаблон newsportal https://www.free-css.com/free-css-templates/page53/newsportal адаптация: Разбит на страницы
Шаблон для меню навигации, который будет интегрироваться в другие шаблоны - left-side.html (https://www.free-css.com/free-css-templates/page277/upright)
### Портал новостей
### Старт с http://127.0.0.1:8000/news/show/

Учетки 
Admin / 20BJCdPj   админ и автор
Writer_001 / 20BJCdPj читатель
Writer_002 / T68LmrAr   автор

ДЗ 3 https://demouserrtc.pythonanywhere.com/news/show/
- [x] Разграничены права доступа
  - [x] Не - авторизированный пользователь:
    - [x] Просмотр всех новостей и выбранной, контакты, о нас, войти в акаунт регистрация
  - [x] Авторизированный с ролью автор:
    - [x] Просмотр всех новостей и выбранной, контакты, о нас, Избранное, Мои статьи, добавление удаление из избраного, Удаление редактирование статьи. Добавление новости, Редактирование профиля, ссылка на Админ панель, выход.  
  - [x] Авторизированный с ролью читатель:
    - [x] Просмотр всех новостей и выбранной, контакты, о нас, Избранное,добавление удаление из избраного,Редактирование профиля, ссылка на Админ панель, выход.
- [x] Изучение  Django.
  - [x] ДЗ - N2
    - [x] Зарегистрируйте модель новости в панели администратора
    - [x] Настройте фильтры по различным полям: заголовок, дата создания, имя автора
    - [x] Реализуйте функционал регистрации и авторизации пользователей на отдельных страницах
    - [x] Обеспечьте валидацию полей ввода данных регистрации и авторизации.
    - [x] Обеспечьте привязку Автора новости к самой Новости (модели User из БД к записи новости - Article) при создании новости.
    - [x] Создайте форму для поиска новости по заголовку, и отдельную страницу результатов поиска. Используйте механизмы аннотации и/или агрегации для получения сведений об Авторе новости в том же запросе к БД,что и запрос поиска новости по заголовку.
  - [x] ДЗ - №3
    - [x] Все работает
    - [x] Пагинация добавлена в избранное/мои новости
    - [x] Публикация на хостинге https://demouserrtc.pythonanywhere.com/news/show/
    - [ ] Доп. мультиязычность gettext на перспективу

