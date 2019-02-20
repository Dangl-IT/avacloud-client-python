# coding: utf-8

"""
    AVACloud API 1.5.3

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import avacloud_client_python
from avacloud_client_python.api.oenorm_conversion_api import OenormConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestOenormConversionApi(unittest.TestCase):
    """OenormConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.oenorm_conversion_api.OenormConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_oenorm_conversion_convert_to_ava(self):
        """Test case for oenorm_conversion_convert_to_ava

        Converts ÖNorm files to Dangl.AVA projects  # noqa: E501
        """
        pass

    def test_oenorm_conversion_convert_to_excel(self):
        """Test case for oenorm_conversion_convert_to_excel

        Converts ÖNorm files to Excel  # noqa: E501
        """
        pass

    def test_oenorm_conversion_convert_to_gaeb(self):
        """Test case for oenorm_conversion_convert_to_gaeb

        Converts ÖNorm files to GAEB files.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
