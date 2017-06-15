
# -*- coding: utf-8 -*-

import os
import unittest
import json
import tempfile # helpful to create fake logs, check data, etc
import myapp  # This is imported thanks to the magic in __init__

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        thisapi.app.config['TESTING'] = True
        self.app = myapp.app.test_client()
        with myapp.app.app_context():
            pass # just kept here as reminder

    def tearDown(self):
        pass


class TestRootPath(BasicTestCase):
    def test_simple_get(self):
        rv = self.app.get("/")
        assert "You are at the homepage" in rv.data


class test_something_here(BasicTestCase)
    def setUp(self):
        super(test_something_here, self).setUp()
        # create a fake party
        self.pid="647050"
        self.party_data = {
                'partyid':self.pid,
                "videos":[
                    {"v":"ZZZZ","title":"papayas"},
                    {"v":"AAAA","title":"bananas"},
                ]
        }
        create = self.app.put("add_vid", self.party_data)


    def not_a_test_a_new_party_is_empty(self):
        """test a new party returns an empty party"""
        rv = self.app.get("/v1/get_party.json?pid=999999")
        print rv.data
        assert json.loads(rv.data) is not None
        assert len(json.loads(rv.data)["videos"]) == 0

if __name__ == "__main__":
    unittest.main()
