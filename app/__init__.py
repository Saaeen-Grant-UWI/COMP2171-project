from flask import Flask

def createApp():
    app = Flask(__name__)
    app.secret_key = "secret_key"

    from .routes import routes

    app.register_blueprint(routes, url_prefix='/')

    return app