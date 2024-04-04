from flask import render_template
from app import app
from models import admin , company , users

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/admin_index/")
def admin_index():
    return render_template('admin_index.html')

@app.route("/registro_admin/")
def registro_admin():
    return render_template('registro_admin.html')


@app.route("/registro/")
def registro():
    return render_template('registro.html')

if __name__=='__main__':
    app.run(debug=True, port=8000)