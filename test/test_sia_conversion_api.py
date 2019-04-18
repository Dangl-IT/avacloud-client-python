# coding: utf-8

"""
    AVACloud API 1.7.5

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.7.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.sia_conversion_api import SiaConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestSiaConversionApi(unittest.TestCase):
    """SiaConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.sia_conversion_api.SiaConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sia_conversion_convert_to_ava(self):
        """Test case for sia_conversion_convert_to_ava

        Converts SIA 451 files to Dangl.AVA projects  # noqa: E501
        """
        pass

    def test_sia_conversion_convert_to_excel(self):
        """Test case for sia_conversion_convert_to_excel

        Converts SIA 451 files to Excel  # noqa: E501
        """
        pass

    def test_sia_conversion_convert_to_gaeb(self):
        """Test case for sia_conversion_convert_to_gaeb

        Converts SIA 451 files to GAEB files  # noqa: E501
        """
        pass

    def test_sia_conversion_convert_to_oenorm(self):
        """Test case for sia_conversion_convert_to_oenorm

        Converts SIA 451 files to Oenorm files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()