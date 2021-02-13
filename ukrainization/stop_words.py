STOP_WORDS = set(
    """а
або
адже
аж
але
алло
б
багато
без
безперервно
би
більш
більше
біля
близько
бо
був
буває
буде
будемо
будете
будеш
буду
будуть
будь
була
були
було
бути
в
вам
вами
вас
ваш
ваша
ваше
вашим
вашими
ваших
ваші
вашій
вашого
вашої
вашому
вашою
вашу
вгорі
вгору
вдалині
весь
вже
ви
від
відсотків
він
вісім
вісімнадцятий
вісімнадцять
вниз
внизу
вона
вони
воно
восьмий
все
всею
всі
всім
всіх
всього
всьому
всю
вся
втім
г
геть
говорив
говорить
давно
далеко
далі
дарма
два
двадцятий
двадцять
дванадцятий
дванадцять
дві
двох
де
дев'ятий
дев'ятнадцятий
дев'ятнадцять
дев'ять
декілька
день
десятий
десять
дійсно
для
дня
до
добре
довго
доки
досить
другий
дуже
дякую
е
є
ж
же
з
за
завжди
зазвичай
занадто
зараз
зате
звичайно
звідси
звідусіль
здається
зі
значить
знову
зовсім
і
із
її
їй
їм
іноді
інша
інше
інший
інших
інші
їх
й
його
йому
каже
ким
кілька
кого
кожен
кожна
кожне
кожні
коли
кому
краще
крім
куди
ласка
ледве
лише
м
має
майже
мало
мати
мене
мені
менш
менше
ми
мимо
міг
між
мій
мільйонів
мною
мого
могти
моє
моєї
моєму
моєю
може
можна
можно
можуть
мої
моїй
моїм
моїми
моїх
мою
моя
на
навіть
навіщо
навколо
навкруги
нагорі
над
назад
найбільш
нам
нами
нарешті
нас
наш
наша
наше
нашим
нашими
наших
наші
нашій
нашого
нашої
нашому
нашою
нашу
не
небагато
небудь
недалеко
неї
немає
нерідко
нещодавно
нею
нибудь
нижче
низько
ним
ними
них
ні
ніби
ніж
ній
ніколи
нікуди
нім
нічого
ну
нього
ньому
о
обидва
обоє
один
одинадцятий
одинадцять
однак
однієї
одній
одного
означає
окрім
он
особливо
ось
п'ятий
п'ятнадцятий
п'ятнадцять
п'ять
перед
перший
під
пізніше
пір
після
по
повинно
подів
поки
пора
поруч
посеред
потім
потрібно
почала
початку
при
про
просто
проте
проти
раз
разу
раніше
рано
раптом
рік
роки
років
року
році
сам
сама
саме
самим
самими
самих
самі
самій
само
самого
самому
саму
свого
своє
своєї
свої
своїй
своїх
свою
себе
сих
сім
сімнадцятий
сімнадцять
сказав
сказала
сказати
скільки
скрізь
собі
собою
спасибі
спочатку
справ
став
суть
сьогодні
сьомий
т
та
так
така
таке
такий
такі
також
там
твій
твого
твоє
твоєї
твоєму
твоєю
твої
твоїй
твоїм
твоїми
твоїх
твою
твоя
те
тебе
теж
тепер
ти
тим
тими
тисяч
тих
ті
тієї
тією
тій
тільки
тім
то
тобі
тобою
того
тоді
той
тому
тою
треба
третій
три
тринадцятий
тринадцять
трохи
ту
туди
тут
у
увесь
уміти
усе
усі
усім
усіма
усіх
усього
усьому
усю
усюди
уся
хіба
хотіти
хоч
хоча
хочеш
хто
це
цей
цим
цими
цих
ці
цієї
цій
цього
цьому
цю
ця
час
частіше
часто
часу
через
четвертий
чи
чиє
чиєї
чиєму
чиї
чиїй
чиїм
чиїми
чиїх
чий
чийого
чийому
чим
численна
численне
численний
численні
чию
чия
чого
чому
чотири
чотирнадцятий
чотирнадцять
шістнадцятий
шістнадцять
шість
шостий
ще
що
щоб
щодо
щось
я
як
яка
який
яких
які
якій
якого
якої
якщо""".split()
)


def remove_stop_words(tokens) -> list:
    """
    Returns a new set with elements in the set that aren’t in the other.
    """
    return list(set(tokens).difference(STOP_WORDS))
