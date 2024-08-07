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


class StandardizedDescriptionDto(object):
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
        'standard_reference_type': 'StandardReferenceTypeDto',
        'standard_reference': 'str',
        'stlb_reference': 'STLBReferenceDto'
    }

    attribute_map = {
        'standard_reference_type': 'standardReferenceType',
        'standard_reference': 'standardReference',
        'stlb_reference': 'stlbReference'
    }

    def __init__(self, standard_reference_type=None, standard_reference=None, stlb_reference=None, _configuration=None):  # noqa: E501
        """StandardizedDescriptionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._standard_reference_type = None
        self._standard_reference = None
        self._stlb_reference = None
        self.discriminator = None

        self.standard_reference_type = standard_reference_type
        if standard_reference is not None:
            self.standard_reference = standard_reference
        if stlb_reference is not None:
            self.stlb_reference = stlb_reference

    @property
    def standard_reference_type(self):
        """Gets the standard_reference_type of this StandardizedDescriptionDto.  # noqa: E501

        This enumeration identifies a pre-known standard used for referencing standardized descriptions.  # noqa: E501

        :return: The standard_reference_type of this StandardizedDescriptionDto.  # noqa: E501
        :rtype: StandardReferenceTypeDto
        """
        return self._standard_reference_type

    @standard_reference_type.setter
    def standard_reference_type(self, standard_reference_type):
        """Sets the standard_reference_type of this StandardizedDescriptionDto.

        This enumeration identifies a pre-known standard used for referencing standardized descriptions.  # noqa: E501

        :param standard_reference_type: The standard_reference_type of this StandardizedDescriptionDto.  # noqa: E501
        :type: StandardReferenceTypeDto
        """
        if self._configuration.client_side_validation and standard_reference_type is None:
            raise ValueError("Invalid value for `standard_reference_type`, must not be `None`")  # noqa: E501

        self._standard_reference_type = standard_reference_type

    @property
    def standard_reference(self):
        """Gets the standard_reference of this StandardizedDescriptionDto.  # noqa: E501

        This string property is the identifier to map to the references standard. Its type is given in the StandardReferenceType  # noqa: E501

        :return: The standard_reference of this StandardizedDescriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._standard_reference

    @standard_reference.setter
    def standard_reference(self, standard_reference):
        """Sets the standard_reference of this StandardizedDescriptionDto.

        This string property is the identifier to map to the references standard. Its type is given in the StandardReferenceType  # noqa: E501

        :param standard_reference: The standard_reference of this StandardizedDescriptionDto.  # noqa: E501
        :type: str
        """

        self._standard_reference = standard_reference

    @property
    def stlb_reference(self):
        """Gets the stlb_reference of this StandardizedDescriptionDto.  # noqa: E501

        This is a special reference to the German STLB \"Standardleistungsbuch Bau\" reference. If this is used, the StandardReference property should not be set.  # noqa: E501

        :return: The stlb_reference of this StandardizedDescriptionDto.  # noqa: E501
        :rtype: STLBReferenceDto
        """
        return self._stlb_reference

    @stlb_reference.setter
    def stlb_reference(self, stlb_reference):
        """Sets the stlb_reference of this StandardizedDescriptionDto.

        This is a special reference to the German STLB \"Standardleistungsbuch Bau\" reference. If this is used, the StandardReference property should not be set.  # noqa: E501

        :param stlb_reference: The stlb_reference of this StandardizedDescriptionDto.  # noqa: E501
        :type: STLBReferenceDto
        """

        self._stlb_reference = stlb_reference

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
        if issubclass(StandardizedDescriptionDto, dict):
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
        if not isinstance(other, StandardizedDescriptionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StandardizedDescriptionDto):
            return True

        return self.to_dict() != other.to_dict()
