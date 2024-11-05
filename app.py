from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clean_csv', methods=['POST'])
def clean_csv():
    # Code pour lancer le script clean_csv
    # Par exemple, vous pouvez appeler une fonction ou exécuter un script externe ici
    return "Le script clean_csv a été lancé."

if __name__ == "__main__":
    app.run()