#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

from flask import render_template, session, redirect, url_for
from flask_login import login_required

from . import main
from .forms import NameForm
from .. import db
from ..domain.model import User, Permission
from ..domain.decorators import permission_required, admin_required


@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    '''
    return render_template('index.html') 
            #form=form, name=session.get('name'),
            #known = session.get('known'))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For aministrators"

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment"
