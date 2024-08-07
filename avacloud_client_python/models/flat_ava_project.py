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


class FlatAvaProject(object):
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
        'project': 'ProjectDto',
        'elements': 'list[FlatElementDto]'
    }

    attribute_map = {
        'project': 'project',
        'elements': 'elements'
    }

    def __init__(self, project=None, elements=None, _configuration=None):  # noqa: E501
        """FlatAvaProject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project = None
        self._elements = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if elements is not None:
            self.elements = elements

    @property
    def project(self):
        """Gets the project of this FlatAvaProject.  # noqa: E501

        The original project, including the service specification, but no elements.  # noqa: E501

        :return: The project of this FlatAvaProject.  # noqa: E501
        :rtype: ProjectDto
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this FlatAvaProject.

        The original project, including the service specification, but no elements.  # noqa: E501

        :param project: The project of this FlatAvaProject.  # noqa: E501
        :type: ProjectDto
        """

        self._project = project

    @property
    def elements(self):
        """Gets the elements of this FlatAvaProject.  # noqa: E501

        The flattened elements of the project.  # noqa: E501

        :return: The elements of this FlatAvaProject.  # noqa: E501
        :rtype: list[FlatElementDto]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this FlatAvaProject.

        The flattened elements of the project.  # noqa: E501

        :param elements: The elements of this FlatAvaProject.  # noqa: E501
        :type: list[FlatElementDto]
        """

        self._elements = elements

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
        if issubclass(FlatAvaProject, dict):
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
        if not isinstance(other, FlatAvaProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlatAvaProject):
            return True

        return self.to_dict() != other.to_dict()
