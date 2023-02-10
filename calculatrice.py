from flask import Flask 
import sys
import csv # bibliothèque pour éditer et lire les fichiers csv
import datetime # bibliothèque pour utiliser la date et l'heure
import hashlib # bibliothèque pour utiliser le hachage sha256

app = Flask(__name__)

id_cpt=0

@app.route("/addition/<int:num1>/<int:num2")
def addition(num1,num2):
    if request.method == 'GET':
        add = num1+num2
        ret = "id de la commande : "+id_cpt + " resultat addition :" + add
        return ret
    else:
        return "Methode invalide"    

@app.route("/multiplication/<int:num1>/<int:num2")
def multiplication(num1,num2):
    if request.method == 'GET':
        mul = num1*num2
        ret = "id de la commande : "+id_cpt + " resultat addition :" + mul
        return ret
    else:
        return "Methode invalide"    

@app.route("/soustraction/<int:num1>/<int:num2")
def soustraction(num1,num2):
    if request.method == 'GET':
        sub = num1-num2
        ret = "id de la commande : "+id_cpt + " resultat addition :" + sub
        return ret
    else:
        return "Methode invalide"    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)  