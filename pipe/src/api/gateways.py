import requests, json
from bitbucket_pipes_toolkit import get_logger

logger = get_logger()


def getDatasources(accessToken: str, gatewayId: str) -> dict:
    """
    :param accessToken: The Access token
    :param gatewayId: The Gateway id
    """

    url = "https://api.powerbi.com/v1.0/myorg/gateways/{gatewayId}/datasources".format(
        gatewayId=gatewayId
    )

    headers = {
        'Authorization': "Bearer {}".format(accessToken)
    }

    response = requests.get(
        url=url,
        headers=headers,
    )

    if response.status_code == 200:
        logger.debug(response.json())

        return response.json()["value"]

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    logger.error(response.text)

    raise Exception("Unable to get datasource with the gateway {}!".format(gatewayId))

