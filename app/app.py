from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.json  # Récupérer les données envoyées par JavaScript
    return jsonify({"message": "Données reçues", "data": data})


if __name__ == "__main__":
    app.run(ssl_context=("/certs/cert.pem", "/certs/key.pem"), host="0.0.0.0", port=8443, debug=True)
