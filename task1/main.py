from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
