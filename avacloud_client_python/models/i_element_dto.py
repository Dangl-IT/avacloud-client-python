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
        'element_type_discriminator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gaeb_xml_id': 'gaebXmlId',
        'element_type_discriminator': 'elementTypeDiscriminator'
    }

    discriminator_value_class_map = {
        'NoteTextDto': 'NoteTextDto',
        'ExecutionDescriptionDto': 'ExecutionDescriptionDto',
        'ServiceSpecificationGroupDto': 'ServiceSpecificationGroupDto',
        'PositionDto': 'PositionDto'
    }

    def __init__(self, id=None, gaeb_xml_id=None, element_type_discriminator=None):  # noqa: E501
        """IElementDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._gaeb_xml_id = None
        self._element_type_discriminator = None
        self.discriminator = 'elementTypeDiscriminator'

        self.id = id
        if gaeb_xml_id is not None:
            self.gaeb_xml_id = gaeb_xml_id
        self.element_type_discriminator = element_type_discriminator

    @property
    def id(self):
        """Gets the id of this IElementDto.  # noqa: E501


        :return: The id of this IElementDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IElementDto.


        :param id: The id of this IElementDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def gaeb_xml_id(self):
        """Gets the gaeb_xml_id of this IElementDto.  # noqa: E501


        :return: The gaeb_xml_id of this IElementDto.  # noqa: E501
        :rtype: str
        """
        return self._gaeb_xml_id

    @gaeb_xml_id.setter
    def gaeb_xml_id(self, gaeb_xml_id):
        """Sets the gaeb_xml_id of this IElementDto.


        :param gaeb_xml_id: The gaeb_xml_id of this IElementDto.  # noqa: E501
        :type: str
        """

        self._gaeb_xml_id = gaeb_xml_id

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
        if element_type_discriminator is None:
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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
