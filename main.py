from flask import Flask
import random
import requests

app = Flask(__name__)
@app.route("/")
def index():
    return '<h1>Привет,на этом сайте ты увидешь несколько интересных фактов о зависимости</h1>  <a href="/random_fact">Посмотреть случайный факт!</a>'

    
@app.route("/random_fact")
def random_fact():
    facts_list = ['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
        'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
        'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
        'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',
        'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',
        'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
        'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',
        'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.']
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/oorr")
def oorr():    
    aaa = ['орёл','решка']
    return f'<p>{random.choice(aaa)}</p>'

@app.route("/rn")
def rn():    
    return f'<h1>{random.randint(1,9999999999999999999999999999)}</h1>'

@app.route("/pp")
def pp():    
    return '<iframe src="https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/widget/daily/%d0%9c%d0%be%d1%81%d0%ba%d0%b2%d0%b0_%d0%a0%d0%be%d1%81%d1%81%d0%b8%d1%8f_524901?geoloc=fixed&days=3&tempunit=CELSIUS&windunit=METER_PER_SECOND&precipunit=MILLIMETER&coloured=coloured&pictoicon=0&pictoicon=1&maxtemperature=0&maxtemperature=1&mintemperature=0&mintemperature=1&windspeed=0&windspeed=1&windgust=0&winddirection=0&winddirection=1&uv=0&humidity=0&precipitation=0&precipitationprobability=0&spot=0&pressure=0&layout=light"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 162px; height: 250px"></iframe>'


app.run(debug=True)
