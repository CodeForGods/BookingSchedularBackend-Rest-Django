from rest_framework.exceptions import APIException

class NOT_FOUND(APIException):
    status_code=404
    default_code="Not Found"
    default_detail="Not Found"