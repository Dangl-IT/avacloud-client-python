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


class OenormNoteTextPropertiesDto(object):
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
        'origin_code': 'OenormOriginCodeDto'
    }

    attribute_map = {
        'origin_code': 'originCode'
    }

    def __init__(self, origin_code=None, _configuration=None):  # noqa: E501
        """OenormNoteTextPropertiesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._origin_code = None
        self.discriminator = None

        self.origin_code = origin_code

    @property
    def origin_code(self):
        """Gets the origin_code of this OenormNoteTextPropertiesDto.  # noqa: E501

        This indicates where the content of this element originates, if set. It corresponds to 'herkunftskennzeichen' in ÖNorm  # noqa: E501

        :return: The origin_code of this OenormNoteTextPropertiesDto.  # noqa: E501
        :rtype: OenormOriginCodeDto
        """
        return self._origin_code

    @origin_code.setter
    def origin_code(self, origin_code):
        """Sets the origin_code of this OenormNoteTextPropertiesDto.

        This indicates where the content of this element originates, if set. It corresponds to 'herkunftskennzeichen' in ÖNorm  # noqa: E501

        :param origin_code: The origin_code of this OenormNoteTextPropertiesDto.  # noqa: E501
        :type: OenormOriginCodeDto
        """
        if self._configuration.client_side_validation and origin_code is None:
            raise ValueError("Invalid value for `origin_code`, must not be `None`")  # noqa: E501

        self._origin_code = origin_code

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
        if issubclass(OenormNoteTextPropertiesDto, dict):
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
        if not isinstance(other, OenormNoteTextPropertiesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OenormNoteTextPropertiesDto):
            return True

        return self.to_dict() != other.to_dict()
