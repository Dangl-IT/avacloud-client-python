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


class LineItemInformation(object):
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
        'name': 'str',
        'description': 'str',
        'seller_identifier': 'str',
        'buyer_identifier': 'str',
        'standard_identifier': 'str',
        'classification_identifiers': 'list[str]',
        'country_of_origin': 'str',
        'attributes': 'list[LineItemAttribute]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'seller_identifier': 'sellerIdentifier',
        'buyer_identifier': 'buyerIdentifier',
        'standard_identifier': 'standardIdentifier',
        'classification_identifiers': 'classificationIdentifiers',
        'country_of_origin': 'countryOfOrigin',
        'attributes': 'attributes'
    }

    def __init__(self, name=None, description=None, seller_identifier=None, buyer_identifier=None, standard_identifier=None, classification_identifiers=None, country_of_origin=None, attributes=None, _configuration=None):  # noqa: E501
        """LineItemInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._seller_identifier = None
        self._buyer_identifier = None
        self._standard_identifier = None
        self._classification_identifiers = None
        self._country_of_origin = None
        self._attributes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if seller_identifier is not None:
            self.seller_identifier = seller_identifier
        if buyer_identifier is not None:
            self.buyer_identifier = buyer_identifier
        if standard_identifier is not None:
            self.standard_identifier = standard_identifier
        if classification_identifiers is not None:
            self.classification_identifiers = classification_identifiers
        if country_of_origin is not None:
            self.country_of_origin = country_of_origin
        if attributes is not None:
            self.attributes = attributes

    @property
    def name(self):
        """Gets the name of this LineItemInformation.  # noqa: E501


        :return: The name of this LineItemInformation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LineItemInformation.


        :param name: The name of this LineItemInformation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this LineItemInformation.  # noqa: E501


        :return: The description of this LineItemInformation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LineItemInformation.


        :param description: The description of this LineItemInformation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def seller_identifier(self):
        """Gets the seller_identifier of this LineItemInformation.  # noqa: E501


        :return: The seller_identifier of this LineItemInformation.  # noqa: E501
        :rtype: str
        """
        return self._seller_identifier

    @seller_identifier.setter
    def seller_identifier(self, seller_identifier):
        """Sets the seller_identifier of this LineItemInformation.


        :param seller_identifier: The seller_identifier of this LineItemInformation.  # noqa: E501
        :type: str
        """

        self._seller_identifier = seller_identifier

    @property
    def buyer_identifier(self):
        """Gets the buyer_identifier of this LineItemInformation.  # noqa: E501


        :return: The buyer_identifier of this LineItemInformation.  # noqa: E501
        :rtype: str
        """
        return self._buyer_identifier

    @buyer_identifier.setter
    def buyer_identifier(self, buyer_identifier):
        """Sets the buyer_identifier of this LineItemInformation.


        :param buyer_identifier: The buyer_identifier of this LineItemInformation.  # noqa: E501
        :type: str
        """

        self._buyer_identifier = buyer_identifier

    @property
    def standard_identifier(self):
        """Gets the standard_identifier of this LineItemInformation.  # noqa: E501


        :return: The standard_identifier of this LineItemInformation.  # noqa: E501
        :rtype: str
        """
        return self._standard_identifier

    @standard_identifier.setter
    def standard_identifier(self, standard_identifier):
        """Sets the standard_identifier of this LineItemInformation.


        :param standard_identifier: The standard_identifier of this LineItemInformation.  # noqa: E501
        :type: str
        """

        self._standard_identifier = standard_identifier

    @property
    def classification_identifiers(self):
        """Gets the classification_identifiers of this LineItemInformation.  # noqa: E501


        :return: The classification_identifiers of this LineItemInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._classification_identifiers

    @classification_identifiers.setter
    def classification_identifiers(self, classification_identifiers):
        """Sets the classification_identifiers of this LineItemInformation.


        :param classification_identifiers: The classification_identifiers of this LineItemInformation.  # noqa: E501
        :type: list[str]
        """

        self._classification_identifiers = classification_identifiers

    @property
    def country_of_origin(self):
        """Gets the country_of_origin of this LineItemInformation.  # noqa: E501


        :return: The country_of_origin of this LineItemInformation.  # noqa: E501
        :rtype: str
        """
        return self._country_of_origin

    @country_of_origin.setter
    def country_of_origin(self, country_of_origin):
        """Sets the country_of_origin of this LineItemInformation.


        :param country_of_origin: The country_of_origin of this LineItemInformation.  # noqa: E501
        :type: str
        """

        self._country_of_origin = country_of_origin

    @property
    def attributes(self):
        """Gets the attributes of this LineItemInformation.  # noqa: E501


        :return: The attributes of this LineItemInformation.  # noqa: E501
        :rtype: list[LineItemAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LineItemInformation.


        :param attributes: The attributes of this LineItemInformation.  # noqa: E501
        :type: list[LineItemAttribute]
        """

        self._attributes = attributes

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
        if issubclass(LineItemInformation, dict):
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
        if not isinstance(other, LineItemInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineItemInformation):
            return True

        return self.to_dict() != other.to_dict()