from .codec import base64url_encode
import abc
import json


__all__ = [
    'JOSEDictionary',
    'JOSEHeader',
    'JOSEObject',
    'JSONCompactSerializableMixin',
    'factory',
]


class JOSEObject(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def compact_serialize(self):  # pragma: no cover
        pass


class JSONCompactSerializableMixin(JOSEObject):
    def compact_serialize(self):
        return base64url_encode(json.dumps(self, separators=(',',':'),
            sort_keys=True))


class JOSEDictionary(dict, JSONCompactSerializableMixin): pass


class JOSEHeader(JOSEDictionary): pass


class JOSEOctetStream(JOSEObject, bytes):
    def compact_serialize(self):
        return base64url_encode(self)


def factory(data):
    if isinstance(data, JOSEObject):
        return data

    elif isinstance(data, dict):
        return JOSEDictionary(data)

    elif isinstance(data, bytes):
        return JOSEOctetStream(data)

    else:
        raise TypeError('Data not convertible to a JOSEObject.')
