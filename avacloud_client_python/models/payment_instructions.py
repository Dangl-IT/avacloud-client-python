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


class PaymentInstructions(object):
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
        'description': 'str',
        'payment_type_code': 'str',
        'payment_means': 'list[PaymentMeans]'
    }

    attribute_map = {
        'description': 'description',
        'payment_type_code': 'paymentTypeCode',
        'payment_means': 'paymentMeans'
    }

    def __init__(self, description=None, payment_type_code=None, payment_means=None, _configuration=None):  # noqa: E501
        """PaymentInstructions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._payment_type_code = None
        self._payment_means = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if payment_type_code is not None:
            self.payment_type_code = payment_type_code
        if payment_means is not None:
            self.payment_means = payment_means

    @property
    def description(self):
        """Gets the description of this PaymentInstructions.  # noqa: E501


        :return: The description of this PaymentInstructions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentInstructions.


        :param description: The description of this PaymentInstructions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def payment_type_code(self):
        """Gets the payment_type_code of this PaymentInstructions.  # noqa: E501


        :return: The payment_type_code of this PaymentInstructions.  # noqa: E501
        :rtype: str
        """
        return self._payment_type_code

    @payment_type_code.setter
    def payment_type_code(self, payment_type_code):
        """Sets the payment_type_code of this PaymentInstructions.


        :param payment_type_code: The payment_type_code of this PaymentInstructions.  # noqa: E501
        :type: str
        """

        self._payment_type_code = payment_type_code

    @property
    def payment_means(self):
        """Gets the payment_means of this PaymentInstructions.  # noqa: E501


        :return: The payment_means of this PaymentInstructions.  # noqa: E501
        :rtype: list[PaymentMeans]
        """
        return self._payment_means

    @payment_means.setter
    def payment_means(self, payment_means):
        """Sets the payment_means of this PaymentInstructions.


        :param payment_means: The payment_means of this PaymentInstructions.  # noqa: E501
        :type: list[PaymentMeans]
        """

        self._payment_means = payment_means

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
        if issubclass(PaymentInstructions, dict):
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
        if not isinstance(other, PaymentInstructions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentInstructions):
            return True

        return self.to_dict() != other.to_dict()
