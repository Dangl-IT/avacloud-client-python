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


class InvoiceAllowance(object):
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
        'net_amount': 'float',
        'relative_allowance_base_amount': 'float',
        'relative_allowance_percentage': 'float',
        'vat_category': 'VatCategory',
        'vat_rate': 'float',
        'reason': 'str',
        'reason_code': 'str'
    }

    attribute_map = {
        'net_amount': 'netAmount',
        'relative_allowance_base_amount': 'relativeAllowanceBaseAmount',
        'relative_allowance_percentage': 'relativeAllowancePercentage',
        'vat_category': 'vatCategory',
        'vat_rate': 'vatRate',
        'reason': 'reason',
        'reason_code': 'reasonCode'
    }

    def __init__(self, net_amount=None, relative_allowance_base_amount=None, relative_allowance_percentage=None, vat_category=None, vat_rate=None, reason=None, reason_code=None, _configuration=None):  # noqa: E501
        """InvoiceAllowance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._net_amount = None
        self._relative_allowance_base_amount = None
        self._relative_allowance_percentage = None
        self._vat_category = None
        self._vat_rate = None
        self._reason = None
        self._reason_code = None
        self.discriminator = None

        if net_amount is not None:
            self.net_amount = net_amount
        if relative_allowance_base_amount is not None:
            self.relative_allowance_base_amount = relative_allowance_base_amount
        if relative_allowance_percentage is not None:
            self.relative_allowance_percentage = relative_allowance_percentage
        self.vat_category = vat_category
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if reason is not None:
            self.reason = reason
        if reason_code is not None:
            self.reason_code = reason_code

    @property
    def net_amount(self):
        """Gets the net_amount of this InvoiceAllowance.  # noqa: E501


        :return: The net_amount of this InvoiceAllowance.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this InvoiceAllowance.


        :param net_amount: The net_amount of this InvoiceAllowance.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def relative_allowance_base_amount(self):
        """Gets the relative_allowance_base_amount of this InvoiceAllowance.  # noqa: E501


        :return: The relative_allowance_base_amount of this InvoiceAllowance.  # noqa: E501
        :rtype: float
        """
        return self._relative_allowance_base_amount

    @relative_allowance_base_amount.setter
    def relative_allowance_base_amount(self, relative_allowance_base_amount):
        """Sets the relative_allowance_base_amount of this InvoiceAllowance.


        :param relative_allowance_base_amount: The relative_allowance_base_amount of this InvoiceAllowance.  # noqa: E501
        :type: float
        """

        self._relative_allowance_base_amount = relative_allowance_base_amount

    @property
    def relative_allowance_percentage(self):
        """Gets the relative_allowance_percentage of this InvoiceAllowance.  # noqa: E501


        :return: The relative_allowance_percentage of this InvoiceAllowance.  # noqa: E501
        :rtype: float
        """
        return self._relative_allowance_percentage

    @relative_allowance_percentage.setter
    def relative_allowance_percentage(self, relative_allowance_percentage):
        """Sets the relative_allowance_percentage of this InvoiceAllowance.


        :param relative_allowance_percentage: The relative_allowance_percentage of this InvoiceAllowance.  # noqa: E501
        :type: float
        """

        self._relative_allowance_percentage = relative_allowance_percentage

    @property
    def vat_category(self):
        """Gets the vat_category of this InvoiceAllowance.  # noqa: E501


        :return: The vat_category of this InvoiceAllowance.  # noqa: E501
        :rtype: VatCategory
        """
        return self._vat_category

    @vat_category.setter
    def vat_category(self, vat_category):
        """Sets the vat_category of this InvoiceAllowance.


        :param vat_category: The vat_category of this InvoiceAllowance.  # noqa: E501
        :type: VatCategory
        """
        if self._configuration.client_side_validation and vat_category is None:
            raise ValueError("Invalid value for `vat_category`, must not be `None`")  # noqa: E501

        self._vat_category = vat_category

    @property
    def vat_rate(self):
        """Gets the vat_rate of this InvoiceAllowance.  # noqa: E501


        :return: The vat_rate of this InvoiceAllowance.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this InvoiceAllowance.


        :param vat_rate: The vat_rate of this InvoiceAllowance.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

    @property
    def reason(self):
        """Gets the reason of this InvoiceAllowance.  # noqa: E501


        :return: The reason of this InvoiceAllowance.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this InvoiceAllowance.


        :param reason: The reason of this InvoiceAllowance.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def reason_code(self):
        """Gets the reason_code of this InvoiceAllowance.  # noqa: E501


        :return: The reason_code of this InvoiceAllowance.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this InvoiceAllowance.


        :param reason_code: The reason_code of this InvoiceAllowance.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

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
        if issubclass(InvoiceAllowance, dict):
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
        if not isinstance(other, InvoiceAllowance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceAllowance):
            return True

        return self.to_dict() != other.to_dict()