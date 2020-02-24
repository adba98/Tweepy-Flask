from flask import Flask,render_template
from flask_restful import Api
import twetools as tt
import analisis as a

app = Flask(__name__)
api = Api(app)
posts = []

@app.route("/")
def index():
    return render_template("index.html", 
    gr1  = a.histograma(),
    gr2 = a.grap(),
    gr3 = a.grap2(),
    gr4 = a.grap3(),
    media = a.media(), 
    moda = a.moda(),
    mediana = a.media(),
    medianaAgr = a.medianaAgrup(),
    longmedia = a.longmedia())

@app.route("/g/<string:slug>/")
def show_post(slug):
    tt.buscPalabra(slug)
    tt.generar(slug)
    return render_template("generar.html", slug_title=slug)

if __name__ == '__main__':
    app.run(debug = True, port =8000)