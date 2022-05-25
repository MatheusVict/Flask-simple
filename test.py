from flask import Flask, render_template

app = Flask(__name__)

#1° página
#route = link dps da barra
#função = oq quer exibir na página
#templates
@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/festa")
def festa():
    return render_template("festa.html")
@app.route("/convidados/<nome_usuario>")
def usuarios(nome_usuario):
    return nome_usuario
#colocando no ar
if __name__ == "__main__":
    app.run(debug=True)