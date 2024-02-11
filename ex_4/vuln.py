from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <form action="/transfer" method="post">
                    <input type="text" name="amount" />
                    <input type="text" name="toaccount" />
                    <input type="submit" value="Transfer" />
                </form>
            </body>
        </html>
    '''

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    toaccount = request.form['toaccount']

    # Vulnérabilité CSRF : absence de vérification de l'origine de la requête
    # Un attaquant peut créer une page malveillante avec un formulaire POST
    # qui soumet automatiquement des fonds vers un compte indésirable

    # Transfert des fonds...

    return f"Transfert de {amount} vers {toaccount} effectué !"

if __name__ == '__main__':
    app.run(debug=True)