# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase
from flask import current_app
from flask_diamond import models


class GeneralTestCase(TestCase):
    def create_app(self):
        from flask_diamond import create_app, db
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.db = db
        return self.app

    def setUp(self):
        self.db.drop_all()
        self.db.create_all()
        models.User.add_system_users()
        current_app.logger.debug("setup complete")

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
