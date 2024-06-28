# coding: utf-8

"""
    AVACloud API 1.52.1

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.52.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""




import unittest

import avacloud_client_python
from avacloud_client_python.api.gaeb_conversion_api import GaebConversionApi  # noqa: E501
from avacloud_client_python.rest import ApiException


class TestGaebConversionApi(unittest.TestCase):
    """GaebConversionApi unit test stubs"""

    def setUp(self):
        self.api = avacloud_client_python.api.gaeb_conversion_api.GaebConversionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gaeb_conversion_convert_to_ava(self):
        """Test case for gaeb_conversion_convert_to_ava

        Converts GAEB files to Dangl.AVA projects  # noqa: E501
        """
        pass

    def test_gaeb_conversion_convert_to_excel(self):
        """Test case for gaeb_conversion_convert_to_excel

        Converts GAEB files to Excel  # noqa: E501
        """
        pass

    def test_gaeb_conversion_convert_to_flat_ava(self):
        """Test case for gaeb_conversion_convert_to_flat_ava

        Converts GAEB files to Dangl.AVA projects  # noqa: E501
        """
        pass

    def test_gaeb_conversion_convert_to_gaeb(self):
        """Test case for gaeb_conversion_convert_to_gaeb

        Converts GAEB files to GAEB files. Used for example when transforming or repairing GAEB files.  # noqa: E501
        """
        pass

    def test_gaeb_conversion_convert_to_oenorm(self):
        """Test case for gaeb_conversion_convert_to_oenorm

        Converts GAEB files to Oenorm files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
