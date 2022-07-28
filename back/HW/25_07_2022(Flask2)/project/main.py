import psycopg2, random
from data.data import *
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify

app = Flask(__name__)


# app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index():
    code = request.cookies.get('cookie')
    print(code)
    code_decode = (code.split("/"))[0]
    email = (code.split("/"))[1]
    if code_decode == "time":
        return redirect(url_for('home', variable=email))
    else:
        return render_template('log.html')


@app.route("/log")
def log():
    code = request.cookies.get('cookie')
    print(code)
    code_decode = (code.split("/"))[0]
    email = (code.split("/"))[1]
    if code_decode == "time":
        return redirect(url_for('home', variable=email))

    # return username
    return render_template('log.html')


@app.route('/log', methods=['POST'])
def log_in():
    name = request.form['name']
    email = request.form['email']
    passwords = request.form['password']
    soll = random.randint(10, 99)
    rand = random.randint(1000, 9999) + soll

    name_code = name + str(rand)

    code_cookie = "time/" + name_code
    res = make_response("Setting a cookie")
    res.set_cookie('cookie', code_cookie,
                   max_age=60 * 60 * 24 * 365 * 2)  # первое значение название второе его значение а третье время

    print(name)
    print(email)
    print(passwords)
    print(name_code)

    # connect to exist database

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO public.users( id, name, email, password, code) VALUES (DEFAULT, '{name}', '{email}', '{passwords}', '{name_code}');""")

    print("[INFO] Data was succefully inserted")
    return res


# @app.route('/home')
# @app.route('/home/<variable>', methods=['GET', 'POST'])
# def home(variable):
#     return render_template('home.html')
# , 'POST'
@app.route('/home/<variable>', methods=['GET'])
def home(variable):
    # print("[INFO] Data was succefully inserted")

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT title, text, data, done, id  FROM public.tasks WHERE "user" = '{variable}' ;""")

        result = cursor.fetchall()
    # result = [[variable] + l for l in result]
    # for key, value in result.iteritems()
    res = []
    for x in result:
        x = list([x, [variable]])
        res.append(x)
    return render_template('home.html', variable=variable, list_data=res)


@app.route('/home_post', methods=['GET', 'POST'])
def home_post():
    variable = request.form['variable']
    data_one = request.form['data_one']
    data_two = request.form['data_two']
    data_three = request.form['data_three']
    data_four = request.form['data_four']
    data_five = request.form['data_five']
    data_six = request.form['data_six']

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE public.tasks SET done=True WHERE "user" = '{data_six}' and "id" = {data_five};""")

    # return data_five
    return redirect(url_for('home', variable=variable))


@app.route('/home_delete', methods=['POST'])
def home_delete():
    variable = request.form['variable']
    data_one = request.form['data_one']
    data_two = request.form['data_two']
    data_three = request.form['data_three']
    data_four = request.form['data_four']
    data_five = request.form['data_five']
    data_six = request.form['data_six']

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            f"""DELETE FROM public.tasks WHERE "user" = '{data_six}' and "id" = {data_five};""")

    return redirect(url_for('home', variable=variable))


@app.route('/home_update', methods=['POST', 'GET'])
def home_update():
    variable = request.form['variable']
    data_one = request.form['data_one']
    data_two = request.form['data_two']
    data_three = request.form['data_three']
    data_four = request.form['data_four']
    data_five = request.form['data_five']
    data_six = request.form['data_six']

    # return redirect(
    #     url_for('task_update'))
    return render_template('task_update.html', variable=variable, data_one=data_one, data_two=data_two, data_three=data_three,
                data_four=data_four, data_five=data_five, data_six=data_six)


@app.route('/task_update', methods=['POST'])
def task_update():
    variable = request.form['variable']
    data_one = request.form['title']
    data_two = request.form['text']
    data_three = request.form['data']
    data_four = request.form['data_four']
    data_five = request.form['data_five']
    data_six = request.form['data_six']

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE public.tasks SET title = '{data_one}', text = '{data_two}', data = '{data_three}' WHERE "user" = '{data_six}' 
            and "id" = {data_five};""")

    return redirect(url_for('home', variable=variable))


@app.route('/task/<variable>', methods=['GET'])
def task(variable):
    return render_template('task.html', variable=variable)


@app.route('/task/<variable>', methods=['POST'])
def new_task(variable):
    title = request.form['title']
    text = request.form['text']
    data = request.form['data']

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO public.tasks(id, title, text, data, "user", done) VALUES (DEFAULT, '{title}', '{text}', '{data}', '{variable}', DEFAULT);""")

    print("[INFO] Data was succefully inserted")

    if request.method == 'POST':
        return redirect(url_for("home", variable=variable))

#
# name = "Mansur"
#
#
# @app.route("/about_through_the_link")
# def about_through_the_link(name1=name):
#     name1 = name1
#     return render_template('about_through_the_link.html', name=name1)
#
# @app.route("/about_directly")
# def about_directly():
#     return f"<h1>Hello, {name}</h1>"

# if __name__ == "__main__":
# 	hello_world()
