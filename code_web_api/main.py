
# Imports
from flask import Flask

# Création d'une instance de l'application Flask
app = Flask(__name__)

# Création d'un contexte en paramètre GET sur l'URL /
@app.route("/", methods=["GET"])
def get():
	return "Hello World", 200

# Exécution de l'application
if __name__ == "__main__":
	app.run("0.0.0.0")

