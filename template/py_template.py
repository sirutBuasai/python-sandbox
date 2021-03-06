#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
SCRIPT TEMPLATE
"""
# pylint: disable=W0311
# pylint: disable=W0611
#
# Standard Imports (can be added as needed)
#
import argparse
import ast
from datetime import date, datetime
import json
import logging
import os
from pathlib import Path
import sys

#
# Non-standard Imports (can be added as needed)
#

#
######################################################################
#
# Global variables
#
DEFAULT_LOG_LEVEL = 'WARNING'

#
######################################################################
#
# main()
#
def main():
  """
  Consider writing docstrings in the Google style:
  https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
  Where possible, add type annotations as well. For example:
  https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html
  Args:
      No arg
  Returns:
      Nothing
  Raises:
      Nothing
  """

  # Configure logging and arguments
  args = handle_arguments()
  _clean_loggers(args.log_level.upper())
  logger = _get_logger()
  logger.info("Log level is '%s'", args.log_level.upper())

  print(__doc__)

#
######################################################################
# Helper methods
######################################################################
#
# _clean_loggers()
#
def _clean_loggers(log_level: str = 'WARNING'):
  """
  Clean logging messages and set logging format.
  """
  root = logging.getLogger()
  if root.handlers:
      for handler in root.handlers:
          root.removeHandler(handler)
  # try this here
  logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s.%(funcName)s:%(message)s',
                      level=getattr(logging, log_level.upper()))

#
######################################################################
#
# _get_logger()
#
def _get_logger():
  """
  Get the correct logger by name of current file
  Returns:
      logging.logger: Instance of logger in name of current file
  """
  return logging.getLogger(Path(__file__).resolve().name)

#
######################################################################
#
# handle_arguments()
#
def handle_arguments():
  """
  Handle CLI arguments
  Returns:
      parser.Namespace: Representation of the parsed arguments
  """
  #
  # Handle CLI args
  #
  parser = argparse.ArgumentParser(description=__doc__)

  parser.add_argument('-l', '--log-level',
                      action='store',
                      required=False,
                      choices=["debug", "info", "warning", "error", "critical"],
                      default=DEFAULT_LOG_LEVEL,
                      help='Logging verbosity. Default: %(default)s')

  return parser.parse_args()

#
######################################################################
#
# Call the main function
#
if __name__ == '__main__':
  main()
