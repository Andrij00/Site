from flask import Flask, render_template
from settings import *
from sql_queries import ShopDB

app = Flask(__name__)
db = ShopDB()

app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def index():
    items = db.get_all_items()
    print(items)
    return render_template("index.html",items= items)

@app.route("/item/<item_id>")
def item(item_id):
    item=db.get_item(item_id)
    return render_template("item.html",item= item)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
