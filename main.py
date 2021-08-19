#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import *
import logging
import argparse
import sys
import traceback

"""Python CLI template

A python scripting boilerplate template 
URL: https://github.com/ohidurbappy/python-cli-template
"""

DEBUG = False


try:
    # import external packages here
    from reusable.functions import splash, print_time_taken
    from dotenv import load_dotenv, find_dotenv
except ImportError:
    print(
        """ERROR: Import Error
One or more package(s) is not installed.\n
    Run `pip install -r requirements.txt` in this directory

Hint: If pip doesn't work try pip3
""")
    sys.exit()

# load environment variables from .env
load_dotenv(find_dotenv())
SECRET_KEY = os.environ.get("SECRET_KEY")

# setting up argsparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "-v",
    "--verbose",
    help="increase output verbosity",
    action="store_true")
args = parser.parse_args()

# setting up the logger
LOG_LEVEL = logging.INFO
if DEBUG or args.verbose:
    LOG_LEVEL = logging.DEBUG
logging.basicConfig(filename='log.txt', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s', level=LOG_LEVEL, datefmt="")


@print_time_taken
def main():
    logging.info("Program Starting.")
    print_system_info()


if __name__ == "__main__":
    splash("Python CLI Template")

    try:
        main()
        logging.info("Program finished successfully")
    except KeyboardInterrupt:
        print("KEYBOARD INTERRUPT. EXITING.")
        logging.info("KEYBOARD INTERRUPT. EXITING.")
        sys.exit()
    except:
        traceback.print_exc()
        logging.error("An exception has occured.", exc_info=True)
