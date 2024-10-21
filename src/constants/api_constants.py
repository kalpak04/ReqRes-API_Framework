
class APIConstants:
    # Endpoints
    USERS_ENDPOINT = "/users"
    SINGLE_USER_ENDPOINT = "/users/{}"
    REGISTER_ENDPOINT = "/register"
    LOGIN_ENDPOINT = "/login"
    RESOURCES_ENDPOINT = "/unknown"
    
    # Response Messages
    SUCCESS_MESSAGE = "Success"
    NOT_FOUND_MESSAGE = "Not found"
    
    # Status Codes
    SUCCESS_CODE = 200
    CREATED_CODE = 201
    NOT_FOUND_CODE = 404
    BAD_REQUEST_CODE = 400