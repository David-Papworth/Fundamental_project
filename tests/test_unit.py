import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Army, Figure

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
        SECRET_KEY='SECRET_KEY',
        WTF_CSRF_ENABLED=False,
        DEBUG=True,
        )
        return app

    def setUp(self):
        db.create_all()
        test_army = Army(name='Army 1', description="This is my main army")
        test_figure = Figure(name='Figure 1', number_of_models=8, faction='Space Marines' ,army_id=test_army.id)
        db.session.add(test_army)
        db.session.add(test_figure)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_figure_get(self):
        response = self.client.get(url_for('add_figure'))
        self.assertEqual(response.status_code, 200)

    def test_update_figure_get(self):
        response = self.client.get(url_for('update_figure', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_figure_get(self):
        response = self.client.get(url_for('delete_figure', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_view_army_get(self):
        response = self.client.get(url_for('view_army'))
        self.assertEqual(response.status_code, 200)

    def test_add_army_get(self):
        response = self.client.get(url_for('add_army'))
        self.assertEqual(response.status_code, 200)

    def test_update_army_get(self):
        response = self.client.get(url_for('update_army', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_army_get(self):
        response = self.client.get(url_for('delete_army', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_army(self):
        response = self.client.get(url_for('view_army'))
        self.assertIn(b"This is my main army", response.data)
        self.assertIn(b"Army 1", response.data)

class TestCreate(TestBase):
    def test_create_army(self):
        response = self.client.post(url_for('add_army'),
        data=dict(name='new army', description="This is my new army"),
        follow_redirects=True
        )
        self.assertIn(b"This is my new army", response.data)
        self.assertIn(b"new army", response.data)

class TestUpdate(TestBase):
    def test_update_army(self):
        response = self.client.post(url_for('update_army', id=1),
        data=dict(name="Update army", description="This is a updated a army"),
        follow_redirects=True
        )
        self.assertIn(b"This is a updated a army", response.data)
        self.assertIn(b"Update army", response.data)

class TestDelete(TestBase):
    def test_delete_army(self):
        response = self.client.get(url_for('delete_army', id=1),
        follow_redirects=True
        )
        self.assertNotIn(b"This is my main army", response.data)
        self.assertNotIn(b"Army 1", response.data)

class TestRead1(TestBase):
    def test_read_army(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Figure 1", response.data)
        self.assertIn(b"8", response.data)
        self.assertIn(b"Space Marine", response.data)
        self.assertIn(b"1", response.data)
        

class TestCreate1(TestBase):
    def test_create_figure(self):
        response = self.client.post(url_for('add_figure'),
        data=dict(name='Figure 2', number_of_models=9, faction='Space Marines', army=1),
        follow_redirects=True
        )
        self.assertIn(b"Figure 2", response.data)
        self.assertIn(b"9", response.data)
        self.assertIn(b"Space Marine", response.data)
        self.assertIn(b"1", response.data)

class TestUpdate1(TestBase):
    def test_update_figure(self):
        response = self.client.post(url_for('update_figure', id=1),
        data=dict(name="Update figure", number_of_models=9, faction='Space Marines', army_id=1),
        follow_redirects=True
        )
        self.assertIn(b"Update figure", response.data)
        self.assertIn(b"9", response.data)
        self.assertIn(b"Space Marine", response.data)
        self.assertIn(b"1", response.data)

class TestDelete1(TestBase):
    def test_delete_figure(self):
        response = self.client.get(url_for('delete_figure', id=1),
        follow_redirects=True
        )
        self.assertNotIn(b"Figure 1", response.data)
        self.assertNotIn(b"8", response.data)
        self.assertNotIn(b"Space Marine", response.data)