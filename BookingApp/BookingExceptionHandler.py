from rest_framework.exceptions import APIException

class NOT_FOUND(APIException):
    status_code=404
    default_code="Not Found"
    default_detail="Not Found"

class NOT_AUTHORIZED(APIException):
    status_code= 403
    default_code="NOT AUTHORIZED"
    default_detail="NOT AUTHORIZED"

class Bad_Request(APIException):
    status_code=400
    default_code = "Bad Request"
    default_detail = "BAD REQUEST"