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
