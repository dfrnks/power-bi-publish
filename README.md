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
| NAME (*)              | The name that will be printed in the logs |
| DEBUG                 | Turn on extra debug information. Default: `false`. |

_(*) = required variable._

## Prerequisites

## Examples

Basic example:

```yaml
script:
  - pipe: dfrnks/power-bi-publish:0.1.0
    variables:
      NAME: "foobar"
```

Advanced example:

```yaml
script:
  - pipe: dfrnks/power-bi-publish:0.1.0
    variables:
      NAME: "foobar"
      DEBUG: "true"
```

## Support
If you’d like help with this pipe, or you have an issue or feature request, let us know.
The pipe is maintained by douglasfrancardoso@gmail.com.

If you’re reporting an issue, please include:

- the version of the pipe
- relevant logs and error messages
- steps to reproduce


## [Donation](https://www.paypal.com/donate?hosted_button_id=6GMU7LV7CAN54)
