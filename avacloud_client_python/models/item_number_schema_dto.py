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


class ItemNumberSchemaDto(object):
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
        'total_length': 'int',
        'tiers': 'list[ItemNumberSchemaTierDto]',
        'separator': 'str',
        'filler': 'str',
        'identifier': 'str',
        'skip_non_existing_levels_in_position_item_numbers': 'bool',
        'skipped_tiers_filler': 'str',
        'schema_is_correctly_defined': 'bool',
        'allow_upper_case_lettering': 'bool'
    }

    attribute_map = {
        'total_length': 'totalLength',
        'tiers': 'tiers',
        'separator': 'separator',
        'filler': 'filler',
        'identifier': 'identifier',
        'skip_non_existing_levels_in_position_item_numbers': 'skipNonExistingLevelsInPositionItemNumbers',
        'skipped_tiers_filler': 'skippedTiersFiller',
        'schema_is_correctly_defined': 'schemaIsCorrectlyDefined',
        'allow_upper_case_lettering': 'allowUpperCaseLettering'
    }

    def __init__(self, total_length=None, tiers=None, separator=None, filler=None, identifier=None, skip_non_existing_levels_in_position_item_numbers=None, skipped_tiers_filler=None, schema_is_correctly_defined=None, allow_upper_case_lettering=None, _configuration=None):  # noqa: E501
        """ItemNumberSchemaDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_length = None
        self._tiers = None
        self._separator = None
        self._filler = None
        self._identifier = None
        self._skip_non_existing_levels_in_position_item_numbers = None
        self._skipped_tiers_filler = None
        self._schema_is_correctly_defined = None
        self._allow_upper_case_lettering = None
        self.discriminator = None

        self.total_length = total_length
        if tiers is not None:
            self.tiers = tiers
        if separator is not None:
            self.separator = separator
        if filler is not None:
            self.filler = filler
        if identifier is not None:
            self.identifier = identifier
        self.skip_non_existing_levels_in_position_item_numbers = skip_non_existing_levels_in_position_item_numbers
        if skipped_tiers_filler is not None:
            self.skipped_tiers_filler = skipped_tiers_filler
        self.schema_is_correctly_defined = schema_is_correctly_defined
        self.allow_upper_case_lettering = allow_upper_case_lettering

    @property
    def total_length(self):
        """Gets the total_length of this ItemNumberSchemaDto.  # noqa: E501

        The count of tiers in the ItemNumberSchema  # noqa: E501

        :return: The total_length of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: int
        """
        return self._total_length

    @total_length.setter
    def total_length(self, total_length):
        """Sets the total_length of this ItemNumberSchemaDto.

        The count of tiers in the ItemNumberSchema  # noqa: E501

        :param total_length: The total_length of this ItemNumberSchemaDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_length is None:
            raise ValueError("Invalid value for `total_length`, must not be `None`")  # noqa: E501

        self._total_length = total_length

    @property
    def tiers(self):
        """Gets the tiers of this ItemNumberSchemaDto.  # noqa: E501

        The collection of tiers for this ItemNumberSchema.  # noqa: E501

        :return: The tiers of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: list[ItemNumberSchemaTierDto]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this ItemNumberSchemaDto.

        The collection of tiers for this ItemNumberSchema.  # noqa: E501

        :param tiers: The tiers of this ItemNumberSchemaDto.  # noqa: E501
        :type: list[ItemNumberSchemaTierDto]
        """

        self._tiers = tiers

    @property
    def separator(self):
        """Gets the separator of this ItemNumberSchemaDto.  # noqa: E501

        The separator to use for separiting the different levels in an ItemNumber. Defaults to DEFAULT_SEPARATOR, which is a point '.'. Setting this to a space or other whitespaces is discouraged, as this might not work correct in all situations and item numbers could be displayed not as intended. This can not be set to an empty or null string, trying that will default to the DEFAULT_SEPARATOR. If a value is set that has a different length than one '1', the DEFAULT_SEPARATOR will be used instead. You should also not use values for the separator that are also valid for the item numbers themselves, as that might also lead to incorrect results  # noqa: E501

        :return: The separator of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this ItemNumberSchemaDto.

        The separator to use for separiting the different levels in an ItemNumber. Defaults to DEFAULT_SEPARATOR, which is a point '.'. Setting this to a space or other whitespaces is discouraged, as this might not work correct in all situations and item numbers could be displayed not as intended. This can not be set to an empty or null string, trying that will default to the DEFAULT_SEPARATOR. If a value is set that has a different length than one '1', the DEFAULT_SEPARATOR will be used instead. You should also not use values for the separator that are also valid for the item numbers themselves, as that might also lead to incorrect results  # noqa: E501

        :param separator: The separator of this ItemNumberSchemaDto.  # noqa: E501
        :type: str
        """

        self._separator = separator

    @property
    def filler(self):
        """Gets the filler of this ItemNumberSchemaDto.  # noqa: E501

        This string is used to fill (left-pad) item numbers. For example, if a tier has a length of '4' but the given item number is '12', with a Filler of '0', then the final item number will be represented as '0'. This must be a single character string, if a value is given where the Length property does not evaluate to '1', the DEFAULT_FILLER '0' is used. A space is fine to use. You should ensure that you use a value different than Separator, as that might produce unexpected results. No attempt is done by the code to recover from such ambiguous configurations.  # noqa: E501

        :return: The filler of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: str
        """
        return self._filler

    @filler.setter
    def filler(self, filler):
        """Sets the filler of this ItemNumberSchemaDto.

        This string is used to fill (left-pad) item numbers. For example, if a tier has a length of '4' but the given item number is '12', with a Filler of '0', then the final item number will be represented as '0'. This must be a single character string, if a value is given where the Length property does not evaluate to '1', the DEFAULT_FILLER '0' is used. A space is fine to use. You should ensure that you use a value different than Separator, as that might produce unexpected results. No attempt is done by the code to recover from such ambiguous configurations.  # noqa: E501

        :param filler: The filler of this ItemNumberSchemaDto.  # noqa: E501
        :type: str
        """

        self._filler = filler

    @property
    def identifier(self):
        """Gets the identifier of this ItemNumberSchemaDto.  # noqa: E501

        This is just a string property that can optionally be used to store additional data for this ItemNumberSchema, e.g. an identification or a type. It does not have any influence over how item numbers are generated, and is not supported in most exchange formats. However, it is used to store ÖNorm service specification structure types.  # noqa: E501

        :return: The identifier of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ItemNumberSchemaDto.

        This is just a string property that can optionally be used to store additional data for this ItemNumberSchema, e.g. an identification or a type. It does not have any influence over how item numbers are generated, and is not supported in most exchange formats. However, it is used to store ÖNorm service specification structure types.  # noqa: E501

        :param identifier: The identifier of this ItemNumberSchemaDto.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def skip_non_existing_levels_in_position_item_numbers(self):
        """Gets the skip_non_existing_levels_in_position_item_numbers of this ItemNumberSchemaDto.  # noqa: E501

        This property indicates if ItemNumbers using this ItemNumberSchema should skip empty group levels. This is commonly only used in GAEB files, where there might be gaps in the hierarchy of elements and position identifiers should be placed at the end of the string representation.  # noqa: E501

        :return: The skip_non_existing_levels_in_position_item_numbers of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: bool
        """
        return self._skip_non_existing_levels_in_position_item_numbers

    @skip_non_existing_levels_in_position_item_numbers.setter
    def skip_non_existing_levels_in_position_item_numbers(self, skip_non_existing_levels_in_position_item_numbers):
        """Sets the skip_non_existing_levels_in_position_item_numbers of this ItemNumberSchemaDto.

        This property indicates if ItemNumbers using this ItemNumberSchema should skip empty group levels. This is commonly only used in GAEB files, where there might be gaps in the hierarchy of elements and position identifiers should be placed at the end of the string representation.  # noqa: E501

        :param skip_non_existing_levels_in_position_item_numbers: The skip_non_existing_levels_in_position_item_numbers of this ItemNumberSchemaDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and skip_non_existing_levels_in_position_item_numbers is None:
            raise ValueError("Invalid value for `skip_non_existing_levels_in_position_item_numbers`, must not be `None`")  # noqa: E501

        self._skip_non_existing_levels_in_position_item_numbers = skip_non_existing_levels_in_position_item_numbers

    @property
    def skipped_tiers_filler(self):
        """Gets the skipped_tiers_filler of this ItemNumberSchemaDto.  # noqa: E501

        This string is used only when the property SkipNonExistingLevelsInPositionItemNumbers in this ItemNumberSchema is also set to true. It defaults to DEFAULT_SKIPPED_TIERS_FILLER, but can be set to any string with a lenght of one. Null values or values with a longer length will lead to this property reverting back to the default value. This is used to fill skipped tiers in item numbers where a position is placed in a higher hierarchy level than what would be defined in the Tiers. For example, it could produce an item number like '01.__.02', which would indicate a skipped second level. This should be using different values than Filler and Separator, since that could cause ambiguities in the code that generates the actual item numbers. No attempt is done by the code to recover from such ambiguous configurations.  # noqa: E501

        :return: The skipped_tiers_filler of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: str
        """
        return self._skipped_tiers_filler

    @skipped_tiers_filler.setter
    def skipped_tiers_filler(self, skipped_tiers_filler):
        """Sets the skipped_tiers_filler of this ItemNumberSchemaDto.

        This string is used only when the property SkipNonExistingLevelsInPositionItemNumbers in this ItemNumberSchema is also set to true. It defaults to DEFAULT_SKIPPED_TIERS_FILLER, but can be set to any string with a lenght of one. Null values or values with a longer length will lead to this property reverting back to the default value. This is used to fill skipped tiers in item numbers where a position is placed in a higher hierarchy level than what would be defined in the Tiers. For example, it could produce an item number like '01.__.02', which would indicate a skipped second level. This should be using different values than Filler and Separator, since that could cause ambiguities in the code that generates the actual item numbers. No attempt is done by the code to recover from such ambiguous configurations.  # noqa: E501

        :param skipped_tiers_filler: The skipped_tiers_filler of this ItemNumberSchemaDto.  # noqa: E501
        :type: str
        """

        self._skipped_tiers_filler = skipped_tiers_filler

    @property
    def schema_is_correctly_defined(self):
        """Gets the schema_is_correctly_defined of this ItemNumberSchemaDto.  # noqa: E501

        This is a read-only property that indicates if this schema has a valid structure. It internally just returns the result from IsCorrectlyDefined. This will return if the ItemNumberSchema is correctly defined. For it to be correctly defined, the following conditions must be true: There may only be one lot group, if there is one, it must be at the top. Following lot levels, there may be at least one group level. After the group levels, there must be one position level. After the position level, there may be one index level. If no tiers are defined at all, this will also return false.  # noqa: E501

        :return: The schema_is_correctly_defined of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: bool
        """
        return self._schema_is_correctly_defined

    @schema_is_correctly_defined.setter
    def schema_is_correctly_defined(self, schema_is_correctly_defined):
        """Sets the schema_is_correctly_defined of this ItemNumberSchemaDto.

        This is a read-only property that indicates if this schema has a valid structure. It internally just returns the result from IsCorrectlyDefined. This will return if the ItemNumberSchema is correctly defined. For it to be correctly defined, the following conditions must be true: There may only be one lot group, if there is one, it must be at the top. Following lot levels, there may be at least one group level. After the group levels, there must be one position level. After the position level, there may be one index level. If no tiers are defined at all, this will also return false.  # noqa: E501

        :param schema_is_correctly_defined: The schema_is_correctly_defined of this ItemNumberSchemaDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and schema_is_correctly_defined is None:
            raise ValueError("Invalid value for `schema_is_correctly_defined`, must not be `None`")  # noqa: E501

        self._schema_is_correctly_defined = schema_is_correctly_defined

    @property
    def allow_upper_case_lettering(self):
        """Gets the allow_upper_case_lettering of this ItemNumberSchemaDto.  # noqa: E501

        Defaults to false. If this is disabled, all letters in the ItemNumber string representations will be transformed to their lowercase representation.  # noqa: E501

        :return: The allow_upper_case_lettering of this ItemNumberSchemaDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_upper_case_lettering

    @allow_upper_case_lettering.setter
    def allow_upper_case_lettering(self, allow_upper_case_lettering):
        """Sets the allow_upper_case_lettering of this ItemNumberSchemaDto.

        Defaults to false. If this is disabled, all letters in the ItemNumber string representations will be transformed to their lowercase representation.  # noqa: E501

        :param allow_upper_case_lettering: The allow_upper_case_lettering of this ItemNumberSchemaDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and allow_upper_case_lettering is None:
            raise ValueError("Invalid value for `allow_upper_case_lettering`, must not be `None`")  # noqa: E501

        self._allow_upper_case_lettering = allow_upper_case_lettering

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
        if issubclass(ItemNumberSchemaDto, dict):
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
        if not isinstance(other, ItemNumberSchemaDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemNumberSchemaDto):
            return True

        return self.to_dict() != other.to_dict()
