import random
import requests
import csv
import pandas as pd
from faker import Faker
from flask import Flask
from database_handler import execute_query
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route("/")
def hello_world():
    home_page = f"<p> Генератор паролів - /generate_password <p>" \
                f"<p> Середнє значення csv - /calculate_average_csv </p>" \
                f"<p> Середнє значення pandas - /calculate_average_pandas </p>" \
                f"<p> Генератор данних студентів - /generate_students </p>" \
                f"<p> Курс бітка - /bitcoin_rate </p>"

    return home_page


@app.route('/generate_password')
def generate_password():
    pass_len = random.randint(10, 20)
    ascii_lowercase = (97, 122)
    ascii_uppercase = (65, 90)
    int_symbol = (48, 57)
    special_symbols = (33, 47)

    all_chars = [ascii_lowercase, ascii_uppercase, int_symbol, special_symbols]
    base_pass = []

    counter = 0
    while counter < pass_len:
        if counter < len(all_chars):
            base_pass.append(chr(random.randint(*all_chars[counter])))
            counter += 1
        else:
            random_symbol = random.choice(all_chars)
            base_pass.append(chr(random.randint(*random_symbol)))
            counter += 1

    random.shuffle(base_pass)
    user_password = ''.join(base_pass)
    return f'user password: {user_password}'


@app.route('/calculate_average_csv')
def calculate_average_csv():
    with open('hw.csv', 'r') as csv_file_object:
        csv_data = list(csv.reader(csv_file_object))

    height_lst = []
    weight_lst = []
    for line in csv_data[1:]:
        height_lst.append(float(line[1]))
        weight_lst.append(float(line[2]))

    average_high = round(sum(height_lst) / len(height_lst))
    average_weight = round(sum(weight_lst) / len(weight_lst))

    return f'<p>Average high = "{average_high}"<p>' \
           f'<p>Average weight = "{average_weight}"<p>'


@app.route('/calculate_average_pandas')
def calculate_average_pandas():
    with open('hw.csv', 'r') as csv_file_object:
        csv_data = pd.read_csv(csv_file_object)

    average_high = round(csv_data[' Height(Inches)'].mean())
    average_weight = round(csv_data[' Weight(Pounds)'].mean())

    return f'Average high = "{average_high}" \n' \
           f'Average weight = "{average_weight}"'


@app.route('/generate_students')
@use_kwargs(
    {
        'limit': fields.Int(
            missing=5,
            validate=[validate.Range(min=1, max=1000)],
        )
    },
    location='query'
)
def generate_students(limit):
    faker_data = Faker()
    students_list = [
        ['First_name', 'Last_name', 'Email', 'Password', 'Birthday']
    ]
    counter = 0
    while counter < limit:
        students_list.append([
            faker_data.first_name(),
            faker_data.last_name(),
            faker_data.email(),
            faker_data.password(),
            str(faker_data.date_of_birth(minimum_age=18, maximum_age=23))
        ])
        counter += 1

    with open('students.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(students_list)

    return students_list


@app.route('/bitcoin_rate')
@use_kwargs(
    {
        'currency': fields.Str(
            load_default='USD',
        ),
        'count': fields.Int(
            missing=1,
        )
    },
    location='query'

)
def get_bitcoin_value(currency, count):
    response_rate = requests.get(f'https://bitpay.com/rates/{currency}').json()
    response_currencies = requests.get('https://bitpay.com/currencies').json()

    if 'error' in response_rate:
        return response_rate['error']

    currency_rate = response_rate['data']['rate']

    currency_symbol = None
    for elem in response_currencies.get('data'):
        if currency == elem['code']:
            currency_symbol = elem['symbol']

    return f'Currency: "{currency}" | rate: "{currency_rate * count}" | symbol: "{currency_symbol}"'


@app.route('/order-price')
@use_kwargs(
    {
        'country': fields.Str(
            load_default=None
        )
    },
    location='query'
)
def order_price(country):
    query = 'SELECT BillingCountry AS Country, round(sum(UnitPrice * Quantity),0) AS Sales' \
            ' FROM (SELECT UnitPrice, Quantity, BillingCountry ' \
            'FROM invoice_items ' \
            'JOIN Invoices ON invoice_items.InvoiceId = invoices.InvoiceId)'

    if country:
        query += f' WHERE BillingCountry = "{country}"'
    else:
        query += 'GROUP BY BillingCountry'

    record = execute_query(query)
    return record


@app.route('/get-all-info-about-track')
@use_kwargs(
    {
        'track_ID': fields.Int(
            missing=None
        )
    },
    location='query'
)
def get_all_info_about_track(track_ID):
    query = 'SELECT * ' \
            'FROM tracks ' \
            'LEFT JOIN genres ON tracks.GenreId = genres.GenreId ' \
            'LEFT JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId ' \
            'LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId ' \
            'LEFT JOIN artists ON albums.ArtistId = artists.ArtistId ' \
            'LEFT JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId ' \
            'LEFT JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId'

    if track_ID:
        query += f' WHERE tracks.TrackId = {track_ID}'

    record = execute_query(query)

    return record


@app.route('/get-all-time-of-all-tracks')
def get_all_time_of_all_tracks():
    query = 'SELECT sum(tracks.Milliseconds) as MillisecondsTime ' \
            'FROM albums ' \
            'LEFT JOIN tracks ON albums.AlbumId = tracks.AlbumId '
    record = execute_query(query)

    return f'Тривалість всіх треків в альбомах {record[0][0] / 3_600_000}'


@app.route('/stats-by-city')
@use_kwargs(
    {
        'genre': fields.Str(
            required=True
        )
    },
    location='query'
)
def stats_by_city(genre):
    query = 'SELECT max(CountCity), City ' \
            'FROM (SELECT count(*) AS CountCity, BillingCity AS City ' \
            'FROM genres ' \
            'LEFT JOIN tracks on genres.GenreId = tracks.GenreId ' \
            'LEFT JOIN invoice_items on tracks.TrackId = invoice_items.TrackId ' \
            'LEFT JOIN invoices on invoice_items.InvoiceId = invoices.InvoiceId ' \
            'WHERE invoices.BillingCity IS NOT null AND genres.Name = ? ' \
            'GROUP BY BillingCity)'

    record = execute_query(query, args=(genre,))

    return record if record[0] != (None, None) else f'Genre "{genre}" not found'


app.run(debug=True)
