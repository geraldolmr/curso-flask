from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from delivery.ext.db import db
from delivery.ext.db.models import User, Category, Address, Store
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


class CategoryAdmin(ModelView):
    """Interface admin de categories"""


def init_app(app):
    # Proteger com senha
    # Traduzir para pt_BR
    admin.name = "CodeFoods"
    admin.template_mode = "bootstrap2"
    admin.add_view(CategoryAdmin(Category, db.session))
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(AddressAdmin(Address, db.session))
    admin.init_app(app)


com

