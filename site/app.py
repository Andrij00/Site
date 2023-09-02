from flask import Flask, render_template, request, flash, redirect, url_for
from settings import *
from sql_queries import ShopDB

app = Flask(__name__)
db = ShopDB()

app.config['SECRET_KEY'] = SECRET_KEY
@app.route("/")
def index():
    categories = db.get_categories()
    items = db.get_all_items()
    print(items)
    return render_template("index.html",items= items,categories = categories)

@app.route("/category/<id>")
def category(id):
    categories = db.get_categories()
    items = db.get_category_items(id)
    return render_template("category.html", items=items, categories = categories)

@app.route("/order/<item_id>", methods = ["GET", "POST"])
def order(item_id):
    categories = db.get_categories()
    item = db.get_item(item_id)
    if request.method == 'POST':
        try:
            db.add_order(item[0], 
                        request.form["name"],
                        request.form["phone"],
                        request.form["email"],
                        request.form["city"],
                        request.form["address"], 
                        item[5],
                        request.form["amount"])
            flash("Додано замовлення!", "alert-light") #надсилаємо швидкі сповіщення у браузер
            return redirect(url_for('index')) #перенаправляємо на головну сторінку
        except:
            flash("Помилка оформлення замовлення!", "alert-danger") #надсилаємо швидкі сповіщення у браузер

    return render_template("order.html", item=item, categories = categories)
@app.route("/item/<item_id>")
def item(item_id):
    item=db.get_item(item_id)
    return render_template("item.html",item= item)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
