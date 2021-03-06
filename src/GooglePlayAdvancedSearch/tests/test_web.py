import os

import pytest
import requests

import GooglePlayAdvancedSearch.tests.testUtils as testUtils

"""
Test the website using regular python/requests without executing JavaScript or advanced browsing features.

If you need to execute JavaScript for testing, write tests in test_selenium.py. 
"""

testFolder = os.path.dirname(os.path.abspath(__file__))


def callback_testResponse(websiteUrl):
	response = requests.get(websiteUrl, verify=True)
	if response.status_code != 200:
		pytest.fail(str(response.status_code) + ' ' + response.reason)


def test_websiteEmptyStart(dbFilePath):
	try:
		if os.path.exists(dbFilePath):
			os.remove(dbFilePath)
	except Exception as e:
		pytest.skip(str(e))

	testUtils.startWebsite(callback_testResponse)



# Allow the file to be run by itself, not in the pytest environment.
# It's for easy development.
if __name__ == "__main__":
	test_websiteEmptyStart()
