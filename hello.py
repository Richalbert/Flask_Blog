# hello.py

from flask import Flask     # importation de la classe Flask du packege flask

app = Flask(__name__)       # creation de l'instance de l'application Flask

@app.route('/')             # decorateur qui transforme la fonction Pythion 
def hello():                # en fonction d'affichage Flask et qui transforme
    return '<h1>Hello</h1>' # le retour de la fonction en une reponse HTTP

# from app import app
# if __name__ == '__main__':
#     app.run(debug=True)


# Commande pour lancer l'application Flask
#    flask --app hello run
#
# ou bien on configure des variables d'environnement suivantes
#    export FLASK_APP=hello
#    flask run
#
# ou export FLASK_APP=hello
#    export FLAK_ENV=development
#    flask run