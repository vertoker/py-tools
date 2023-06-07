# vimeworld-bot
Бот для режима Prison для Minecraft сервера Vimeworld.
Это мой старый личный проект, над которым я по фану работал в конце 2019.
Слабонервных программистов прошу не лезть в логику бота (плохо кончится).

<h1><b>Для чего этот бот нужен?</b></h1>

На Prison существует система ежедневных наград, среди которых есть достаточно ценные "звёзды".
Также в этом режиме существует относительно полноценная торговая площадка.
И также сам сайт vimeworld.ru очень поверхностно защищён от создания аккаунтов.
А клиент заставляет запросто перезаходить в аккаунт.

<h1><b>Понимаете к чему я клоню?</b></h1>

Этот бот был создан для замены многочасового монотонного труда.
Он собирает ежедневные награды с каждого аккаунта на каждом сервере.
И все награды передаёт через торговую площадку на основной аккаунт.
Бот умеет запускать, регистрироваться, собирать аккаунты, закрывать и повторить n количество раз.

<h1><b>Важно понимать!</b></h1>

Этот бот работает не с самим процессом Vimeworld'а, а по сути эмулирует реальную деятельность игрока.
То есть бот забирает управление мышкой и самостоятельно работает с клиентом.
Из этого следует, что бот работает попиксельно.
Это конечно ужасный костыль, ну уж как сделал.

<h1><b>Какие тонкости необходимо учитывать?</b></h1>

1) Бот работает только если в системе установлен FullHD (1920X1080)
2) Бот работает только если приложение Vimeworld запущен не в полноэкранный режим
3) Бот я писал до августовского обновления (очевидно) и он учитывает лишь первые 9 серверов
4) Бот в состоянии понимать забитость сервера. Если он не может войти на сервер Prison в течении 2 минут, то бот перезапускает клиент
5) Бот может передавать деньги и все ресурсы в основных 9-ти ячейках инвертаря в личный trade игроку, которого можно указать в параметрах
6) Игрок обязан находится на сервере, на который должны отдаваться награды (сервер можно изменить опять же в параметрах)
7) Если хочется убрать лишние сервера и оставить только избранный, то придётся ждать истечение времени, через которое можно залогиниться в клиенте. Время ожидания, между которым можно залогинится снова составляет 5 минут. Так что я бы не советовал убирать лишние сервера.
8) !ВАЖНО! Я его не тестировал в отрыве от IDE. Он может плохо работать если запускать отдельно py скрипты

<h1><b>Личные советы от себя</b></h1>

1) Для работы бота советую выделить отдельный ПК для работы с ним (на слабых идёт вполне адекватно, если предварительно настроить клиент на минимальную графику)
2) Совету установить IDE PyCharm, на котором я писал и тестировал этого бота
3) Бот крайне кастомный для моего доп. ПК особенно в плане таймингов. Поэтому если есть желание, лучше настроить тайминги в загрузках

<h1><b>Ну и самое главное</b></h1>

Если у вас не работает, а выше мной написанное не помогает, то лучше вам бросить эту затею (если вы не безумец программист, который захочет заставить этот кусок кода работать).
Надеюсь этот бот кому-то пригодится.
Всем удачи!