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


class ForgotPasswordPost(object):
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
        'identifier': 'str',
        'preferred_languages': 'list[str]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'preferred_languages': 'preferredLanguages'
    }

    def __init__(self, identifier=None, preferred_languages=None, _configuration=None):  # noqa: E501
        """ForgotPasswordPost - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifier = None
        self._preferred_languages = None
        self.discriminator = None

        self.identifier = identifier
        if preferred_languages is not None:
            self.preferred_languages = preferred_languages

    @property
    def identifier(self):
        """Gets the identifier of this ForgotPasswordPost.  # noqa: E501


        :return: The identifier of this ForgotPasswordPost.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ForgotPasswordPost.


        :param identifier: The identifier of this ForgotPasswordPost.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                identifier is not None and len(identifier) < 1):
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._identifier = identifier

    @property
    def preferred_languages(self):
        """Gets the preferred_languages of this ForgotPasswordPost.  # noqa: E501


        :return: The preferred_languages of this ForgotPasswordPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._preferred_languages

    @preferred_languages.setter
    def preferred_languages(self, preferred_languages):
        """Sets the preferred_languages of this ForgotPasswordPost.


        :param preferred_languages: The preferred_languages of this ForgotPasswordPost.  # noqa: E501
        :type: list[str]
        """

        self._preferred_languages = preferred_languages

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
        if issubclass(ForgotPasswordPost, dict):
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
        if not isinstance(other, ForgotPasswordPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForgotPasswordPost):
            return True

        return self.to_dict() != other.to_dict()

