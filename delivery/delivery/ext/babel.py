from flask_babelex import Babel

babel = Babel()


@babel.localeselector
def get_locale():
    # if request.args.get("lang"):
    #     session["lang"] = request.args.get("lang")
    # return session.get("lang", "en")
    return "pt_BR"


def init_app(app):
    babel.init_app(app)
    get_locale()

