# conus.py принцип работы
## 1: area(r,h)
### Параметры функции
- h - высота конуса.
- r - радиус конуса.
### Возвращает:
- площадь поверхности конуса 
### Пример:
- input-> 5 4
- area(5, 4)
- return pi * 5 * (4 + ((4**2) + (5**2))**0.5)
- output -> 179.1197053653833
## 2: sum(r,h)
### Параметры функции
- h - высота конуса.
- r - радиус конуса.
### Возвращает:
- сумму радиуса и высоты 
### Пример:
- input-> 5 4
- area(5, 4)
- return 5 + 4
- output -> 9

# Отчет по тестированию 

## Цели и задачи тестирования

- Проверить корректность работы функций conus.py

## Описание функционала
- В директории находится файл с несколькими функциями, необходимо проверить правильность его вычислений

## Область тестирования

- Функции area и sum из conus.py

## Стратегия тестирования
- Проверка значений функций на тривиальных тестах и иррациональных для проверки погрешности.


## Критерии приемки
- Правильная работа алгоритма

## Ожидаемые результаты

- Работа без погрешностей на натуральных числах