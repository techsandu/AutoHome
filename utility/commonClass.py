
class MyCustomException(Exception):
    pass
class JsonData:
    method_error_message = {"status": 0, "message": "Unsupported Method"}
    out_response = {"status":0,"data":[],"message":""}