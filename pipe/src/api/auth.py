import requests
from bitbucket_pipes_toolkit import get_logger

logger = get_logger()


def getToken(client_id: str, client_secret: str, username: str, password: str) -> str:
    """
    :param client_id: Client ID of Auth Azure App
    :param client_secret: Client Secret of Auth Azuere App
    :param username: Username for authenticator into Power BI Service
    :param password: Password of the username
    """

    url = "https://login.microsoftonline.com/common/oauth2/token"

    payload = {
        'grant_type': 'password',
        'scope': 'openid',
        'resource': 'https://analysis.windows.net/powerbi/api',
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password,
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return response.json()['access_token']
    elif response.status_code in (400, 401):
        raise Exception(response.json()["error_description"])

    logger.error(response.text)

    raise Exception("Authentication failed!")

