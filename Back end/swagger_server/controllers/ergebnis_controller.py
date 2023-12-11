import connexion

import six

from swagger_server.models.ergebnis import Ergebnis  # noqa: E501

from swagger_server.models.ergebnis_array import ErgebnisArray  # noqa: E501

from swagger_server.models.ergebnis_create_payload import ErgebnisCreatePayload  # noqa: E501

from swagger_server.models.ergebnis_update_payload import ErgebnisUpdatePayload  # noqa: E501

from swagger_server.models.ergebnisse import Ergebnisse  # noqa: E501

from swagger_server import util

def create_ergebnis(body):  # noqa: E501
    """create_ergebnis

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Ergebnis
    """
    if connexion.request.is_json:

        body = ErgebnisCreatePayload.from_dict(connexion.request.get_json())  # noqa: E501

    con = util.getDatabase()

    cur = con.cursor()

    sql = "INSERT INTO ergebnis (disziplin_id, schueler_id, wert) VALUES (?, ?, ?) RETURNING *"

    res = cur.execute(sql, body)

    row = res.fetchOne()

    return ergebnis_service(row)

def delete_ergebnis(id):  # noqa: E501
    """delete_ergebnis

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    
    con = util.getDatabase()

    cur = con.cursor()

    sql = "DELETE FROM ergebisse WHERE ergebnisse.id = ?"

    res = cur.execute(sql, id)

    res.fetchOne()

    return None

def get_ergebnis(id):  # noqa: E501
    """get_ergebnis

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Ergebnis
    """
    
    con = util.getDatabase()

    cur = con.cursor()

    sql = "SELECT * FROM ergbenisse WHERE ergebnisse.id = ?"

    res = cur.execute(sql, id)

    row = res.fetchOne()

    return ergebnis_service(row)

def ergebnis_service(row):

    data = []

    data.id = row[0]

    data.disziplin_id = row[1]

    data.schueler_id = row[2]

    data.wert = row[3]

    data.punkte = row[4]

    return Ergebnis(data.id, data.disziplin_id, data.schueler_id, data.wert, data.punkte)

def get_ergebnisse():  # noqa: E501
    """get_ergebnisse

     # noqa: E501


    :rtype: ErgebnisArray
    """

    ergebnisse = list()

    con = util.getDatabase()

    cur = con.cursor()
    
    sql = "SELECT * FROM ergebnisse"
    
    res = cur.execute(sql)

    for row in res:

        ergebnisse.append(ergebnis_service(row))
    
    return Ergebnisse(ergebnisse)

def update_ergebnis(body, id):  # noqa: E501
    """update_ergebnis

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: Ergebnis
    """
    if connexion.request.is_json:
        body = ErgebnisUpdatePayload.from_dict(connexion.request.get_json())  # noqa: E501
        
    
    
    con = getDatabase()

    cur = con.cursor()

    res = cur.execute(sql, id)
    
    return 'do some magic!'

