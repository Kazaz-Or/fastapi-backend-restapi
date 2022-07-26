from fastapi import HTTPException, status


def http_exception():
    return HTTPException(status_code=404, detail="Todo not found")


def http_exception_user():
    return HTTPException(status_code=404, detail="User not found")


def get_user_exception():
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                             detail="Incorrect Username or Password",
                                             headers={"WWW-Authenticate": "Bearer"})
    return token_exception_response
