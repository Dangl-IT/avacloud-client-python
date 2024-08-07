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


class PostGaebDestinationOptions(object):
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
        'destination_gaeb_type': 'DestinationGaebType',
        'target_exchange_phase_transform': 'DestinationGaebExchangePhase',
        'enforce_strict_offer_phase_long_text_output': 'bool',
        'export_quantity_determination': 'bool',
        'remove_unprintable_characters_from_texts': 'bool',
        'force_include_descriptions': 'bool',
        'treat_null_item_number_schema_as_invalid': 'bool'
    }

    attribute_map = {
        'destination_gaeb_type': 'destinationGaebType',
        'target_exchange_phase_transform': 'targetExchangePhaseTransform',
        'enforce_strict_offer_phase_long_text_output': 'enforceStrictOfferPhaseLongTextOutput',
        'export_quantity_determination': 'exportQuantityDetermination',
        'remove_unprintable_characters_from_texts': 'removeUnprintableCharactersFromTexts',
        'force_include_descriptions': 'forceIncludeDescriptions',
        'treat_null_item_number_schema_as_invalid': 'treatNullItemNumberSchemaAsInvalid'
    }

    def __init__(self, destination_gaeb_type=None, target_exchange_phase_transform=None, enforce_strict_offer_phase_long_text_output=None, export_quantity_determination=None, remove_unprintable_characters_from_texts=None, force_include_descriptions=None, treat_null_item_number_schema_as_invalid=None, _configuration=None):  # noqa: E501
        """PostGaebDestinationOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_gaeb_type = None
        self._target_exchange_phase_transform = None
        self._enforce_strict_offer_phase_long_text_output = None
        self._export_quantity_determination = None
        self._remove_unprintable_characters_from_texts = None
        self._force_include_descriptions = None
        self._treat_null_item_number_schema_as_invalid = None
        self.discriminator = None

        self.destination_gaeb_type = destination_gaeb_type
        self.target_exchange_phase_transform = target_exchange_phase_transform
        self.enforce_strict_offer_phase_long_text_output = enforce_strict_offer_phase_long_text_output
        self.export_quantity_determination = export_quantity_determination
        self.remove_unprintable_characters_from_texts = remove_unprintable_characters_from_texts
        self.force_include_descriptions = force_include_descriptions
        self.treat_null_item_number_schema_as_invalid = treat_null_item_number_schema_as_invalid

    @property
    def destination_gaeb_type(self):
        """Gets the destination_gaeb_type of this PostGaebDestinationOptions.  # noqa: E501

        Defaults to GAEB XML V3.2  # noqa: E501

        :return: The destination_gaeb_type of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: DestinationGaebType
        """
        return self._destination_gaeb_type

    @destination_gaeb_type.setter
    def destination_gaeb_type(self, destination_gaeb_type):
        """Sets the destination_gaeb_type of this PostGaebDestinationOptions.

        Defaults to GAEB XML V3.2  # noqa: E501

        :param destination_gaeb_type: The destination_gaeb_type of this PostGaebDestinationOptions.  # noqa: E501
        :type: DestinationGaebType
        """
        if self._configuration.client_side_validation and destination_gaeb_type is None:
            raise ValueError("Invalid value for `destination_gaeb_type`, must not be `None`")  # noqa: E501

        self._destination_gaeb_type = destination_gaeb_type

    @property
    def target_exchange_phase_transform(self):
        """Gets the target_exchange_phase_transform of this PostGaebDestinationOptions.  # noqa: E501

        Defaults to none, meaning no transformation will be done. The phases are: Base = 81 CostEstimate = 82 OfferRequest = 83 Offer = 84 SideOffer = 85 Grant = 86  # noqa: E501

        :return: The target_exchange_phase_transform of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: DestinationGaebExchangePhase
        """
        return self._target_exchange_phase_transform

    @target_exchange_phase_transform.setter
    def target_exchange_phase_transform(self, target_exchange_phase_transform):
        """Sets the target_exchange_phase_transform of this PostGaebDestinationOptions.

        Defaults to none, meaning no transformation will be done. The phases are: Base = 81 CostEstimate = 82 OfferRequest = 83 Offer = 84 SideOffer = 85 Grant = 86  # noqa: E501

        :param target_exchange_phase_transform: The target_exchange_phase_transform of this PostGaebDestinationOptions.  # noqa: E501
        :type: DestinationGaebExchangePhase
        """
        if self._configuration.client_side_validation and target_exchange_phase_transform is None:
            raise ValueError("Invalid value for `target_exchange_phase_transform`, must not be `None`")  # noqa: E501

        self._target_exchange_phase_transform = target_exchange_phase_transform

    @property
    def enforce_strict_offer_phase_long_text_output(self):
        """Gets the enforce_strict_offer_phase_long_text_output of this PostGaebDestinationOptions.  # noqa: E501

        Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export.  # noqa: E501

        :return: The enforce_strict_offer_phase_long_text_output of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_strict_offer_phase_long_text_output

    @enforce_strict_offer_phase_long_text_output.setter
    def enforce_strict_offer_phase_long_text_output(self, enforce_strict_offer_phase_long_text_output):
        """Sets the enforce_strict_offer_phase_long_text_output of this PostGaebDestinationOptions.

        Defaults to false. If this is enabled, exported long texts to GAEB XML that use text additions will be strictly schema compliant. If this is not enabled, any text that is marked to contain a text addition is exported in full to ensure that incorrectly used text additions are still preserved in the export.  # noqa: E501

        :param enforce_strict_offer_phase_long_text_output: The enforce_strict_offer_phase_long_text_output of this PostGaebDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enforce_strict_offer_phase_long_text_output is None:
            raise ValueError("Invalid value for `enforce_strict_offer_phase_long_text_output`, must not be `None`")  # noqa: E501

        self._enforce_strict_offer_phase_long_text_output = enforce_strict_offer_phase_long_text_output

    @property
    def export_quantity_determination(self):
        """Gets the export_quantity_determination of this PostGaebDestinationOptions.  # noqa: E501

        Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property.  # noqa: E501

        :return: The export_quantity_determination of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._export_quantity_determination

    @export_quantity_determination.setter
    def export_quantity_determination(self, export_quantity_determination):
        """Sets the export_quantity_determination of this PostGaebDestinationOptions.

        Defaults to false. If this is enabled, quantities are exported in detail in GAEB XML targets via the 'QtyDeterm' (Quantity Determination, or Quantity Take Off) fields. To control this, you can set custom quantity calculations in the 'QuantityComponents' property of positions. Please see the entry for 'Quantity Determination' in the Dangl.AVA HowTo documentation section. Please be advised that enabling this might export data that was not intended to be exported, like internal quantity calculation details, depending on what data you put in the 'QuantityComponents' property.  # noqa: E501

        :param export_quantity_determination: The export_quantity_determination of this PostGaebDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and export_quantity_determination is None:
            raise ValueError("Invalid value for `export_quantity_determination`, must not be `None`")  # noqa: E501

        self._export_quantity_determination = export_quantity_determination

    @property
    def remove_unprintable_characters_from_texts(self):
        """Gets the remove_unprintable_characters_from_texts of this PostGaebDestinationOptions.  # noqa: E501

        If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.  # noqa: E501

        :return: The remove_unprintable_characters_from_texts of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._remove_unprintable_characters_from_texts

    @remove_unprintable_characters_from_texts.setter
    def remove_unprintable_characters_from_texts(self, remove_unprintable_characters_from_texts):
        """Sets the remove_unprintable_characters_from_texts of this PostGaebDestinationOptions.

        If this is enabled, unprintable characters are removed from text elements. Otherwise, the conversion might fail in case some text content contains characters that are not allowed in XML output formats. Defaults to true.  # noqa: E501

        :param remove_unprintable_characters_from_texts: The remove_unprintable_characters_from_texts of this PostGaebDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and remove_unprintable_characters_from_texts is None:
            raise ValueError("Invalid value for `remove_unprintable_characters_from_texts`, must not be `None`")  # noqa: E501

        self._remove_unprintable_characters_from_texts = remove_unprintable_characters_from_texts

    @property
    def force_include_descriptions(self):
        """Gets the force_include_descriptions of this PostGaebDestinationOptions.  # noqa: E501

        If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions.  # noqa: E501

        :return: The force_include_descriptions of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._force_include_descriptions

    @force_include_descriptions.setter
    def force_include_descriptions(self, force_include_descriptions):
        """Sets the force_include_descriptions of this PostGaebDestinationOptions.

        If this is enabled, all description elements like texts and execution descriptions will be output to the result. This is mostly only applicable to GAEB exports to phase 84 - Offer, which does typically not include descriptions.  # noqa: E501

        :param force_include_descriptions: The force_include_descriptions of this PostGaebDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and force_include_descriptions is None:
            raise ValueError("Invalid value for `force_include_descriptions`, must not be `None`")  # noqa: E501

        self._force_include_descriptions = force_include_descriptions

    @property
    def treat_null_item_number_schema_as_invalid(self):
        """Gets the treat_null_item_number_schema_as_invalid of this PostGaebDestinationOptions.  # noqa: E501

        When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons.  # noqa: E501

        :return: The treat_null_item_number_schema_as_invalid of this PostGaebDestinationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._treat_null_item_number_schema_as_invalid

    @treat_null_item_number_schema_as_invalid.setter
    def treat_null_item_number_schema_as_invalid(self, treat_null_item_number_schema_as_invalid):
        """Sets the treat_null_item_number_schema_as_invalid of this PostGaebDestinationOptions.

        When exporting to GAEB, an item number schema is usually required. AVACloud will try to fix invalid item number schemas. With this setting, you can also tell AVACloud to treat a null value as invalid. Otherwise, null schemas will simply be ignored and not lead to any schema being generated. It is recommended to enable this option, but it is disabled by default for compatibility reasons.  # noqa: E501

        :param treat_null_item_number_schema_as_invalid: The treat_null_item_number_schema_as_invalid of this PostGaebDestinationOptions.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and treat_null_item_number_schema_as_invalid is None:
            raise ValueError("Invalid value for `treat_null_item_number_schema_as_invalid`, must not be `None`")  # noqa: E501

        self._treat_null_item_number_schema_as_invalid = treat_null_item_number_schema_as_invalid

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
        if issubclass(PostGaebDestinationOptions, dict):
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
        if not isinstance(other, PostGaebDestinationOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostGaebDestinationOptions):
            return True

        return self.to_dict() != other.to_dict()
