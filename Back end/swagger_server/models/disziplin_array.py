# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.disziplin import Disziplin  # noqa: F401,E501
from swagger_server import util


class DisziplinArray(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, disziplinen: List[Disziplin]=None):  # noqa: E501
        """DisziplinArray - a model defined in Swagger

        :param disziplinen: The disziplinen of this DisziplinArray.  # noqa: E501
        :type disziplinen: List[Disziplin]
        """
        self.swagger_types = {
            'disziplinen': List[Disziplin]
        }

        self.attribute_map = {
            'disziplinen': 'disziplinen'
        }
        self._disziplinen = disziplinen

    @classmethod
    def from_dict(cls, dikt) -> 'DisziplinArray':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The disziplinArray of this DisziplinArray.  # noqa: E501
        :rtype: DisziplinArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def disziplinen(self) -> List[Disziplin]:
        """Gets the disziplinen of this DisziplinArray.


        :return: The disziplinen of this DisziplinArray.
        :rtype: List[Disziplin]
        """
        return self._disziplinen

    @disziplinen.setter
    def disziplinen(self, disziplinen: List[Disziplin]):
        """Sets the disziplinen of this DisziplinArray.


        :param disziplinen: The disziplinen of this DisziplinArray.
        :type disziplinen: List[Disziplin]
        """

        self._disziplinen = disziplinen
