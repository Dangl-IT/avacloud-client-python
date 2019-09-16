# coding: utf-8

"""
    AVACloud API 1.10.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.reb_conversion_api import RebConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestRebConversionApi(unittest.TestCase):
    """RebConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.reb_conversion_api.RebConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reb_conversion_convert_to_ava(self):
        """Test case for reb_conversion_convert_to_ava

        Converts REB files to Dangl.AVA projects  # noqa: E501
        """
        pass

    def test_reb_conversion_convert_to_excel(self):
        """Test case for reb_conversion_convert_to_excel

        Converts REB files to Excel  # noqa: E501
        """
        pass

    def test_reb_conversion_convert_to_gaeb(self):
        """Test case for reb_conversion_convert_to_gaeb

        Converts REB files to GAEB files  # noqa: E501
        """
        pass

    def test_reb_conversion_convert_to_oenorm(self):
        """Test case for reb_conversion_convert_to_oenorm

        Converts REB files to Oenorm  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
