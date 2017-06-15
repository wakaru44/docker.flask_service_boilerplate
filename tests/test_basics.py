
# -*- coding: utf-8 -*-

import os
import tempfile
import unittest
import myapp  # This is imported thanks to the magic in __init__
import json

class ThisApiTestCase(unittest.TestCase):
    def setUp(self):
        thisapi.app.config['TESTING'] = True
        self.app = myapp.app.test_client()
        with myapp.app.app_context():
            pass # just kept here as reminder

    def tearDown(self):
        pass
