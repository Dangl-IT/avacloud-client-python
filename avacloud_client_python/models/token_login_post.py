# coding: utf-8

"""
    AVACloud API 1.12.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TokenLoginPost(object):
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
        'password': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'password': 'password'
    }

    def __init__(self, identifier=None, password=None):  # noqa: E501
        """TokenLoginPost - a model defined in Swagger"""  # noqa: E501

        self._identifier = None
        self._password = None
        self.discriminator = None

        self.identifier = identifier
        self.password = password

    @property
    def identifier(self):
        """Gets the identifier of this TokenLoginPost.  # noqa: E501


        :return: The identifier of this TokenLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TokenLoginPost.


        :param identifier: The identifier of this TokenLoginPost.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501
        if identifier is not None and len(identifier) < 1:
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._identifier = identifier

    @property
    def password(self):
        """Gets the password of this TokenLoginPost.  # noqa: E501


        :return: The password of this TokenLoginPost.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TokenLoginPost.


        :param password: The password of this TokenLoginPost.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

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
        if issubclass(TokenLoginPost, dict):
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
        if not isinstance(other, TokenLoginPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
