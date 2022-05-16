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


class STLBReferenceDto(object):
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
        'version_date': 'datetime',
        'catalogue_name': 'str',
        'group': 'str',
        'cost_group': 'str',
        'service_area': 'str',
        'keys': 'list[STLBKeyDto]'
    }

    attribute_map = {
        'version_date': 'versionDate',
        'catalogue_name': 'catalogueName',
        'group': 'group',
        'cost_group': 'costGroup',
        'service_area': 'serviceArea',
        'keys': 'keys'
    }

    def __init__(self, version_date=None, catalogue_name=None, group=None, cost_group=None, service_area=None, keys=None, _configuration=None):  # noqa: E501
        """STLBReferenceDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._version_date = None
        self._catalogue_name = None
        self._group = None
        self._cost_group = None
        self._service_area = None
        self._keys = None
        self.discriminator = None

        if version_date is not None:
            self.version_date = version_date
        if catalogue_name is not None:
            self.catalogue_name = catalogue_name
        if group is not None:
            self.group = group
        if cost_group is not None:
            self.cost_group = cost_group
        if service_area is not None:
            self.service_area = service_area
        if keys is not None:
            self.keys = keys

    @property
    def version_date(self):
        """Gets the version_date of this STLBReferenceDto.  # noqa: E501

        The date of the STLB version. Typically, only the Year and Month are used  # noqa: E501

        :return: The version_date of this STLBReferenceDto.  # noqa: E501
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """Sets the version_date of this STLBReferenceDto.

        The date of the STLB version. Typically, only the Year and Month are used  # noqa: E501

        :param version_date: The version_date of this STLBReferenceDto.  # noqa: E501
        :type: datetime
        """

        self._version_date = version_date

    @property
    def catalogue_name(self):
        """Gets the catalogue_name of this STLBReferenceDto.  # noqa: E501

        The name of the catalogue within the STLB  # noqa: E501

        :return: The catalogue_name of this STLBReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._catalogue_name

    @catalogue_name.setter
    def catalogue_name(self, catalogue_name):
        """Sets the catalogue_name of this STLBReferenceDto.

        The name of the catalogue within the STLB  # noqa: E501

        :param catalogue_name: The catalogue_name of this STLBReferenceDto.  # noqa: E501
        :type: str
        """

        self._catalogue_name = catalogue_name

    @property
    def group(self):
        """Gets the group of this STLBReferenceDto.  # noqa: E501

        The name of the group in STLB  # noqa: E501

        :return: The group of this STLBReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this STLBReferenceDto.

        The name of the group in STLB  # noqa: E501

        :param group: The group of this STLBReferenceDto.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def cost_group(self):
        """Gets the cost_group of this STLBReferenceDto.  # noqa: E501

        The cost group this service is associated with  # noqa: E501

        :return: The cost_group of this STLBReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._cost_group

    @cost_group.setter
    def cost_group(self, cost_group):
        """Sets the cost_group of this STLBReferenceDto.

        The cost group this service is associated with  # noqa: E501

        :param cost_group: The cost_group of this STLBReferenceDto.  # noqa: E501
        :type: str
        """

        self._cost_group = cost_group

    @property
    def service_area(self):
        """Gets the service_area of this STLBReferenceDto.  # noqa: E501

        The service area (or type) in the STLB  # noqa: E501

        :return: The service_area of this STLBReferenceDto.  # noqa: E501
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this STLBReferenceDto.

        The service area (or type) in the STLB  # noqa: E501

        :param service_area: The service_area of this STLBReferenceDto.  # noqa: E501
        :type: str
        """

        self._service_area = service_area

    @property
    def keys(self):
        """Gets the keys of this STLBReferenceDto.  # noqa: E501

        These keys may optionally be used to further reference multiple, specific items within the STLB  # noqa: E501

        :return: The keys of this STLBReferenceDto.  # noqa: E501
        :rtype: list[STLBKeyDto]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this STLBReferenceDto.

        These keys may optionally be used to further reference multiple, specific items within the STLB  # noqa: E501

        :param keys: The keys of this STLBReferenceDto.  # noqa: E501
        :type: list[STLBKeyDto]
        """

        self._keys = keys

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
        if issubclass(STLBReferenceDto, dict):
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
        if not isinstance(other, STLBReferenceDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, STLBReferenceDto):
            return True

        return self.to_dict() != other.to_dict()
