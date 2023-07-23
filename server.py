from flask import Flask, render_template, send_from_directory, request, redirect
import os
import csv

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def my_home():
    return render_template('index.html')


sites = os.listdir('templates')


@app.route('/<name>')
def any(name=None):
    if name in sites:
        return render_template(name, name=name)
    else:
        return render_template('404.html')


def write_to_database(data):
    with open('database.txt', 'a') as storage:
        for k in data:
            storage.write(k + ": " + data[k] + ' | ')
        storage.write('\n')
        storage.write('\n')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as storage2:
        csv_writer = csv.writer(storage2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow((data["name"], data["email"],
                            data["subject"], data["message"]))


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # try:
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('thankyou.html')
        # except:
        #     return "couldn't save to data base"
    return 'something went wrong'
