"""Checks availability of a name on a corresponding service.

Usage:
  check-availability <service> <name> [options]
  check-availability (-h|--help)
  
Options:
  -h, --help           Show this help
  -v, --verbose=LEVEL  Set verbosity. 0 for quiet, 4 for debug. [default: 0]

Status codes:
  1: An error occured
  2: The name is not available
  0: The name is available
  
Example:
  $ check-availability pypi check_availability --verbose 3
  GET https://pypi.org/project/check_availability
  Got status code 200
  The name check_availability is not available on pypi
  
"""
from typing import *
from docopt import docopt
import json
import requests
from .log import Logger
from os import path, stat
from sys import exit

def main():
  # Parse the CLI input
  args: Dict[str, str] = docopt(__doc__)
  service: str = args['<service>']
  name: str = args['<name>']
  # Initialize the logger
  log = Logger(int(args['--verbose']))
  log.debug("Running with args: {0}", json.dumps(args, ensure_ascii=False))
  # Get the mapping of <service> to URL to test on
  serices_filepath = path.join(path.dirname(__file__), 'services.json')
  with open(serices_filepath, 'r') as file:
    services: Dict[str, str] = json.loads(file.read())
  # Get the URL to test
  url = services[service].format(name)
  # Make the request and get the status code
  log.info("GET {0}", url)
  status_code = requests.get(url).status_code
  log.info("Got status code {0}", status_code)
  # Check if the status_code is 404
  available = status_code == 404
  # Output
  if available:
    log.success("The name {0} is available on {1}", name, service)
  else:
    log.error("The name {0} is <options=bold>not</options=bold> available on {1}", name, service)
  # Exit w/ 0 if available, 1 otherwise.
  exit(0 if available else 2)
  
