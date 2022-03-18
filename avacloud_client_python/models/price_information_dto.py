# coding: utf-8

"""
    AVACloud API 1.26.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class PriceInformationDto(object):
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
        'hourly_wage': 'float',
        'deduction_factor': 'float',
        'flat_sum': 'float',
        'tax_rate': 'float',
        'trade_discounts': 'list[TradeDiscountDto]'
    }

    attribute_map = {
        'id': 'id',
        'hourly_wage': 'hourlyWage',
        'deduction_factor': 'deductionFactor',
        'flat_sum': 'flatSum',
        'tax_rate': 'taxRate',
        'trade_discounts': 'tradeDiscounts'
    }

    def __init__(self, id=None, hourly_wage=None, deduction_factor=None, flat_sum=None, tax_rate=None, trade_discounts=None, _configuration=None):  # noqa: E501
        """PriceInformationDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._hourly_wage = None
        self._deduction_factor = None
        self._flat_sum = None
        self._tax_rate = None
        self._trade_discounts = None
        self.discriminator = None

        self.id = id
        self.hourly_wage = hourly_wage
        self.deduction_factor = deduction_factor
        self.flat_sum = flat_sum
        self.tax_rate = tax_rate
        if trade_discounts is not None:
            self.trade_discounts = trade_discounts

    @property
    def id(self):
        """Gets the id of this PriceInformationDto.  # noqa: E501

        Elements GUID identifier.  # noqa: E501

        :return: The id of this PriceInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PriceInformationDto.

        Elements GUID identifier.  # noqa: E501

        :param id: The id of this PriceInformationDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def hourly_wage(self):
        """Gets the hourly_wage of this PriceInformationDto.  # noqa: E501

        The amount of currency per one hour of manual labour work in this project.  # noqa: E501

        :return: The hourly_wage of this PriceInformationDto.  # noqa: E501
        :rtype: float
        """
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, hourly_wage):
        """Sets the hourly_wage of this PriceInformationDto.

        The amount of currency per one hour of manual labour work in this project.  # noqa: E501

        :param hourly_wage: The hourly_wage of this PriceInformationDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and hourly_wage is None:
            raise ValueError("Invalid value for `hourly_wage`, must not be `None`")  # noqa: E501

        self._hourly_wage = hourly_wage

    @property
    def deduction_factor(self):
        """Gets the deduction_factor of this PriceInformationDto.  # noqa: E501

        The final, total price will be deducted by this rate.  # noqa: E501

        :return: The deduction_factor of this PriceInformationDto.  # noqa: E501
        :rtype: float
        """
        return self._deduction_factor

    @deduction_factor.setter
    def deduction_factor(self, deduction_factor):
        """Sets the deduction_factor of this PriceInformationDto.

        The final, total price will be deducted by this rate.  # noqa: E501

        :param deduction_factor: The deduction_factor of this PriceInformationDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and deduction_factor is None:
            raise ValueError("Invalid value for `deduction_factor`, must not be `None`")  # noqa: E501

        self._deduction_factor = deduction_factor

    @property
    def flat_sum(self):
        """Gets the flat_sum of this PriceInformationDto.  # noqa: E501

        This is given when there is only one flat price for the whole service specification.  # noqa: E501

        :return: The flat_sum of this PriceInformationDto.  # noqa: E501
        :rtype: float
        """
        return self._flat_sum

    @flat_sum.setter
    def flat_sum(self, flat_sum):
        """Sets the flat_sum of this PriceInformationDto.

        This is given when there is only one flat price for the whole service specification.  # noqa: E501

        :param flat_sum: The flat_sum of this PriceInformationDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and flat_sum is None:
            raise ValueError("Invalid value for `flat_sum`, must not be `None`")  # noqa: E501

        self._flat_sum = flat_sum

    @property
    def tax_rate(self):
        """Gets the tax_rate of this PriceInformationDto.  # noqa: E501

        Global tax rate for the project. Note that certain elements may have a different, specific tax rate.  # noqa: E501

        :return: The tax_rate of this PriceInformationDto.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this PriceInformationDto.

        Global tax rate for the project. Note that certain elements may have a different, specific tax rate.  # noqa: E501

        :param tax_rate: The tax_rate of this PriceInformationDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")  # noqa: E501

        self._tax_rate = tax_rate

    @property
    def trade_discounts(self):
        """Gets the trade_discounts of this PriceInformationDto.  # noqa: E501

        Trade discounts for offered in this ServiceSpecification.  # noqa: E501

        :return: The trade_discounts of this PriceInformationDto.  # noqa: E501
        :rtype: list[TradeDiscountDto]
        """
        return self._trade_discounts

    @trade_discounts.setter
    def trade_discounts(self, trade_discounts):
        """Sets the trade_discounts of this PriceInformationDto.

        Trade discounts for offered in this ServiceSpecification.  # noqa: E501

        :param trade_discounts: The trade_discounts of this PriceInformationDto.  # noqa: E501
        :type: list[TradeDiscountDto]
        """

        self._trade_discounts = trade_discounts

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
        if issubclass(PriceInformationDto, dict):
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
        if not isinstance(other, PriceInformationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriceInformationDto):
            return True

        return self.to_dict() != other.to_dict()
