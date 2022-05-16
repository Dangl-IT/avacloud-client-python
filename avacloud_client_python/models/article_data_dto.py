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


class ArticleDataDto(object):
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
        'id': 'str',
        'name': 'str',
        'article_number': 'str',
        'quantity': 'float',
        'unit_tag': 'str',
        'description': 'str',
        'short_text': 'str',
        'long_text': 'str',
        'html_long_text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'article_number': 'articleNumber',
        'quantity': 'quantity',
        'unit_tag': 'unitTag',
        'description': 'description',
        'short_text': 'shortText',
        'long_text': 'longText',
        'html_long_text': 'htmlLongText'
    }

    def __init__(self, id=None, name=None, article_number=None, quantity=None, unit_tag=None, description=None, short_text=None, long_text=None, html_long_text=None, _configuration=None):  # noqa: E501
        """ArticleDataDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._article_number = None
        self._quantity = None
        self._unit_tag = None
        self._description = None
        self._short_text = None
        self._long_text = None
        self._html_long_text = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if article_number is not None:
            self.article_number = article_number
        self.quantity = quantity
        if unit_tag is not None:
            self.unit_tag = unit_tag
        if description is not None:
            self.description = description
        if short_text is not None:
            self.short_text = short_text
        if long_text is not None:
            self.long_text = long_text
        if html_long_text is not None:
            self.html_long_text = html_long_text

    @property
    def id(self):
        """Gets the id of this ArticleDataDto.  # noqa: E501

        Elements GUID identifier.  # noqa: E501

        :return: The id of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArticleDataDto.

        Elements GUID identifier.  # noqa: E501

        :param id: The id of this ArticleDataDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ArticleDataDto.  # noqa: E501

        The name (or brand name) for this article, usually given by the supplier or vendor.  # noqa: E501

        :return: The name of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArticleDataDto.

        The name (or brand name) for this article, usually given by the supplier or vendor.  # noqa: E501

        :param name: The name of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def article_number(self):
        """Gets the article_number of this ArticleDataDto.  # noqa: E501

        An article number that describes it, useful when integrating other systems.  # noqa: E501

        :return: The article_number of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._article_number

    @article_number.setter
    def article_number(self, article_number):
        """Sets the article_number of this ArticleDataDto.

        An article number that describes it, useful when integrating other systems.  # noqa: E501

        :param article_number: The article_number of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._article_number = article_number

    @property
    def quantity(self):
        """Gets the quantity of this ArticleDataDto.  # noqa: E501

        Quantity for this article. If this is used within a Position, the quantity here should be the quantity required for the full quantity of the position, not for a single unit.  # noqa: E501

        :return: The quantity of this ArticleDataDto.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ArticleDataDto.

        Quantity for this article. If this is used within a Position, the quantity here should be the quantity required for the full quantity of the position, not for a single unit.  # noqa: E501

        :param quantity: The quantity of this ArticleDataDto.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def unit_tag(self):
        """Gets the unit_tag of this ArticleDataDto.  # noqa: E501

        The unit tag for this single ArticleData.  # noqa: E501

        :return: The unit_tag of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._unit_tag

    @unit_tag.setter
    def unit_tag(self, unit_tag):
        """Sets the unit_tag of this ArticleDataDto.

        The unit tag for this single ArticleData.  # noqa: E501

        :param unit_tag: The unit_tag of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._unit_tag = unit_tag

    @property
    def description(self):
        """Gets the description of this ArticleDataDto.  # noqa: E501

        This is an optional text element that can be used to further describe the ArticleData.  # noqa: E501

        :return: The description of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArticleDataDto.

        This is an optional text element that can be used to further describe the ArticleData.  # noqa: E501

        :param description: The description of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def short_text(self):
        """Gets the short_text of this ArticleDataDto.  # noqa: E501

        Short description for this ITextElement element.  # noqa: E501

        :return: The short_text of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._short_text

    @short_text.setter
    def short_text(self, short_text):
        """Sets the short_text of this ArticleDataDto.

        Short description for this ITextElement element.  # noqa: E501

        :param short_text: The short_text of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._short_text = short_text

    @property
    def long_text(self):
        """Gets the long_text of this ArticleDataDto.  # noqa: E501

        Detailed description for this ITextElement element. When the HtmlLongText is set, this is automatically overwritten and filled with the appropriate plain text representation of the Html text. Vice versa, setting this property overrides the HtmlLongText.  # noqa: E501

        :return: The long_text of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._long_text

    @long_text.setter
    def long_text(self, long_text):
        """Sets the long_text of this ArticleDataDto.

        Detailed description for this ITextElement element. When the HtmlLongText is set, this is automatically overwritten and filled with the appropriate plain text representation of the Html text. Vice versa, setting this property overrides the HtmlLongText.  # noqa: E501

        :param long_text: The long_text of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._long_text = long_text

    @property
    def html_long_text(self):
        """Gets the html_long_text of this ArticleDataDto.  # noqa: E501

        This contains the Html representation of the Longtext. When the LongText is set, this is automatically overwritten and filled with the appropriate Html representation of the plaintext. Vice versa, setting this property overrides the LongText. GAEB 90 and GAEB 2000 exports do not support any image functionality. In GAEB XML, only images that use an embedded Base64 data uri are exported, regular url references are cleared before written out.  # noqa: E501

        :return: The html_long_text of this ArticleDataDto.  # noqa: E501
        :rtype: str
        """
        return self._html_long_text

    @html_long_text.setter
    def html_long_text(self, html_long_text):
        """Sets the html_long_text of this ArticleDataDto.

        This contains the Html representation of the Longtext. When the LongText is set, this is automatically overwritten and filled with the appropriate Html representation of the plaintext. Vice versa, setting this property overrides the LongText. GAEB 90 and GAEB 2000 exports do not support any image functionality. In GAEB XML, only images that use an embedded Base64 data uri are exported, regular url references are cleared before written out.  # noqa: E501

        :param html_long_text: The html_long_text of this ArticleDataDto.  # noqa: E501
        :type: str
        """

        self._html_long_text = html_long_text

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
        if issubclass(ArticleDataDto, dict):
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
        if not isinstance(other, ArticleDataDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArticleDataDto):
            return True

        return self.to_dict() != other.to_dict()

