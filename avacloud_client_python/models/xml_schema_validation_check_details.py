# coding: utf-8

"""
    AVACloud API 1.41.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class XmlSchemaValidationCheckDetails(object):
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
        'line_number': 'int',
        'line_position': 'int'
    }

    attribute_map = {
        'line_number': 'lineNumber',
        'line_position': 'linePosition'
    }

    def __init__(self, line_number=None, line_position=None, _configuration=None):  # noqa: E501
        """XmlSchemaValidationCheckDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._line_number = None
        self._line_position = None
        self.discriminator = None

        self.line_number = line_number
        self.line_position = line_position

    @property
    def line_number(self):
        """Gets the line_number of this XmlSchemaValidationCheckDetails.  # noqa: E501

        The line number on which the validation happened  # noqa: E501

        :return: The line_number of this XmlSchemaValidationCheckDetails.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this XmlSchemaValidationCheckDetails.

        The line number on which the validation happened  # noqa: E501

        :param line_number: The line_number of this XmlSchemaValidationCheckDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and line_number is None:
            raise ValueError("Invalid value for `line_number`, must not be `None`")  # noqa: E501

        self._line_number = line_number

    @property
    def line_position(self):
        """Gets the line_position of this XmlSchemaValidationCheckDetails.  # noqa: E501

        The position in the line  # noqa: E501

        :return: The line_position of this XmlSchemaValidationCheckDetails.  # noqa: E501
        :rtype: int
        """
        return self._line_position

    @line_position.setter
    def line_position(self, line_position):
        """Sets the line_position of this XmlSchemaValidationCheckDetails.

        The position in the line  # noqa: E501

        :param line_position: The line_position of this XmlSchemaValidationCheckDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and line_position is None:
            raise ValueError("Invalid value for `line_position`, must not be `None`")  # noqa: E501

        self._line_position = line_position

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(XmlSchemaValidationCheckDetails, dict):
            for key, value in self.items():
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
        if not isinstance(other, XmlSchemaValidationCheckDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XmlSchemaValidationCheckDetails):
            return True

        return self.to_dict() != other.to_dict()
