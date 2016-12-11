#!/usr/bin/env python
# coding=utf-8

import unittest
from app.domain.model import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'ybp')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'ybp')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verifcation(self):
        u = User(password = 'ybp')
        self.assertTrue(u.verify_password('ybp'))
        self.assertFalse(u.verify_password('lcg'))

    def test_password_salts_are_random(self):
        u = User(password = 'ybp')
        u2 = User(password = 'ybp')
        self.assertTrue(u.password_hash != u2.password_hash)
            
