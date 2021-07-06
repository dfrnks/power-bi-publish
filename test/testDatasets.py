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


def testGetDatasources(requests_mock):
    requests_mock.get(
        url + "/{groupId}/datasets/{datasetId}/datasources".format(groupId='yyy', datasetId='xxx'),
        status_code=200,
        text="""{
  "value": [
    {
      "datasourceType": "ODBC",
      "connectionDetails": {
        "connectionString": "dsn=simba athena test"
      },
      "datasourceId": "e189230a-06bb-4fd1-82c1-50799e339176",
      "gatewayId": "055d3f69-5dc5-4d19-9941-07e7670305aa"
    }
  ]
}"""
    )

    response = datasets.getDatasources(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx'
    )

    assert "e189230a-06bb-4fd1-82c1-50799e339176" == response[0]["datasourceId"]
    assert "055d3f69-5dc5-4d19-9941-07e7670305aa" == response[0]["gatewayId"]


def testGetDatasourcesWithoutDatasource(requests_mock):
    requests_mock.get(
        url + "/{groupId}/datasets/{datasetId}/datasources".format(groupId='yyy', datasetId='xxx'),
        status_code=200,
        text="""{
    "value": [
        {
            "datasourceType": "ODBC",
            "connectionDetails": {
                "connectionString": "dsn=simba athena"
            }
        }
    ]
}"""
    )

    response = datasets.getDatasources(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx'
    )

    assert "ODBC" == response[0]["datasourceType"]
    assert "datasourceId" not in response[0]
    assert "gatewayId" not in response[0]


def testDiscoverGateways(requests_mock):
    requests_mock.get(
        url + "/{groupId}/datasets/{datasetId}/Default.DiscoverGateways".format(groupId='yyy', datasetId='xxx'),
        status_code=200,
        text="""{
  "value": [
    {
      "id": "b6d69417-a714-45c7-8e1a-bd1196b97be0",
      "gatewayId": 0,
      "name": "Gateway Test",
      "type": "Resource",
      "publicKey": {
        "exponent": "AQAB",
        "modulus": "..."
      },
      "gatewayAnnotation": "..."
    }
  ]
}"""
    )

    response = datasets.discoverGateways(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx'
    )

    assert "b6d69417-a714-45c7-8e1a-bd1196b97be0" == response[0]["id"]
    assert "Gateway Test" == response[0]["name"]
    assert "Resource" == response[0]["type"]


def testBindDatasourceToGatewayDatasource(requests_mock):
    requests_mock.post(
        url + "/{groupId}/datasets/{datasetId}/Default.BindToGateway".format(groupId='yyy', datasetId='xxx'),
        status_code=200,
        text=""""""
    )

    response = datasets.bindDatasourceToGatewayDatasource(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx',
        gatewayId="zzz",
        datasourceId="www"
    )

    assert response


def testGetRefreshes(requests_mock):
    requests_mock.get(
        url + "/{groupId}/datasets/{datasetId}/refreshes?$top={top}".format(groupId='yyy', datasetId='xxx', top=1),
        status_code=200,
        text="""{
  "value": [
    {
      "refreshType": "ViaApi",
      "startTime": "2017-06-13T09:25:43.153Z",
      "endTime": "2017-06-13T09:31:43.153Z",
      "status": "Completed",
      "requestId": "9399bb89-25d1-44f8-8576-136d7e9014b1"
    },
    {
      "refreshType": "ViaApi",
      "startTime": "2017-06-13T09:25:43.153Z",
      "endTime": "2017-06-13T09:31:43.153Z",
      "serviceExceptionJson": "{\\"errorCode\\":\\"ModelRefreshFailed_CredentialsNotSpecified\\"}",
      "status": "Failed",
      "requestId": "11bf290a-346b-48b7-8973-c5df149337ff"
    }
  ]
}"""
    )

    response = datasets.getRefreshes(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        datasetId='xxx',
        top=1
    )

    assert "ViaApi" == response[0]["refreshType"]
    assert "Completed" == response[0]["status"]

    assert "ViaApi" == response[1]["refreshType"]
    assert "Failed" == response[1]["status"]
