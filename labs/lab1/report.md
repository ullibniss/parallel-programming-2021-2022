# НИЯУ МИФИ ИИКС Кафедра 42
## Федоров Алексей Евгеньевич Б19-505
### Лабароторная работа №1
### Введение в параллельные вычисления. Технология OpenMP

#### Цель работы  
    Приобрести базовые навыки теоретического и экспериментального анализа         
    высокопроизводительных параллельных алгоритмов, построения параллельных программ. 
    
#### Окружение
  - Операционная система: macOS Catalina version 10.15.7
  - Процессор: 3,1 GHz 2‑ядерный процессор Intel Core i5
  - Оперативная память: 8 ГБ 2133 MHz LPDDR3
  - Среда разработки: vim
  - Компиляция производится с помощью clang
  - Команда: ```clang -Xpreprocessor -fopenmp -lomp -o bin``` и дальнейший запуск 			бинарника ```./bin```
  - Версия OpenMP: 5.1

#### Анализ работы [алгоритма](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c)
  
  Алгоритм [генерирует](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c#L21) массив из [10000000](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c#L6) случайных чисел. Затем передает их в исполнительную часть алгоритма, где идет разделение на потоки. Массив [делится между потоками](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c#L24) на 16 частей([16 потоков](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c#L7)). На каждом потоке выполняется поиск максимального чилсла [методом перебора](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c#L27). По окончании работы каждым потоком, все результаты [агрегируются](https://github.com/ullibniss/parallel-programming-2021/blob/master/labs/lab1/test.c#L24) в общий максимум. Выводится ответ.

 ![image](https://user-images.githubusercontent.com/55274498/132395963-c748f278-77c1-4838-abca-62aef4ea9c31.png)



