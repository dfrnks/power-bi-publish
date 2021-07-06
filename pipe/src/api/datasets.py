import requests, json
from bitbucket_pipes_toolkit import get_logger

logger = get_logger()


def updateParameters(accessToken: str, groupId: str, datasetId: str, parameters: list) -> bool:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param datasetId: The dataset id
    :param parameters
    """

    updateDetails = []
    for value in parameters:
        updateDetails.append({
            "name": value[0],
            "newValue": value[1]
        })

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/Default.UpdateParameters".format(
        groupId=groupId,
        datasetId=datasetId
    )

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {
        "updateDetails": updateDetails
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    logger.error(response.text)

    raise Exception("Unable to update parameters of the dataset with id {}!".format(datasetId))


def forceRefresh(accessToken: str, groupId: str, datasetId: str) -> bool:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param datasetId: The dataset id
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/refreshes".format(
        groupId=groupId,
        datasetId=datasetId
    )

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.post(
        url=url,
        headers=headers,
    )

    logger.debug(response.text)

    if response.status_code == 202:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    logger.error(response.text)

    raise Exception("Unable to refresh the dataset with id {}!".format(datasetId))


def getDatasources(accessToken: str, groupId: str, datasetId: str) -> dict:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param datasetId: The dataset id
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/datasources".format(
        groupId=groupId,
        datasetId=datasetId
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

    raise Exception("Unable to get the datasource of dataset with id {}!".format(datasetId))


def discoverGateways(accessToken: str, groupId: str, datasetId: str) -> dict:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param datasetId: The dataset id
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/Default.DiscoverGateways".format(
        groupId=groupId,
        datasetId=datasetId
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

    raise Exception("Unable to discover gateways into dataset with id {}!".format(datasetId))


def bindDatasourceToGatewayDatasource(accessToken: str, groupId: str, datasetId: str, gatewayId: str, datasourceId: str) -> bool:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param datasetId: The dataset id
    :param gatewayId: The gateway id
    :param datasourceId: The datasource of the gateway id
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/Default.BindToGateway".format(
        groupId=groupId,
        datasetId=datasetId
    )

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {
        "gatewayObjectId": gatewayId,
        "datasourceObjectIds": [
            datasourceId
        ]
    }

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(payload)
    )

    logger.debug(response.text)

    if response.status_code == 200:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    logger.error(response.text)

    raise Exception("Unable to bind Datasource into to gateway with id {}!".format(gatewayId))


def getRefreshes(accessToken: str, groupId: str, datasetId: str, top: int = 10) -> dict:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param datasetId: The dataset id
    :param top: The requested number of entries in the refresh history. If not provided, the default is all available entries.
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/refreshes?$top={top}".format(
        groupId=groupId,
        datasetId=datasetId,
        top=top
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

    raise Exception("Unable to get refresh history of the dataset with id {}".format(datasetId))
