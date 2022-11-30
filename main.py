from flask import Flask
import random
import csv
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello_world():
    home_page = f"<p> Генератор паролів - /generate_password <p>" \
                f"<p> Середнє значення csv - /calculate_average_csv </p>" \
                f"<p> Середнє значення pandas - /calculate_average_pandas </p>"
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
        csv_data  = pd.read_csv(csv_file_object)

    average_high = round(csv_data[' Height(Inches)'].mean())
    average_weight = round(csv_data[' Weight(Pounds)'].mean())

    return f'Average high = "{average_high}" \n' \
           f'Average weight = "{average_weight}"'


app.run(debug=True)
