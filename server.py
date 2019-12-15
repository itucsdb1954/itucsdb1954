import os
from flask import Flask
from flask_login import LoginManager
import views
from database import Database
from user import User,get_user

lm=LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")


    app.add_url_rule("/", view_func=views.home_page, methods=["GET", "POST"])
    app.add_url_rule("/guide",view_func=views.guide_page)
    app.add_url_rule("/courses", view_func=views.courses_page, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout_page)
    app.add_url_rule("/courses/<int:course_key>", view_func=views.course_page)
    app.add_url_rule("/courses/<int:course_key>/edit",view_func=views.course_edit_page,methods=["GET", "POST"])
    app.add_url_rule("/new-course",view_func=views.course_add_page, methods=["GET","POST"])
    app.add_url_rule("/user", view_func=views.user_page)
    app.add_url_rule("/courses/<int:course_key>/VF_conditions_add",view_func=views.conditionAdding_page,methods=["GET", "POST"])
    app.add_url_rule("/courses/<int:course_key>/VF_conditions_edit",view_func=views.conditionEditing_page,methods=["GET", "POST"])
    app.add_url_rule("/courses/<int:course_key>/VF_conditions",view_func=views.conditions_page,methods=["GET", "POST"])
    app.add_url_rule("/Register",view_func=views.register_page,methods=["GET", "POST"])

    lm.init_app(app)
    lm.login_view = "home_page"

    url="postgres://eqxokbcjiseyei:3bc64a91ec58aab73ba937f8652296acf5ab9b2671aba9deb9420dfbe25e5cf6@ec2-46-137-188-105.eu-west-1.compute.amazonaws.com:5432/d1f2968dk53lod"
    db = Database(url)
    app.config["db"] = db

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
