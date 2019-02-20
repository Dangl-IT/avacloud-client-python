# coding: utf-8

"""
    AVACloud API 1.5.3

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TradeDiscountDto(object):
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
        'id': 'str',
        'deadline': 'int',
        'rate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'deadline': 'deadline',
        'rate': 'rate'
    }

    def __init__(self, id=None, deadline=None, rate=None):  # noqa: E501
        """TradeDiscountDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._deadline = None
        self._rate = None
        self.discriminator = None

        self.id = id
        self.deadline = deadline
        self.rate = rate

    @property
    def id(self):
        """Gets the id of this TradeDiscountDto.  # noqa: E501


        :return: The id of this TradeDiscountDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TradeDiscountDto.


        :param id: The id of this TradeDiscountDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def deadline(self):
        """Gets the deadline of this TradeDiscountDto.  # noqa: E501


        :return: The deadline of this TradeDiscountDto.  # noqa: E501
        :rtype: int
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this TradeDiscountDto.


        :param deadline: The deadline of this TradeDiscountDto.  # noqa: E501
        :type: int
        """
        if deadline is None:
            raise ValueError("Invalid value for `deadline`, must not be `None`")  # noqa: E501

        self._deadline = deadline

    @property
    def rate(self):
        """Gets the rate of this TradeDiscountDto.  # noqa: E501


        :return: The rate of this TradeDiscountDto.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this TradeDiscountDto.


        :param rate: The rate of this TradeDiscountDto.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

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
        if issubclass(TradeDiscountDto, dict):
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
        if not isinstance(other, TradeDiscountDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
