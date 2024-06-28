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


class FlatElementDto(object):
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
        'previous_element_id': 'str',
        'parent_element_id': 'str',
        'element': 'IElementDto'
    }

    attribute_map = {
        'previous_element_id': 'previousElementId',
        'parent_element_id': 'parentElementId',
        'element': 'element'
    }

    def __init__(self, previous_element_id=None, parent_element_id=None, element=None, _configuration=None):  # noqa: E501
        """FlatElementDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._previous_element_id = None
        self._parent_element_id = None
        self._element = None
        self.discriminator = None

        if previous_element_id is not None:
            self.previous_element_id = previous_element_id
        if parent_element_id is not None:
            self.parent_element_id = parent_element_id
        if element is not None:
            self.element = element

    @property
    def previous_element_id(self):
        """Gets the previous_element_id of this FlatElementDto.  # noqa: E501

        If this is not null, then this contains the id of the previous element in the hierarchy on the same level.  # noqa: E501

        :return: The previous_element_id of this FlatElementDto.  # noqa: E501
        :rtype: str
        """
        return self._previous_element_id

    @previous_element_id.setter
    def previous_element_id(self, previous_element_id):
        """Sets the previous_element_id of this FlatElementDto.

        If this is not null, then this contains the id of the previous element in the hierarchy on the same level.  # noqa: E501

        :param previous_element_id: The previous_element_id of this FlatElementDto.  # noqa: E501
        :type: str
        """

        self._previous_element_id = previous_element_id

    @property
    def parent_element_id(self):
        """Gets the parent_element_id of this FlatElementDto.  # noqa: E501

        If this is not null, then this contains the id of the parent element.  # noqa: E501

        :return: The parent_element_id of this FlatElementDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_element_id

    @parent_element_id.setter
    def parent_element_id(self, parent_element_id):
        """Sets the parent_element_id of this FlatElementDto.

        If this is not null, then this contains the id of the parent element.  # noqa: E501

        :param parent_element_id: The parent_element_id of this FlatElementDto.  # noqa: E501
        :type: str
        """

        self._parent_element_id = parent_element_id

    @property
    def element(self):
        """Gets the element of this FlatElementDto.  # noqa: E501

        The element itself.  # noqa: E501

        :return: The element of this FlatElementDto.  # noqa: E501
        :rtype: IElementDto
        """
        return self._element

    @element.setter
    def element(self, element):
        """Sets the element of this FlatElementDto.

        The element itself.  # noqa: E501

        :param element: The element of this FlatElementDto.  # noqa: E501
        :type: IElementDto
        """

        self._element = element

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
        if issubclass(FlatElementDto, dict):
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
        if not isinstance(other, FlatElementDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlatElementDto):
            return True

        return self.to_dict() != other.to_dict()
