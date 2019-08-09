from error_code import ErrorCodeDefine

class BaseError(Exception):
    """Base Error Class"""
    def __init__(self, code=400, message='', status='', field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field

    def to_dict(self):
        return {"code":self.code,
                "message":self.message,
                "status":self.status,
                "field":self.field
                }

class NotFoundError(BaseError):
    def __init__(self, message="Data Not Found", error_code=ErrorCodeDefine.BASE_ERROR):
        BaseError.__init__(slef) #??????
        self.code = 404
        self.message = message
        self.status = "NOT_FOUND"
        self.error_code = error_code
        self.error_key = ErrorCodeDefine.get_error_key(self.error_code)
        self.error_msg = ErrorCodeDefine.get_error_msg(self.error_code)

