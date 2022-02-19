from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def main_page(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        return render_template("training.html",
                               title="Инженерные тренажёры",
                               image=url_for("static", filename="img/engineer.jpg"))
    else:
        return render_template("training.html",
                               title="Научные симуляторы",
                               image=url_for("static", filename="img/science.jpg"))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
