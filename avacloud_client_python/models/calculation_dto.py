# coding: utf-8

"""
    AVACloud API 1.26.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class CalculationDto(object):
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
        'description': 'str',
        'formula': 'str',
        'result': 'float',
        'valid': 'bool',
        'error_position_in_line': 'int',
        'project_catalogues': 'list[CatalogueDto]',
        'catalogue_references': 'list[CatalogueReferenceDto]'
    }

    attribute_map = {
        'description': 'description',
        'formula': 'formula',
        'result': 'result',
        'valid': 'valid',
        'error_position_in_line': 'errorPositionInLine',
        'project_catalogues': 'projectCatalogues',
        'catalogue_references': 'catalogueReferences'
    }

    def __init__(self, description=None, formula=None, result=None, valid=None, error_position_in_line=None, project_catalogues=None, catalogue_references=None, _configuration=None):  # noqa: E501
        """CalculationDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._formula = None
        self._result = None
        self._valid = None
        self._error_position_in_line = None
        self._project_catalogues = None
        self._catalogue_references = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if formula is not None:
            self.formula = formula
        self.result = result
        self.valid = valid
        self.error_position_in_line = error_position_in_line
        if project_catalogues is not None:
            self.project_catalogues = project_catalogues
        if catalogue_references is not None:
            self.catalogue_references = catalogue_references

    @property
    def description(self):
        """Gets the description of this CalculationDto.  # noqa: E501

        Descriptive text for this calculation.  # noqa: E501

        :return: The description of this CalculationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CalculationDto.

        Descriptive text for this calculation.  # noqa: E501

        :param description: The description of this CalculationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """Gets the formula of this CalculationDto.  # noqa: E501

        This Calculation's mathematical expression. Please note that thousands separators are not supported. Both comma and point will be treated as decimal separators.  # noqa: E501

        :return: The formula of this CalculationDto.  # noqa: E501
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this CalculationDto.

        This Calculation's mathematical expression. Please note that thousands separators are not supported. Both comma and point will be treated as decimal separators.  # noqa: E501

        :param formula: The formula of this CalculationDto.  # noqa: E501
        :type: str
        """

        self._formula = formula

    @property
    def result(self):
        """Gets the result of this CalculationDto.  # noqa: E501

        The calculated result from the formula, 0 if invalid.  # noqa: E501

        :return: The result of this CalculationDto.  # noqa: E501
        :rtype: float
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CalculationDto.

        The calculated result from the formula, 0 if invalid.  # noqa: E501

        :param result: The result of this CalculationDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def valid(self):
        """Gets the valid of this CalculationDto.  # noqa: E501

        Whether the Formula is a valid expression.  # noqa: E501

        :return: The valid of this CalculationDto.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this CalculationDto.

        Whether the Formula is a valid expression.  # noqa: E501

        :param valid: The valid of this CalculationDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and valid is None:
            raise ValueError("Invalid value for `valid`, must not be `None`")  # noqa: E501

        self._valid = valid

    @property
    def error_position_in_line(self):
        """Gets the error_position_in_line of this CalculationDto.  # noqa: E501

        Will be -1 if the Formula is correct, else it will show the position in the formula where an error was encountered. This is a zero based index.  # noqa: E501

        :return: The error_position_in_line of this CalculationDto.  # noqa: E501
        :rtype: int
        """
        return self._error_position_in_line

    @error_position_in_line.setter
    def error_position_in_line(self, error_position_in_line):
        """Sets the error_position_in_line of this CalculationDto.

        Will be -1 if the Formula is correct, else it will show the position in the formula where an error was encountered. This is a zero based index.  # noqa: E501

        :param error_position_in_line: The error_position_in_line of this CalculationDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and error_position_in_line is None:
            raise ValueError("Invalid value for `error_position_in_line`, must not be `None`")  # noqa: E501

        self._error_position_in_line = error_position_in_line

    @property
    def project_catalogues(self):
        """Gets the project_catalogues of this CalculationDto.  # noqa: E501

        These are Catalogues that are used within this Calculation. Catalogues are used to describe catalogues, or collections, that can be used to describe elements with commonly known properties. For example, QuantityAssignments use these to categorize themselves. They are propagate to all child elements, e.g. other containers and QuantityAssignments. In the context of a ServiceSpecification, all elements share the same instance of the collection.  # noqa: E501

        :return: The project_catalogues of this CalculationDto.  # noqa: E501
        :rtype: list[CatalogueDto]
        """
        return self._project_catalogues

    @project_catalogues.setter
    def project_catalogues(self, project_catalogues):
        """Sets the project_catalogues of this CalculationDto.

        These are Catalogues that are used within this Calculation. Catalogues are used to describe catalogues, or collections, that can be used to describe elements with commonly known properties. For example, QuantityAssignments use these to categorize themselves. They are propagate to all child elements, e.g. other containers and QuantityAssignments. In the context of a ServiceSpecification, all elements share the same instance of the collection.  # noqa: E501

        :param project_catalogues: The project_catalogues of this CalculationDto.  # noqa: E501
        :type: list[CatalogueDto]
        """

        self._project_catalogues = project_catalogues

    @property
    def catalogue_references(self):
        """Gets the catalogue_references of this CalculationDto.  # noqa: E501

        Referenced catalogues for this Calculation.  # noqa: E501

        :return: The catalogue_references of this CalculationDto.  # noqa: E501
        :rtype: list[CatalogueReferenceDto]
        """
        return self._catalogue_references

    @catalogue_references.setter
    def catalogue_references(self, catalogue_references):
        """Sets the catalogue_references of this CalculationDto.

        Referenced catalogues for this Calculation.  # noqa: E501

        :param catalogue_references: The catalogue_references of this CalculationDto.  # noqa: E501
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
        if issubclass(CalculationDto, dict):
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
        if not isinstance(other, CalculationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculationDto):
            return True

        return self.to_dict() != other.to_dict()
