# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestErgebnisController(BaseTestCase):
    """ErgebnisController integration test stubs"""

    def test_create_ergebnis(self):
        """Test case for create_ergebnis

        
        """
        response = self.client.open(
            '/ergebnisse',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ergebnis(self):
        """Test case for delete_ergebnis

        
        """
        response = self.client.open(
            '/ergebnisse/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ergebnis(self):
        """Test case for get_ergebnis

        
        """
        response = self.client.open(
            '/ergebnisse/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ergebnisse(self):
        """Test case for get_ergebnisse

        
        """
        response = self.client.open(
            '/ergebnisse',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_ergebnis(self):
        """Test case for update_ergebnis

        
        """
        response = self.client.open(
            '/ergebnisse/{id}'.format(id=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
