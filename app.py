import logging
import sys


def main():
	logging.info("Starting app...")

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	sys.exit(main())