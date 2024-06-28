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


class NoteTextDto(object):
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
        'identifier': 'str',
        'standardized_description': 'StandardizedDescriptionDto',
        'element_type': 'str',
        'description_id': 'str',
        'oenorm_note_text_properties': 'OenormNoteTextPropertiesDto',
        'has_bidder_comment_in_html_long_text': 'bool'
    }

    attribute_map = {
        'is_opening_text': 'isOpeningText',
        'is_closing_text': 'isClosingText',
        'short_text': 'shortText',
        'addition_type': 'additionType',
        'long_text': 'longText',
        'html_long_text': 'htmlLongText',
        'identifier': 'identifier',
        'standardized_description': 'standardizedDescription',
        'element_type': 'elementType',
        'description_id': 'descriptionId',
        'oenorm_note_text_properties': 'oenormNoteTextProperties',
        'has_bidder_comment_in_html_long_text': 'hasBidderCommentInHtmlLongText'
    }

    def __init__(self, is_opening_text=None, is_closing_text=None, short_text=None, addition_type=None, long_text=None, html_long_text=None, identifier=None, standardized_description=None, element_type=None, description_id=None, oenorm_note_text_properties=None, has_bidder_comment_in_html_long_text=None, _configuration=None):  # noqa: E501
        """NoteTextDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_opening_text = None
        self._is_closing_text = None
        self._short_text = None
        self._addition_type = None
        self._long_text = None
        self._html_long_text = None
        self._identifier = None
        self._standardized_description = None
        self._element_type = None
        self._description_id = None
        self._oenorm_note_text_properties = None
        self._has_bidder_comment_in_html_long_text = None
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
        if identifier is not None:
            self.identifier = identifier
        if standardized_description is not None:
            self.standardized_description = standardized_description
        if element_type is not None:
            self.element_type = element_type
        if description_id is not None:
            self.description_id = description_id
        if oenorm_note_text_properties is not None:
            self.oenorm_note_text_properties = oenorm_note_text_properties
        self.has_bidder_comment_in_html_long_text = has_bidder_comment_in_html_long_text

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
        if self._configuration.client_side_validation and is_opening_text is None:
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
        if self._configuration.client_side_validation and is_closing_text is None:
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
        if self._configuration.client_side_validation and addition_type is None:
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
    def identifier(self):
        """Gets the identifier of this NoteTextDto.  # noqa: E501

        This is an optional internal identifier that may be used to add additional information to this NoteText. It is not supported in GAEB import or export.  # noqa: E501

        :return: The identifier of this NoteTextDto.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this NoteTextDto.

        This is an optional internal identifier that may be used to add additional information to this NoteText. It is not supported in GAEB import or export.  # noqa: E501

        :param identifier: The identifier of this NoteTextDto.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

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

    @property
    def description_id(self):
        """Gets the description_id of this NoteTextDto.  # noqa: E501

        This is an identifier specific for this description. Some exchange formats, like GAEB XML, use it to identify descriptions. It's different to an elements identifier in that it should only apply to the description component, meaning the text itself.  # noqa: E501

        :return: The description_id of this NoteTextDto.  # noqa: E501
        :rtype: str
        """
        return self._description_id

    @description_id.setter
    def description_id(self, description_id):
        """Sets the description_id of this NoteTextDto.

        This is an identifier specific for this description. Some exchange formats, like GAEB XML, use it to identify descriptions. It's different to an elements identifier in that it should only apply to the description component, meaning the text itself.  # noqa: E501

        :param description_id: The description_id of this NoteTextDto.  # noqa: E501
        :type: str
        """

        self._description_id = description_id

    @property
    def oenorm_note_text_properties(self):
        """Gets the oenorm_note_text_properties of this NoteTextDto.  # noqa: E501

        This class models special properties that only apply to some exchange scenarios where ÖNorm is used. It is special for NoteTexts.  # noqa: E501

        :return: The oenorm_note_text_properties of this NoteTextDto.  # noqa: E501
        :rtype: OenormNoteTextPropertiesDto
        """
        return self._oenorm_note_text_properties

    @oenorm_note_text_properties.setter
    def oenorm_note_text_properties(self, oenorm_note_text_properties):
        """Sets the oenorm_note_text_properties of this NoteTextDto.

        This class models special properties that only apply to some exchange scenarios where ÖNorm is used. It is special for NoteTexts.  # noqa: E501

        :param oenorm_note_text_properties: The oenorm_note_text_properties of this NoteTextDto.  # noqa: E501
        :type: OenormNoteTextPropertiesDto
        """

        self._oenorm_note_text_properties = oenorm_note_text_properties

    @property
    def has_bidder_comment_in_html_long_text(self):
        """Gets the has_bidder_comment_in_html_long_text of this NoteTextDto.  # noqa: E501


        :return: The has_bidder_comment_in_html_long_text of this NoteTextDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_bidder_comment_in_html_long_text

    @has_bidder_comment_in_html_long_text.setter
    def has_bidder_comment_in_html_long_text(self, has_bidder_comment_in_html_long_text):
        """Sets the has_bidder_comment_in_html_long_text of this NoteTextDto.


        :param has_bidder_comment_in_html_long_text: The has_bidder_comment_in_html_long_text of this NoteTextDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and has_bidder_comment_in_html_long_text is None:
            raise ValueError("Invalid value for `has_bidder_comment_in_html_long_text`, must not be `None`")  # noqa: E501

        self._has_bidder_comment_in_html_long_text = has_bidder_comment_in_html_long_text

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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NoteTextDto):
            return True

        return self.to_dict() != other.to_dict()
