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

from avacloud_client_python.models.addition_type_dto import AdditionTypeDto  # noqa: F401,E501
from avacloud_client_python.models.i_element_dto import IElementDto  # noqa: F401,E501
from avacloud_client_python.models.standardized_description_dto import StandardizedDescriptionDto  # noqa: F401,E501


class NoteTextDto(IElementDto):
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
        'is_opening_text': 'bool',
        'is_closing_text': 'bool',
        'short_text': 'str',
        'addition_type': 'AdditionTypeDto',
        'long_text': 'str',
        'html_long_text': 'str',
        'standardized_description': 'StandardizedDescriptionDto',
        'element_type': 'str'
    }

    attribute_map = {
        'is_opening_text': 'isOpeningText',
        'is_closing_text': 'isClosingText',
        'short_text': 'shortText',
        'addition_type': 'additionType',
        'long_text': 'longText',
        'html_long_text': 'htmlLongText',
        'standardized_description': 'standardizedDescription',
        'element_type': 'elementType'
    }

    def __init__(self, is_opening_text=None, is_closing_text=None, short_text=None, addition_type=None, long_text=None, html_long_text=None, standardized_description=None, element_type=None):  # noqa: E501
        """NoteTextDto - a model defined in Swagger"""  # noqa: E501

        self._is_opening_text = None
        self._is_closing_text = None
        self._short_text = None
        self._addition_type = None
        self._long_text = None
        self._html_long_text = None
        self._standardized_description = None
        self._element_type = None
        self.discriminator = None

        self.is_opening_text = is_opening_text
        self.is_closing_text = is_closing_text
        if short_text is not None:
            self.short_text = short_text
        self.addition_type = addition_type
        if long_text is not None:
            self.long_text = long_text
        if html_long_text is not None:
            self.html_long_text = html_long_text
        if standardized_description is not None:
            self.standardized_description = standardized_description
        if element_type is not None:
            self.element_type = element_type

    @property
    def is_opening_text(self):
        """Gets the is_opening_text of this NoteTextDto.  # noqa: E501

        If this is set to true, this text is meant to not be seen as part of the regular elements hierarchy but as a special opening text at the beginning of the project. For example, in GAEB XML, this would map to the GAEB.Award.AddText. Typically, such texts describe project-wide contractual definitions. If this is set to true, this NoteText should be placed at the top of the elements hierarchy directly in the ServiceSpecification.Elements group, otherwise it will likely not be treated correctly when exporting to GAEB. You can only set IsOpeningText or IsClosingText to true.  # noqa: E501

        :return: The is_opening_text of this NoteTextDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_opening_text

    @is_opening_text.setter
    def is_opening_text(self, is_opening_text):
        """Sets the is_opening_text of this NoteTextDto.

        If this is set to true, this text is meant to not be seen as part of the regular elements hierarchy but as a special opening text at the beginning of the project. For example, in GAEB XML, this would map to the GAEB.Award.AddText. Typically, such texts describe project-wide contractual definitions. If this is set to true, this NoteText should be placed at the top of the elements hierarchy directly in the ServiceSpecification.Elements group, otherwise it will likely not be treated correctly when exporting to GAEB. You can only set IsOpeningText or IsClosingText to true.  # noqa: E501

        :param is_opening_text: The is_opening_text of this NoteTextDto.  # noqa: E501
        :type: bool
        """
        if is_opening_text is None:
            raise ValueError("Invalid value for `is_opening_text`, must not be `None`")  # noqa: E501

        self._is_opening_text = is_opening_text

    @property
    def is_closing_text(self):
        """Gets the is_closing_text of this NoteTextDto.  # noqa: E501

        If this is set to true, this text is meant to not be seen as part of the regular elements hierarchy but as a special closing text at the end of the project. For Example, in GAEB XML, this would map to the GAEB.AddText. Typically, such texts are used to describe project wide finishing descriptions. If this is set to true, this NoteText should be placed at the top of the elements hierarchy directly in the ServiceSpecification.Elements group, otherwise it will likely not be treated correctly when exporting to GAEB. You can only set IsOpeningText or IsClosingText to true.  # noqa: E501

        :return: The is_closing_text of this NoteTextDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_closing_text

    @is_closing_text.setter
    def is_closing_text(self, is_closing_text):
        """Sets the is_closing_text of this NoteTextDto.

        If this is set to true, this text is meant to not be seen as part of the regular elements hierarchy but as a special closing text at the end of the project. For Example, in GAEB XML, this would map to the GAEB.AddText. Typically, such texts are used to describe project wide finishing descriptions. If this is set to true, this NoteText should be placed at the top of the elements hierarchy directly in the ServiceSpecification.Elements group, otherwise it will likely not be treated correctly when exporting to GAEB. You can only set IsOpeningText or IsClosingText to true.  # noqa: E501

        :param is_closing_text: The is_closing_text of this NoteTextDto.  # noqa: E501
        :type: bool
        """
        if is_closing_text is None:
            raise ValueError("Invalid value for `is_closing_text`, must not be `None`")  # noqa: E501

        self._is_closing_text = is_closing_text

    @property
    def short_text(self):
        """Gets the short_text of this NoteTextDto.  # noqa: E501

        Short description for this DescriptionBase element.  # noqa: E501

        :return: The short_text of this NoteTextDto.  # noqa: E501
        :rtype: str
        """
        return self._short_text

    @short_text.setter
    def short_text(self, short_text):
        """Sets the short_text of this NoteTextDto.

        Short description for this DescriptionBase element.  # noqa: E501

        :param short_text: The short_text of this NoteTextDto.  # noqa: E501
        :type: str
        """

        self._short_text = short_text

    @property
    def addition_type(self):
        """Gets the addition_type of this NoteTextDto.  # noqa: E501

        Indicates if this DescriptionBase element contains Buyer or Bidder additions to the text.  # noqa: E501

        :return: The addition_type of this NoteTextDto.  # noqa: E501
        :rtype: AdditionTypeDto
        """
        return self._addition_type

    @addition_type.setter
    def addition_type(self, addition_type):
        """Sets the addition_type of this NoteTextDto.

        Indicates if this DescriptionBase element contains Buyer or Bidder additions to the text.  # noqa: E501

        :param addition_type: The addition_type of this NoteTextDto.  # noqa: E501
        :type: AdditionTypeDto
        """
        if addition_type is None:
            raise ValueError("Invalid value for `addition_type`, must not be `None`")  # noqa: E501

        self._addition_type = addition_type

    @property
    def long_text(self):
        """Gets the long_text of this NoteTextDto.  # noqa: E501

        Detailed description for this DescriptionBase element. When the HtmlLongText is set, this is automatically overwritten and filled with the appropriate plain text representation of the Html text. Vice versa, setting this property overrides the HtmlLongText.  # noqa: E501

        :return: The long_text of this NoteTextDto.  # noqa: E501
        :rtype: str
        """
        return self._long_text

    @long_text.setter
    def long_text(self, long_text):
        """Sets the long_text of this NoteTextDto.

        Detailed description for this DescriptionBase element. When the HtmlLongText is set, this is automatically overwritten and filled with the appropriate plain text representation of the Html text. Vice versa, setting this property overrides the HtmlLongText.  # noqa: E501

        :param long_text: The long_text of this NoteTextDto.  # noqa: E501
        :type: str
        """

        self._long_text = long_text

    @property
    def html_long_text(self):
        """Gets the html_long_text of this NoteTextDto.  # noqa: E501

        This contains the Html representation of the Longtext. When the LongText is set, this is automatically overwritten and filled with the appropriate Html representation of the plaintext. Vice versa, setting this property overrides the LongText. GAEB 90 and GAEB 2000 exports do not support any image functionality. In GAEB XML, only images that use an embedded Base64 data uri are exported, regular url references are cleared before written out.  # noqa: E501

        :return: The html_long_text of this NoteTextDto.  # noqa: E501
        :rtype: str
        """
        return self._html_long_text

    @html_long_text.setter
    def html_long_text(self, html_long_text):
        """Sets the html_long_text of this NoteTextDto.

        This contains the Html representation of the Longtext. When the LongText is set, this is automatically overwritten and filled with the appropriate Html representation of the plaintext. Vice versa, setting this property overrides the LongText. GAEB 90 and GAEB 2000 exports do not support any image functionality. In GAEB XML, only images that use an embedded Base64 data uri are exported, regular url references are cleared before written out.  # noqa: E501

        :param html_long_text: The html_long_text of this NoteTextDto.  # noqa: E501
        :type: str
        """

        self._html_long_text = html_long_text

    @property
    def standardized_description(self):
        """Gets the standardized_description of this NoteTextDto.  # noqa: E501

        This represents a standardized description. This means that instead of solely relying on texts to describe a service, external standards and definitions are referenced for a common understanding.  # noqa: E501

        :return: The standardized_description of this NoteTextDto.  # noqa: E501
        :rtype: StandardizedDescriptionDto
        """
        return self._standardized_description

    @standardized_description.setter
    def standardized_description(self, standardized_description):
        """Sets the standardized_description of this NoteTextDto.

        This represents a standardized description. This means that instead of solely relying on texts to describe a service, external standards and definitions are referenced for a common understanding.  # noqa: E501

        :param standardized_description: The standardized_description of this NoteTextDto.  # noqa: E501
        :type: StandardizedDescriptionDto
        """

        self._standardized_description = standardized_description

    @property
    def element_type(self):
        """Gets the element_type of this NoteTextDto.  # noqa: E501


        :return: The element_type of this NoteTextDto.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this NoteTextDto.


        :param element_type: The element_type of this NoteTextDto.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

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
        if issubclass(NoteTextDto, dict):
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
        if not isinstance(other, NoteTextDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
