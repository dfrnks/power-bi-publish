import requests, json
from bitbucket_pipes_toolkit import get_logger

logger = get_logger()


def upload(accessToken: str, groupId: str, fileName: str, file) -> str:
    """
    :param accessToken
    :param groupId
    :param fileName
    :param file
    """
    url = 'https://api.powerbi.com/v1.0/myorg/groups/{groupId}/imports?datasetDisplayName={datasetDisplayName}' \
          '&nameConflict={nameConflict}'.format(
                groupId=groupId,
                datasetDisplayName=fileName,
                nameConflict='CreateOrOverwrite'
            )

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
    }

    files = [
        (
            'value',
            (fileName, file, 'application/octet-stream')
        )
    ]

    response = requests.post(
        url=url,
        headers=headers,
        files=files
    )

    if response.status_code in (200, 202):
        logger.debug(response.json())

        return response.json()["id"]

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    logger.error(response.text)

    raise Exception("Unable to import {} PBIX!".format(fileName))


def getImport(accessToken: str, groupId: str, importId: str) -> dict:
    """
    :param accessToken
    :param groupId
    :param importId
    """
    url = 'https://api.powerbi.com/v1.0/myorg/groups/{groupId}/imports/{importId}'.format(
        groupId=groupId,
        importId=importId,
    )

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        logger.debug(response.json())

        return response.json()

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    logger.error(response.text)

    raise Exception("Unable to get PBIX!")
