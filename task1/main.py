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


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    data = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
            'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
            'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']

    return render_template("list_prof.html", title="Список профессий", list_prof=data, list_type=list_type)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {'title': 'Автоматический ответ', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
            'profession': ' штурман марсохода', 'sex': 'make', 'motivation': 'Всегда мечтал застрять на Марсе!',
            'ready': 'True'}

    return render_template("auto_answer.html", **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
