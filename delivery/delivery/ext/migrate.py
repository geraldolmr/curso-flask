from flask_migrate import Migrate
from delivery.ext.db import db, models  # noqa

migrate = Migrate()

# Rodar inicialmente 'flask db init' para criar a pasta 'migrations'
# Depois rodar: flask db migrate -m "initial migrate"
# isso irá salvar a versão inicial base da base de dados (para fazer alterações depois)

# para fazer alteração da estrutura de alguma tabela do banco
# 1. Fazer as alterações em models.py
# 2. rodar: flask db migrate -m "<msg do que foi alterado>" (é como se fosse um "commit")
#    o migrate cria um arquivo com os passos do que ele vai fazer para atualizar a base (é bom olhar)
#    ele cria uma função upgrade() para migrar e uma downgrade() caso queira fazer 'rollback'
# 3. flask db upgrade (pode usar um 'flask db upgrade --help' para ajuda)


def init_app(app):
    migrate.init_app(app, db)
