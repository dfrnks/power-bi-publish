import requests


def createGroup(accessToken: str, name: str) -> str:
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
        return response.json()["value"][0]["id"]

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

    raise Exception("Unable to get the workspaces!")


def getUsersGroup(accessToken:str, groupId: str) -> list:
    """
    Returns a list of users that have access to the specified workspace.

    :param accessToken: The Access token
    :param groupId: The workspace id
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/users".format(groupId=groupId)

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response["value"]

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    raise Exception("Unable to get users of workspaces!")


def addUserGroup(accessToken: str, groupId: str, identifier: str, groupUserAccessRight: str) -> bool:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    # :param displayName: Display name of the principal
    :param identifier: The ID/Email of the user
    :param groupUserAccessRight: Access rights user has for the workspace https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#groupuseraccessright
    # :param principalType: The principal type https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#principaltype
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/users".format(groupId=groupId)

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {
        "identifier": identifier,
        "groupUserAccessRight": groupUserAccessRight,
    }

    response = requests.post(url=url, headers=headers, data=payload)

    if response.status_code == 200 and response.json()["emailAddress"] == identifier:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    raise Exception("Unable to add user to workspaces!")


def changeUserGroup(accessToken: str, groupId: str, identifier: str, groupUserAccessRight: str) -> bool:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param identifier: The ID/Email of the user
    :param groupUserAccessRight: Access rights user has for the workspace https://docs.microsoft.com/en-us/rest/api/power-bi/groups/addgroupuser#groupuseraccessright
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/users".format(groupId=groupId)

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
        'Content-Type': 'application/json; charset=utf-8'
    }

    payload = {
        "identifier": identifier,
        "groupUserAccessRight": groupUserAccessRight,
    }

    response = requests.put(url=url, headers=headers, data=payload)

    if response.status_code == 200:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    raise Exception("Unable to change user to workspaces!")


def deleteUserGroup(accessToken: str, groupId: str, user: str) -> bool:
    """
    :param accessToken: The Access token
    :param groupId: The workspace id
    :param user: The email address of the user or the service principal object id to delete
    """

    url = "https://api.powerbi.com/v1.0/myorg/groups/{groupId}/users/{user}".format(groupId=groupId, user=user)

    headers = {
        'Authorization': "Bearer {}".format(accessToken),
    }

    response = requests.delete(url=url, headers=headers)

    if response.status_code == 200:
        return True

    if response.status_code == 403:
        raise Exception("Token expired or invalid!")

    raise Exception("Unable to delete user to workspaces!")

