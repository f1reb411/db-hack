# Взлом электронного дневника школьника
***
Программа позволяет исправить оценки, удалить замечания и создать 
хвалебные отзывы в электронном дневнике.

## Запуск
***

* Электронный дневник скачать [здесь](https://github.com/devmanorg/e-diary/tree/master)
* [Архив с базой данных](https://dropmefiles.com/DLeXF)
* Выгрузить файл с базой в папку проекта
* Импортировать `scripts.py`

## Использование

Выбрать ученика:

`schoolkid = scripts.find_schoolkid('Фамилия Имя')`

Исправить плохие оценки:

`scripts.fix_marks(schoolkid)`

Удалить замечания:

`scripts.remove_chastisements(schoolkid)`

Похвалить:

`scripts.add_random_commendation(schoolkid, 'Предмет')`

## Цели проекта
***

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](dvmn.org)