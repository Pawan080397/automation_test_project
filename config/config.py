
BROWSER = "chrome"
class ReadConfig:

    BASE_URL = "http://192.168.1.127:8000/"

    USERS = {
        "admin": {
            "username": "fatadmin",
            "password": "fatadmin"
        },
        "analyst": {
            "username": "nRupal",
            "password": "123456"
        }
    }

    @staticmethod
    def get_user(role):
        return ReadConfig.USERS.get(role)
