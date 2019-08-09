
class ErrorCodeDefine:
    BASE_ERROR = 1  # 基本系統錯誤
    JSON_DECODE_ERROR = 2  # json解析錯誤

    NEED_AUTH_TOKEN = 100  # 需要授權的token
    INVALID_TOKEN = 101  # 無效的token
    TOKEN_EXPIRED = 102  # token已過期
    USER_NOT_EXIST = 103  # 帳號不存在

    @staticmethod
    def get_error_key(error_code):
        input_dict = dict()
        for key, value in ErrorCodeDefine.__dict__.items():
            if not key.startswith('_'):
                input_dict.update({value: key})
        return input_dict[error_code]

    @classmethod
    def get_error_msg(cls, error_code):
        input_dict = {
            cls.BASE_ERROR: 'Base System Error',  # 基本系統錯誤
            cls.JSON_DECODE_ERROR: 'Json decode error',  # json解析錯誤
            cls.NEED_AUTH_TOKEN: 'Need Authorization Token',  # 需要授權的token
            cls.INVALID_TOKEN: 'Invalid Token',  # 無效的token
            cls.TOKEN_EXPIRED: 'Token Expired',  # token已過期
            cls.USER_NOT_EXIST: 'This account is not exist',  # 帳號不存在
        }
        return input_dict[error_code]
