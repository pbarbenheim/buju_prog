import sqlite3

from unittest import result

import connexion

import six

from swagger_server.models.riege import Riege  # noqa: E501

from swagger_server.models.riege_array import RiegeArray  # noqa: E501

from swagger_server.models.riege_payload import RiegePayload  # noqa: E501

from swagger_server.models.riege_payload import Riegen  # noqa: E501

from swagger_server import util

def create_riege(body):  # noqa: E501
    """create_riege

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Riege
    """
    if connexion.request.is_json:

        body = RiegePayload.from_dict(connexion.request.get_json())  # noqa: E501

    con = util.getDatabase()

    cur = con.cursor()

    sql = "INSERT into riege (name) VALUES (?) RETURNING *"

    res = cur.execute(sql, body.name())

    row = res.fetchOne()

    return riege_service(row)

def delete_riege(id):  # noqa: E501
    """delete_riege

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    con = util.getDatabase()

    cur = con.cursor()

    sql = "DELETE FROM riegen WHERE riegen.id = ?"

    res = cur.execute(sql, id)

    res.fetchOne()

    return None

def get_riege(id):  # noqa: E501
    """get_riege

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Riege
    """
    
    con = util.getDatabase()

    cur = con.cursor()

    sql = "SELECT * FROM riegen WHERE riegen.id = ?"

    res = cur.execute(sql, id)

    row = res.fetchOne()
    
    return riege_service(row)

def riege_service(row):

    data = []

    data.id = row[0]

    data.name = row[1]

    return Riege(data.id, data.name)

def get_riegen():  # noqa: E501
    """get_riegen

     # noqa: E501


    :rtype: RiegeArray
    """

    con = getDatabase()

    cur= con.cursor()

    sql = "SELECT * FROM riegen"

    riegen = list()

    res = cur.execute(sql)

    for row in res:

        riegen.append(riege_service(row))

    return Riegen(riegen)

def update_riege(body, id):  # noqa: E501
    """update_riege

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: Riege
    """
    if connexion.request.is_json:
        body = RiegePayload.from_dict(connexion.request.get_json())  # noqa: E501
    

    sql = "UPDATE riegen SET riegen.name = wert1 WHERE riegen.name = wert" 

    return Riege()