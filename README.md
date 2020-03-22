check-availability
====



## Installation

```sh-session
$ pip install check_availability
```

## Usage

```sh-session
$ check-availability <service> <name> [options]
```

## Example

```sh-session
$ check-availability pypi check_availability
GET https://pypi.org/project/check_availability
Got status code 200
The name check_availability is not available on pypi
```

## Options

| Shorthand | Option | Description | Default value
|-----------|-------------|-------------|--------------
| -h | --help | Show the help. | N/A |
| -v | --verbose=LEVEL | Set verbosity. 0 for quiet, 4 for debug. | 0 |

## Status codes

| Code | Meaning
|------|--------
| 0 | The name is available
| 1 | An error occured
| 2 | The name is not available
