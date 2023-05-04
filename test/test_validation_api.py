# coding: utf-8

"""
    AVACloud API 1.41.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.validation_api import ValidationApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestValidationApi(unittest.TestCase):
    """ValidationApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.validation_api.ValidationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_validation_validate_file(self):
        """Test case for validation_validate_file

        This endpoint validates AVA files, typically GAEB or ÖNorm. The type of file needs to be provided as a query parameter, since there is no auto detection of the uploaded file type.  # noqa: E501
        """
        pass

    def test_validation_validate_project(self):
        """Test case for validation_validate_project

        This endpoint provides a full validation of a provided ProjectDto. It will take the given exchange phase into account and do some general project validation. Optionally, a conversion to a desired target can also be done, in which case the target file will also be validated.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
