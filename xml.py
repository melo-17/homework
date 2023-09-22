# This Python file uses the following encoding: utf-8
import re

f: str = '''
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/"  >
  <channel>
    <title>Все публикации подряд на Хабре</title>
    <link>https://habr.com/ru/articles/</link>
    <description><![CDATA[Все публикации подряд на Хабре]]></description>
    <language>ru</language>
    <managingEditor>editor@habr.com</managingEditor>
    <generator>habr.com</generator>
    <pubDate>Sun, 17 Sep 2023 20:52:26 GMT</pubDate>
    
      <image>
        <link>https://habr.com/ru/</link>
        <url>https://habrastorage.org/webt/ym/el/wk/ymelwk3zy1gawz4nkejl_-ammtc.png</url>
        <title>Хабр</title>
      </image>

              <item>
      <title><![CDATA[Работа с Gradient через jobs + burst]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761572/</guid>
      <link>https://habr.com/ru/articles/761572/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761572</link>
      <description><![CDATA[<p>В Unity есть класс Gradient, который предоставляет удобные средства для управления градиентом в рантайме и редакторе. Но т.к. это класс, а не структура использовать его через Job system и burst нельзя. Это первая проблема. Вторая проблема — это работа с ключами градиента. Получение значений осуществляется через массив, который создаётся в куче. И как следствие напрягает сборщик мусора.</p><p>Сейчас я покажу как можно решить эти проблемы. И в качестве бонуса получить увеличение производительности до 8 раз при выполнении метода Evaluate.</p><p></p> <a href="https://habr.com/ru/articles/761572/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761572#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 20:51:52 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[gradient]]></category><category><![CDATA[unsafe]]></category><category><![CDATA[c#]]></category><category><![CDATA[unity]]></category>
    </item>






      <item>
      <title><![CDATA[Создаем мини-игру с капельным эффектом и движущимися кружками. Часть 1]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761608/</guid>
      <link>https://habr.com/ru/articles/761608/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761608</link>
      <description><![CDATA[<p>Привет, дорогие пользователи мира IT!</p><p>В современной веб-разработке существует множество способов сделать ваш сайт интересным и привлекательным для пользователей. И даже используя простые техники можно добиться высоких результатов!</p><p>Предлагаю вам самим создать мини-игру с нуля. И затем, вы сможете использовать её, чтобы оживить и добавить интерактивность любой веб-странице.</p><p></p> <a href="https://habr.com/ru/articles/761608/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761608#habracut">Читать дальше &rarr;</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 20:09:30 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[капельный эффект]]></category><category><![CDATA[нативный код]]></category><category><![CDATA[javascript классы]]></category>
    </item>






      <item>
      <title><![CDATA[Разбор светодиодной лампы ED-SON с внешним источником питания]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761604/</guid>
      <link>https://habr.com/ru/articles/761604/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761604</link>
      <description><![CDATA[<p>Разбор LED лампы с внешним источником тока. <br>Взгляд на реализацию лампы за 500 рублей. <br>Вскрытие, фото, схема.</p><p></p> <a href="https://habr.com/ru/articles/761604/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761604#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 20:01:12 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[слономышь]]></category><category><![CDATA[led]]></category><category><![CDATA[led-лампы]]></category><category><![CDATA[led driver]]></category><category><![CDATA[ed-son]]></category><category><![CDATA[светодиодные лампы]]></category><category><![CDATA[светодиодная лампа]]></category><category><![CDATA[светодиодное освещение]]></category><category><![CDATA[светодиодный светильник]]></category><category><![CDATA[светодиодная лампа для дома]]></category>
    </item>






      <item>
      <title><![CDATA[Введение в Cloud native. Часть 2. Принципы облачных приложений]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/760348/</guid>
      <link>https://habr.com/ru/articles/760348/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=760348</link>
      <description><![CDATA[<p>В прошлой <a href="https://habr.com/ru/articles/758250/" rel="noopener noreferrer nofollow">первой части </a>мы рассмотрели само понятие Cloud native и модели облачных вычислений. А так же выделили концепцию облачных приложений. В этой части рассмотрим их принципы. </p><p></p> <a href="https://habr.com/ru/articles/760348/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=760348#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 19:19:18 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[it-компании]]></category><category><![CDATA[it-инфраструктура]]></category><category><![CDATA[облачные технологии]]></category>
    </item>






      <item>
      <title><![CDATA[Римские числа или как не запоминать дифтонги]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761596/</guid>
      <link>https://habr.com/ru/articles/761596/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761596</link>
      <description><![CDATA[<p>Откройте почти любую реализацию перевода чисел из арабской системы в римскую и вы почти со 100% вероятностью увидите там знаменитые дифтонги "CM" (900), "CD" (400) и так далее. И поначалу кажется, что без них не обойтись. Но это не так!</p><p></p> <a href="https://habr.com/ru/articles/761596/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761596#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 18:31:57 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[математика]]></category><category><![CDATA[римская нумерация]]></category><category><![CDATA[арабская нумерация]]></category><category><![CDATA[дифтонги]]></category>
    </item>






      <item>
      <title><![CDATA[Эволюция блокировщиков рекламы. Технологическое противостояние]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/globalsign/articles/761594/</guid>
      <link>https://habr.com/ru/companies/globalsign/articles/761594/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761594</link>
      <description><![CDATA[<img src="https://habrastorage.org/webt/ki/f0/mp/kif0mpdlyoiirc-gqkbwe_6h1ho.png"><br>
<br>
Работа в интернете без блокировщиков рекламы практически невозможна. Всё больше людей используют их на постоянной основе, устанавливая также друзьям и родственникам. Что тут говорить, если даже ФБР <a href="https://www.ic3.gov/Media/Y2022/PSA221221" rel="nofollow noopener noreferrer">официально рекомендует их использовать</a> для защиты от мошенничества в интернете.<br>
<br>
Однако некоторые интернет-компании до сих пор получают львиную часть дохода от интернет-рекламы, и для них блокировщики представляют экзистенциальную угрозу, поэтому они борются с ними всеми силами. В первую очередь, техническими мерами.<br> <a href="https://habr.com/ru/articles/761594/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761594#habracut">Читать дальше &rarr;</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 18:17:57 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[блокировка рекламы]]></category><category><![CDATA[баннеры]]></category><category><![CDATA[Google]]></category><category><![CDATA[Chrome]]></category><category><![CDATA[Web Environment Integrity]]></category><category><![CDATA[YouTube]]></category><category><![CDATA[uBlock Origin]]></category><category><![CDATA[блокировка интеграций]]></category><category><![CDATA[SponsorBlock]]></category><category><![CDATA[Manifest V3]]></category><category><![CDATA[Firefox]]></category>
    </item>






      <item>
      <title><![CDATA[Полгода с компьютером Topton Mini PC]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761592/</guid>
      <link>https://habr.com/ru/articles/761592/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761592</link>
      <description><![CDATA[<p>Приближался мой 55 день рождения, и я задумался - чем же себя порадовать? На прошлый юбилей - 5 лет назад - я купил себе мощнейший по тем временам ноутбук - HP OMEN. Он всем хорош! Но я устал таскать его на работу и обратно домой - все-таки около 5 кг (и это без блока питания). Почему бы не заменить его на что-то более легкое и современное? </p> <a href="https://habr.com/ru/articles/761592/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761592#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 17:54:19 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[обзор]]></category><category><![CDATA[Мини ПК]]></category><category><![CDATA[Core i9]]></category><category><![CDATA[topton]]></category>
    </item>






      <item>
      <title><![CDATA[Huawei будет использовать китайские чипы даже в том случае, если они морально устарели. Перспективы компании]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/selectel/articles/761584/</guid>
      <link>https://habr.com/ru/companies/selectel/articles/761584/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761584</link>
      <description><![CDATA[<img src="https://habrastorage.org/getpro/habr/post_images/9cc/e61/214/9cce612148be89f40a688108cc9fa064.jpg" alt="image"><br>
<br>
Мы уже писали о том, что китайская компания Huawei, несмотря на санкции со стороны США, успешно выпускает различные устройства. Более того, компания выпустила новый процессор с использованием 7-нм техпроцесса второго поколения. Произведен этот процессор компанией SMIC, которая, насколько можно судить, постепенно совершенствует технологические процессы и выпускает все более современные чипы. Тем не менее, компоненты, выпускаемые этой компанией, отстают от передовых чипов, выпускаемых TSMC и другими контрактными производителями. В Huawei считают, что это не страшно, главное — то, что уже есть возможность выпускать такие компоненты даже под санкциями. Подробности — под катом. <br> <a href="https://habr.com/ru/articles/761584/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761584#habracut">Читать дальше &rarr;</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 16:52:43 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[huawei]]></category><category><![CDATA[гаджеты]]></category><category><![CDATA[процессоры]]></category>
    </item>






      <item>
      <title><![CDATA[Стандарт JDF простыми словами]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761582/</guid>
      <link>https://habr.com/ru/articles/761582/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761582</link>
      <description><![CDATA[<p>Организация CIP4 разработала стандарт JDF для автоматизации производственных процессов в печатной индустрии. Давайте подробнее рассмотрим сам формат и сегодняшнее состояние стандарта JDF.</p><p></p> <a href="https://habr.com/ru/articles/761582/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761582#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 16:42:11 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[автоматизация производства]]></category><category><![CDATA[типография]]></category><category><![CDATA[полиграфия]]></category><category><![CDATA[печатный станок]]></category>
    </item>






      <item>
      <title><![CDATA[Как сделать свой UI Kit на Vue 3 + storybook и задеплоить его на npm]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761570/</guid>
      <link>https://habr.com/ru/articles/761570/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761570</link>
      <description><![CDATA[<p>Сейчас очень популярная история создавать свой UI Kit и везде рассказывать какой он крутой и как он ускорил разработку, поэтому я решил написать небольшой гайд, как заиметь себе собственный UI Kit. </p><p>После моего туториала, вы тоже сможете рассказывать какой у вас крутой UI Kit, но это не точно :)</p> <a href="https://habr.com/ru/articles/761570/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761570#habracut">Запилить свой UI Kit</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 16:26:22 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[ui-kit]]></category><category><![CDATA[vue.js]]></category><category><![CDATA[vue]]></category><category><![CDATA[ui]]></category><category><![CDATA[ui/ux]]></category><category><![CDATA[uikit]]></category><category><![CDATA[javascript]]></category>
    </item>






      <item>
      <title><![CDATA[Лидерство руководителя: как привести коллектив к работе не за страх, а за совесть]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761574/</guid>
      <link>https://habr.com/ru/articles/761574/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761574</link>
      <description><![CDATA[<p><strong>• </strong>Почему спортсмен сам идет к тренеру и рассказывает о том, что у него не получается, а в офисе часто наоборот? <br><strong>• </strong>Как влиять на сотрудников? <br><strong>• </strong>Как вести коллектив к цели за счет его собственной энергии? <br>В этой статье я постарался интересно и вдумчиво изложить свой опыт управления сотрудниками.</p><p></p> <a href="https://habr.com/ru/articles/761574/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761574#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 16:06:18 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[руководитель]]></category><category><![CDATA[тимлидство]]></category><category><![CDATA[команда]]></category><category><![CDATA[менеджмент]]></category><category><![CDATA[управление]]></category><category><![CDATA[управление людьми]]></category><category><![CDATA[управление командой]]></category><category><![CDATA[управление персоналом]]></category>
    </item>






  



    <item>
      <title><![CDATA[[Перевод] JavaScript триггеры и функции появились в Redis 7.2]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761514/</guid>
      <link>https://habr.com/ru/articles/761514/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761514</link>
      <description><![CDATA[<p>В Redis уже много лет используется язык программирования Lua для исполнения пользовательского кода налету (eval) или определении пользовательских функций. Lua действительно удобный язык, но скорее с точки зрения встраивания внутрь проекта на C/C++ для выполнение простых скриптов. Большинство же разработчиков, которые используют Redis, предпочли бы не учить новый язык, а работать с уже известным и более популярным скриптовым языком, таким как JavaScript. И это наконец-то случилось.</p><p>Предлагаю ознакомиться с тем, как команда Redis в релизе 7.2 дошла до долгожданного внедрения JavaScript и как сделать первый шаги по запуску триггеров и функций.</p><p></p> <a href="https://habr.com/ru/articles/761514/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761514#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 16:05:13 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category>javascript</category><category>redis</category><category>redisgears</category><category>lua</category><category>v8</category><category>redis-stack</category>
    </item>


      <item>
      <title><![CDATA[Парадокс Гранди. Как современные школьники повторяют ошибку Лейбница и Эйлера]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761560/</guid>
      <link>https://habr.com/ru/articles/761560/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761560</link>
      <description><![CDATA[<p>Было у отца два сына. И оставил он им наследство — камень драгоценный. А чтобы никого не обидеть, поставил он перед сыновьями условие: нельзя тот камень ни пилить, ни продавать. Можно только по очереди владеть им. И повелось так — каждый год камень переходил от одного брата к другому. Потом камнем по очереди владели их потомки, потом потомки их потомков… И длилось так вечно.</p><p>Этой притчей итальянский математик, монах и философ Гвидо Гранди пытался объяснить решение задачи, которую сам же и сформулировал. В 18 веке её считали парадоксом и предлагали разные варианты&nbsp;решения. Долгое время она не давала покоя математикам.</p><p>Задача Гранди формулируется очень просто: какой результат мы получим, если будем до бесконечности складывать 1 и -1? <br></p><p></p> <a href="https://habr.com/ru/articles/761560/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761560#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 15:07:39 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[парадокс]]></category><category><![CDATA[ряды]]></category><category><![CDATA[математика]]></category><category><![CDATA[эйлер]]></category><category><![CDATA[лейбниц]]></category><category><![CDATA[задачи]]></category><category><![CDATA[математический анализ]]></category><category><![CDATA[история математики]]></category><category><![CDATA[ошибка гранди]]></category><category><![CDATA[гранди]]></category>
    </item>






      <item>
      <title><![CDATA[Всеслав Чародей. Лучшая российская игра и самый громкий провал]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761568/</guid>
      <link>https://habr.com/ru/articles/761568/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761568</link>
      <description><![CDATA[<p>Здорова, народ. Вот и новый блог подъехал. Сегодня поговорим, не побоюсь этих слов, об амбициозной игре в истории российского&nbsp;геймдева. О той, которая должна была перевернуть всю историю российских игр и показать западу, на что мы способны. Речь пойдет о культовой игре 90-х, а именно «Всеслав Чародей».&nbsp;Чаро. Что? Да, возможно, вы о ней никогда и не слышали. Наверное, потому, что игра так и не вышла в релиз? Но поверьте, это игра была убийцей сразу всех игр тех времен. А простым игрокам запомнилась как великий долгострой с кучей обещаний, громких слов и печальной концовкой.&nbsp;</p><p>В блоге мы узнаем: Что&nbsp;такое этот ваш Всеслав Чародей? Как игра разрабатывалась? С какими трудностями встретилась на пути? Что нам о ней рассказывали? Какие надежды на неё возлагали? И как вся эта история закончилась?</p><p>Ну что? Отправимся в&nbsp;геймдев&nbsp;90-х? Где каждый стремился создать игру мечты!</p><p></p> <a href="https://habr.com/ru/articles/761568/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761568#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 14:37:31 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[Всеслав Чародей]]></category><category><![CDATA[старые игры]]></category><category><![CDATA[олдскул]]></category><category><![CDATA[российские игры]]></category><category><![CDATA[игры 90х]]></category>
    </item>






      <item>
      <title><![CDATA[VimPorn]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761534/</guid>
      <link>https://habr.com/ru/articles/761534/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761534</link>
      <description><![CDATA[<p>На reddit большое комьюнини, которое посвящено vim:&nbsp;<a href="https://www.reddit.com/r/neovim/" rel="noopener noreferrer nofollow">neovim</a>,  <a href="https://www.reddit.com/r/vim/" rel="noopener noreferrer nofollow">vim</a>, <a href="https://www.reddit.com/r/vimplugins/" rel="noopener noreferrer nofollow">implugins</a>,&nbsp; <a href="https://www.reddit.com/r/vimporn/" rel="noopener noreferrer nofollow">vimporn</a>. И чтобы не пропускать какие-то интересные вещи, которые случаются в мире vim, я накидал bash-скрипт.  Скрипт выводит топ-5 лучших постов за год по каждому сабредиту. В статье будет сам скрипт, а также я своими словами расскажу о каждом посте, который попал в топ.</p><p></p> <a href="https://habr.com/ru/articles/761534/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761534#habracut">Читать далее, под катом много картинок ...</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 13:20:56 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[vim]]></category><category><![CDATA[neovim]]></category>
    </item>






      <item>
      <title><![CDATA[CUBIC или как собрать свой Ubuntu]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761532/</guid>
      <link>https://habr.com/ru/articles/761532/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761532</link>
      <description><![CDATA[<p>В этой статье вы найдете простой тутоиал по тому, как сделать свою сборку Ubuntu при помощи Cubic. Я постарался рассказать об основах работы с  Cubic шаг за шагом, хотя в этом нет ничего сложного.</p><p></p> <a href="https://habr.com/ru/articles/761532/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761532#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 11:02:47 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[cubic]]></category><category><![CDATA[os]]></category><category><![CDATA[linux]]></category><category><![CDATA[ubuntu]]></category><category><![CDATA[custom ubuntu]]></category><category><![CDATA[qemu]]></category>
    </item>






      <item>
      <title><![CDATA[Как использовать нейросети веб-студиям и вымрут ли дизайнеры. Бесплатная нейросеть онлайн и как пользоваться Midjourney]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761528/</guid>
      <link>https://habr.com/ru/articles/761528/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761528</link>
      <description><![CDATA[<p>Совсем недавно устраивались интернет протесты и практически похороны художников в связи с появлением нейросети Midjourney. Сейчас ИИ, которые генерируют изображения, достаточно много. Сбер и Яндекс запустили свои нейросети.&nbsp;</p><p>Как это повлияет на веб-дизайнеров и пора ли им подыскивать новую профессию? Или нужно подойти с другой стороны, запрячь искусственный интеллект и использовать в своих целях? Разбираемся!&nbsp;</p><p></p> <a href="https://habr.com/ru/articles/761528/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761528#habracut">Как использовать нейросеть</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 10:54:46 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[нейросети]]></category><category><![CDATA[midjourney]]></category><category><![CDATA[искусственный интеллект]]></category><category><![CDATA[веб-дизайн]]></category><category><![CDATA[дизайнеры]]></category><category><![CDATA[дизайн]]></category><category><![CDATA[веб-студия]]></category><category><![CDATA[ai]]></category>
    </item>






      <item>
      <title><![CDATA[«Право на ремонт» становится всё сильнее: в США производителей обяжут в течение 7 лет поставлять запчасти к устройствам]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/ru_mts/articles/761462/</guid>
      <link>https://habr.com/ru/companies/ru_mts/articles/761462/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761462</link>
      <description><![CDATA[<p>О «праве на ремонт» на Хабре писали уже не раз и не два. Если коротко, то это движение, которое ратует за предоставление пользователю возможности ремонтировать купленные электронные устройства, бытовую технику и транспортные/сельскохозяйственные средства. На днях в Калифорнии, США, приняли один из наиболее строгих для производителей законопроектов. Он даёт больше возможностей относительно ремонта техники пользователям и обязывает производителей этой техники помогать покупателям в случае поломки. Развивается «право на ремонт» и в других регионах. Подробности — под катом.</p><p></p> <a href="https://habr.com/ru/articles/761462/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761462#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 10:00:04 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[гаджеты]]></category><category><![CDATA[законодательство]]></category><category><![CDATA[законодательство и ит]]></category><category><![CDATA[законодательство в it]]></category>
    </item>






  



    <item>
      <title><![CDATA[[Перевод] Разбираем формат EXIF на примере Apple Photos]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/ruvds/articles/761190/</guid>
      <link>https://habr.com/ru/companies/ruvds/articles/761190/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761190</link>
      <description><![CDATA[<a href="https://habr.com/ru/companies/ruvds/articles/761190/"><div style="text-align:center;"><img src="https://habrastorage.org/webt/se/gw/my/segwmyc5zg4h0v-ou3mhodlbs_y.jpeg"></div></a><br>
В этой статье мы познакомимся с форматом EXIF и узнаем, какую информацию содержат метаданные фотографий, как эту информацию можно получить, и каким образом использовать. В качестве примера будем использовать фототеку, управляемую с помощью Apple Photos. <a href="https://habr.com/ru/articles/761190/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761190#habracut">Читать дальше &rarr;</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 10:00:02 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category>ruvds_перевод</category><category>обработка фотографий</category><category>apple photos</category><category>iPhone</category><category>exif</category><category>ExifReader</category><category>osxphotos</category><category>exiftool</category>
    </item>


      <item>
      <title><![CDATA[Что наука не может сказать об изменении климата]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761394/</guid>
      <link>https://habr.com/ru/articles/761394/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761394</link>
      <description><![CDATA[<p><em>Как "…говорит наука" захватила власть в климатических дискуссиях - и почему она сбила нас с пути</em></p><p>"Наука хороша тем, что она истинна, независимо от того, верите вы в нее или нет". - Нил деГрасс Тайсон. Утешительна мысль о том, что наука истинна, независимо от того, принимает ее человек или нет. Такой образ мышления, поддерживаемый известным ученым и защитником науки Нилом деГрасс Тайсоном, предполагает, что в неопределенном мире, где часто происходит столкновение убеждений, наука может быть арбитром истины.</p><p>К сожалению, объективного арбитра истины не существует. Хотя "говорит наука" может быть точной для ограниченного круга фундаментальных вопросов, она просто не применима к большинству сложных решений, с которыми сталкивается современное общество. Именно поэтому так тревожно, что эта фраза стала привычной приставкой в дискуссиях об изменении климата.</p> <a href="https://habr.com/ru/articles/761394/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761394#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 09:00:01 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[наука]]></category><category><![CDATA[климат]]></category><category><![CDATA[парижское соглашение]]></category><category><![CDATA[глобальное потепление]]></category><category><![CDATA[выбросы]]></category><category><![CDATA[парниковые газы]]></category><category><![CDATA[изменение климата]]></category>
    </item>






      <item>
      <title><![CDATA[Актуальный гайд по написанию простого Windows-драйвера]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761512/</guid>
      <link>https://habr.com/ru/articles/761512/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761512</link>
      <description><![CDATA[<p>В рамках данной статьи я постарался написать полноценное руководство по разработке простого драйвера под операционную систему Windows 10. Всем новичкам, заинтересованным в системном программировании рекомендую ознакомиться. Это поможет вам сделать первые шаги в разработке драйверов.</p><p></p> <a href="https://habr.com/ru/articles/761512/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761512#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 08:30:43 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[драйвер]]></category><category><![CDATA[первый драйвер]]></category><category><![CDATA[windows]]></category><category><![CDATA[KMDF]]></category><category><![CDATA[c/c++]]></category><category><![CDATA[системное программирование]]></category><category><![CDATA[WDF]]></category>
    </item>






      <item>
      <title><![CDATA[Управление техническим долгом]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761508/</guid>
      <link>https://habr.com/ru/articles/761508/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761508</link>
      <description><![CDATA[<p>Технический долг в разработке по-разному воспринимают разработчики и бизнес. Для первых - это важная часть работы, которой нужно выделять время. Для вторых, как правило - нерациональная трата человеко-часов. Редко, когда управление техническим долгом ведется организованно и на регулярной основе. А именно здесь, на мой взгляд, и зарыт ключ к разрешению конфликта между бизнесом и разработкой. Именно об этом я сегодня и хочу поговорить.</p> <a href="https://habr.com/ru/articles/761508/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761508#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 07:46:31 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[технический долг]]></category><category><![CDATA[управление техническим долгом]]></category>
    </item>






      <item>
      <title><![CDATA[Обзор 42&quot; OLED монитора KTC G42P5. Или как использовать почти телевизор для работы]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761118/</guid>
      <link>https://habr.com/ru/articles/761118/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761118</link>
      <description><![CDATA[<p>Можно ли работать на OLED? Не слишком ли он большой? Сгорят или не сгорят пиксели? Что с картинкой, реально новый уровень? Стоит ли игра свеч? Попробую ответить на эти и другие вопросы простым человечьим языком после  месяца активного использования монитора. В рунете я этих ответов не нашел, поэтому – пусть будут.</p><p></p> <a href="https://habr.com/ru/articles/761118/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761118#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sun, 17 Sep 2023 00:05:49 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[oled]]></category><category><![CDATA[tv]]></category><category><![CDATA[тв]]></category><category><![CDATA[монитор]]></category><category><![CDATA[KTC]]></category><category><![CDATA[G42P5]]></category><category><![CDATA[дизайн]]></category><category><![CDATA[матрица]]></category><category><![CDATA[выгорание]]></category><category><![CDATA[игры]]></category>
    </item>






      <item>
      <title><![CDATA[Разбираемся в отличии среднего чека от ARPU на примере одного интернет-магазина]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761490/</guid>
      <link>https://habr.com/ru/articles/761490/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761490</link>
      <description><![CDATA[<p>Ко мне обратился коллега с вопросами про бизнес-метрики – средний чек и ARPU. </p><p>В этой статье я разобрался в бизнес-метриках и ответил на вопросы:</p><p>- Что такое ARPU и средний чек? Как их рассчитывать? На какие вопросы они отвечают и для чего нужны?&nbsp;</p><p>- Могут ли они ARPU и средний чек быть&nbsp; равны между собой? Будут ли отличаться в динамике месяц от месяца?</p><p>- Что если в бизнесе кол-во продуктов фиксировано и все они с одинаковой ценой? Будет ли показатель от месяца к месяцу одинаков? А если рассчитывать среднюю выручку?</p><p>А для наглядности – рассчитал данные метрики на реальных данных интернет-магазина. </p><p></p> <a href="https://habr.com/ru/articles/761490/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761490#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 16:43:03 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[продуктовая аналитика]]></category><category><![CDATA[метрики продукта]]></category><category><![CDATA[анализ данных]]></category><category><![CDATA[аналитик данных]]></category><category><![CDATA[arpu]]></category><category><![CDATA[средний чек]]></category><category><![CDATA[python]]></category><category><![CDATA[pandas]]></category><category><![CDATA[seaborn]]></category><category><![CDATA[data science]]></category>
    </item>






      <item>
      <title><![CDATA[Почему одна из самых популярных программ по BIM моделированию названа REVIT?]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761488/</guid>
      <link>https://habr.com/ru/articles/761488/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761488</link>
      <description><![CDATA[<p>Недавно в одном из чатов вновь наткнулся на шутку о схожести названия известных отечественных витаминов Ревит и американской системы информационного моделирования Revit. Есть ли основания полагать, что известные витамины повлияли на имя популярного программного обеспечения. Давайте попытаемся разобраться ).    </p><p></p> <a href="https://habr.com/ru/articles/761488/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761488#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 16:19:00 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[revit]]></category><category><![CDATA[история названия]]></category><category><![CDATA[Ревит витамин проектировщика]]></category><category><![CDATA[Revit продукт с Российскими корнями]]></category>
    </item>






      <item>
      <title><![CDATA[Python в помощь инженеру ПТО]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761484/</guid>
      <link>https://habr.com/ru/articles/761484/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761484</link>
      <description><![CDATA[<p>Всем привет.<br> В статье приведу немного скриптов на Python для решения вопросов с которыми иногда пересекается инженер ПТО строительной организации. Склёпал сам по мотивам информации из инета. Профи будет скучно), уровень "без диплома программиста".</p><p>На рабочем ноуте используется: Win10, Python 3.11, Office2019. Програмлю в PyScripter (нравится мне он))</p><p></p> <a href="https://habr.com/ru/articles/761484/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761484#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 14:55:36 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[python]]></category>
    </item>






      <item>
      <title><![CDATA[Альтер эго. Как создать виртуальную личность и распознать фейк]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/ruvds/articles/760786/</guid>
      <link>https://habr.com/ru/companies/ruvds/articles/760786/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=760786</link>
      <description><![CDATA[<a href="https://habr.com/ru/companies/ruvds/articles/760786/"><img src="https://habrastorage.org/webt/bm/r1/kr/bmr1krmnmm30h_0x8u30s8uac8a.png"></a><br>
<br>
Я люблю общаться с ботами и владельцами фейковых аккаунтов в социальных сетях. В большинстве случаев они довольно милые и относительно безобидные. Порой даже интересно угадывать, что именно они попытаются впарить мне в очередной раз: тотализаторы, БАДы, лохотрон с криптой или недвижимость в Дубае? На днях я несколько часов обстоятельно общался с одной обаятельной девушкой, пока по ряду характерных признаков не убедился в том, что этот аккаунт — тоже фейковый. Признаюсь, раскусить подделку в этот раз было непросто: создатели липовых учёток научились придавать им определённую правдоподобность. Любопытства ради я захотел разузнать, как сейчас создаются виртуальные личности, какой софт и технологии для этого используются и существуют ли способы с ходу определить, что перед тобой не живой человек, а подделка? <a href="https://habr.com/ru/articles/760786/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=760786#habracut">Читать дальше &rarr;</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 14:00:01 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[ruvds_статьи_выходного_дня]]></category><category><![CDATA[социальные сети]]></category><category><![CDATA[сообщества]]></category><category><![CDATA[читальный зал]]></category>
    </item>






      <item>
      <title><![CDATA[Как создать сайт на фреймворке Cample.js?]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761400/</guid>
      <link>https://habr.com/ru/articles/761400/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761400</link>
      <description><![CDATA[<p>В данной статье будет описано небольшое руководство по тому, как создать сайт на таком фреймворке как <a href="https://github.com/Camplejs/Cample.js" rel="noopener noreferrer nofollow">Cample.js</a>. На момент написания статьи (версия 3.1.1), фреймворк уже более года находится в разработке. За это время был реализован минимальный функционал для создания современных веб-приложений. </p><p></p> <a href="https://habr.com/ru/articles/761400/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761400#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 13:07:47 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[cample]]></category><category><![CDATA[javascript]]></category><category><![CDATA[веб-разработа]]></category><category><![CDATA[разработка сайтов]]></category><category><![CDATA[html-верстка]]></category><category><![CDATA[html]]></category><category><![CDATA[интерфейсы]]></category>
    </item>






      <item>
      <title><![CDATA[Protobuf vs Reflection]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761474/</guid>
      <link>https://habr.com/ru/articles/761474/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761474</link>
      <description><![CDATA[<p>Вы когда нибудь задумывались, на сколько <a href="https://grpc.io/" rel="noopener noreferrer nofollow">grpc</a> быстрый. Да в сети, ему равных нет. Если вы гоняете маленькие сообщения, которые надо быстро доставить, то лучше grpc попросту не найти. Но насколько он хорош? Сможет ли он к примеру сравнится просто с нативными вызовами? </p><p>Попробуем сравнить это, но так как в обычной жизни нам это может не пригодится, то добавим еще одно условие - сравниваем как лучший способ взаимодействия с <abbr class="habraabbr" title="Java Native Interface" data-title="&lt;p&gt;Java Native Interface&lt;/p&gt;" data-abbr="jni">jni</abbr> библиотекой. </p><p></p> <a href="https://habr.com/ru/articles/761474/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761474#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 11:49:08 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[Gradle]]></category><category><![CDATA[protobuf]]></category><category><![CDATA[reflection]]></category><category><![CDATA[java]]></category>
    </item>






      <item>
      <title><![CDATA[Зачем нам Kyverno?]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761476/</guid>
      <link>https://habr.com/ru/articles/761476/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761476</link>
      <description><![CDATA[<p><a href="https://kyverno.io/" rel="noopener noreferrer nofollow">Kyverno</a>&nbsp;&nbsp;— это&nbsp;&nbsp;<strong>механизм политики с открытым исходным кодом</strong>&nbsp;&nbsp;для&nbsp;&nbsp;<a href="https://kubernetes.io/" rel="noopener noreferrer nofollow">Kubernetes</a>&nbsp;&nbsp;, который позволяет вам определять, проверять и применять политики для вашего кластера.</p><p>Он&nbsp;&nbsp;<strong>прост в использовании и гибок</strong>&nbsp;, позволяя определять политики с помощью простых декларативных файлов конфигурации, которыми можно управлять и контролировать версии, как и любым другим кодом.</p><p><a href="https://kyverno.io/" rel="noopener noreferrer nofollow">Kyverno</a>&nbsp;&nbsp;можно использовать для реализации&nbsp;&nbsp;<strong>широкого спектра политик</strong>&nbsp;, включая безопасность, соответствие требованиям и передовые методы эксплуатации, и может помочь вам гарантировать, что ваш кластер всегда находится в&nbsp;&nbsp;<strong>известном, совместимом состоянии</strong>&nbsp;.</p><p></p> <a href="https://habr.com/ru/articles/761476/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761476#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 11:35:26 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[devops]]></category><category><![CDATA[kubernetes]]></category><category><![CDATA[kubernetes cluster]]></category><category><![CDATA[kyverno]]></category>
    </item>






      <item>
      <title><![CDATA[Как изменится работа автотаргетинга в Яндекс.Директе в 2023 году]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761472/</guid>
      <link>https://habr.com/ru/articles/761472/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761472</link>
      <description><![CDATA[<p>Компания Яндекс планирует значительно расширить использование технологии автоматического подбора ключевых слов в своей рекламной платформе Яндекс.Директ. Эти обновления алгоритмов автотаргетинга будут запущены в течение осени 2023 года.</p><p>По сути <strong>изменится сам подход к созданию рекламных кампаний</strong>. Если ранее в основе эффективной работы поисковых кампаний лежало качество подбора и использования набора ключевых слов, то после применения обновлений не менее важное значение будут иметь также тексты первого заголовка и описания объявлений. Ведь именно на основе анализа этих двух элементов (впрочем, есть и третий - посадочная страница, которая также будет анализироваться автотаргетингом для подбора ключевых слова) будут подбираться фактические ключевые слова, по которым пользователи Яндекса начнут видеть наши рекламные объявления. </p><p>Главным нововведением станет то, что <strong>автотаргетинг превратится в обязательную настройку для всех создаваемых рекламных кампаний</strong>. То есть при формировании любой новой группы объявлений потребуется включить хотя бы одну категорию автоматически подбираемых ключевых слов - целевые, узкие, широкие и так далее. Без автотаргетинга система не разрешит сохранить настройки группы.</p><p>Кроме того, <strong>автоматический подбор фраз будет включен по умолчанию и в уже существующих рекламных кампаниях</strong>. </p><p>Также для автоматически подобранных ключевых слов в режиме ручного управления ставками можно будет включить авторасчет ставок на основе средних показателей по группе.</p><p>В настройках автотаргетинга <strong>появится новая категория "Узкие запросы"</strong>. Она будет содержать более узкоспециализированные и конкретные запросы, которые сейчас входят в группу "Целевые запросы". Такое разделение позволит точнее настраивать охват аудитории.</p><p></p> <a href="https://habr.com/ru/articles/761472/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761472#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 11:21:21 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[яндекс директ]]></category><category><![CDATA[автотаргетинг]]></category><category><![CDATA[контекстная реклама]]></category>
    </item>






  



    <item>
      <title><![CDATA[[Перевод] Observability в Spring Boot 3]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/otus/articles/761334/</guid>
      <link>https://habr.com/ru/companies/otus/articles/761334/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761334</link>
      <description><![CDATA[<p>Отдел Observability Spring уже довольно долго работает над поддержкой наблюдаемости в Spring-приложениях, и мы рады сообщить вам, что в Spring Framework 6 и Spring Boot 3 вы наконец-то увидите результаты этой работы!</p><p></p> <a href="https://habr.com/ru/articles/761334/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761334#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 10:53:02 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category>java spring</category><category>spring boot</category><category>Observability</category>
    </item>


      <item>
      <title><![CDATA[Как оцифровать и автоматизировать разработку, чтобы увеличить пропускную способность и ресурсоемкость производства]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761470/</guid>
      <link>https://habr.com/ru/articles/761470/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761470</link>
      <description><![CDATA[<p>Узкое место разработки — пропускная способность и ресурсоемкость производства. Мы его обошли с помощью сбора данных и автоматизации.</p><p>Когда проектов и сотрудников становится много, то большинство проблем возникает не из-за объемов и сложности задач, а из-за неумения выстраивать и автоматизировать процессы производства. В этом мы убедились на собственном опыте.</p><p></p> <a href="https://habr.com/ru/articles/761470/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761470#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 10:35:20 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[разработка]]></category><category><![CDATA[разработка сайтов]]></category><category><![CDATA[управление разработкой]]></category><category><![CDATA[управление проектами]]></category><category><![CDATA[управление командой]]></category><category><![CDATA[php]]></category><category><![CDATA[веб-разработа]]></category><category><![CDATA[web-разработка]]></category><category><![CDATA[e-commerce]]></category><category><![CDATA[e-commerce разработка]]></category>
    </item>






  



    <item>
      <title><![CDATA[[Перевод] Как Instagram увеличился до 14 миллионов пользователей всего с тремя инженерами]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761464/</guid>
      <link>https://habr.com/ru/articles/761464/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761464</link>
      <description><![CDATA[<p>Простыми словами про руководящие принципы и стек технологий</p><p>Instagram увеличил количество пользователей с <strong>0 до 14 миллионов всего за год</strong>, с октября 2010 по декабрь 2011 года. Они сделали это всего с <strong>тремя инженерами</strong>.</p><p>Они сделали это, следуя 3 ключевым принципам и имея надежный технологический стек.</p><p></p> <a href="https://habr.com/ru/articles/761464/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761464#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 10:21:49 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category>архитектура</category><category>django</category><category>redis</category><category>memcached</category><category>munin</category><category>sentry</category><category>gearman</category><category>pingdom</category><category>nginx</category><category>gunicorn</category>
    </item>


  



    <item>
      <title><![CDATA[[Перевод] Почему мой любимый API — это файл zip на сайте Европейского центрального банка]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761466/</guid>
      <link>https://habr.com/ru/articles/761466/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761466</link>
      <description><![CDATA[<p>Когда был максимальный курс доллара к евро?</p><p>Вот небольшая программа, вычисляющая это:</p><p><code>curl -s https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip \ | gunzip \ | sqlite3 -csv ':memory:' '.import /dev/stdin stdin' \   "select Date from stdin order by USD asc limit 1;"</code></p><p>Результат:&nbsp;<code>2000-10-26</code>. (Можете попробовать запустить её самостоятельно.)</p><p></p> <a href="https://habr.com/ru/articles/761466/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761466#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 10:16:18 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category>zip</category><category>csv</category><category>обмен данными</category><category>преобразование данных</category><category>командная строка</category>
    </item>


      <item>
      <title><![CDATA[История компьютерных стратегий. Часть 10. «Age of Mythology»: древние боги, шогготы и рептилоиды в одном флаконе]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/ruvds/articles/761192/</guid>
      <link>https://habr.com/ru/companies/ruvds/articles/761192/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761192</link>
      <description><![CDATA[<a href="https://habr.com/ru/company/ruvds/blog/761192/"><div style="text-align:center;"><img src="https://habrastorage.org/webt/2s/s-/ye/2ss-yetshrwvekayyolmg75nbpu.jpeg"></div></a><br>
Успех первой <a href="https://habr.com/ru/companies/ruvds/articles/756830/">«Age of Empires»</a> сподвиг её создателей из Ensemble Studios развивать тему исторических RTS дальше. Следом появилась посвящённая средневековью «Age of Empires II», ставшая главным хитом всей серии и по сей день имеющая массу поклонников и активных игроков. Однако не всё было так линейно. В недрах студии-создательницы возникло желание поэкспериментировать с концепцией, сделать что-то похожее, но при этом совсем иное. Это стремление не породило мегахитов и прорывов — но оставило в истории RTS такое яркое и запоминающееся явление, как «Age of Mythology» <a href="https://habr.com/ru/articles/761192/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761192#habracut">Читать дальше &rarr;</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 10:00:01 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[ruvds_статьи_выходного_дня]]></category><category><![CDATA[игры и игровые приставки]]></category><category><![CDATA[старые игры]]></category><category><![CDATA[стратегические игры]]></category><category><![CDATA[игры]]></category><category><![CDATA[компьютерные игры]]></category>
    </item>






      <item>
      <title><![CDATA[Предельный анализ распределения простых чисел, и допуск к решению задачи равенство классов p и Np]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761460/</guid>
      <link>https://habr.com/ru/articles/761460/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761460</link>
      <description><![CDATA[<p>Монография представляет собой исследовательскую работу, посвященную решению одной из важных математических задач, поставленных институтом Клэя, а именно задачи равенства классов P и NP. В ней представлены новые теоремы и концепции, разработанные автором в областях теории чисел и теории алгоритмов. Монография претендует на фундаментальную новизну своего математического введения, учитывая предшествующие работы других математиков, а также до актуальные математические публикации.</p> <a href="https://habr.com/ru/articles/761460/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761460#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 09:35:15 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[задача тысячелетия]]></category><category><![CDATA[простые числа]]></category><category><![CDATA[методы оптимизации]]></category><category><![CDATA[теория чисел]]></category><category><![CDATA[улучшение навыков]]></category><category><![CDATA[программные ошибки]]></category><category><![CDATA[вычисления]]></category><category><![CDATA[вычислительная сложность]]></category><category><![CDATA[вычислительная математика]]></category>
    </item>






      <item>
      <title><![CDATA[Ноутбуков со складными экранами стало больше: 17-дюймовый 3 в 1 девайс от HP и его ближайшие конкуренты]]></title>
      <guid isPermaLink="true">https://habr.com/ru/companies/ru_mts/articles/761456/</guid>
      <link>https://habr.com/ru/companies/ru_mts/articles/761456/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761456</link>
      <description><![CDATA[<p>Похоже на то, что устройства с гибкими экранами всё же смогли заполучить свою часть рынка. Телефонов с такими дисплеями сейчас много — каждый более-менее крупный производитель уже выпустил подобный девайс. А сейчас аналогичный тренд наблюдается и среди разработчиков ноутбуков. На днях HP представила весьма интересный девайс, способный заменить планшет, настольный ПК и ноутбук. Правда, стоит он столько, что хватит на все три девайса и останется ещё на дорогой смартфон или даже парочку. Давайте посмотрим на это чудо техники.</p><p></p> <a href="https://habr.com/ru/articles/761456/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761456#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 09:25:24 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[ноутбуки]]></category><category><![CDATA[настольные компьютеры]]></category><category><![CDATA[гаджеты]]></category><category><![CDATA[компьютерное железо]]></category><category><![CDATA[гибкий экран]]></category><category><![CDATA[hp]]></category>
    </item>






      <item>
      <title><![CDATA[Как работает внутриигровая экономика]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761454/</guid>
      <link>https://habr.com/ru/articles/761454/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761454</link>
      <description><![CDATA[<p>Практически каждый из нас покупал себе какой-либо внутриигровой контент в любимой игре. Оказывается, за этим стоит не только целая индустрия разработки, законодательство и патенты, но еще и живой интерес исследователей. </p><p></p> <a href="https://habr.com/ru/articles/761454/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761454#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 09:07:22 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[видео игры]]></category>
    </item>






      <item>
      <title><![CDATA[Ожидания в вакансии QA Engineer: Знакомство с JSON, REST и Типами запросов]]></title>
      <guid isPermaLink="true">https://habr.com/ru/articles/761452/</guid>
      <link>https://habr.com/ru/articles/761452/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761452</link>
      <description><![CDATA[<p>Одним из таких ключевых ожиданий со стороны работодателей является знание JSON, REST и типов запросов HTTP. В этой статье мы рассмотрим, почему это важно и какие преимущества это приносит как для специалистов, так и для компаний.</p><p></p> <a href="https://habr.com/ru/articles/761452/?utm_source=habrahabr&amp;utm_medium=rss&amp;utm_campaign=761452#habracut">Читать далее</a>]]></description>
      
      <pubDate>Sat, 16 Sep 2023 09:05:33 GMT</pubDate>
      <dc:creator></dc:creator>
      
      <category><![CDATA[rest]]></category><category><![CDATA[rest api]]></category><category><![CDATA[json]]></category><category><![CDATA[api]]></category><category><![CDATA[postman]]></category><category><![CDATA[devtools]]></category><category><![CDATA[test]]></category><category><![CDATA[qa]]></category><category><![CDATA[qa testing]]></category><category><![CDATA[qa engineer]]></category>
    </item>












  </channel>
</rss>
'''

print(re.findall('https?://\S+', f))