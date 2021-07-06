# Bitbucket Pipelines Pipe: Power BI Publish

This pipe will publish .pbix files into Power BI Service

## YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
- pipe: dfrnks/power-bi-publish:0.1.1
  variables:
    NAME: "<string>"
    USERNAME: "<string>"
    PASSWORD: "<string>"
    CLIENT_ID: "<string>"
    CLIENT_SECRET: "<string>"
    WORKSPACE: "<string>"
    DIRECTORY_PBIX: "<string>"
    # GATEWAY: "<string>" # Optional
    # PERMISSION_0: "<string>" # Optional
    # PERMISSION_1: "<string>" # Optional
    # PERMISSION_COUNT: "<string>" # Optional
    # PARAMETER_0: "<string>" # Optional
    # PARAMETER_1: "<string>" # Optional
    # PARAMETER_COUNT: "<string>" # Optional
    # WAIT: "<boolean>" # Optional
    # DEBUG: "<boolean>" # Optional
```
## Variables

| Variable              | Usage                                                       |
| --------------------- | ----------------------------------------------------------- |
| USERNAME (*)          | The Power BI Service Username, the username do can't have MFA |
| PASSWORD (*)          | The Power BI Service Password |
| CLIENT_ID (*)         | The Client ID of Azure Auth App |
| CLIENT_SECRET (*)     | The Client Secret of Azure Auth App |
| WORKSPACE (*)         | The name of Power BI Service Workspace |
| DIRECTORY_PBIX (*)    | The directory that contain the .pbix files |
| GATEWAY               | The name of the gateway and data source |
| PERMISSION_0          | The firts permission identifier:groupUserAccessRight |
| PERMISSION_1          | The secondy permission identifier:groupUserAccessRight |
| PERMISSION_n          | The n permissions identifier:groupUserAccessRight |
| PERMISSION_COUNT      | The quantity of permissions |
| PARAMETER_0           | The firts parameter key:value |
| PARAMETER_1           | The secondy parameter key:value |
| PARAMETER_n           | The n parameters key:value |
| PARAMETER_COUNT       | The quantity of parameters |
| WAIT                  | Waiting the update of all reports. Default: `false`. |
| DEBUG                 | Turn on extra debug information. Default: `false`. |

_(*) = required variable._

## Prerequisites

## Examples

Basic example:

```yaml
script:
  - pipe: dfrnks/power-bi-publish:0.1.1
    variables:
      USERNAME: "username"
      PASSWORD: "password"
      CLIENT_ID: "xxxx-xxx-xxxx"
      CLIENT_SECRET: "yyy-yyyy-yyy"
      WORKSPACE: "The My Workspace"
      DIRECTORY_PBIX: "workspaces/the_my_workspace"
      GATEWAY: "My Gateway:My Data Source"
      PERMISSION_0: "jp@mail.com:Admin"
      PERMISSION_1: "olv@mail.com:Viewer"
      PERMISSION_COUNT: "2"
      PARAMETER_0: "dsn:dsn=Simba Athena"
      PARAMETER_1: "Schema:default"
      PARAMETER_COUNT: "2"
```

Advanced example:

```yaml
script:
  - pipe: dfrnks/power-bi-publish:0.1.1
    variables:
      USERNAME: "username"
      PASSWORD: "password"
      CLIENT_ID: "xxxx-xxx-xxxx"
      CLIENT_SECRET: "yyy-yyyy-yyy"
      WORKSPACE: "The My Workspace"
      DIRECTORY_PBIX: "workspaces/the_my_workspace"
      GATEWAY: "My Gateway:My Data Source"
      PERMISSION_0: "jp@mail.com:Admin"
      PERMISSION_1: "olv@mail.com:Viewer"
      PERMISSION_COUNT: "2"
      PARAMETER_0: "dsn:dsn=Simba Athena"
      PARAMETER_1: "Schema:default"
      PARAMETER_COUNT: "2"
      WAIT: "true"
      DEBUG: "true"
```

## Support
If you’d like help with this pipe, or you have an issue or feature request, let us know.
The pipe is maintained by douglasfrancardoso@gmail.com.

If you’re reporting an issue, please include:

- the version of the pipe
- relevant logs and error messages
- steps to reproduce

You can donate if you want in this link [Donation](https://www.paypal.com/donate?hosted_button_id=6GMU7LV7CAN54)
