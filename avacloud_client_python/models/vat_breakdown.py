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


class VatBreakdown(object):
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
        'net_taxable_amount': 'float',
        'vat_amount': 'float',
        'vat_category': 'VatCategory',
        'tax_rate': 'float',
        'vat_exemption_reason_text': 'str',
        'vat_exemption_reason_code': 'str'
    }

    attribute_map = {
        'net_taxable_amount': 'netTaxableAmount',
        'vat_amount': 'vatAmount',
        'vat_category': 'vatCategory',
        'tax_rate': 'taxRate',
        'vat_exemption_reason_text': 'vatExemptionReasonText',
        'vat_exemption_reason_code': 'vatExemptionReasonCode'
    }

    def __init__(self, net_taxable_amount=None, vat_amount=None, vat_category=None, tax_rate=None, vat_exemption_reason_text=None, vat_exemption_reason_code=None, _configuration=None):  # noqa: E501
        """VatBreakdown - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._net_taxable_amount = None
        self._vat_amount = None
        self._vat_category = None
        self._tax_rate = None
        self._vat_exemption_reason_text = None
        self._vat_exemption_reason_code = None
        self.discriminator = None

        if net_taxable_amount is not None:
            self.net_taxable_amount = net_taxable_amount
        if vat_amount is not None:
            self.vat_amount = vat_amount
        self.vat_category = vat_category
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if vat_exemption_reason_text is not None:
            self.vat_exemption_reason_text = vat_exemption_reason_text
        if vat_exemption_reason_code is not None:
            self.vat_exemption_reason_code = vat_exemption_reason_code

    @property
    def net_taxable_amount(self):
        """Gets the net_taxable_amount of this VatBreakdown.  # noqa: E501


        :return: The net_taxable_amount of this VatBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._net_taxable_amount

    @net_taxable_amount.setter
    def net_taxable_amount(self, net_taxable_amount):
        """Sets the net_taxable_amount of this VatBreakdown.


        :param net_taxable_amount: The net_taxable_amount of this VatBreakdown.  # noqa: E501
        :type: float
        """

        self._net_taxable_amount = net_taxable_amount

    @property
    def vat_amount(self):
        """Gets the vat_amount of this VatBreakdown.  # noqa: E501


        :return: The vat_amount of this VatBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, vat_amount):
        """Sets the vat_amount of this VatBreakdown.


        :param vat_amount: The vat_amount of this VatBreakdown.  # noqa: E501
        :type: float
        """

        self._vat_amount = vat_amount

    @property
    def vat_category(self):
        """Gets the vat_category of this VatBreakdown.  # noqa: E501


        :return: The vat_category of this VatBreakdown.  # noqa: E501
        :rtype: VatCategory
        """
        return self._vat_category

    @vat_category.setter
    def vat_category(self, vat_category):
        """Sets the vat_category of this VatBreakdown.


        :param vat_category: The vat_category of this VatBreakdown.  # noqa: E501
        :type: VatCategory
        """
        if self._configuration.client_side_validation and vat_category is None:
            raise ValueError("Invalid value for `vat_category`, must not be `None`")  # noqa: E501

        self._vat_category = vat_category

    @property
    def tax_rate(self):
        """Gets the tax_rate of this VatBreakdown.  # noqa: E501


        :return: The tax_rate of this VatBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this VatBreakdown.


        :param tax_rate: The tax_rate of this VatBreakdown.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def vat_exemption_reason_text(self):
        """Gets the vat_exemption_reason_text of this VatBreakdown.  # noqa: E501


        :return: The vat_exemption_reason_text of this VatBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._vat_exemption_reason_text

    @vat_exemption_reason_text.setter
    def vat_exemption_reason_text(self, vat_exemption_reason_text):
        """Sets the vat_exemption_reason_text of this VatBreakdown.


        :param vat_exemption_reason_text: The vat_exemption_reason_text of this VatBreakdown.  # noqa: E501
        :type: str
        """

        self._vat_exemption_reason_text = vat_exemption_reason_text

    @property
    def vat_exemption_reason_code(self):
        """Gets the vat_exemption_reason_code of this VatBreakdown.  # noqa: E501


        :return: The vat_exemption_reason_code of this VatBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._vat_exemption_reason_code

    @vat_exemption_reason_code.setter
    def vat_exemption_reason_code(self, vat_exemption_reason_code):
        """Sets the vat_exemption_reason_code of this VatBreakdown.


        :param vat_exemption_reason_code: The vat_exemption_reason_code of this VatBreakdown.  # noqa: E501
        :type: str
        """

        self._vat_exemption_reason_code = vat_exemption_reason_code

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
        if issubclass(VatBreakdown, dict):
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
        if not isinstance(other, VatBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VatBreakdown):
            return True

        return self.to_dict() != other.to_dict()
