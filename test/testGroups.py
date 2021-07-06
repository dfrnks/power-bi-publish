import pytest
from pipe.src.api import groups


urlGroups = "https://api.powerbi.com/v1.0/myorg/groups"


def testCreateWorkspace(requests_mock):
    requests_mock.post(urlGroups + "?workspaceV2=True", status_code=200, text="""{
      "id": "f089354e-8366-4e18-aea3-4cb4a3a50b48",
      "isOnDedicatedCapacity": false,
      "name": "sample workspace V2"
  }""")

    assert "f089354e-8366-4e18-aea3-4cb4a3a50b48" == groups.createGroup(
        accessToken='xxx',
        name='sample workspace V2'
    )


def testCreateWorkspaceInvalid(requests_mock):
    requests_mock.post(urlGroups + "?workspaceV2=True", status_code=500, text="""{
  "value": [
    {
      "id": "f089354e-8366-4e18-aea3-4cb4a3a50b48",
      "isOnDedicatedCapacity": false,
      "name": "sample workspace V2"
    }
  ]
}""")

    with pytest.raises(Exception) as excinfo:
        groups.createGroup(
            accessToken='xxx',
            name='Not Possible'
        )

    assert str(excinfo.value) == 'Unable to create workspace!'


def testCreateWorkspaceTokenExpired(requests_mock):
    requests_mock.post(urlGroups + "?workspaceV2=True", status_code=403, text="""""")

    with pytest.raises(Exception) as excinfo:
        groups.createGroup(
            accessToken='xxx',
            name='Not Possible'
        )

    assert str(excinfo.value) == 'Token expired or invalid!'


def testGetWorkspacesTokenExpired(requests_mock):
    requests_mock.get(urlGroups, status_code=403, text="""""")

    with pytest.raises(Exception) as excinfo:
        groups.getAllGroups(
            accessToken='xxx'
        )
    
    assert str(excinfo.value) == 'Token expired or invalid!'


def testGetAllGroups(requests_mock):
    requests_mock.get(urlGroups, status_code=200, text="""{
  "value": [
    {
      "id": "3d9b93c6-7b6d-4801-a491-1738910904fd",
      "isReadOnly": false,
      "isOnDedicatedCapacity": false,
      "name": "marketing group"
    },
    {
      "id": "a2f89923-421a-464e-bf4c-25eab39bb09f",
      "isReadOnly": false,
      "isOnDedicatedCapacity": false,
      "name": "contoso",
      "dataflowStorageId": "d692ae06-708c-485e-9987-06ff0fbdbb1f"
    }
  ]
}""")

    response = groups.getAllGroups(accessToken='xxx')

    assert len(response) == 2
    assert "marketing group" == response[0]["name"]
    assert "contoso" == response[1]["name"]


def testAddUsersGroup(requests_mock):
    requests_mock.post(urlGroups + "/{groupId}/users".format(groupId='yyy'), status_code=200, text="""{
  "emailAddress": "john@contoso.com",
  "groupUserAccessRight": "Admin"
}""")

    response = groups.addUserGroup(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        identifier='john@contoso.com',
        groupUserAccessRight='Admin'
    )

    assert response


def testChangeUserGroup(requests_mock):
    requests_mock.put(urlGroups + "/{groupId}/users".format(groupId='yyy'), status_code=200, text="""{
  "emailAddress": "john@contoso.com",
  "groupUserAccessRight": "Viewer"
}""")

    response = groups.changeUserGroup(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        identifier='john@contoso.com',
        groupUserAccessRight='Viewer',
        principalType="User"
    )

    assert response


def testDeleteUserGroup(requests_mock):
    requests_mock.delete(
        urlGroups + "/{groupId}/users/{user}".format(groupId='yyy', user="john@contoso.com"),
        status_code=200,
        text="""""")

    response = groups.deleteUserGroup(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        user='john@contoso.com'
    )

    assert response

