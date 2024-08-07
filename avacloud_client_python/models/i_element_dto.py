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


class IElementDto(object):
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
        'gaeb_xml_id': 'str',
        'addendum_number': 'str',
        'project_catalogues': 'list[CatalogueDto]',
        'catalogue_references': 'list[CatalogueReferenceDto]',
        'element_type_discriminator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gaeb_xml_id': 'gaebXmlId',
        'addendum_number': 'addendumNumber',
        'project_catalogues': 'projectCatalogues',
        'catalogue_references': 'catalogueReferences',
        'element_type_discriminator': 'elementTypeDiscriminator'
    }

    discriminator_value_class_map = {
        'NoteTextDto': 'NoteTextDto',
        'ExecutionDescriptionDto': 'ExecutionDescriptionDto',
        'ServiceSpecificationGroupDto': 'ServiceSpecificationGroupDto',
        'PositionDto': 'PositionDto'
    }

    def __init__(self, id=None, gaeb_xml_id=None, addendum_number=None, project_catalogues=None, catalogue_references=None, element_type_discriminator=None, _configuration=None):  # noqa: E501
        """IElementDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._gaeb_xml_id = None
        self._addendum_number = None
        self._project_catalogues = None
        self._catalogue_references = None
        self._element_type_discriminator = None
        self.discriminator = 'elementTypeDiscriminator'

        self.id = id
        if gaeb_xml_id is not None:
            self.gaeb_xml_id = gaeb_xml_id
        if addendum_number is not None:
            self.addendum_number = addendum_number
        if project_catalogues is not None:
            self.project_catalogues = project_catalogues
        if catalogue_references is not None:
            self.catalogue_references = catalogue_references
        self.element_type_discriminator = element_type_discriminator

    @property
    def id(self):
        """Gets the id of this IElementDto.  # noqa: E501

        Elements GUID identifier.  # noqa: E501

        :return: The id of this IElementDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IElementDto.

        Elements GUID identifier.  # noqa: E501

        :param id: The id of this IElementDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def gaeb_xml_id(self):
        """Gets the gaeb_xml_id of this IElementDto.  # noqa: E501

        This is used to store the GAEB XML Id within this IElement. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization.  # noqa: E501

        :return: The gaeb_xml_id of this IElementDto.  # noqa: E501
        :rtype: str
        """
        return self._gaeb_xml_id

    @gaeb_xml_id.setter
    def gaeb_xml_id(self, gaeb_xml_id):
        """Sets the gaeb_xml_id of this IElementDto.

        This is used to store the GAEB XML Id within this IElement. This data is not used for any calculations or evaluations but only for GAEB serialization and deserialization.  # noqa: E501

        :param gaeb_xml_id: The gaeb_xml_id of this IElementDto.  # noqa: E501
        :type: str
        """

        self._gaeb_xml_id = gaeb_xml_id

    @property
    def addendum_number(self):
        """Gets the addendum_number of this IElementDto.  # noqa: E501

        This optional string property is shared by all IElements, and indicates if the element is part of an addendum, a 'Nachtrag' in German.  # noqa: E501

        :return: The addendum_number of this IElementDto.  # noqa: E501
        :rtype: str
        """
        return self._addendum_number

    @addendum_number.setter
    def addendum_number(self, addendum_number):
        """Sets the addendum_number of this IElementDto.

        This optional string property is shared by all IElements, and indicates if the element is part of an addendum, a 'Nachtrag' in German.  # noqa: E501

        :param addendum_number: The addendum_number of this IElementDto.  # noqa: E501
        :type: str
        """

        self._addendum_number = addendum_number

    @property
    def project_catalogues(self):
        """Gets the project_catalogues of this IElementDto.  # noqa: E501


        :return: The project_catalogues of this IElementDto.  # noqa: E501
        :rtype: list[CatalogueDto]
        """
        return self._project_catalogues

    @project_catalogues.setter
    def project_catalogues(self, project_catalogues):
        """Sets the project_catalogues of this IElementDto.


        :param project_catalogues: The project_catalogues of this IElementDto.  # noqa: E501
        :type: list[CatalogueDto]
        """

        self._project_catalogues = project_catalogues

    @property
    def catalogue_references(self):
        """Gets the catalogue_references of this IElementDto.  # noqa: E501


        :return: The catalogue_references of this IElementDto.  # noqa: E501
        :rtype: list[CatalogueReferenceDto]
        """
        return self._catalogue_references

    @catalogue_references.setter
    def catalogue_references(self, catalogue_references):
        """Sets the catalogue_references of this IElementDto.


        :param catalogue_references: The catalogue_references of this IElementDto.  # noqa: E501
        :type: list[CatalogueReferenceDto]
        """

        self._catalogue_references = catalogue_references

    @property
    def element_type_discriminator(self):
        """Gets the element_type_discriminator of this IElementDto.  # noqa: E501


        :return: The element_type_discriminator of this IElementDto.  # noqa: E501
        :rtype: str
        """
        return self._element_type_discriminator

    @element_type_discriminator.setter
    def element_type_discriminator(self, element_type_discriminator):
        """Sets the element_type_discriminator of this IElementDto.


        :param element_type_discriminator: The element_type_discriminator of this IElementDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and element_type_discriminator is None:
            raise ValueError("Invalid value for `element_type_discriminator`, must not be `None`")  # noqa: E501

        self._element_type_discriminator = element_type_discriminator

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(IElementDto, dict):
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
        if not isinstance(other, IElementDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IElementDto):
            return True

        return self.to_dict() != other.to_dict()
