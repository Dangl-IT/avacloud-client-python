# coding: utf-8

"""
    AVACloud API 1.30.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.30.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class ApiError(object):
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
        'errors': 'dict(str, list[str])'
    }

    attribute_map = {
        'errors': 'errors'
    }

    def __init__(self, errors=None, _configuration=None):  # noqa: E501
        """ApiError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._errors = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors

    @property
    def errors(self):
        """Gets the errors of this ApiError.  # noqa: E501

        This dictionary contains a set of all errors and their messages  # noqa: E501

        :return: The errors of this ApiError.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ApiError.

        This dictionary contains a set of all errors and their messages  # noqa: E501

        :param errors: The errors of this ApiError.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._errors = errors

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
        if issubclass(ApiError, dict):
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
        if not isinstance(other, ApiError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiError):
            return True

        return self.to_dict() != other.to_dict()

