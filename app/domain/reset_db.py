#!/usr/bin/env python
# coding=utf-8

from manage import db
import domain.model

db.drop_all()
db.create_all()
