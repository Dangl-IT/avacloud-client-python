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


class GetStatus(object):
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
        'is_healthy': 'bool',
        'version': 'str',
        'environment': 'str'
    }

    attribute_map = {
        'is_healthy': 'isHealthy',
        'version': 'version',
        'environment': 'environment'
    }

    def __init__(self, is_healthy=None, version=None, environment=None, _configuration=None):  # noqa: E501
        """GetStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_healthy = None
        self._version = None
        self._environment = None
        self.discriminator = None

        self.is_healthy = is_healthy
        if version is not None:
            self.version = version
        if environment is not None:
            self.environment = environment

    @property
    def is_healthy(self):
        """Gets the is_healthy of this GetStatus.  # noqa: E501

        If any problems in the service health are known, this is set to false  # noqa: E501

        :return: The is_healthy of this GetStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """Sets the is_healthy of this GetStatus.

        If any problems in the service health are known, this is set to false  # noqa: E501

        :param is_healthy: The is_healthy of this GetStatus.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_healthy is None:
            raise ValueError("Invalid value for `is_healthy`, must not be `None`")  # noqa: E501

        self._is_healthy = is_healthy

    @property
    def version(self):
        """Gets the version of this GetStatus.  # noqa: E501

        The current version of the AVACloud service  # noqa: E501

        :return: The version of this GetStatus.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetStatus.

        The current version of the AVACloud service  # noqa: E501

        :param version: The version of this GetStatus.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def environment(self):
        """Gets the environment of this GetStatus.  # noqa: E501

        The environment of the current instance  # noqa: E501

        :return: The environment of this GetStatus.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this GetStatus.

        The environment of the current instance  # noqa: E501

        :param environment: The environment of this GetStatus.  # noqa: E501
        :type: str
        """

        self._environment = environment

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
        if issubclass(GetStatus, dict):
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
        if not isinstance(other, GetStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStatus):
            return True

        return self.to_dict() != other.to_dict()
