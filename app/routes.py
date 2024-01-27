from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route("/")
@app.route("/index")
def index():
    user = {"name": "Jonathan"}

    posts = [
        {
            "title": "Exploring the Art of Stargazing: A Cosmic Journey",
            "body": "In the hustle and bustle of our daily lives, we often find solace in the serene beauty of the night sky. Stargazing, a timeless activity that has captivated human hearts for centuries, offers a cosmic escape from the ordinary. Let's embark on a mini journey into the enchanting world of stars and constellations.",
        },
        {
            "title": "The Surprising Benefits of Mindful Walking",
            "body": "In our fast-paced lives, finding moments of calm and mindfulness can be a challenge. While meditation and yoga are popular choices, there's another, often overlooked, activity that can bring tranquility to our hectic routines – mindful walking.",
        },
    ]
    return render_template("index.html", user=user, title="Homepage", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login_users():
    form = LoginForm()

    if form.validate_on_submit():
        flash(
            f"Login successful for {form.username}, remember me is {form.remember_me.data}"
        )
        return redirect(url_for("index"))
    return render_template("login.html", form=form)
