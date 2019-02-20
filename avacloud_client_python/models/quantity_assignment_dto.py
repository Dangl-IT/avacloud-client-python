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

from avacloud_client_python.models.catalogue_dto import CatalogueDto  # noqa: F401,E501
from avacloud_client_python.models.catalogue_reference_dto import CatalogueReferenceDto  # noqa: F401,E501


class QuantityAssignmentDto(object):
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
        'quantity': 'float',
        'project_catalogues': 'list[CatalogueDto]',
        'catalogue_references': 'list[CatalogueReferenceDto]'
    }

    attribute_map = {
        'id': 'id',
        'quantity': 'quantity',
        'project_catalogues': 'projectCatalogues',
        'catalogue_references': 'catalogueReferences'
    }

    def __init__(self, id=None, quantity=None, project_catalogues=None, catalogue_references=None):  # noqa: E501
        """QuantityAssignmentDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._quantity = None
        self._project_catalogues = None
        self._catalogue_references = None
        self.discriminator = None

        self.id = id
        self.quantity = quantity
        if project_catalogues is not None:
            self.project_catalogues = project_catalogues
        if catalogue_references is not None:
            self.catalogue_references = catalogue_references

    @property
    def id(self):
        """Gets the id of this QuantityAssignmentDto.  # noqa: E501


        :return: The id of this QuantityAssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuantityAssignmentDto.


        :param id: The id of this QuantityAssignmentDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def quantity(self):
        """Gets the quantity of this QuantityAssignmentDto.  # noqa: E501


        :return: The quantity of this QuantityAssignmentDto.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this QuantityAssignmentDto.


        :param quantity: The quantity of this QuantityAssignmentDto.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def project_catalogues(self):
        """Gets the project_catalogues of this QuantityAssignmentDto.  # noqa: E501


        :return: The project_catalogues of this QuantityAssignmentDto.  # noqa: E501
        :rtype: list[CatalogueDto]
        """
        return self._project_catalogues

    @project_catalogues.setter
    def project_catalogues(self, project_catalogues):
        """Sets the project_catalogues of this QuantityAssignmentDto.


        :param project_catalogues: The project_catalogues of this QuantityAssignmentDto.  # noqa: E501
        :type: list[CatalogueDto]
        """

        self._project_catalogues = project_catalogues

    @property
    def catalogue_references(self):
        """Gets the catalogue_references of this QuantityAssignmentDto.  # noqa: E501


        :return: The catalogue_references of this QuantityAssignmentDto.  # noqa: E501
        :rtype: list[CatalogueReferenceDto]
        """
        return self._catalogue_references

    @catalogue_references.setter
    def catalogue_references(self, catalogue_references):
        """Sets the catalogue_references of this QuantityAssignmentDto.


        :param catalogue_references: The catalogue_references of this QuantityAssignmentDto.  # noqa: E501
        :type: list[CatalogueReferenceDto]
        """

        self._catalogue_references = catalogue_references

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
        if issubclass(QuantityAssignmentDto, dict):
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
        if not isinstance(other, QuantityAssignmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
