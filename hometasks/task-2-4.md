# Федоров Алексей Б19-505

## Домашнее задание 2.4 - Алгоритм поиска в списке с дубликатами в модели CRCW PRAM

В модели CRCW PRAM нужно разрешать возникающие конфликты. Можно каждому процессору приписать приоритет по следующему правилу: процессор с наименьшим номером имеет наибольший приоритет. Тогда алгоритм поиска будет выглядеть следующим образом:

```
Parallel Sort
	for j=l to N do
		P[j] читает M[j] в Х и M[N+1] в target
		P[j] читает M[N+2] в index
		if X=target and (index=0 or j<index) then
			записать j в M[N+2]
		end if
	end for
Parallel End
```

С помощью условия j<index право на запись в ячейку M[N+2] предоставляется процессору с наименьшим приоритетом.

## Используемая литература

Дж. Макконнелл Основы современных алгоритмов
