from dynaconf import FlaskDynaconf

def init_app(app):
    FlaskDynaconf(app)
    app.config.load_extensions("EXTENSIONS")

    # Há várias formas de carregar a configuração

    # Pode ser diretamente através de variáveis
    # app.config["SECRET_KEY"] = "abacate01"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///delivery.db"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # if app.debug:
    #     app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
    #     app.config["DEBUG_TB_PROFILER_ENABLED"] = True
    #     app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    #     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    # Pode ser através de arquivos de configuração (settings.py)
    # from flask import Flask as app

    # if not app.debug:
    #     import settings

    #     app.config.from_object("settings")
    # else:
    #     import settings_debug

    #     app.config.from_object("settings-debug")

    # Pode também usar from_pyfile com arquivos settings.cfg (que é um formato do python) ou settings.py

    # Outra opção é definir o parâmetro "instance_path=" ao create o app (app = Flask(__name__, instance_path='prod'))
    # e criar pastas na raiz para as instâncias (prod, dev, test, etc.) e colocar o setting.py lá
    # O problema é que a raiz agora para a ser <instance_path>/ e os templates e demais arquivos devem ser copiados
    # para as diversas pastas (duplicados) ou então definir o caminho para eles com 'template_folder'
    # Não é muito prático

    # Pode ser definido também como uma classe, carregada também por app.config.from_object()

    # -------------------------------------------------------------------------------------------------------------------

    # Mas vamos usar o dynaconf, que é uma extensão mais flexível
    # Ele lê de 'env vars', vault server, redis, bancos de dados, etcd, aws param store

    # Ler o The Twelve-Factor App: https://12factor.net/pt_br/
    # criar arquivo .env para cada ambiente (dev, prod, test, staging) e não enviar para o github
    # usar o dynaconf (módulo FlaskDynaconf) para automatizar
    # Ele importa todas as env vars começadas com FLASK_ e retira o prefixo FLASK_
    # O dynaconf normal (sem flask), faz o mesmo para variáveis com prefixo "DYNACONF_"
    # As variáveis podem conter estruturas python: ex: FLASK_VAR={nome: meu_nome, idade: minha_idade}
    # Ao importar: from dynaconf import FlaskDynaconf e fazer FlaskDynaconf(app)
    # podemos fazer: app.config.VAR.nome que vai retornar meu_nome

    # O dynaconf também lê de arquivos, no formato .toml e considera o valor de FLASK_ENV para
    # identificar o grupo que vai usar: development ou production ou outro valor qualquer
    # o grupo default sempre é lido

    # Ela faz uma cascata, primeiro o arquivo, depois a variável de ambiente correspondente
    # se tiver no arquivo (no default) GERA=10 e a variável FLASK_GERA=20, o valor de app.config.GERA será 20
