from flask import request

from config import Config


# check permission
def check_permission():
    rule = request.url_rule
    method = request.method
    role_permission = Config.PERMISSION[Config.TEAM_ID]['api']

    valid = False
    for api_role in role_permission:
        if api_role.path == rule:
            valid = True



    if not valid:
        pass


def token_required(f):
    def decorator(*args, **kwargs):
        Config.USER_ID = 1
        Config.TEAM_ID = 1

        status = check_permission()

        if not status:
            pass
        return f(*args, **kwargs)

    return decorator
