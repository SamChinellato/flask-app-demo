#!/usr/bin/env python
import os
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        expected_text = "Welcome"
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray("{}".format(expected_text), 'utf-8'), rv.data)

    def test_hello_hello(self):
        expected_text = "Hello from Flask"
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray("{}".format(expected_text), 'utf-8'), rv.data)

    def test_hello_name(self):
        name = 'Sam'
        rv = self.app.get('/hello/{}'.format(name))
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray("{}".format(name), 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()