import sqlite3

from unittest import result

import connexion

import six

from swagger_server.models.schueler import Schueler  # noqa: E501

from swagger_server.models.schueler_create_payload import SchuelerCreatePayload  # noqa: E501

from swagger_server.models.schueler_update_payload import SchuelerUpdatePayload  # noqa: E501

from swagger_server.models.schuelers import Schuelers  # noqa: E501

from swagger_server import util

def create_schueler(body):  # noqa: E501

    """create_schueler

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Schueler
    """
    if connexion.request.is_json:

        body = SchuelerCreatePayload.from_dict(connexion.request.get_json())  # noqa: E501

    con = util.getDatabase()

    cur = con.cursor()
    
    sql = "INSERT INTO schueler (vorname, nachname, geburtsjahr, unterscheider, geschlecht, anwesenheit, riegen_id) VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING *"
    
    res = cur.execute(sql, body.vorname(), body.nachname(), body.geburtsjahr(), body.unterscheider(), body.geschlecht(), body.anwesenheit(), body.riegen_id())

    row = res.fetchOne()

    return schueler_service(row)

def delete_schueler(id):  # noqa: E501
    """delete_schueler

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    con = util.getDatabase()

    cur = con.cursor()

    sql = "DELETE FROM schueler WHERE schueler.id = ?"
    
    res = cur.execute(sql, id)

    res.fetchOne()

    return  None

def get_schueler(id):  # noqa: E501
    """get_schueler

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Schueler
    """
    con = util.getDatabase()

    cur = con.cursor()

    sql = "SELECT * FROM schueler WHERE schueler.id = ?"
    
    res = cur.execute(sql, id)

    row = res.fetchOne()

    return schueler_service(row)

def schueler_service(row):
    
    data = []
    
    data.id = row[0]

    data.vorname = row[1]
    
    data.nachname = row[2]
    
    data.gaburtsjahr = row[3]
    
    data.unterscheider = row[4]
    
    data.geschlecht = row[5]

    data.anwesenheit = row[6]

    data.riegen_id = row[7]

    return Schueler(data.id, data.vorname, data.nachname, data.gaburtsjahr, data.unterscheider, data.geschlecht, data.anwesenheit, data.riegen_id)

def get_schuelers():  # noqa: E501
    """get_schuelers

     # noqa: E501

    :rtype: Schuelers
    """

    sql = "SELECT * FROM schueler"

    schuelers = list()

    con = util.getDatabase()

    cur = con.cursor()

    res = cur.execute(sql)

    for row in res:
        
        schuelers.append(schueler_service(row))

    return Schuelers(schuelers)

def update_schueler(body, id):  # noqa: E501
    """update_schueler

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: Schueler
    """
    if connexion.request.is_json:

        body = SchuelerUpdatePayload.from_dict(connexion.request.get_json())  # noqa: E501
    
    sql = "UPDATE schueler "
    
    return Schueler()