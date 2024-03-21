from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login/")
def login():
    return render_template('login.html')

@app.route("/admin_index/")
def admin_index():
    return render_template('admin_index.html')

@app.route("/perfiluser/")
def perfiluser():
    return render_template('perfiluser.html')

@app.route("/registro_admin/")
def registro_admin():
    return render_template('registro_admin.html')

@app.route("/registro/")
def registro():
    return render_template('registro.html')

if __name__=='__main__':
    app.run(debug=True , port=8000)

# def pagina_no_encontrada(error):
#     return redirect(url_for('index'))
