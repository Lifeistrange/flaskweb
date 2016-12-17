#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

from flask import render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user

from . import main
from .forms import NameForm, EditProfileForm
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

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user, current_user=current_user)

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

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

