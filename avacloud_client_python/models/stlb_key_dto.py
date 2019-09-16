# coding: utf-8

"""
    AVACloud API 1.10.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class STLBKeyDto(object):
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
        'art_identifier': 'int',
        'art_index': 'int',
        'kind_identifier': 'int'
    }

    attribute_map = {
        'art_identifier': 'artIdentifier',
        'art_index': 'artIndex',
        'kind_identifier': 'kindIdentifier'
    }

    def __init__(self, art_identifier=None, art_index=None, kind_identifier=None):  # noqa: E501
        """STLBKeyDto - a model defined in Swagger"""  # noqa: E501

        self._art_identifier = None
        self._art_index = None
        self._kind_identifier = None
        self.discriminator = None

        self.art_identifier = art_identifier
        if art_index is not None:
            self.art_index = art_index
        if kind_identifier is not None:
            self.kind_identifier = kind_identifier

    @property
    def art_identifier(self):
        """Gets the art_identifier of this STLBKeyDto.  # noqa: E501

        This identifier is required and uniquely describes a single reference within the STLB standard. It maps to \"ArtChrIdent\" in GAEB XML  # noqa: E501

        :return: The art_identifier of this STLBKeyDto.  # noqa: E501
        :rtype: int
        """
        return self._art_identifier

    @art_identifier.setter
    def art_identifier(self, art_identifier):
        """Sets the art_identifier of this STLBKeyDto.

        This identifier is required and uniquely describes a single reference within the STLB standard. It maps to \"ArtChrIdent\" in GAEB XML  # noqa: E501

        :param art_identifier: The art_identifier of this STLBKeyDto.  # noqa: E501
        :type: int
        """
        if art_identifier is None:
            raise ValueError("Invalid value for `art_identifier`, must not be `None`")  # noqa: E501

        self._art_identifier = art_identifier

    @property
    def art_index(self):
        """Gets the art_index of this STLBKeyDto.  # noqa: E501

        This optional index property further categorizes a single reference within the STLB standard. It maps to \"ArtChIdx\" in GAEB XML  # noqa: E501

        :return: The art_index of this STLBKeyDto.  # noqa: E501
        :rtype: int
        """
        return self._art_index

    @art_index.setter
    def art_index(self, art_index):
        """Sets the art_index of this STLBKeyDto.

        This optional index property further categorizes a single reference within the STLB standard. It maps to \"ArtChIdx\" in GAEB XML  # noqa: E501

        :param art_index: The art_index of this STLBKeyDto.  # noqa: E501
        :type: int
        """

        self._art_index = art_index

    @property
    def kind_identifier(self):
        """Gets the kind_identifier of this STLBKeyDto.  # noqa: E501

        This optional identifier further specifies the execution kind of the reference in the STLB standard. It maps to \"ChVIdent\" in GAEB XML  # noqa: E501

        :return: The kind_identifier of this STLBKeyDto.  # noqa: E501
        :rtype: int
        """
        return self._kind_identifier

    @kind_identifier.setter
    def kind_identifier(self, kind_identifier):
        """Sets the kind_identifier of this STLBKeyDto.

        This optional identifier further specifies the execution kind of the reference in the STLB standard. It maps to \"ChVIdent\" in GAEB XML  # noqa: E501

        :param kind_identifier: The kind_identifier of this STLBKeyDto.  # noqa: E501
        :type: int
        """

        self._kind_identifier = kind_identifier

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
        if issubclass(STLBKeyDto, dict):
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
        if not isinstance(other, STLBKeyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
