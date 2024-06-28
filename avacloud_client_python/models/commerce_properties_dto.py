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


class CommercePropertiesDto(object):
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
        'article_number': 'str',
        'ean_gtin_article_number': 'str',
        'iln_article_number': 'str',
        'catalogue_number': 'str',
        'catalogue_article_number': 'str',
        'price_basis': 'float',
        'sub_position_identifier': 'str',
        'customer_base_item_number': 'str'
    }

    attribute_map = {
        'article_number': 'articleNumber',
        'ean_gtin_article_number': 'eanGtinArticleNumber',
        'iln_article_number': 'ilnArticleNumber',
        'catalogue_number': 'catalogueNumber',
        'catalogue_article_number': 'catalogueArticleNumber',
        'price_basis': 'priceBasis',
        'sub_position_identifier': 'subPositionIdentifier',
        'customer_base_item_number': 'customerBaseItemNumber'
    }

    def __init__(self, article_number=None, ean_gtin_article_number=None, iln_article_number=None, catalogue_number=None, catalogue_article_number=None, price_basis=None, sub_position_identifier=None, customer_base_item_number=None, _configuration=None):  # noqa: E501
        """CommercePropertiesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._article_number = None
        self._ean_gtin_article_number = None
        self._iln_article_number = None
        self._catalogue_number = None
        self._catalogue_article_number = None
        self._price_basis = None
        self._sub_position_identifier = None
        self._customer_base_item_number = None
        self.discriminator = None

        if article_number is not None:
            self.article_number = article_number
        if ean_gtin_article_number is not None:
            self.ean_gtin_article_number = ean_gtin_article_number
        if iln_article_number is not None:
            self.iln_article_number = iln_article_number
        if catalogue_number is not None:
            self.catalogue_number = catalogue_number
        if catalogue_article_number is not None:
            self.catalogue_article_number = catalogue_article_number
        if price_basis is not None:
            self.price_basis = price_basis
        if sub_position_identifier is not None:
            self.sub_position_identifier = sub_position_identifier
        if customer_base_item_number is not None:
            self.customer_base_item_number = customer_base_item_number

    @property
    def article_number(self):
        """Gets the article_number of this CommercePropertiesDto.  # noqa: E501

        This maps to ArtNo in GAEB XML and represents an article number given by the supplier.  # noqa: E501

        :return: The article_number of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._article_number

    @article_number.setter
    def article_number(self, article_number):
        """Sets the article_number of this CommercePropertiesDto.

        This maps to ArtNo in GAEB XML and represents an article number given by the supplier.  # noqa: E501

        :param article_number: The article_number of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._article_number = article_number

    @property
    def ean_gtin_article_number(self):
        """Gets the ean_gtin_article_number of this CommercePropertiesDto.  # noqa: E501

        This maps to EAN in GAEB XML and represents an GTIN (formerly EAN) article number.  # noqa: E501

        :return: The ean_gtin_article_number of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._ean_gtin_article_number

    @ean_gtin_article_number.setter
    def ean_gtin_article_number(self, ean_gtin_article_number):
        """Sets the ean_gtin_article_number of this CommercePropertiesDto.

        This maps to EAN in GAEB XML and represents an GTIN (formerly EAN) article number.  # noqa: E501

        :param ean_gtin_article_number: The ean_gtin_article_number of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._ean_gtin_article_number = ean_gtin_article_number

    @property
    def iln_article_number(self):
        """Gets the iln_article_number of this CommercePropertiesDto.  # noqa: E501

        This maps to ArtNoID in GAEB XML and represents an ILN article number.  # noqa: E501

        :return: The iln_article_number of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._iln_article_number

    @iln_article_number.setter
    def iln_article_number(self, iln_article_number):
        """Sets the iln_article_number of this CommercePropertiesDto.

        This maps to ArtNoID in GAEB XML and represents an ILN article number.  # noqa: E501

        :param iln_article_number: The iln_article_number of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._iln_article_number = iln_article_number

    @property
    def catalogue_number(self):
        """Gets the catalogue_number of this CommercePropertiesDto.  # noqa: E501

        This maps to CatalogNo in GAEB XML and represents an identifier of a specific catalogue. The referenced catalogue is usually a customer specific one, not related to CatalogueReferences.  # noqa: E501

        :return: The catalogue_number of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._catalogue_number

    @catalogue_number.setter
    def catalogue_number(self, catalogue_number):
        """Sets the catalogue_number of this CommercePropertiesDto.

        This maps to CatalogNo in GAEB XML and represents an identifier of a specific catalogue. The referenced catalogue is usually a customer specific one, not related to CatalogueReferences.  # noqa: E501

        :param catalogue_number: The catalogue_number of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._catalogue_number = catalogue_number

    @property
    def catalogue_article_number(self):
        """Gets the catalogue_article_number of this CommercePropertiesDto.  # noqa: E501

        This maps to CatalogArtNo in GAEB XML and represents a key that maps to an entry in a specific catalogue. The referenced catalogue is usually a customer specific one, not related to CatalogueReferences.  # noqa: E501

        :return: The catalogue_article_number of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._catalogue_article_number

    @catalogue_article_number.setter
    def catalogue_article_number(self, catalogue_article_number):
        """Sets the catalogue_article_number of this CommercePropertiesDto.

        This maps to CatalogArtNo in GAEB XML and represents a key that maps to an entry in a specific catalogue. The referenced catalogue is usually a customer specific one, not related to CatalogueReferences.  # noqa: E501

        :param catalogue_article_number: The catalogue_article_number of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._catalogue_article_number = catalogue_article_number

    @property
    def price_basis(self):
        """Gets the price_basis of this CommercePropertiesDto.  # noqa: E501

        This optional property can be used to indicate the basis for prices for a single position. Price basis means that the price is given per unit of the basis, e.g. per a pack of five when this property is set to '5'.  # noqa: E501

        :return: The price_basis of this CommercePropertiesDto.  # noqa: E501
        :rtype: float
        """
        return self._price_basis

    @price_basis.setter
    def price_basis(self, price_basis):
        """Sets the price_basis of this CommercePropertiesDto.

        This optional property can be used to indicate the basis for prices for a single position. Price basis means that the price is given per unit of the basis, e.g. per a pack of five when this property is set to '5'.  # noqa: E501

        :param price_basis: The price_basis of this CommercePropertiesDto.  # noqa: E501
        :type: float
        """

        self._price_basis = price_basis

    @property
    def sub_position_identifier(self):
        """Gets the sub_position_identifier of this CommercePropertiesDto.  # noqa: E501

        This optional property can be used to indicate a sub position identifier specific for the commerce exchange  # noqa: E501

        :return: The sub_position_identifier of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._sub_position_identifier

    @sub_position_identifier.setter
    def sub_position_identifier(self, sub_position_identifier):
        """Sets the sub_position_identifier of this CommercePropertiesDto.

        This optional property can be used to indicate a sub position identifier specific for the commerce exchange  # noqa: E501

        :param sub_position_identifier: The sub_position_identifier of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._sub_position_identifier = sub_position_identifier

    @property
    def customer_base_item_number(self):
        """Gets the customer_base_item_number of this CommercePropertiesDto.  # noqa: E501

        In a commerce exchange, this property is usually used to reference the base item number of an underlying phase 83 exchange file  # noqa: E501

        :return: The customer_base_item_number of this CommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._customer_base_item_number

    @customer_base_item_number.setter
    def customer_base_item_number(self, customer_base_item_number):
        """Sets the customer_base_item_number of this CommercePropertiesDto.

        In a commerce exchange, this property is usually used to reference the base item number of an underlying phase 83 exchange file  # noqa: E501

        :param customer_base_item_number: The customer_base_item_number of this CommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._customer_base_item_number = customer_base_item_number

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
        if issubclass(CommercePropertiesDto, dict):
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
        if not isinstance(other, CommercePropertiesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommercePropertiesDto):
            return True

        return self.to_dict() != other.to_dict()
