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


class CatalogueReferenceDto(object):
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
        'catalogue_reference_key': 'str',
        'catalogue_reference_id': 'str',
        'project_catalogues': 'list[CatalogueDto]',
        'catalogue': 'object'
    }

    attribute_map = {
        'id': 'id',
        'catalogue_reference_key': 'catalogueReferenceKey',
        'catalogue_reference_id': 'catalogueReferenceId',
        'project_catalogues': 'projectCatalogues',
        'catalogue': 'catalogue'
    }

    def __init__(self, id=None, catalogue_reference_key=None, catalogue_reference_id=None, project_catalogues=None, catalogue=None):  # noqa: E501
        """CatalogueReferenceDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._catalogue_reference_key = None
        self._catalogue_reference_id = None
        self._project_catalogues = None
        self._catalogue = None
        self.discriminator = None

        self.id = id
        if catalogue_reference_key is not None:
            self.catalogue_reference_key = catalogue_reference_key
        self.catalogue_reference_id = catalogue_reference_id
        if project_catalogues is not None:
            self.project_catalogues = project_catalogues
        if catalogue is not None:
            self.catalogue = catalogue

    @property
    def id(self):
        """Gets the id of this CatalogueReferenceDto.  # noqa: E501


        :return: The id of this CatalogueReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CatalogueReferenceDto.


        :param id: The id of this CatalogueReferenceDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def catalogue_reference_key(self):
        """Gets the catalogue_reference_key of this CatalogueReferenceDto.  # noqa: E501


        :return: The catalogue_reference_key of this CatalogueReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._catalogue_reference_key

    @catalogue_reference_key.setter
    def catalogue_reference_key(self, catalogue_reference_key):
        """Sets the catalogue_reference_key of this CatalogueReferenceDto.


        :param catalogue_reference_key: The catalogue_reference_key of this CatalogueReferenceDto.  # noqa: E501
        :type: str
        """

        self._catalogue_reference_key = catalogue_reference_key

    @property
    def catalogue_reference_id(self):
        """Gets the catalogue_reference_id of this CatalogueReferenceDto.  # noqa: E501


        :return: The catalogue_reference_id of this CatalogueReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._catalogue_reference_id

    @catalogue_reference_id.setter
    def catalogue_reference_id(self, catalogue_reference_id):
        """Sets the catalogue_reference_id of this CatalogueReferenceDto.


        :param catalogue_reference_id: The catalogue_reference_id of this CatalogueReferenceDto.  # noqa: E501
        :type: str
        """
        if catalogue_reference_id is None:
            raise ValueError("Invalid value for `catalogue_reference_id`, must not be `None`")  # noqa: E501

        self._catalogue_reference_id = catalogue_reference_id

    @property
    def project_catalogues(self):
        """Gets the project_catalogues of this CatalogueReferenceDto.  # noqa: E501


        :return: The project_catalogues of this CatalogueReferenceDto.  # noqa: E501
        :rtype: list[CatalogueDto]
        """
        return self._project_catalogues

    @project_catalogues.setter
    def project_catalogues(self, project_catalogues):
        """Sets the project_catalogues of this CatalogueReferenceDto.


        :param project_catalogues: The project_catalogues of this CatalogueReferenceDto.  # noqa: E501
        :type: list[CatalogueDto]
        """

        self._project_catalogues = project_catalogues

    @property
    def catalogue(self):
        """Gets the catalogue of this CatalogueReferenceDto.  # noqa: E501


        :return: The catalogue of this CatalogueReferenceDto.  # noqa: E501
        :rtype: object
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        """Sets the catalogue of this CatalogueReferenceDto.


        :param catalogue: The catalogue of this CatalogueReferenceDto.  # noqa: E501
        :type: object
        """

        self._catalogue = catalogue

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
        if issubclass(CatalogueReferenceDto, dict):
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
        if not isinstance(other, CatalogueReferenceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
