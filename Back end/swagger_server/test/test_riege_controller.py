# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestRiegeController(BaseTestCase):
    """RiegeController integration test stubs"""

    def test_create_riege(self):
        """Test case for create_riege

        
        """
        response = self.client.open(
            '/riegen',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_riege(self):
        """Test case for delete_riege

        
        """
        response = self.client.open(
            '/riegen/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_riege(self):
        """Test case for get_riege

        
        """
        response = self.client.open(
            '/riegen/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_riegen(self):
        """Test case for get_riegen

        
        """
        response = self.client.open(
            '/riegen',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_riege(self):
        """Test case for update_riege

        
        """
        response = self.client.open(
            '/riegen/{id}'.format(id=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
