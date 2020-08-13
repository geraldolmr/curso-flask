
def init_app(app):
    @app.before_first_request
    def init_everything():
        print('--> @app.before_first_request - isso roda sempre antes do primeiro request da app!!!')