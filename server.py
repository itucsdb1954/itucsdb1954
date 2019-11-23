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
    app.add_url_rule("/courses", view_func=views.courses_page, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout_page)
    app.add_url_rule("/courses/<int:course_key>", view_func=views.course_page)
    app.add_url_rule("/courses/<int:course_key>/edit",view_func=views.course_edit_page,methods=["GET", "POST"])
    app.add_url_rule("/new-course",view_func=views.course_add_page, methods=["GET","POST"])

    lm.init_app(app)
    lm.login_view = "home_page"

    db = Database()
    app.config["db"] = db

    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
