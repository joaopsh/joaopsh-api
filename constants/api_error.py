class Error:
    def __init__(self, _id:str, code:int):
        self._id = _id
        self._code = code

    @property
    def id(self):
        return self._id

    @property
    def code(self):
        return self._code

INTERNAL_SERVER_ERROR = Error('INTERNAL_SERVER_ERROR', 500_000)
