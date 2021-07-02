# Bitbucket Pipelines Pipe: Power BI Publish

This pipe will publish .pbix files into Power BI Service

## YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
- pipe: dfrnks/power-bi-publish:0.1.0
  variables:
    NAME: "<string>"
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
| PARAMETER_0           | The firts parameter key:value |
| PARAMETER_1           | The secondy parameter key:value |
| PARAMETER_n           | The n parameter key:value |
| PARAMETER_COUNT       | The quantity of parameters |
| DEBUG                 | Turn on extra debug information. Default: `false`. |

_(*) = required variable._

## Prerequisites

## Examples

Basic example:

```yaml
script:
  - pipe: dfrnks/power-bi-publish:0.1.0
    variables:
      USERNAME: "username"
      PASSWORD: "password"
      CLIENT_ID: "xxxx-xxx-xxxx"
      CLIENT_SECRET: "yyy-yyyy-yyy"
      WORKSPACE: "The My Workspace"
      DIRECTORY_PBIX: "workspaces/the_my_workspace"
      GATEWAY: "My Gateway:My Data Source"
      PARAMETER_0: "dsn:dsn=Simba Athena"
      PARAMETER_1: "Schema:default"
      PARAMETER_COUNT: "2"
```

Advanced example:

```yaml
script:
  - pipe: dfrnks/power-bi-publish:0.1.0
    variables:
      USERNAME: "username"
      PASSWORD: "password"
      CLIENT_ID: "xxxx-xxx-xxxx"
      CLIENT_SECRET: "yyy-yyyy-yyy"
      WORKSPACE: "The My Workspace"
      DIRECTORY_PBIX: "workspaces/the_my_workspace"
      GATEWAY: "My Gateway:My Data Source"
      PARAMETER_0: "dsn:dsn=Simba Athena"
      PARAMETER_1: "Schema:default"
      PARAMETER_COUNT: "2"
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
