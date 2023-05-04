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
from avacloud_client_python.api.aslv_conversion_api import AslvConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestAslvConversionApi(unittest.TestCase):
    """AslvConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.aslv_conversion_api.AslvConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aslv_conversion_convert_to_ava(self):
        """Test case for aslv_conversion_convert_to_ava

        Converts Aslv files to Dangl.AVA projects  # noqa: E501
        """
        pass

    def test_aslv_conversion_convert_to_excel(self):
        """Test case for aslv_conversion_convert_to_excel

        Converts Aslv files to Excel  # noqa: E501
        """
        pass

    def test_aslv_conversion_convert_to_gaeb(self):
        """Test case for aslv_conversion_convert_to_gaeb

        Converts Aslv files to GAEB files  # noqa: E501
        """
        pass

    def test_aslv_conversion_convert_to_oenorm(self):
        """Test case for aslv_conversion_convert_to_oenorm

        Converts Aslv files to Oenorm files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
