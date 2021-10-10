from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def main_page():
    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = all_dojos)

@app.route('/create_dojo', methods=['POST'])
def createdojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save_dojo(data)
    return redirect('/')

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html', dojos = dojos)

@app.route('/dojos/<int:dojo_id>')
def ninjas_in_dojo(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    all_ninjas = Ninja.get_all()
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('show_dojo.html', dojo = dojo, all_ninjas = all_ninjas)

