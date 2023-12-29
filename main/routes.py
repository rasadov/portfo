import os
from main import app
from flask import send_from_directory, render_template, request, redirect

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

