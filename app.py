
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
@app.route("/main/<name>", methods=['GET', 'POST'])
def index(name):
    if request.method == 'GET':
        return f"<p>Wellcom {name}! Here you can read all information about our company</p>"
    elif request.method == 'POST':
        return request.get_json()



@app.route("/products/-<int:number_of_product>", methods=['GET', 'POST'])
def about(number_of_product):
    if number_of_product <=50:
        return ' Your product is microwafe'
    elif number_of_product >50:
        return 'Your product is phone'
    


if __name__ == "__main__":
    app.run(debug=True)
