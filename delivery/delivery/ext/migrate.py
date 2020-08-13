from flask_migrate import Migrate
from delivery.ext.db import db, models  # noqa

migrate = Migrate()

# Rodar inicialmente 'flask db init' para criar a pasta 'migrations'
# Depois rodar: flask db migrate -m "initial migrate"
# isso irá salvar a versão inicial da base da base de dados (para fazer alterações depois)

# para fazer alteração da estrutura de alguma tabela do banco
# 1. Fazer as alterações em models.py
# 2. rodar: flask db migrate -m "<msg do que foi alterado>" (é como se fosse um "commit")
#    o migrate cria um arquivo com os passos do que ele vai fazer para atualizar a base (é bom olhar)
#    ele cria uma função upgrade() para migrar e uma downgrade() caso queira fazer 'rollback'
# 3. flask db upgrade (pode usar um 'flask db upgrade --help' para ajuda)

# Importante: ler a observação sobre o sqlite3: https://github.com/miguelgrinberg/Flask-Migrate/issues/61
# O SQLite3 não aceita ALTER TABLE, então tem de fazer um hack, que é o "render_as_batch"

def init_app(app):

    with app.app_context():
        if db.engine.url.drivername == "sqlite":
            print("--> usando sqlite3: flask_migrate com render_as_batch=True")
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    # migrate.init_app(app, db)
