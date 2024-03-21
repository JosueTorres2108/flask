from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    # return "solo millos"

if __name__=='__main__':
    app.run(debug=True , port=8000)

# def pagina_no_encontrada(error):
#     return redirect(url_for('index'))
