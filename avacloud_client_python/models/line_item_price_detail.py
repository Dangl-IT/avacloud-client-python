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


class LineItemPriceDetail(object):
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
        'net_price': 'float',
        'discount': 'float',
        'gross_price': 'float',
        'base_quantity': 'float',
        'base_quantity_unit_code': 'str'
    }

    attribute_map = {
        'net_price': 'netPrice',
        'discount': 'discount',
        'gross_price': 'grossPrice',
        'base_quantity': 'baseQuantity',
        'base_quantity_unit_code': 'baseQuantityUnitCode'
    }

    def __init__(self, net_price=None, discount=None, gross_price=None, base_quantity=None, base_quantity_unit_code=None, _configuration=None):  # noqa: E501
        """LineItemPriceDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._net_price = None
        self._discount = None
        self._gross_price = None
        self._base_quantity = None
        self._base_quantity_unit_code = None
        self.discriminator = None

        if net_price is not None:
            self.net_price = net_price
        if discount is not None:
            self.discount = discount
        if gross_price is not None:
            self.gross_price = gross_price
        if base_quantity is not None:
            self.base_quantity = base_quantity
        if base_quantity_unit_code is not None:
            self.base_quantity_unit_code = base_quantity_unit_code

    @property
    def net_price(self):
        """Gets the net_price of this LineItemPriceDetail.  # noqa: E501


        :return: The net_price of this LineItemPriceDetail.  # noqa: E501
        :rtype: float
        """
        return self._net_price

    @net_price.setter
    def net_price(self, net_price):
        """Sets the net_price of this LineItemPriceDetail.


        :param net_price: The net_price of this LineItemPriceDetail.  # noqa: E501
        :type: float
        """

        self._net_price = net_price

    @property
    def discount(self):
        """Gets the discount of this LineItemPriceDetail.  # noqa: E501


        :return: The discount of this LineItemPriceDetail.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this LineItemPriceDetail.


        :param discount: The discount of this LineItemPriceDetail.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def gross_price(self):
        """Gets the gross_price of this LineItemPriceDetail.  # noqa: E501


        :return: The gross_price of this LineItemPriceDetail.  # noqa: E501
        :rtype: float
        """
        return self._gross_price

    @gross_price.setter
    def gross_price(self, gross_price):
        """Sets the gross_price of this LineItemPriceDetail.


        :param gross_price: The gross_price of this LineItemPriceDetail.  # noqa: E501
        :type: float
        """

        self._gross_price = gross_price

    @property
    def base_quantity(self):
        """Gets the base_quantity of this LineItemPriceDetail.  # noqa: E501


        :return: The base_quantity of this LineItemPriceDetail.  # noqa: E501
        :rtype: float
        """
        return self._base_quantity

    @base_quantity.setter
    def base_quantity(self, base_quantity):
        """Sets the base_quantity of this LineItemPriceDetail.


        :param base_quantity: The base_quantity of this LineItemPriceDetail.  # noqa: E501
        :type: float
        """

        self._base_quantity = base_quantity

    @property
    def base_quantity_unit_code(self):
        """Gets the base_quantity_unit_code of this LineItemPriceDetail.  # noqa: E501


        :return: The base_quantity_unit_code of this LineItemPriceDetail.  # noqa: E501
        :rtype: str
        """
        return self._base_quantity_unit_code

    @base_quantity_unit_code.setter
    def base_quantity_unit_code(self, base_quantity_unit_code):
        """Sets the base_quantity_unit_code of this LineItemPriceDetail.


        :param base_quantity_unit_code: The base_quantity_unit_code of this LineItemPriceDetail.  # noqa: E501
        :type: str
        """

        self._base_quantity_unit_code = base_quantity_unit_code

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
        if issubclass(LineItemPriceDetail, dict):
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
        if not isinstance(other, LineItemPriceDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineItemPriceDetail):
            return True

        return self.to_dict() != other.to_dict()
