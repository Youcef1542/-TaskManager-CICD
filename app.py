from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Installer Docker", "status": "terminee"},
    {"id": 2, "title": "Configurer GitHub Actions", "status": "en_cours"},
    {"id": 3, "title": "Tester le pipeline", "status": "a_faire"}
]


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)