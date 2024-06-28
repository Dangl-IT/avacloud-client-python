# coding: utf-8

"""
    AVACloud API 1.52.1

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.52.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class PostAvaSourceOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'try_auto_generate_item_numbers_and_schema': 'bool'
    }

    attribute_map = {
        'try_auto_generate_item_numbers_and_schema': 'tryAutoGenerateItemNumbersAndSchema'
    }

    def __init__(self, try_auto_generate_item_numbers_and_schema=None, _configuration=None):  # noqa: E501
        """PostAvaSourceOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._try_auto_generate_item_numbers_and_schema = None
        self.discriminator = None

        self.try_auto_generate_item_numbers_and_schema = try_auto_generate_item_numbers_and_schema

    @property
    def try_auto_generate_item_numbers_and_schema(self):
        """Gets the try_auto_generate_item_numbers_and_schema of this PostAvaSourceOptions.  # noqa: E501

        If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number.  # noqa: E501

        :return: The try_auto_generate_item_numbers_and_schema of this PostAvaSourceOptions.  # noqa: E501
        :rtype: bool
        """
        return self._try_auto_generate_item_numbers_and_schema

    @try_auto_generate_item_numbers_and_schema.setter
    def try_auto_generate_item_numbers_and_schema(self, try_auto_generate_item_numbers_and_schema):
        """Sets the try_auto_generate_item_numbers_and_schema of this PostAvaSourceOptions.

        If this is set to true, AVACloud will try to generate item numbers and an item number schema automatically for the input project. The operation will not have any effect if either an item number schema is already present, or if any of the elements already has an item number.  # noqa: E501

        :param try_auto_generate_item_numbers_and_schema: The try_auto_generate_item_numbers_and_schema of this PostAvaSourceOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and try_auto_generate_item_numbers_and_schema is None:
            raise ValueError("Invalid value for `try_auto_generate_item_numbers_and_schema`, must not be `None`")  # noqa: E501

        self._try_auto_generate_item_numbers_and_schema = try_auto_generate_item_numbers_and_schema

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value
        if issubclass(PostAvaSourceOptions, dict):
            for key, value in list(self.items()):
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostAvaSourceOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostAvaSourceOptions):
            return True

        return self.to_dict() != other.to_dict()
