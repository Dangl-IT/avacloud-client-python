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


class OenormPositionPropertiesDto(object):
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
        'origin_code': 'OenormOriginCodeDto',
        'opening_text_is_free_text': 'bool',
        'is_main_position': 'bool',
        'is_undivided_position': 'bool',
        'oenorm_short_text': 'str',
        'oenorm_short_text_addition': 'str'
    }

    attribute_map = {
        'origin_code': 'originCode',
        'opening_text_is_free_text': 'openingTextIsFreeText',
        'is_main_position': 'isMainPosition',
        'is_undivided_position': 'isUndividedPosition',
        'oenorm_short_text': 'oenormShortText',
        'oenorm_short_text_addition': 'oenormShortTextAddition'
    }

    def __init__(self, origin_code=None, opening_text_is_free_text=None, is_main_position=None, is_undivided_position=None, oenorm_short_text=None, oenorm_short_text_addition=None, _configuration=None):  # noqa: E501
        """OenormPositionPropertiesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._origin_code = None
        self._opening_text_is_free_text = None
        self._is_main_position = None
        self._is_undivided_position = None
        self._oenorm_short_text = None
        self._oenorm_short_text_addition = None
        self.discriminator = None

        self.origin_code = origin_code
        self.opening_text_is_free_text = opening_text_is_free_text
        self.is_main_position = is_main_position
        self.is_undivided_position = is_undivided_position
        if oenorm_short_text is not None:
            self.oenorm_short_text = oenorm_short_text
        if oenorm_short_text_addition is not None:
            self.oenorm_short_text_addition = oenorm_short_text_addition

    @property
    def origin_code(self):
        """Gets the origin_code of this OenormPositionPropertiesDto.  # noqa: E501

        This indicates where the content of this element originates, if set. It corresponds to 'herkunftskennzeichen' in ÖNorm  # noqa: E501

        :return: The origin_code of this OenormPositionPropertiesDto.  # noqa: E501
        :rtype: OenormOriginCodeDto
        """
        return self._origin_code

    @origin_code.setter
    def origin_code(self, origin_code):
        """Sets the origin_code of this OenormPositionPropertiesDto.

        This indicates where the content of this element originates, if set. It corresponds to 'herkunftskennzeichen' in ÖNorm  # noqa: E501

        :param origin_code: The origin_code of this OenormPositionPropertiesDto.  # noqa: E501
        :type: OenormOriginCodeDto
        """
        if self._configuration.client_side_validation and origin_code is None:
            raise ValueError("Invalid value for `origin_code`, must not be `None`")  # noqa: E501

        self._origin_code = origin_code

    @property
    def opening_text_is_free_text(self):
        """Gets the opening_text_is_free_text of this OenormPositionPropertiesDto.  # noqa: E501

        This marks if the opening texts within this element are considered free text. It corresponds to 'vorbemerkungskennzeichen' in ÖNorm.  # noqa: E501

        :return: The opening_text_is_free_text of this OenormPositionPropertiesDto.  # noqa: E501
        :rtype: bool
        """
        return self._opening_text_is_free_text

    @opening_text_is_free_text.setter
    def opening_text_is_free_text(self, opening_text_is_free_text):
        """Sets the opening_text_is_free_text of this OenormPositionPropertiesDto.

        This marks if the opening texts within this element are considered free text. It corresponds to 'vorbemerkungskennzeichen' in ÖNorm.  # noqa: E501

        :param opening_text_is_free_text: The opening_text_is_free_text of this OenormPositionPropertiesDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and opening_text_is_free_text is None:
            raise ValueError("Invalid value for `opening_text_is_free_text`, must not be `None`")  # noqa: E501

        self._opening_text_is_free_text = opening_text_is_free_text

    @property
    def is_main_position(self):
        """Gets the is_main_position of this OenormPositionPropertiesDto.  # noqa: E501

        This indicates if the ÖNorm 'wesentliche position' mark is set  # noqa: E501

        :return: The is_main_position of this OenormPositionPropertiesDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_main_position

    @is_main_position.setter
    def is_main_position(self, is_main_position):
        """Sets the is_main_position of this OenormPositionPropertiesDto.

        This indicates if the ÖNorm 'wesentliche position' mark is set  # noqa: E501

        :param is_main_position: The is_main_position of this OenormPositionPropertiesDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_main_position is None:
            raise ValueError("Invalid value for `is_main_position`, must not be `None`")  # noqa: E501

        self._is_main_position = is_main_position

    @property
    def is_undivided_position(self):
        """Gets the is_undivided_position of this OenormPositionPropertiesDto.  # noqa: E501

        This indicates if the ÖNorm position was a 'ungeteilteposition' (undivided position). This will only be taken into account when the position is also the sole element inside it's parent group  # noqa: E501

        :return: The is_undivided_position of this OenormPositionPropertiesDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_undivided_position

    @is_undivided_position.setter
    def is_undivided_position(self, is_undivided_position):
        """Sets the is_undivided_position of this OenormPositionPropertiesDto.

        This indicates if the ÖNorm position was a 'ungeteilteposition' (undivided position). This will only be taken into account when the position is also the sole element inside it's parent group  # noqa: E501

        :param is_undivided_position: The is_undivided_position of this OenormPositionPropertiesDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_undivided_position is None:
            raise ValueError("Invalid value for `is_undivided_position`, must not be `None`")  # noqa: E501

        self._is_undivided_position = is_undivided_position

    @property
    def oenorm_short_text(self):
        """Gets the oenorm_short_text of this OenormPositionPropertiesDto.  # noqa: E501

        In some ÖNorm formats, the short text can have it's own addition, so the text is split up in OenormShortText and OenormShortTextAddition To serialize this, either the ShortText property of the parent position needs to be null, or OenormShortText ' ' OenormShortTextAddition needs to match the ShortText.  # noqa: E501

        :return: The oenorm_short_text of this OenormPositionPropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._oenorm_short_text

    @oenorm_short_text.setter
    def oenorm_short_text(self, oenorm_short_text):
        """Sets the oenorm_short_text of this OenormPositionPropertiesDto.

        In some ÖNorm formats, the short text can have it's own addition, so the text is split up in OenormShortText and OenormShortTextAddition To serialize this, either the ShortText property of the parent position needs to be null, or OenormShortText ' ' OenormShortTextAddition needs to match the ShortText.  # noqa: E501

        :param oenorm_short_text: The oenorm_short_text of this OenormPositionPropertiesDto.  # noqa: E501
        :type: str
        """

        self._oenorm_short_text = oenorm_short_text

    @property
    def oenorm_short_text_addition(self):
        """Gets the oenorm_short_text_addition of this OenormPositionPropertiesDto.  # noqa: E501

        In some ÖNorm formats, the short text can have it's own addition, so the text is split up in OenormShortText and OenormShortTextAddition To serialize this, either the ShortText property of the parent position needs to be null, or OenormShortText ' ' OenormShortTextAddition needs to match the ShortText.  # noqa: E501

        :return: The oenorm_short_text_addition of this OenormPositionPropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._oenorm_short_text_addition

    @oenorm_short_text_addition.setter
    def oenorm_short_text_addition(self, oenorm_short_text_addition):
        """Sets the oenorm_short_text_addition of this OenormPositionPropertiesDto.

        In some ÖNorm formats, the short text can have it's own addition, so the text is split up in OenormShortText and OenormShortTextAddition To serialize this, either the ShortText property of the parent position needs to be null, or OenormShortText ' ' OenormShortTextAddition needs to match the ShortText.  # noqa: E501

        :param oenorm_short_text_addition: The oenorm_short_text_addition of this OenormPositionPropertiesDto.  # noqa: E501
        :type: str
        """

        self._oenorm_short_text_addition = oenorm_short_text_addition

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
        if issubclass(OenormPositionPropertiesDto, dict):
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
        if not isinstance(other, OenormPositionPropertiesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OenormPositionPropertiesDto):
            return True

        return self.to_dict() != other.to_dict()

