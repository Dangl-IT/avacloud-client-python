# coding: utf-8

"""
    AVACloud API 1.27.4

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.27.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class PriceComponentDto(object):
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
        'price': 'float',
        'label': 'str',
        'values': 'list[CalculationDto]',
        'project_catalogues': 'list[CatalogueDto]'
    }

    attribute_map = {
        'price': 'price',
        'label': 'label',
        'values': 'values',
        'project_catalogues': 'projectCatalogues'
    }

    def __init__(self, price=None, label=None, values=None, project_catalogues=None, _configuration=None):  # noqa: E501
        """PriceComponentDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._price = None
        self._label = None
        self._values = None
        self._project_catalogues = None
        self.discriminator = None

        self.price = price
        if label is not None:
            self.label = label
        if values is not None:
            self.values = values
        if project_catalogues is not None:
            self.project_catalogues = project_catalogues

    @property
    def price(self):
        """Gets the price of this PriceComponentDto.  # noqa: E501

        The total, calculated price of this component.  # noqa: E501

        :return: The price of this PriceComponentDto.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PriceComponentDto.

        The total, calculated price of this component.  # noqa: E501

        :param price: The price of this PriceComponentDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def label(self):
        """Gets the label of this PriceComponentDto.  # noqa: E501

        The label associated with this price component. Will be taken from the parent Projects ProjectInformation.  # noqa: E501

        :return: The label of this PriceComponentDto.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PriceComponentDto.

        The label associated with this price component. Will be taken from the parent Projects ProjectInformation.  # noqa: E501

        :param label: The label of this PriceComponentDto.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def values(self):
        """Gets the values of this PriceComponentDto.  # noqa: E501

        The single Calculation elements this price component is composed of.  # noqa: E501

        :return: The values of this PriceComponentDto.  # noqa: E501
        :rtype: list[CalculationDto]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this PriceComponentDto.

        The single Calculation elements this price component is composed of.  # noqa: E501

        :param values: The values of this PriceComponentDto.  # noqa: E501
        :type: list[CalculationDto]
        """

        self._values = values

    @property
    def project_catalogues(self):
        """Gets the project_catalogues of this PriceComponentDto.  # noqa: E501

        These are Catalogues that are used within this PriceComponent. Catalogues are used to describe catalogues, or collections, that can be used to describe elements with commonly known properties. For example, QuantityAssignments use these to categorize themselves. They are propagate to all child elements, e.g. other containers and QuantityAssignments. In the context of a ServiceSpecification, all elements share the same instance of the collection.  # noqa: E501

        :return: The project_catalogues of this PriceComponentDto.  # noqa: E501
        :rtype: list[CatalogueDto]
        """
        return self._project_catalogues

    @project_catalogues.setter
    def project_catalogues(self, project_catalogues):
        """Sets the project_catalogues of this PriceComponentDto.

        These are Catalogues that are used within this PriceComponent. Catalogues are used to describe catalogues, or collections, that can be used to describe elements with commonly known properties. For example, QuantityAssignments use these to categorize themselves. They are propagate to all child elements, e.g. other containers and QuantityAssignments. In the context of a ServiceSpecification, all elements share the same instance of the collection.  # noqa: E501

        :param project_catalogues: The project_catalogues of this PriceComponentDto.  # noqa: E501
        :type: list[CatalogueDto]
        """

        self._project_catalogues = project_catalogues

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
        if issubclass(PriceComponentDto, dict):
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
        if not isinstance(other, PriceComponentDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriceComponentDto):
            return True

        return self.to_dict() != other.to_dict()
