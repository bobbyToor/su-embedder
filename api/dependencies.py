from core.config import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
)

from fastapi.security import OAuth2PasswordBearer, HTTPBasic, HTTPBasicCredentials
from fastapi.params import Depends
import secrets

security = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def validate_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)

    return correct_username and correct_password
