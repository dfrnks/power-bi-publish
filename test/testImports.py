import pytest
from pipe.src.api import imports

url = "https://api.powerbi.com/v1.0/myorg/groups"


def testGetImport(requests_mock):
    requests_mock.get(
        url + "/{groupId}/imports/{importId}".format(groupId='yyy', importId='82d9a37a-2b45-4221-b012-cb109b8e30c7'),
        status_code=200,
        text="""{
  "id": "82d9a37a-2b45-4221-b012-cb109b8e30c7",
  "importState": "Succeeded",
  "createdDateTime": "2018-05-08T14:56:18.477Z",
  "updatedDateTime": "2018-05-08T14:56:18.477Z",
  "name": "SalesMarketing",
  "connectionType": "import",
  "source": "Upload",
  "datasets": [
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
      "name": "SalesMarketing",
      "webUrl": "https://app.powerbi.com/groups/f089354e-8366-4e18-aea3-4cb4a3a50b48/datasets/cfafbeb1-8037-4d0c-896e-a46fb27ff229"
    }
  ],
  "reports": [
    {
      "id": "5b218778-e7a5-4d73-8187-f10824047715",
      "name": "SalesMarketing",
      "webUrl": "https://app.powerbi.com/groups/f089354e-8366-4e18-aea3-4cb4a3a50b48/reports/5b218778-e7a5-4d73-8187-f10824047715",
      "embedUrl": "https://app.powerbi.com/reportEmbed?reportId=5b218778-e7a5-4d73-8187-f10824047715&groupId=f089354e-8366-4e18-aea3-4cb4a3a50b48"
    }
  ]
}""")

    response = imports.getImport(
        accessToken='xxx-yy-xxx',
        groupId='yyy',
        importId='82d9a37a-2b45-4221-b012-cb109b8e30c7',
    )

    assert "82d9a37a-2b45-4221-b012-cb109b8e30c7" == response["id"]
    assert "Succeeded" == response["importState"]
    assert "Upload" == response["source"]


