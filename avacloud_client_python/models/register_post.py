# coding: utf-8

"""
    AVACloud API 1.17.3

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.17.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RegisterPost(object):
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
        'username': 'str',
        'email': 'str',
        'password': 'str',
        'preferred_languages': 'list[str]'
    }

    attribute_map = {
        'username': 'username',
        'email': 'email',
        'password': 'password',
        'preferred_languages': 'preferredLanguages'
    }

    def __init__(self, username=None, email=None, password=None, preferred_languages=None):  # noqa: E501
        """RegisterPost - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._email = None
        self._password = None
        self._preferred_languages = None
        self.discriminator = None

        self.username = username
        self.email = email
        self.password = password
        if preferred_languages is not None:
            self.preferred_languages = preferred_languages

    @property
    def username(self):
        """Gets the username of this RegisterPost.  # noqa: E501


        :return: The username of this RegisterPost.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RegisterPost.


        :param username: The username of this RegisterPost.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this RegisterPost.  # noqa: E501


        :return: The email of this RegisterPost.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RegisterPost.


        :param email: The email of this RegisterPost.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this RegisterPost.  # noqa: E501


        :return: The password of this RegisterPost.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegisterPost.


        :param password: The password of this RegisterPost.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) < 10:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `10`")  # noqa: E501

        self._password = password

    @property
    def preferred_languages(self):
        """Gets the preferred_languages of this RegisterPost.  # noqa: E501


        :return: The preferred_languages of this RegisterPost.  # noqa: E501
        :rtype: list[str]
        """
        return self._preferred_languages

    @preferred_languages.setter
    def preferred_languages(self, preferred_languages):
        """Sets the preferred_languages of this RegisterPost.


        :param preferred_languages: The preferred_languages of this RegisterPost.  # noqa: E501
        :type: list[str]
        """

        self._preferred_languages = preferred_languages

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
        if issubclass(RegisterPost, dict):
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
        if not isinstance(other, RegisterPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
