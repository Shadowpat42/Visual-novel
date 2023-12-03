# Игра начинается здесь:
label start:


# <Пролог>
    $ bad_condition = 0
    play music "music/prolog.ogg" fadein (0.2)
    "{color=#000000}Простите что так неожиданно, но пожалуйста, выслушайте мой вопрос и как следует подумайте над ответом{/color}"
    "{color=#000000}Действительно ли экзамены - главный показатель успеха?{/color}"
    "{color=#000000}Наверное вы не замечали... {w}Но большинство людей подвержены оценки из вне уже с самого рождения{/color}"
    "{color=#000000}Будь то наши манеры, внешний вид, речь - все это оценивается уже на уровне младенчества{/color}"
    "{color=#000000}Уже с приходом школьной поры начинается внедрение определенной системы...{/color}"
    "{color=#000000}Такая система напоминает процесс выращивания виноградной лозы{/color}"
    "{color=#000000}Во время пикирования садовник удаляет слабые и непродуктивные ростки, оставляя только наиболее сильные и здоровые{/color}"
    "{color=#000000}В процессе подготовки к Единому Государственному экзамену мое ментальное состояние менялось по разному...{/color}"
    "{color=#000000}В начале я был очень заряжен мотивацией и был готов работать на результат!{/color}"
    "{color=#000000}Потом постепенно приходило осознание того, что школьной системы недостаточно и приходилось заниматься дополнительно{/color}"
    "{color=#000000}А после...{/color}"
    "{color=#000000}Я не помнил и дня, когда не задавал себе {i}этот{/i} вопрос...{/color}"
    "{color=#000000}{i}Когда это все закончится?{/i}{/color}"
    "{color=#000000}Тогда я не понимал, для чего это все и какой меня ждет конец...{/color}"
# </Пролог>

# <Эпизод |: Первые шаги>
    # Превью
    window hide
    show episode_1 with fade
    pause
    stop music

    # Основные действия
    scene room with fade
    play music "music/on_room.ogg" fadein(1.0)
    "{color=#000000}Был обычный утренний день. Солнце только начало подниматься на небосвод и его теплые лучи начали падать на мою голову{/color}"
    "{color=#000000}Я почувствовал приятное ощущение тепла, растекающегося по всему телу{/color}"
    "{color=#000000}В мою голову начинали приходить мысли о сне, который недавно закончился{/color}"
    "{color=#000000}Странно, обычно я всегда забываю, что мне снится{/color}"
    "{color=#000000}Тут же с другой комнаты стал доноситься громкий отчетливый голос{/color}"
    m "{color=#000000}Егор! Уже 8 часов утра. Просыпайся!{/color}"
    "{color=#000000}Неожиданный поток слов быстро перебил желание спать дальше{/color}"
    "{color=#000000}Я медленно начал вставать, нащупывая смартфон{/color}"
    "{color=#000000}Разблокировав экран на меня обрушилось большое множество push-уведомлений, первое из которых не заставило себя ждать...{/color}"
    "{color=#000000}Первое сентября!{/color}"
    "{color=#000000}Казалось бы важный праздник: День знаний... Однако для меня это лишняя морока{/color}"
    m "{color=#000000}Завтрак я уже приготовила, а поглаженная одежда тебя ждет в шкафу{/color}"
    m "{color=#000000}Не забудь надеть галстук!{/color}"
    play sound "music/close_door.mp3" volume 0.5
    "{color=#000000}Дверь захлопнулась{/color}"
    e "{color=#000000}Хорошо - тихо промолвил я самому себе{/color}"
    "{color=#000000}В последнее время она часто засиживается допоздна на работе, а иногда и вовсе приходит под утро...{/color}"
    "{color=#000000}Мы стали меньше общаться, а пересекаться лишь вечером{/color}"
    "{color=#000000}Надеюсь когда-нибудь мы сможем пережить {i}этот{/i} период{/color}"
    "{color=#000000}Как же нам {i}тебя{/i} не хватает...{/color}"
    "{color=#000000}Но не будем о грустном!{/color}"
    play sound "music/steps.mp3"
    "{color=#000000}Я открыл дверь и направился на кухню, где меня ждал еще теплый завтрак{/color}"
    scene kitchen with fade
    window hide
    pause
    scene food with fade
    "{color=#000000}На столе меня ждала яичница-глазунья с копченной колбасой, а также пара ломтиков хлеба{/color}"
    "{color=#000000}Я принялся за еду!{/color}"
    # Звук поедания пищи - добавить!
    "{color=#000000}Колбаса покрытая желтком нежно таяла во рту, создавая приятное ощущение наслаждения{/color}"
    "{color=#000000}Ммм... Просто небесно!{/color}"
    "{color=#000000}Вытягивая крошечные глотки чая, я чувствовал как его аромат и тепло окутывают каждую клеточку моего тела{/color}"
    "{color=#000000}Так... Нужно поторопиться, а то можно опоздать!{/color}"
    "{color=#000000}Я ускорился и через несколько минут тарелки были пустыми{/color}"
    scene koridor with fade
    "{color=#000000}Покончив с едой, я быстро накинул заранее приготовленную одежду, обулся и вышел из дома{/color}"
    play sound "music/close_door.mp3" volume 0.5
    scene street with fade
    "{color=#000000}На улице была тёплая осенняя погода, начал чувствоваться холодный ветерок, но солнце ещё грело{/color}"
    e "{color=#000000}Осень...{/color}"
    "{color=#000000}Такое ощущение будто вчера лето только началось. Быстро же летит время{/color}"
    "{color=#000000}Мельком глянув на часы я увидел время: 9:30 AM.{w}\nЛинейка была примерно в 10 часов, так что у меня было где-то 30 минут{/color}"
    "{color=#000000}До школы было идти примерно минут 10, так что я мог позволить себе идти не спеша{/color}"
    "{color=#000000}По дороге я заметил, что на улицах было пусто.{w}\nСтранно... Я не мог проспать{/color}"
    scene phone with fade
    "{color=#000000}Я проверил свои часы и увидел точное время: 9:35 PM{/color}"
    play music "music/danger.ogg" fadein(2.0)
    scene street with fade
    "{color=#000000}Тут я заметил кое-что странное...{/color}"
    scene streetDog with dissolve
    "{color=#000000}Вдали виднелась черная собака неизвестной мне породы и я бы готов поклясться...{/color}"
    "{color=#000000}Она уставилась на меня!{/color}"
    "{color=#000000}Собака стремительны приближалась и уже через несколько секунд начала гавкать{/color}"
    play sound "music/dog.mp3"
    "{color=#000000}*Гав Гав!{/color}"
    play sound "music/vdoh.mp3"
    "{color=#000000}Спокойно... Вдох, выдох!{/color}"
    "{color=#000000}Что делать? Как мне следует поступить?{/color}"
    menu:
        "{color=#000000}Сбежать!{/color}":
            # <ГЛАВА |: Выбор сбежать!>
            label run_away:
                play music "music/kripota.ogg" fadein(2.0)
                "{color=#000000}Я оглянулся.{w} Поблизости никого не было!{/color}"
                "{color=#000000}Страшно...Очень страшно!{w} А вдруг меня съедят?{/color}"
                "{color=#000000}Не раздумывая, я бросился прочь{/color}"
                scene street at migga_running
                play sound "music/dog_aggressive.mp3" volume 0.3
                "{color=#000000}Ноги запинались о камни. В голове витали безумные мысли:{/color}"
                "{color=#000000}сейчас схватят{/color}"
                "{color=#000000}Сцапают.{/color}"
                "{color=#000000}Утащат навсегда!{/color}"
                "{color=#000000}Но был другой голос, наверное голос разума. Он придавал сил, ускоряя бег{/color}"
                "{color=#000000}«{i}Ты сможешь! Не останавливайся!{/i}»{/color}"
                "{color=#000000}Кто-то мчался за мной, ломая осинник, стремительно сокращая расстояние{/color}"
                "{color=#000000}Собака начала лаять еще сильнее!{/color}"
                "{color=#000000}Я начал слышать ее шаги!{w}\nА вдруг она меня догонит?{/color}"
                "{color=#000000}С каждым шагом сердце билось все сильнее{/color}"
                scene street_with_tree with dissolve
                "{color=#000000}Я завернул за угол и вышел на школьный двор{/color}"
                "{color=#000000}Звуки погони стихли...{w}\nМожет собака отстала?{/color}"
                play music "music/relax.ogg" fadein(2.0)
                "{color=#000000}Я обернулся. Ее и правда нету.{/color}"
                "{color=#000000}Может быть она и вовсе не была злой?{/color}"
                "{color=#000000}Возможно она хотела просто поесть или ... {/color}"
                "{color=#000000}Неважно!{/color}"
                "{color=#000000}Я посмотрел на свои часы: 9:40 PM.{w}\nДо школы было еще примерно 15 минут{/color}"
                "{color=#000000}Я уже хотел сесть на скамейку как вдруг...{/color}"
                "{color=#000000}?{/color}" "{color=#000000}Привет! Я тебе не помешаю?{/color}"
                show person_1 at center
                with dissolve
                "{color=#000000}?{/color}" "{color=#000000}У тебя такое смешное лицо.{/color}"
                scene episode_end with fade
                pause
                return
            # </ГЛАВА |: Выбор сбежать!>

        "{color=#000000}Покормить{/color}":
            label feed_dog:
                # </ГЛАВА |: Выбор покормить!>
                play music "music/kripota.ogg" fadein(2.0)
                "{color=#000000}Я решил не терять голову и спокойно оценить ситуацию.{/color}"
                "{color=#000000}У меня было несколько пачек собачьего корма в рюкзаке, которые я взял с собой{/color}"
                "{color=#000000}Было страшно, но я решил попробовать успокоить собаку{/color}"
                scene street_with_dog
                "{color=#000000}Подойдя к собаке, я осторожно протянул ей корм.{/color}"
                "{color=#000000}Сначала она казалась напряженной, но потом начала подходить ближе.{/color}"
                play sound "music/feed_dog.mp3"
                "{color=#000000}Собака начала есть корм, и я почувствовал, как напряжение постепенно уходит.{/color}"
                "{color=#000000}Я остался на месте, наблюдая, как она ест.{/color}"
                "{color=#000000}Постепенно она расслабилась, и я смог даже погладить ее по голове.{/color}"
                "{color=#000000}Я чувствовал себя героем, спасителем в трудной ситуации.{/color}"
                "{color=#000000}Вдруг, неожиданно, собака резко начала приближаться...{/color}"
                play sound "music/dog_rik.mp3"
                "{color=#000000}Кажется она разозлилаась еще сильнее.{/color}"
                play sound "music/dog.mp3"
                "{color=#000000}*Гав, гав!{/color}"
                scene street with vpunch
                play sound "music/dog_damage.mp3" volume 0.5
                "{color=#000000}Поняв, что ситуация накаляется я резко пнул собаку и бросился прочь!{/color}"
                scene street at migga_running
                "{color=#000000}Собака начала гоняться за мной, лая и рыча.{/color}"
                play sound "music/dog_aggressive.mp3" volume 0.4
                "{color=#000000}Ноги запинались о камни. В голове витали безумные мысли:{/color}"
                "{color=#000000}сейчас схватят{/color}"
                "{color=#000000}Сцапают.{/color}"
                "{color=#000000}Утащат навсегда!{/color}"
                "{color=#000000}Но был другой голос, наверное голос разума. Он придавал сил, ускоряя бег.{/color}"
                "{color=#000000}«{i}Ты сможешь! Не останавливайся!{/i}»{/color}"
                "{color=#000000}Кто-то мчался за мной, ломая осинник, стремительно сокращая расстояние.{/color}"
                "{color=#000000}Собака не отставала, и ее зловещий визг был всё ближе.{/color}"
                scene street_with_tree with dissolve
                "{color=#000000}Я завернул за угол и вышел на школьный двор.{/color}"
                "{color=#000000}Звуки погони стихли... Может, собака отстала?{/color}"
                play music "music/relax.ogg" fadein(2.0)
                "{color=#000000}Я обернулся. Ее и правда нету.{/color}"
                "{color=#000000}Может быть, она и вовсе не была злой?{/color}"
                "{color=#000000}Возможно, она хотела просто поесть или... Неважно!{/color}"
                "{color=#000000}Я посмотрел на свои часы: 9:40 PM. До школы было еще примерно 15 минут{/color}"
                "{color=#000000}Я уже хотел сесть на скамейку, как вдруг...{/color}"
                "{color=#000000}?{/color}" "{color=#000000}Привет! Я тебе не помешаю?{/color}"
                show person_1 at center
                with dissolve
                "{color=#000000}?{/color}" "{color=#000000}У тебя такое смешное лицо.{/color}"
                scene episode_end with fade
                pause
                return
            # </ГЛАВА |: Выбор Покормить!>


        "{color=#000000}Насилие{/color}":
            # <ГЛАВА |: Выбор Насилие!>
            label fight:
                play music "music/kripota.ogg" fadein(2.0)
                $ bad_condition += 1
                "{color=#000000}Я решил не отступать.{/color}"
                "{color=#000000}В конце концов я человек, а это всего лишь бродячий пес.{/color}"
                "{color=#000000}Он не обладает интеллектом и действует лишь из чувства голода.{/color}"
                "{color=#000000}Я начал осматривать местность в поисках вспомогательных вещей{/color}"
                "{color=#000000}Слева от меня лежала деревянная палка длиною 1 метр.{/color}"
                e "{color=#000000}Вполне сойдет.{/color}"
                play sound "music/dog_rik.mp3"
                "{color=#000000}Собака начала приближаться и рычать.{/color}"
                "{color=#000000}Стоило мне посмотреть ей в глаза, как тут же издался громкий лай.{/color}"
                play sound "music/dog_aggressive.mp3" volume 0.5
                "{color=#000000}Недолго думая, собака нацелилась на мою ногу и ринулась вперед{/color}"
                e "{color=#000000}Как глупо... Думаешь самая умная?!{/color}"
                "{color=#000000}Разозлившись от столь прямолинейного хода, я замахнулся палкой и ударил собаку по носу{/color}"
                play sound "music/dog_damage.mp3"
                scene fall_dog with vpunch
                "{color=#000000}Собака упала.{/color}"
                "{color=#000000}Кажется я не рассчитал силу... Иначе она бы не упала так быстро.{/color}"
                "{color=#000000}Я выбросил палку и оглянулся.{w} На улице никого не было.{/color}"
                "{color=#000000}Я подошел к вырубившейся собаке{/color}"
                "{color=#000000}Дыхание есть. Значит она еще жива.{/color}"
                e "{color=#000000}Ты уж прости, но моей вины тут нет.{/color}"
                e "{color=#000000}Ты - провокатор, а значит и должна быть готова нести ответственность.{/color}"
                "{color=#000000}Кажется я начинаю опаздывать.{/color}"
                "{color=#000000}Я прошел мимо лежащей собаки и направился в школу{/color}"
                # "{color=#000000}{/color}"
                scene vorota with fade
                play music "music/music_for_school.mp3" fadein(5.0)
                "{color=#000000}За углом улицы я уже видел контуры здания, в котором скрыт первый день моей новой жизни{/color}"
                "{color=#000000}Проходя через школьные ворота я увидел улыбающееся лицо охранника, который часто закрывал ворота чуть позже{/color}"
                menu:
                    "{color=#000000}Улыбнуться в ответ{/color}":
                        label smile_face:
                             "{color=#000000}Я улыбнулся в ответ{/color}"
                             "{color=#000000}Охранник кивнул в знак приветствия и я поспешил внутрь{/color}"
                    "{color=#000000}Пройти мимо{/color}":
                        label unsmile_face:
                            "{color=#000000}Нужно поторопиться. {w} Не хочется опоздать в первый же день{/color}"

                scene dvor with fade
                "{color=#000000}Вдали виднелась толпа школьников, рассматривающих списки распределения.{/color}"
                "{color=#000000}Вот они, изменения в действии. Каждый год – новый класс. Государство считает, что таким образом мы будем лучше общаться, находить общие интересы{/color}"
                "{color=#000000}Логично наверное...{/color}"
                "{color=#000000}Но что, если следующий класс окажется ещё хуже?{/color}"
                "{color=#000000}Разве можно строить настоящие дружеские отношения за один год? Мы просто пересаживаемся, как фишки на шахматной доске{/color}"
                "{color=#000000}Интересно, а в следующем классе будет кто-то, кто действительно поймет?{/color}"
                "{color=#000000}Или опять будут те же стандартные роли: популярные, отстающие, странные…{/color}"
                "{color=#000000}Надеюсь, на этот раз повезет. Надеюсь, что новый класс окажется не просто группой людей, собранных вместе, а настоящим сообществом, где каждый найдет свое место.{/color}"
                "{color=#000000}Жизнь учит, но что-то мне подсказывает, что это только начало нового этапа, и я лучше подготовлюсь к переменам.{/color}"
                "{color=#000000}Возможно, в этот раз стоит открыться для новых знакомств и взглядов.{/color}"

                "{color=#000000}Тут я заметил знакомый силуэт...{/color}"
                e "{color=#000000}Привет? - сомневаясь промолвил я.{/color}"
                "{color=#000000}Девушка обернулась, пытаясь найти источник отклика, вопросительно всматривалась в толпу около стенда.{/color}"
                e "{color=#000000}Эй, я здесь!{/color}"
                "{color=#000000}Я помахал ей рукой, после чего она с легкостью меня нашла.{/color}"
                i "{color=#000000}Привет, давно не виделись.{/color}"
                show friend_smile with dissolve
                "{color=#000000}Передо мной предстала серебристоволосая девушка 18 лет. От нее пахло нежным ароматом цветов, который будто переплетался с запахом свежести осеннего ветерка{/color}"
                "{color=#000000}Ее взгляд был ясным, а улыбка игриво скрывалась на губах, придавая ей загадочную привлекательность.{/color}"
                e "{color=#000000}За лето ты стала красивее, что я тебя почти не узнал.{/color}"
                "{color=#000000}Если бы не волосы и глаза, то я и вовсе бы не смог распознать в ней свою давнюю подругу.{/color}"
                i "{color=#000000}Привет! А ты я смотрю наоборот, все такой же мрачный и унылый!{/color}"
                "{color=#000000}Такое откровение очень сильно ударило по моей самооценке, ввиду чего я решил контратаковать.{/color}"
                e "{color=#000000}А ты, кажется, обрела небесную легкость. Как пройденное лето? Чем занималась?{/color}"
                i "{color=#000000}О, ты знаешь, то тут, то там. Путешествовала, училась новому, встречала интересных людей. Такие обычные вещи.{/color}"
                "{color=#000000}Мне стало интересно, что еще она скрывает за своей загадочной улыбкой.{/color}"
                e "{color=#000000}Новые встречи? Может, есть кто-то особенный?{/color}"
                "{color=#000000}Она рассмеялась, и в ее глазах мелькнул неведомый свет.{/color}"
                i "{color=#000000}Кто знает, может быть... Но что с тобой? Почему такой серьезный?{/color}"
                e "{color=#000000}Ну, ты же знаешь, всегда был немного мрачноватым.{/color}"
                i "{color=#000000}Может, пора изменить этот образ? Ведь жизнь — это такое удивительное приключение, а ты еще только в начале своего пути.{/color}"
                "{color=#000000}Эти слова задели меня за живое, заставив задуматься. В ее глазах мерцал огонек приключений, который манил меня открыть для себя что-то новое.{/color}"
                e "{color=#000000}Может быть, ты и права. Но вспомни как ты всегда опаздывала на урок математики у Александры Владимировны?{/color}"
                i "{color=#000000}Ах, эти бесконечные опоздания! Да, да, ты мне вовремя напомнил. Я уже бегу.{/color}"
                i "{color=#000000}Будь осторожен, и не забывай, жизнь слишком коротка, чтобы проводить ее в серьезности.{/color}"
                hide friend_smile with dissolve
                "{color=#000000}Она мелькнула взглядом, прошла мимо меня, и ее аромат цветов остался в воздухе.{/color}"
                "{color=#000000}Я смотрел, как она исчезает из виду, унося с собой частичку таинственной легкости, которую она приносила одним своим присутствием.{/color}"
                "{color=#000000}Вдыхая запах осеннего ветерка, я задумался о ее словах и решил, что, возможно, пора по-настоящему насладиться этим удивительным приключением под названием жизнь.{/color}"
                e "{color=#000000}Ну ладно, пора-бы идти в класс..,{/color}"
                scene black with fade

                "{color=#000000}Поднимаясь по лестнице к новому классу, я размышлял о том, какие люди меня ждут.{/color}"
                "{color=#000000}Новые лица, новые имена — все это создавало ощущение волнения и неопределенности.{/color}"
                "{color=#000000}Может быть, в этот раз стоит по-настоящему открыться. Просто быть самим собой и дать другим возможность узнать меня, такого, какой я есть?{/color}"
                "{color=#000000}А вдруг, среди этой толпы, я найду настоящих друзей?{/color}"
                "{color=#000000}Я приблизился к двери класса и услышал, как начали перекличку.{/color}"
                scene classroom with fade
                e "{color=#000000}Здравствуйте, я немного опоздал, - громко сказал я{/color}"
                a "{color=#000000}О, микронин, давно я тебя не видела. Заходи, снова будешь опаздывать — пускать не буду. Ты же помнишь, как под дверью половину уроков простоял?{/color}"
                e "{color=#000000}Больше не повторится, — с ухмылкой ответил я и зашёл в кабинет.{/color}"
                "{color=#000000}В прошлом году Александра Владимировна вела у нас математику, и я часто опаздывал к ней на урок.{/color}"
                "{color=#000000}Она та ещё злюка: за каждое опоздание готова мне двойки ставить, но не ставит, иначе бы журнала не хватило на такое количество оценок.{/color}"
                "{color=#000000}Я уселся за свободную парту и начал слушать её рассказ о предстоящем учебном годе.{/color}"
                a "{color=#000000}Ну, как твои летние каникулы? — спросила Александра Владимировна, обращая внимание на меня.{/color}"
                e "{color=#000000}Довольно насыщенно, узнал много нового...{/color}"
                a "{color=#000000}Хорошо, что хоть кто-то пользуется своим временем. В этом году мы будем заниматься более серьезно. Рассчитываю на тебя.{/color}"
                e "{color=#000000}Конечно. Я постараюсь не подвести.{/color}"
                "{color=#000000}Учительница кивнула, и я погрузился в её рассказ, стараясь проигнорировать наказующий взгляд, который время от времениметался в мою сторону... {/color}"




            # </ГЛАВА |: Выбор Насилие!>



    # scene episode_end with dissolve
    # DOG:
    # Насилие --> Минус баллы у Екатерины Лебедевой.
    # Дать еды --> укус --> bad.
    # Сбежать! --> Опоздал.
    "{color=#000000}{/color}"
    "{color=#000000}{/color}"
    "{color=#000000}{/color}"
    "{color=#000000}{/color}"
    "{color=#000000}{/color}"

# Эффект бега!
transform migga_running:
    anchor(0,0) pos(0,0)
    linear 0.1 pos(-9, -7)
    linear 0.1 pos(0,0)
    linear 0.1 pos(9, -7)
    linear 0.1 pos(0,0)
    repeat
