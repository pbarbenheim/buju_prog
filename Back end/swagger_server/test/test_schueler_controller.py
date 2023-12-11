# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.schueler import Schueler  # noqa: E501
from swagger_server.models.schueler_create_payload import SchuelerCreatePayload  # noqa: E501
from swagger_server.models.schueler_update_payload import SchuelerUpdatePayload  # noqa: E501
from swagger_server.models.schuelers import Schuelers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSchuelerController(BaseTestCase):
    """SchuelerController integration test stubs"""

    def test_create_schueler(self):
        """Test case for create_schueler

        
        """
        body = SchuelerCreatePayload()
        response = self.client.open(
            '/schueler',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_schueler(self):
        """Test case for delete_schueler

        
        """
        response = self.client.open(
            '/schueler/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schueler(self):
        """Test case for get_schueler

        
        """
        response = self.client.open(
            '/schueler/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schuelers(self):
        """Test case for get_schuelers

        
        """
        response = self.client.open(
            '/schueler',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_schueler(self):
        """Test case for update_schueler

        
        """
        body = SchuelerUpdatePayload()
        response = self.client.open(
            '/schueler/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
