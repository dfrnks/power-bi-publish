from pipe.src.auth.auth import getToken
import pytest


def test_auth(requests_mock):
    authToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTdmYTFmOTYtNzg3Ny00NjlmLWFhMzctMWY4NTY4ZTNhM2ZmLyIsImlhdCI6MTYyNTQ4NzYxNiwibmJmIjoxNjI1NDg3NjE2LCJleHAiOjE2MjU0OTE1MTYsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJFMlpnWVBpaHArKzI2M1Bnc243bCtwUHpiUnc4dWRKMmFFM0xmU3o4TWpuL2o4cXo5NVVBIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6Ijk5YWM2YTM1LWFkNDYtNDI4My04NTU1LTQzYTk0YWE2NDk1MyIsImFwcGlkYWNyIjoiMSIsImZhbWlseV9uYW1lIjoiTVggRGF0YWxha2UiLCJnaXZlbl9uYW1lIjoiU2VydmljZSIsImlwYWRkciI6IjE3OS4xMjcuMTM1LjEzNSIsIm5hbWUiOiJTZXJ2aWNlIE1YIERhdGFsYWtlIiwib2lkIjoiYmExNjBhMTQtMGNjOC00MGM3LTlmOGItNGQ1NjI5OTllOWY1Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTIwMTA5MTU4MDItNDIyMzQ3OTUyMS05NzMzMjk1MzAtMTE1NzMiLCJwdWlkIjoiMTAwMzIwMDEzOEJCMkMwNSIsInJoIjoiMC5BUW9BbGhfNmwzZDRuMGFxTngtRmFPT2pfelZxckpsR3JZTkNoVlZEcVVxbVNWTUtBRm8uIiwic2NwIjoiRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzdWIiOiJ5S0JOSUl1R0NoMjI4TnVELTFDR0JhWlZWUTdoLTBQRWYtX1NRVDhySU9BIiwidGlkIjoiOTdmYTFmOTYtNzg3Ny00NjlmLWFhMzctMWY4NTY4ZTNhM2ZmIiwidW5pcXVlX25hbWUiOiJzdmMubXhkYXRhbGFrZUBjb21wYXNzby5jb20uYnIiLCJ1cG4iOiJzdmMubXhkYXRhbGFrZUBjb21wYXNzby5jb20uYnIiLCJ1dGkiOiJDUnVtQVlYX1ZrQ0hkWmRhelRPd0FRIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXX0.fF3Yqcp2zK76AbLk0mprwOsiuz2g5KZTqvl1xktS5NjugdxCccJZ02UiXXwINg0UA6FQWPCmdOonfg4-2WegmO3Zmb6dgaJkGAt6Aqz8PIRnA_hlp_nap_LYRjS3a909lmQV95asONb4_kW_qsPbc-yDfvYA6i4iJVjj52LvSLrIL0LTRMgqM68K10wA4pcw33iXDD4iq_drqWrd6Ig55JIioqS2hOG8kkCwDJFP4L6MaS3ElsEmruPF0TAmiNs9v_22XFLRxzk8qDruAOAn__bwXQsT8SZYW3EHYnbWDbNR0grUV_RiEyHAJnBr_uDcElQLE8OJGXlLXFSnvZbncg"

    requests_mock.post('https://login.microsoftonline.com/common/oauth2/token', text="""{
    "token_type": "Bearer",
    "scope": "Dataset.Read.All Dataset.ReadWrite.All Workspace.ReadWrite.All",
    "expires_in": "3599",
    "ext_expires_in": "3599",
    "expires_on": "1625491516",
    "not_before": "1625487616",
    "resource": "https://analysis.windows.net/powerbi/api",
    "access_token": \"""" + authToken + """\",
    "refresh_token": "0.AQoAlh_6l3d4n0aqNx-FaOOj_zVqrJlGrYNChVVDqUqmSVMKAFo.AgABAAAAAAD--DLA3VO7QrddgJg7WevrAgDs_wQA9P-cUOr6p5O7tIkMLtAzo-KbZDQVk_-w-HxmSRQkPBHJc2SR_cpRFbSwFUfCPv87JUuMDV1zErm_0Kp1ZZPCQ0HIgta2zNykx-_PhLTFv6GX34sgTOHWQGURVxUghsg8QTLk2I629jUYMRi7os78bWOkl9hY6KBY9hB9JSE1_9G2O83q31dg0IF1E3vwWsBf_mpSEGejkUHp8edceSLKTLqXRA5P21oldPdz3PMe_kAT14eyjbtj5C-V-SQyYz-FXQCqu9KvuLUsCG6vlj_6Pc9DlzE84ipdH3i9P-QY9jjvJo2SyzM15lmj6AqlMjA6nYfgAtguUS1iXRAVQnP6LynuQY8esOW4U7ksL0QRKRXynn9PxctVG6TLiXxrwvnQ67H8v9lATGghlvRdODF_XW0UwK8TBGi7BQtOvk5mxUAGGy8TaaxerGouPPYECdp5-YU7ck7DK2Z4FgiqkVdRONL84hgjZoLGF7stFArMon_1Cuhux0lmMrg5QXmqhohyJVl02571fj0F64FcFcphrB1TXnlewqhRK0FU4uUqgW3WttWMUHm7Z-Y2Xf2X5qHFn4_U7SWyhdXSI_cUyeOGA5tRodsx1vzqJRR17TkaJWyIwH-hAVoHHVLVjfEhdpJSHAEbMHKAhz9UgLuq89CgNHUPV_scyGFXmFWA-x_mMrc5yfMMZ-NISkZJXbOdcfo50yT01sMTQnpEUtxZZVEhpF0Xy8NSi1Xz39_XqdXfHd90rgyhPRLsuUEhtKPsg0TgGPrPlNLGbXXq-c7XcXNeq7XIbClneLFd3M4AU6Kqx3SaaPGX_viRBzRd97E7ysOFyie7p1sDd7FwWASudZq_N9Qqs56gR8BcAWsV7fpE9hvka00ojwHH7FD06kXipFa_WjvTD_mtT1qrHNDEXI54VgLrjWS6wYbhn-eKAHEsTTjBv7nqpyCHRg6AJlQ",
    "id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiI5OWFjNmEzNS1hZDQ2LTQyODMtODU1NS00M2E5NGFhNjQ5NTMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85N2ZhMWY5Ni03ODc3LTQ2OWYtYWEzNy0xZjg1NjhlM2EzZmYvIiwiaWF0IjoxNjI1NDg3NjE2LCJuYmYiOjE2MjU0ODc2MTYsImV4cCI6MTYyNTQ5MTUxNiwiYW1yIjpbInB3ZCJdLCJmYW1pbHlfbmFtZSI6Ik1YIERhdGFsYWtlIiwiZ2l2ZW5fbmFtZSI6IlNlcnZpY2UiLCJpcGFkZHIiOiIxNzkuMTI3LjEzNS4xMzUiLCJuYW1lIjoiU2VydmljZSBNWCBEYXRhbGFrZSIsIm9pZCI6ImJhMTYwYTE0LTBjYzgtNDBjNy05ZjhiLTRkNTYyOTk5ZTlmNSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0yMDEwOTE1ODAyLTQyMjM0Nzk1MjEtOTczMzI5NTMwLTExNTczIiwicmgiOiIwLkFRb0FsaF82bDNkNG4wYXFOeC1GYU9Pal96VnFySmxHcllOQ2hWVkRxVXFtU1ZNS0FGby4iLCJzdWIiOiJuZVFGQjV3blg2MWNqRmdmYktPbEdTQ0MyWE03ZzNIcFZtVGxNSzNZV3pnIiwidGlkIjoiOTdmYTFmOTYtNzg3Ny00NjlmLWFhMzctMWY4NTY4ZTNhM2ZmIiwidW5pcXVlX25hbWUiOiJzdmMubXhkYXRhbGFrZUBjb21wYXNzby5jb20uYnIiLCJ1cG4iOiJzdmMubXhkYXRhbGFrZUBjb21wYXNzby5jb20uYnIiLCJ2ZXIiOiIxLjAifQ."
    }""")

    assert authToken == getToken(
        client_id='xxx',
        client_secret='yyy',
        username='username@mail.com',
        password='xxxyyy088'
    )


def test_auth_password_incorrect(requests_mock):
    requests_mock.post('https://login.microsoftonline.com/common/oauth2/token', text="""{
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
        getToken(
            client_id='xxx',
            client_secret='yyy',
            username='username@mail.com',
            password='xxxyyy088'
        )

    assert str(excinfo.value) == 'AADSTS50126: Error validating credentials due to invalid username or ' \
                                 'password.\r\nTrace ID: 8adc5510-13ac-464d-902f-7e20ce9c8e01\r\nCorrelation ID: ' \
                                 '5e437e0a-6a78-4a52-b9cf-5ccc7a354561\r\nTimestamp: 2021-07-05 13:20:07Z'


def test_auth_username_incorrect(requests_mock):
    requests_mock.post('https://login.microsoftonline.com/common/oauth2/token', text="""{
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
        getToken(
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
    requests_mock.post('https://login.microsoftonline.com/common/oauth2/token', text="""{
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
        getToken(
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
    requests_mock.post('https://login.microsoftonline.com/common/oauth2/token', text="""{
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
        getToken(
            client_id='xxx',
            client_secret='yyy',
            username='username@mail.com',
            password='xxxyyy088'
        )

    assert str(excinfo.value) == 'AADSTS7000215: Invalid client secret is provided.\r\nTrace ID: ' \
                                 '01a61b09-ff85-4056-8775-975a5dc7b501\r\nCorrelation ID: ' \
                                 '52ac6351-fc6f-409b-8a3f-866b0b3004db\r\nTimestamp: 2021-07-05 13:55:20Z'
