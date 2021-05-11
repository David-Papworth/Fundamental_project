from application import app, db
from application.models import Army, Figure
from application.forms import ArmyForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", title="Home-FigureList")

@app.route('/view_army')
def view_army():
    all_armies = Army.query.all()
    output = ""
    return render_template("viewarmy.html", title="Army view", all_armies=all_armies)

@app.route('/add_army', methods=["GET", "POST"])
def add_army():
    form = ArmyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_army = Army(description=form.description.data, name=form.name.data)
            db.session.add(new_army)
            db.session.commit()
            return redirect(url_for('view_army'))
    return render_template('addarmy.html', title="Add a army", form=form)

@app.route('/update_army/<int:id>', methods=["GET", "POST"])
def update_army(id):
    form = ArmyForm()
    army = Army.query.filter_by(id=id).first()
    if request.method == "POST":
        army.description = form.description.data
        army.name = form.name.data
        db.session.commit()
        return redirect(url_for('view_army'))
    return render_template("updatearmy.html", title="Updata Army", form=form, army=army)

@app.route('/delete_army/<int:id>', methods=["GET", "POST"])
def delete_army(id):
    army = Army.query.filter_by(id=id).first()
    db.session.delete(army)
    db.session.commit()
    return redirect(url_for('view_army'))