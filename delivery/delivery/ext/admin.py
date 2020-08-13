from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView, filters, ajax
from flask_admin.actions import action
from wtforms.validators import DataRequired
from delivery.ext.db import db
from delivery.ext.db.models import User, Category, Address, Store, Items
from flask import flash, Markup

admin = Admin()


class UserAdmin(ModelView):
    """Interface admin de users"""

    # can_edit = False
    # can_create = False
    # can_delete = False

    column_list = ["email", "admin"]

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(User.email, "Domínio", options=(("@gmail", "Gmail"), ("@yahoo", "Yahoo"), ("@aol", "Aol"))),
    ]

    form_args = dict(
        email=dict(validators=[DataRequired()]),
    )

    form_widget_args = {
        'email': {
            'style': 'color:blue;background:yellow',
            'onclick': 'alert("teste")'
        }
    }

    # column_formatters = {"email": lambda v,c,m,p: Markup(f'<b>{m.email.upper()}</b>')}

    @action("toggle_admin", "toggle admin status", "are you sure?")
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f" {len(users)} users successfully changed.")


class CategoryAdmin(ModelView):
    """Interface admin de categories"""


class AddressAdmin(ModelView):
    """Interface admin de categories"""
    # form_ajax_refs = {
    #     'user': {
    #         'fields': ['email', 'admin'],
    #         'page_size': 10
    #     }
    # }

    

class StoreAdmin(ModelView):
    """Interface admin de categories"""

class ItemsAdmin(ModelView):
    """Interface admin de categories"""



def init_app(app):
    # Proteger com senha
    # Traduzir para pt_BR
    admin.name = app.config.get("ADMIN_NAME", "SemNome")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.add_view(CategoryAdmin(Category, db.session))
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(AddressAdmin(Address, db.session))
    admin.add_view(StoreAdmin(Store, db.session))
    admin.add_view(ItemsAdmin(Items, db.session))
    admin.init_app(app)

