import pytest
from pipe.src.api import gateways


def testGetDatasources(requests_mock):
    requests_mock.get(
        "https://api.powerbi.com/v1.0/myorg/gateways/{gatewayId}/datasources".format(gatewayId="b6d69417-a714-45c7-8e1a-bd1196b97be0"),
        status_code=200,
        text="""{
  "value": [
    {
      "id": "838683f8-0bb6-4693-b91f-79e01bb61008",
      "gatewayId": "b6d69417-a714-45c7-8e1a-bd1196b97be0",
      "datasourceType": "ODBC",
      "connectionDetails": "{\\"connectionString\\":\\"dsn=Simba Athena\\"}",
      "credentialType": "Windows",
      "credentialDetails": {
        "useEndUserOAuth2Credentials": false
      },
      "datasourceName": "Simba Athena"
    }
  ]
}"""
    )

    response = gateways.getDatasources(
        accessToken='xxx-yy-xxx',
        gatewayId='b6d69417-a714-45c7-8e1a-bd1196b97be0'
    )

    assert "838683f8-0bb6-4693-b91f-79e01bb61008" == response[0]["id"]
    assert "b6d69417-a714-45c7-8e1a-bd1196b97be0" == response[0]["gatewayId"]
    assert "ODBC" == response[0]["datasourceType"]
    assert "Simba Athena" == response[0]["datasourceName"]
