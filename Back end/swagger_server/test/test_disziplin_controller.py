# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDisziplinController(BaseTestCase):
    """DisziplinController integration test stubs"""

    def test_get_disziplin(self):
        """Test case for get_disziplin

        
        """
        response = self.client.open(
            '/disziplinen/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_disziplinen(self):
        """Test case for get_disziplinen

        
        """
        response = self.client.open(
            '/disziplinen',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
