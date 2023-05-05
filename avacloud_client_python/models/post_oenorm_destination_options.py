# coding: utf-8

"""
    AVACloud API 1.41.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.configuration import Configuration


class PostOenormDestinationOptions(object):
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
        'destination_oenorm_type': 'DestinationOenormType',
        'try_repair_project_structure': 'bool',
        'skip_try_enforce_schema_compliant_xml_output': 'bool',
        'remove_unprintable_characters_from_texts': 'bool'
    }

    attribute_map = {
        'destination_oenorm_type': 'destinationOenormType',
        'try_repair_project_structure': 'tryRepairProjectStructure',
        'skip_try_enforce_schema_compliant_xml_output': 'skipTryEnforceSchemaCompliantXmlOutput',
        'remove_unprintable_characters_from_texts': 'removeUnprintableCharactersFromTexts'
    }

    def __init__(self, destination_oenorm_type=None, try_repair_project_structure=None, skip_try_enforce_schema_compliant_xml_output=None, remove_unprintable_characters_from_texts=None, _configuration=None):  # noqa: E501
        """PostOenormDestinationOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_oenorm_type = None
        self._try_repair_project_structure = None
        self._skip_try_enforce_schema_compliant_xml_output = None
        self._remove_unprintable_characters_from_texts = None
        self.discriminator = None

        self.destination_oenorm_type = destination_oenorm_type
        self.try_repair_project_structure = try_repair_project_structure
        self.skip_try_enforce_schema_compliant_xml_output = skip_try_enforce_schema_compliant_xml_output
        self.remove_unprintable_characters_from_texts = remove_unprintable_characters_from_texts

    @property
    def destination_oenorm_type(self):
        """Gets the destination_oenorm_type of this PostOenormDestinationOptions.  # noqa: E501

        Defaults to Lv2015  # noqa: E501

        :return: The destination_oenorm_type of this PostOenormDestinationOptions.  # noqa: E501
        :rtype: DestinationOenormType
        """
        return self._destination_oenorm_type

    @destination_oenorm_type.setter
    def destination_oenorm_type(self, destination_oenorm_type):
        """Sets the destination_oenorm_type of this PostOenormDestinationOptions.

        Defaults to Lv2015  # noqa: E501

        :param destination_oenorm_type: The destination_oenorm_type of this PostOenormDestinationOptions.  # noqa: E501
        :type: DestinationOenormType
        """
        if self._configuration.client_side_validation and destination_oenorm_type is None:
            raise ValueError("Invalid value for `destination_oenorm_type`, must not be `None`")  # noqa: E501

        self._destination_oenorm_type = destination_oenorm_type

    @property
    def try_repair_project_structure(self):
        """Gets the try_repair_project_structure of this PostOenormDestinationOptions.  # noqa: E501

        Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target  # noqa: E501

        :return: The try_repair_project_structure of this PostOenormDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._try_repair_project_structure

    @try_repair_project_structure.setter
    def try_repair_project_structure(self, try_repair_project_structure):
        """Sets the try_repair_project_structure of this PostOenormDestinationOptions.

        Defaults to false. If this is enabled, the converter will try to ensure that the project structure can be mapped to Oenorm. It might introduce additional group levels to ensure a compatible target  # noqa: E501

        :param try_repair_project_structure: The try_repair_project_structure of this PostOenormDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and try_repair_project_structure is None:
            raise ValueError("Invalid value for `try_repair_project_structure`, must not be `None`")  # noqa: E501

        self._try_repair_project_structure = try_repair_project_structure

    @property
    def skip_try_enforce_schema_compliant_xml_output(self):
        """Gets the skip_try_enforce_schema_compliant_xml_output of this PostOenormDestinationOptions.  # noqa: E501

        If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option.  # noqa: E501

        :return: The skip_try_enforce_schema_compliant_xml_output of this PostOenormDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._skip_try_enforce_schema_compliant_xml_output

    @skip_try_enforce_schema_compliant_xml_output.setter
    def skip_try_enforce_schema_compliant_xml_output(self, skip_try_enforce_schema_compliant_xml_output):
        """Sets the skip_try_enforce_schema_compliant_xml_output of this PostOenormDestinationOptions.

        If this option is enabled, AVACloud will not attempt to force a schema-compliant Xml output for ÖNorm targets that are Xml based. By default, AVACloud will try to add required fields, even if no data is present, with sensible defaults. This behavior can be disabled with this option.  # noqa: E501

        :param skip_try_enforce_schema_compliant_xml_output: The skip_try_enforce_schema_compliant_xml_output of this PostOenormDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and skip_try_enforce_schema_compliant_xml_output is None:
            raise ValueError("Invalid value for `skip_try_enforce_schema_compliant_xml_output`, must not be `None`")  # noqa: E501

        self._skip_try_enforce_schema_compliant_xml_output = skip_try_enforce_schema_compliant_xml_output

    @property
    def remove_unprintable_characters_from_texts(self):
        """Gets the remove_unprintable_characters_from_texts of this PostOenormDestinationOptions.  # noqa: E501

        If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.  # noqa: E501

        :return: The remove_unprintable_characters_from_texts of this PostOenormDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._remove_unprintable_characters_from_texts

    @remove_unprintable_characters_from_texts.setter
    def remove_unprintable_characters_from_texts(self, remove_unprintable_characters_from_texts):
        """Sets the remove_unprintable_characters_from_texts of this PostOenormDestinationOptions.

        If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.  # noqa: E501

        :param remove_unprintable_characters_from_texts: The remove_unprintable_characters_from_texts of this PostOenormDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and remove_unprintable_characters_from_texts is None:
            raise ValueError("Invalid value for `remove_unprintable_characters_from_texts`, must not be `None`")  # noqa: E501

        self._remove_unprintable_characters_from_texts = remove_unprintable_characters_from_texts

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
        if issubclass(PostOenormDestinationOptions, dict):
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
        if not isinstance(other, PostOenormDestinationOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostOenormDestinationOptions):
            return True

        return self.to_dict() != other.to_dict()

