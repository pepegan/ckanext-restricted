# coding: utf8 


from ckan.common import c

from logging import getLogger
log = getLogger(__name__)


def _json2dict_or_empty(value, field_name=""):
    try:
        json_dict = json.loads(value)
    except Exception as e:
        log.warning("Field " + field_name + "('" + str(value) + "') could not be parsed: " + str(e))
        json_dict = {}
    return json_dict


def restricted_get_as_dict(value):
    '''
    Template helper funciton.
    Returns the value as a dictionary. If if is already
    a dictionary, the original value is returned. If it is
    a json dump, it will be parsed into a dictionary. Otherwise
    an empty dictionary is returned.
    '''
    if isinstance(value, dict):
        return value
    else:
        return (_json2dict_or_empty(value))


def restricted_get_user_id():
    return (str(c.user))
