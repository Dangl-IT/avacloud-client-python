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


class LabourPriceComponentDto(object):
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
        'label': 'str',
        'price': 'float',
        'hourly_wage': 'float',
        'values': 'list[CalculationDto]',
        'use_own_hourly_wage': 'bool',
        'total_time': 'float'
    }

    attribute_map = {
        'label': 'label',
        'price': 'price',
        'hourly_wage': 'hourlyWage',
        'values': 'values',
        'use_own_hourly_wage': 'useOwnHourlyWage',
        'total_time': 'totalTime'
    }

    def __init__(self, label=None, price=None, hourly_wage=None, values=None, use_own_hourly_wage=None, total_time=None):  # noqa: E501
        """LabourPriceComponentDto - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._price = None
        self._hourly_wage = None
        self._values = None
        self._use_own_hourly_wage = None
        self._total_time = None
        self.discriminator = None

        if label is not None:
            self.label = label
        self.price = price
        self.hourly_wage = hourly_wage
        if values is not None:
            self.values = values
        self.use_own_hourly_wage = use_own_hourly_wage
        self.total_time = total_time

    @property
    def label(self):
        """Gets the label of this LabourPriceComponentDto.  # noqa: E501

        The label associated with this price component. Will be taken from the parent Projects ProjectInformation.  # noqa: E501

        :return: The label of this LabourPriceComponentDto.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabourPriceComponentDto.

        The label associated with this price component. Will be taken from the parent Projects ProjectInformation.  # noqa: E501

        :param label: The label of this LabourPriceComponentDto.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def price(self):
        """Gets the price of this LabourPriceComponentDto.  # noqa: E501

        The total, calculated price of this component. Will multiply the calculated amount of hours with the ServiceSpecifications hourly wage rate.  # noqa: E501

        :return: The price of this LabourPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LabourPriceComponentDto.

        The total, calculated price of this component. Will multiply the calculated amount of hours with the ServiceSpecifications hourly wage rate.  # noqa: E501

        :param price: The price of this LabourPriceComponentDto.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def hourly_wage(self):
        """Gets the hourly_wage of this LabourPriceComponentDto.  # noqa: E501

        The cost per hour of manual labor.  # noqa: E501

        :return: The hourly_wage of this LabourPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, hourly_wage):
        """Sets the hourly_wage of this LabourPriceComponentDto.

        The cost per hour of manual labor.  # noqa: E501

        :param hourly_wage: The hourly_wage of this LabourPriceComponentDto.  # noqa: E501
        :type: float
        """
        if hourly_wage is None:
            raise ValueError("Invalid value for `hourly_wage`, must not be `None`")  # noqa: E501

        self._hourly_wage = hourly_wage

    @property
    def values(self):
        """Gets the values of this LabourPriceComponentDto.  # noqa: E501

        The single Calculation elements this price component is composed of.  # noqa: E501

        :return: The values of this LabourPriceComponentDto.  # noqa: E501
        :rtype: list[CalculationDto]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this LabourPriceComponentDto.

        The single Calculation elements this price component is composed of.  # noqa: E501

        :param values: The values of this LabourPriceComponentDto.  # noqa: E501
        :type: list[CalculationDto]
        """

        self._values = values

    @property
    def use_own_hourly_wage(self):
        """Gets the use_own_hourly_wage of this LabourPriceComponentDto.  # noqa: E501

        Indicates if the ServiceSpecification's standard HourlyWage is to be used or a custom value.  # noqa: E501

        :return: The use_own_hourly_wage of this LabourPriceComponentDto.  # noqa: E501
        :rtype: bool
        """
        return self._use_own_hourly_wage

    @use_own_hourly_wage.setter
    def use_own_hourly_wage(self, use_own_hourly_wage):
        """Sets the use_own_hourly_wage of this LabourPriceComponentDto.

        Indicates if the ServiceSpecification's standard HourlyWage is to be used or a custom value.  # noqa: E501

        :param use_own_hourly_wage: The use_own_hourly_wage of this LabourPriceComponentDto.  # noqa: E501
        :type: bool
        """
        if use_own_hourly_wage is None:
            raise ValueError("Invalid value for `use_own_hourly_wage`, must not be `None`")  # noqa: E501

        self._use_own_hourly_wage = use_own_hourly_wage

    @property
    def total_time(self):
        """Gets the total_time of this LabourPriceComponentDto.  # noqa: E501

        The total, calculated time of this component. Will return the result rounded to three decimal places.  # noqa: E501

        :return: The total_time of this LabourPriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this LabourPriceComponentDto.

        The total, calculated time of this component. Will return the result rounded to three decimal places.  # noqa: E501

        :param total_time: The total_time of this LabourPriceComponentDto.  # noqa: E501
        :type: float
        """
        if total_time is None:
            raise ValueError("Invalid value for `total_time`, must not be `None`")  # noqa: E501

        self._total_time = total_time

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
        if issubclass(LabourPriceComponentDto, dict):
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
        if not isinstance(other, LabourPriceComponentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
