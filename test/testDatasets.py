import pytest
from pipe.src.api import datasets

url = "https://api.powerbi.com/v1.0/myorg/groups"


def testUpdateParameters(requests_mock):
    requests_mock.post(
        url + "/{groupId}/datasets/{datasetId}/Default.UpdateParameters".format(groupId='yyy', datasetId='xxx'),
        status_code=200,
        text="""{
  "updateDetails": [
    {
      "name": "DatabaseName",
      "newValue": "NewDB"
    },
    {
      "name": "MaxId",
      "newValue": "5678"
    }
  ]
}"""
    )

    response = datasets.updateParameters(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx',
        parameters=[
            ["DatabaseName", "NewDB"],
            ["MaxId", "5678"],
        ]
    )

    assert response


def testForceRefresh(requests_mock):
    requests_mock.post(
        url + "/{groupId}/datasets/{datasetId}/refreshes".format(groupId='yyy', datasetId='xxx'),
        status_code=202,
        text=""""""
    )

    response = datasets.forceRefresh(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx'
    )

    assert response
