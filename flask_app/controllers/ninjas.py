from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/create_ninja', methods=['POST'])
def createninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.save_ninja(data)
    print("NINJA DATA!!!!!!!!", data)
    return redirect('/')