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


class ItemNumberSchemaTierDto(object):
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
        'length': 'int',
        'type': 'ItemNumberTypeDto',
        'tier_type': 'ItemNumberSchemaTierTypeDto',
        'is_lot': 'bool',
        'increment': 'int',
        'tier_name': 'str'
    }

    attribute_map = {
        'length': 'length',
        'type': 'type',
        'tier_type': 'tierType',
        'is_lot': 'isLot',
        'increment': 'increment',
        'tier_name': 'tierName'
    }

    def __init__(self, length=None, type=None, tier_type=None, is_lot=None, increment=None, tier_name=None, _configuration=None):  # noqa: E501
        """ItemNumberSchemaTierDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._length = None
        self._type = None
        self._tier_type = None
        self._is_lot = None
        self._increment = None
        self._tier_name = None
        self.discriminator = None

        self.length = length
        self.type = type
        self.tier_type = tier_type
        self.is_lot = is_lot
        self.increment = increment
        if tier_name is not None:
            self.tier_name = tier_name

    @property
    def length(self):
        """Gets the length of this ItemNumberSchemaTierDto.  # noqa: E501

        The (maximum) length for this tier. Will not accept a length less than 1. Defaults to 1 if length less than one is specified.  # noqa: E501

        :return: The length of this ItemNumberSchemaTierDto.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ItemNumberSchemaTierDto.

        The (maximum) length for this tier. Will not accept a length less than 1. Defaults to 1 if length less than one is specified.  # noqa: E501

        :param length: The length of this ItemNumberSchemaTierDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def type(self):
        """Gets the type of this ItemNumberSchemaTierDto.  # noqa: E501

        This ItemNumberSchemaTier's type.  # noqa: E501

        :return: The type of this ItemNumberSchemaTierDto.  # noqa: E501
        :rtype: ItemNumberTypeDto
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ItemNumberSchemaTierDto.

        This ItemNumberSchemaTier's type.  # noqa: E501

        :param type: The type of this ItemNumberSchemaTierDto.  # noqa: E501
        :type: ItemNumberTypeDto
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def tier_type(self):
        """Gets the tier_type of this ItemNumberSchemaTierDto.  # noqa: E501

        This specifies which ItemNumberSchemaTierType this tier represents. This can be, for example, a group tier / level, a position level or a lot level.  # noqa: E501

        :return: The tier_type of this ItemNumberSchemaTierDto.  # noqa: E501
        :rtype: ItemNumberSchemaTierTypeDto
        """
        return self._tier_type

    @tier_type.setter
    def tier_type(self, tier_type):
        """Sets the tier_type of this ItemNumberSchemaTierDto.

        This specifies which ItemNumberSchemaTierType this tier represents. This can be, for example, a group tier / level, a position level or a lot level.  # noqa: E501

        :param tier_type: The tier_type of this ItemNumberSchemaTierDto.  # noqa: E501
        :type: ItemNumberSchemaTierTypeDto
        """
        if self._configuration.client_side_validation and tier_type is None:
            raise ValueError("Invalid value for `tier_type`, must not be `None`")  # noqa: E501

        self._tier_type = tier_type

    @property
    def is_lot(self):
        """Gets the is_lot of this ItemNumberSchemaTierDto.  # noqa: E501

        Indicates if this tier represents a lot. See the documentation for more information about lots.  # noqa: E501

        :return: The is_lot of this ItemNumberSchemaTierDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_lot

    @is_lot.setter
    def is_lot(self, is_lot):
        """Sets the is_lot of this ItemNumberSchemaTierDto.

        Indicates if this tier represents a lot. See the documentation for more information about lots.  # noqa: E501

        :param is_lot: The is_lot of this ItemNumberSchemaTierDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_lot is None:
            raise ValueError("Invalid value for `is_lot`, must not be `None`")  # noqa: E501

        self._is_lot = is_lot

    @property
    def increment(self):
        """Gets the increment of this ItemNumberSchemaTierDto.  # noqa: E501

        This value is the increment, or step size, that should be used for new item numbers. It defaults to DEFAULT_INCREMENT, but can be changed to any other positive number greater than zero. Invalid values make this be set to one '1'  # noqa: E501

        :return: The increment of this ItemNumberSchemaTierDto.  # noqa: E501
        :rtype: int
        """
        return self._increment

    @increment.setter
    def increment(self, increment):
        """Sets the increment of this ItemNumberSchemaTierDto.

        This value is the increment, or step size, that should be used for new item numbers. It defaults to DEFAULT_INCREMENT, but can be changed to any other positive number greater than zero. Invalid values make this be set to one '1'  # noqa: E501

        :param increment: The increment of this ItemNumberSchemaTierDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and increment is None:
            raise ValueError("Invalid value for `increment`, must not be `None`")  # noqa: E501

        self._increment = increment

    @property
    def tier_name(self):
        """Gets the tier_name of this ItemNumberSchemaTierDto.  # noqa: E501

        This is an optional name for the given tier  # noqa: E501

        :return: The tier_name of this ItemNumberSchemaTierDto.  # noqa: E501
        :rtype: str
        """
        return self._tier_name

    @tier_name.setter
    def tier_name(self, tier_name):
        """Sets the tier_name of this ItemNumberSchemaTierDto.

        This is an optional name for the given tier  # noqa: E501

        :param tier_name: The tier_name of this ItemNumberSchemaTierDto.  # noqa: E501
        :type: str
        """

        self._tier_name = tier_name

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
        if issubclass(ItemNumberSchemaTierDto, dict):
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
        if not isinstance(other, ItemNumberSchemaTierDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemNumberSchemaTierDto):
            return True

        return self.to_dict() != other.to_dict()
