import click
from delivery.ext.db import db

# precisa desse import para que as tabelas sejam criadas
# mesmo que ele não seja usado explicitamente
from delivery.ext.site import models

def init_app(app):

    # É possível também usar o decorator como uma função e
    # passar a função que executa o comando para o app.cli.command()
    # app.cli.add_command(app.cli.command(func_acao))


    @app.cli.command()
    def create_db():
        """Este comando inicializa o banco de dados"""
        db.create_all()
        click.echo("db criado")

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """add new user"""
        user = models.User(email=email, passwd=passwd, admin=admin)
        db.session.add(user)
        db.session.commit()
        click.echo(f"user {user.id} created")

