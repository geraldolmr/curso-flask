import click
from delivery.ext.db import db, models

# precisa desse import do models para que as tabelas sejam criadas
# mesmo que ele não seja usado explicitamente
# o models foi movido de site/ para db/
# from delivery.ext.site import models

def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """adiciona novo usuario"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

    @app.cli.command()
    @click.option("--table", "-t")
    def list_table(table):
        """List all lines from a table"""
        try:
            _table = getattr(models, table)
            rows = _table.query.all()
            # {_table.__table__.name}
            click.echo(f'Rows from table "{table}": {rows}')
        except AttributeError:
            click.echo(f'Table "{table}" not found.')
