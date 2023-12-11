import connexion

import six

from swagger_server.models.disziplin import Disziplin  # noqa: E501

from swagger_server.models.disziplin_array import DisziplinArray  # noqa: E501

from swagger_server.models.disziplin import Disziplinen  # noqa: E501

from swagger_server import util

def get_disziplin(id):  # noqa: E501
    """get_disziplin

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Disziplin
    """
    
    con = util.getDatabase()
    
    cur = con.cursor()
    
    sql = "SELECT * FROM disziplinen WHERE disziplinen.id = ?"

    res = cur.execute(sql, id)

    row = res.fetchOne()

    return disziplin_service(row)

def disziplin_service(row):

    data = []

    data.id = row[0]

    data.name = row[1]

    data.a = row[2]

    data.c = row[3]

    data.d = row[4]

    data.geschlecht = row[5]

    data.formel = row[6]

    return Disziplin(data.id, data.name, data.a, data.c, data.d, data.geschlecht, data.formel)

def get_disziplinen():  # noqa: E501
    """get_disziplinen

     # noqa: E501


    :rtype: DisziplinArray
    """
    
    sql = "SELECT * FROM disziplinen;"

    disziplinen = list()

    con = util.getDatabase()

    cur = con.cursor

    res = cur.execute(sql)

    for row in res:

        disziplinen.append(disziplin_service(row))

    return Disziplinen(disziplinen)