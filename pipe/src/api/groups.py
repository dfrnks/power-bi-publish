import requests


def createGroup(accessToken: str, name: str) -> bool:
    """
    :param accessToken: The Access token
    :param name: The Workspace name
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups?workspaceV2=True"

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {
        'name': name,
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    raise Exception("Unable to create workspace!")


def getAllGroups(accessToken: str) -> list:
    """
    :param accessToken: The Access token
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups"

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
    }

    response = requests.get(
        url=url,
        headers=headers
    )

    if response.status_code == 200:
        return response.json()["value"]

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    raise Exception("Unable to get ths workspaces!")
