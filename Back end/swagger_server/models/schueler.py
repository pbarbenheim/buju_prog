# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Schueler(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, vorname: str=None, nachname: str=None, geburtsjahr: float=None, unterscheider: str=None, geschlecht: str=None, anwesenheit: bool=True, riegen_id: str=None):  # noqa: E501
        """Schueler - a model defined in Swagger

        :param id: The id of this Schueler.  # noqa: E501
        :type id: str
        :param vorname: The vorname of this Schueler.  # noqa: E501
        :type vorname: str
        :param nachname: The nachname of this Schueler.  # noqa: E501
        :type nachname: str
        :param geburtsjahr: The geburtsjahr of this Schueler.  # noqa: E501
        :type geburtsjahr: float
        :param unterscheider: The unterscheider of this Schueler.  # noqa: E501
        :type unterscheider: str
        :param geschlecht: The geschlecht of this Schueler.  # noqa: E501
        :type geschlecht: str
        :param anwesenheit: The anwesenheit of this Schueler.  # noqa: E501
        :type anwesenheit: bool
        :param riegen_id: The riegen_id of this Schueler.  # noqa: E501
        :type riegen_id: str
        """
        self.swagger_types = {
            'id': str,
            'vorname': str,
            'nachname': str,
            'geburtsjahr': float,
            'unterscheider': str,
            'geschlecht': str,
            'anwesenheit': bool,
            'riegen_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'vorname': 'vorname',
            'nachname': 'nachname',
            'geburtsjahr': 'geburtsjahr',
            'unterscheider': 'unterscheider',
            'geschlecht': 'geschlecht',
            'anwesenheit': 'anwesenheit',
            'riegen_id': 'riegen_id'
        }
        self._id = id
        self._vorname = vorname
        self._nachname = nachname
        self._geburtsjahr = geburtsjahr
        self._unterscheider = unterscheider
        self._geschlecht = geschlecht
        self._anwesenheit = anwesenheit
        self._riegen_id = riegen_id

    @classmethod
    def from_dict(cls, dikt) -> 'Schueler':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The schueler of this Schueler.  # noqa: E501
        :rtype: Schueler
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Schueler.


        :return: The id of this Schueler.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Schueler.


        :param id: The id of this Schueler.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def vorname(self) -> str:
        """Gets the vorname of this Schueler.


        :return: The vorname of this Schueler.
        :rtype: str
        """
        return self._vorname

    @vorname.setter
    def vorname(self, vorname: str):
        """Sets the vorname of this Schueler.


        :param vorname: The vorname of this Schueler.
        :type vorname: str
        """
        if vorname is None:
            raise ValueError("Invalid value for `vorname`, must not be `None`")  # noqa: E501

        self._vorname = vorname

    @property
    def nachname(self) -> str:
        """Gets the nachname of this Schueler.


        :return: The nachname of this Schueler.
        :rtype: str
        """
        return self._nachname

    @nachname.setter
    def nachname(self, nachname: str):
        """Sets the nachname of this Schueler.


        :param nachname: The nachname of this Schueler.
        :type nachname: str
        """
        if nachname is None:
            raise ValueError("Invalid value for `nachname`, must not be `None`")  # noqa: E501

        self._nachname = nachname

    @property
    def geburtsjahr(self) -> float:
        """Gets the geburtsjahr of this Schueler.


        :return: The geburtsjahr of this Schueler.
        :rtype: float
        """
        return self._geburtsjahr

    @geburtsjahr.setter
    def geburtsjahr(self, geburtsjahr: float):
        """Sets the geburtsjahr of this Schueler.


        :param geburtsjahr: The geburtsjahr of this Schueler.
        :type geburtsjahr: float
        """

        self._geburtsjahr = geburtsjahr

    @property
    def unterscheider(self) -> str:
        """Gets the unterscheider of this Schueler.


        :return: The unterscheider of this Schueler.
        :rtype: str
        """
        return self._unterscheider

    @unterscheider.setter
    def unterscheider(self, unterscheider: str):
        """Sets the unterscheider of this Schueler.


        :param unterscheider: The unterscheider of this Schueler.
        :type unterscheider: str
        """

        self._unterscheider = unterscheider

    @property
    def geschlecht(self) -> str:
        """Gets the geschlecht of this Schueler.


        :return: The geschlecht of this Schueler.
        :rtype: str
        """
        return self._geschlecht

    @geschlecht.setter
    def geschlecht(self, geschlecht: str):
        """Sets the geschlecht of this Schueler.


        :param geschlecht: The geschlecht of this Schueler.
        :type geschlecht: str
        """
        allowed_values = ["maennlich", "weiblich", "divers"]  # noqa: E501
        if geschlecht not in allowed_values:
            raise ValueError(
                "Invalid value for `geschlecht` ({0}), must be one of {1}"
                .format(geschlecht, allowed_values)
            )

        self._geschlecht = geschlecht

    @property
    def anwesenheit(self) -> bool:
        """Gets the anwesenheit of this Schueler.


        :return: The anwesenheit of this Schueler.
        :rtype: bool
        """
        return self._anwesenheit

    @anwesenheit.setter
    def anwesenheit(self, anwesenheit: bool):
        """Sets the anwesenheit of this Schueler.


        :param anwesenheit: The anwesenheit of this Schueler.
        :type anwesenheit: bool
        """

        self._anwesenheit = anwesenheit

    @property
    def riegen_id(self) -> str:
        """Gets the riegen_id of this Schueler.


        :return: The riegen_id of this Schueler.
        :rtype: str
        """
        return self._riegen_id

    @riegen_id.setter
    def riegen_id(self, riegen_id: str):
        """Sets the riegen_id of this Schueler.


        :param riegen_id: The riegen_id of this Schueler.
        :type riegen_id: str
        """

        self._riegen_id = riegen_id
