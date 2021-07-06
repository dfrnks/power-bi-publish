import pytest
from pipe.src.api import auth

urlMock = 'https://login.microsoftonline.com/common/oauth2/token'


def test_auth(requests_mock):
    authToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
                '.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ' \
                '.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c '

    requests_mock.post(urlMock, text="""{
    "token_type": "Bearer",
    "scope": "Dataset.Read.All Dataset.ReadWrite.All Workspace.ReadWrite.All",
    "expires_in": "3599",
    "ext_expires_in": "3599",
    "expires_on": "1625491516",
    "not_before": "1625487616",
    "resource": "https://analysis.windows.net/powerbi/api",
    "access_token": \"""" + authToken + """\",
    "refresh_token": "0.AQoAlh_6l3d4n0aqNx-F...HNDEXI54VgLrjWS6wYbhn-eKAHEsTTjBv7nqpyCHRg6AJlQ",
    "id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJu...by5jb20uYnIiLCJ2ZXIiOiIxLjAifQ."
    }""")

    assert authToken == auth.getToken(
        client_id='xxx',
        client_secret='yyy',
        username='username@mail.com',
        password='xxxyyy088'
    )


def test_auth_password_incorrect(requests_mock):
    requests_mock.post(urlMock, text="""{
    "error": "invalid_grant",
    "error_description": "AADSTS50126: Error validating credentials due to invalid username or password.\\r\\nTrace ID: 8adc5510-13ac-464d-902f-7e20ce9c8e01\\r\\nCorrelation ID: 5e437e0a-6a78-4a52-b9cf-5ccc7a354561\\r\\nTimestamp: 2021-07-05 13:20:07Z",
    "error_codes": [
        50126
    ],
    "timestamp": "2021-07-05 13:20:07Z",
    "trace_id": "8adc5510-13ac-464d-902f-7e20ce9c8e01",
    "correlation_id": "5e437e0a-6a78-4a52-b9cf-5ccc7a354561",
    "error_uri": "https://login.microsoftonline.com/error?code=50126"
}""", status_code=400)

    with pytest.raises(Exception) as excinfo:
        auth.getToken(
            client_id='xxx',
            client_secret='yyy',
            username='username@mail.com',
            password='xxxyyy088'
        )

    assert str(excinfo.value) == 'AADSTS50126: Error validating credentials due to invalid username or ' \
                                 'password.\r\nTrace ID: 8adc5510-13ac-464d-902f-7e20ce9c8e01\r\nCorrelation ID: ' \
                                 '5e437e0a-6a78-4a52-b9cf-5ccc7a354561\r\nTimestamp: 2021-07-05 13:20:07Z'


def test_auth_username_incorrect(requests_mock):
    requests_mock.post(urlMock, text="""{
    "error": "invalid_request",
    "error_description": "AADSTS50059: No tenant-identifying information found in either the request or implied by any provided credentials.\\r\\nTrace ID: f4f34ca7-b508-44fe-adfb-3a7eda502401\\r\\nCorrelation ID: e248f8ed-a938-4adc-acd9-f9364c418a65\\r\\nTimestamp: 2021-07-05 13:50:01Z",
    "error_codes": [
        50059
    ],
    "timestamp": "2021-07-05 13:50:01Z",
    "trace_id": "f4f34ca7-b508-44fe-adfb-3a7eda502401",
    "correlation_id": "e248f8ed-a938-4adc-acd9-f9364c418a65"
}""", status_code=400)

    with pytest.raises(Exception) as excinfo:
        auth.getToken(
            client_id='xxx',
            client_secret='yyy',
            username='username@mail.com',
            password='xxxyyy088'
        )

    assert str(excinfo.value) == 'AADSTS50059: No tenant-identifying information found in either the request or ' \
                                 'implied by any provided credentials.\r\nTrace ID: ' \
                                 'f4f34ca7-b508-44fe-adfb-3a7eda502401\r\nCorrelation ID: ' \
                                 'e248f8ed-a938-4adc-acd9-f9364c418a65\r\nTimestamp: 2021-07-05 13:50:01Z'


def test_auth_client_id_incorrect(requests_mock):
    requests_mock.post(urlMock, text="""{
    "error": "unauthorized_client",
    "error_description": "AADSTS700016: Application with identifier 'xxx' was not found in the directory 'tenant.com.br'. This can happen if the application has not been installed by the administrator of the tenant or consented to by any user in the tenant. You may have sent your authentication request to the wrong tenant.\\r\\nTrace ID: eee1763c-c602-405a-a6b4-5cb8e5ca2301\\r\\nCorrelation ID: 26c0174a-6457-4331-9bd1-d7f55c5257e8\\r\\nTimestamp: 2021-07-05 13:52:44Z",
    "error_codes": [
        700016
    ],
    "timestamp": "2021-07-05 13:52:44Z",
    "trace_id": "eee1763c-c602-405a-a6b4-5cb8e5ca2301",
    "correlation_id": "26c0174a-6457-4331-9bd1-d7f55c5257e8",
    "error_uri": "https://login.microsoftonline.com/error?code=700016"
}""", status_code=400)

    with pytest.raises(Exception) as excinfo:
        auth.getToken(
            client_id='xxx',
            client_secret='yyy',
            username='username@mail.com',
            password='xxxyyy088'
        )

    assert str(excinfo.value) == 'AADSTS700016: Application with identifier \'xxx\' was not found in the directory ' \
                                 '\'tenant.com.br\'. This can happen if the application has not been installed by the ' \
                                 'administrator of the tenant or consented to by any user in the tenant. You may have ' \
                                 'sent your authentication request to the wrong tenant.\r\nTrace ID: ' \
                                 'eee1763c-c602-405a-a6b4-5cb8e5ca2301\r\nCorrelation ID: ' \
                                 '26c0174a-6457-4331-9bd1-d7f55c5257e8\r\nTimestamp: 2021-07-05 13:52:44Z'


def test_auth_secret_id_incorrect(requests_mock):
    requests_mock.post(urlMock, text="""{
    "error": "invalid_client",
    "error_description": "AADSTS7000215: Invalid client secret is provided.\\r\\nTrace ID: 01a61b09-ff85-4056-8775-975a5dc7b501\\r\\nCorrelation ID: 52ac6351-fc6f-409b-8a3f-866b0b3004db\\r\\nTimestamp: 2021-07-05 13:55:20Z",
    "error_codes": [
        7000215
    ],
    "timestamp": "2021-07-05 13:55:20Z",
    "trace_id": "01a61b09-ff85-4056-8775-975a5dc7b501",
    "correlation_id": "52ac6351-fc6f-409b-8a3f-866b0b3004db",
    "error_uri": "https://login.microsoftonline.com/error?code=7000215"
}""", status_code=401)

    with pytest.raises(Exception) as excinfo:
        auth.getToken(
            client_id='xxx',
            client_secret='yyy',
            username='username@mail.com',
            password='xxxyyy088'
        )

    assert str(excinfo.value) == 'AADSTS7000215: Invalid client secret is provided.\r\nTrace ID: ' \
                                 '01a61b09-ff85-4056-8775-975a5dc7b501\r\nCorrelation ID: ' \
                                 '52ac6351-fc6f-409b-8a3f-866b0b3004db\r\nTimestamp: 2021-07-05 13:55:20Z'
