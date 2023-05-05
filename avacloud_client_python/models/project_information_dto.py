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


class ProjectInformationDto(object):
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
        'buyer': 'PartyInformationDto',
        'description': 'str',
        'description_short': 'str',
        'name': 'str',
        'site': 'PartyInformationDto',
        'item_number_schema': 'ItemNumberSchemaDto',
        'currency_short': 'str',
        'currency_long': 'str',
        'labour_time_label': 'str',
        'price_components': 'list[str]',
        'price_component_types': 'dict(str, PriceComponentTypeDto)',
        'bidder_comment_allowed': 'bool',
        'side_offers_allowed': 'bool',
        'award_type': 'AwardTypeDto',
        'special_award_kind': 'SpecialAwardKindDto',
        'requesters': 'list[PartyInformationDto]',
        'notification_sites': 'list[PartyInformationDto]'
    }

    attribute_map = {
        'buyer': 'buyer',
        'description': 'description',
        'description_short': 'descriptionShort',
        'name': 'name',
        'site': 'site',
        'item_number_schema': 'itemNumberSchema',
        'currency_short': 'currencyShort',
        'currency_long': 'currencyLong',
        'labour_time_label': 'labourTimeLabel',
        'price_components': 'priceComponents',
        'price_component_types': 'priceComponentTypes',
        'bidder_comment_allowed': 'bidderCommentAllowed',
        'side_offers_allowed': 'sideOffersAllowed',
        'award_type': 'awardType',
        'special_award_kind': 'specialAwardKind',
        'requesters': 'requesters',
        'notification_sites': 'notificationSites'
    }

    def __init__(self, buyer=None, description=None, description_short=None, name=None, site=None, item_number_schema=None, currency_short=None, currency_long=None, labour_time_label=None, price_components=None, price_component_types=None, bidder_comment_allowed=None, side_offers_allowed=None, award_type=None, special_award_kind=None, requesters=None, notification_sites=None, _configuration=None):  # noqa: E501
        """ProjectInformationDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._buyer = None
        self._description = None
        self._description_short = None
        self._name = None
        self._site = None
        self._item_number_schema = None
        self._currency_short = None
        self._currency_long = None
        self._labour_time_label = None
        self._price_components = None
        self._price_component_types = None
        self._bidder_comment_allowed = None
        self._side_offers_allowed = None
        self._award_type = None
        self._special_award_kind = None
        self._requesters = None
        self._notification_sites = None
        self.discriminator = None

        if buyer is not None:
            self.buyer = buyer
        if description is not None:
            self.description = description
        if description_short is not None:
            self.description_short = description_short
        if name is not None:
            self.name = name
        if site is not None:
            self.site = site
        if item_number_schema is not None:
            self.item_number_schema = item_number_schema
        if currency_short is not None:
            self.currency_short = currency_short
        if currency_long is not None:
            self.currency_long = currency_long
        if labour_time_label is not None:
            self.labour_time_label = labour_time_label
        if price_components is not None:
            self.price_components = price_components
        if price_component_types is not None:
            self.price_component_types = price_component_types
        self.bidder_comment_allowed = bidder_comment_allowed
        self.side_offers_allowed = side_offers_allowed
        self.award_type = award_type
        self.special_award_kind = special_award_kind
        if requesters is not None:
            self.requesters = requesters
        if notification_sites is not None:
            self.notification_sites = notification_sites

    @property
    def buyer(self):
        """Gets the buyer of this ProjectInformationDto.  # noqa: E501

        Information about the buyer.  # noqa: E501

        :return: The buyer of this ProjectInformationDto.  # noqa: E501
        :rtype: PartyInformationDto
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this ProjectInformationDto.

        Information about the buyer.  # noqa: E501

        :param buyer: The buyer of this ProjectInformationDto.  # noqa: E501
        :type: PartyInformationDto
        """

        self._buyer = buyer

    @property
    def description(self):
        """Gets the description of this ProjectInformationDto.  # noqa: E501

        Description for the project.  # noqa: E501

        :return: The description of this ProjectInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectInformationDto.

        Description for the project.  # noqa: E501

        :param description: The description of this ProjectInformationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_short(self):
        """Gets the description_short of this ProjectInformationDto.  # noqa: E501

        Short description for the project.  # noqa: E501

        :return: The description_short of this ProjectInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """Sets the description_short of this ProjectInformationDto.

        Short description for the project.  # noqa: E501

        :param description_short: The description_short of this ProjectInformationDto.  # noqa: E501
        :type: str
        """

        self._description_short = description_short

    @property
    def name(self):
        """Gets the name of this ProjectInformationDto.  # noqa: E501

        Name of the project.  # noqa: E501

        :return: The name of this ProjectInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectInformationDto.

        Name of the project.  # noqa: E501

        :param name: The name of this ProjectInformationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def site(self):
        """Gets the site of this ProjectInformationDto.  # noqa: E501

        Information about the site.  # noqa: E501

        :return: The site of this ProjectInformationDto.  # noqa: E501
        :rtype: PartyInformationDto
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this ProjectInformationDto.

        Information about the site.  # noqa: E501

        :param site: The site of this ProjectInformationDto.  # noqa: E501
        :type: PartyInformationDto
        """

        self._site = site

    @property
    def item_number_schema(self):
        """Gets the item_number_schema of this ProjectInformationDto.  # noqa: E501

        The ItemNumberSchema used in the project.  # noqa: E501

        :return: The item_number_schema of this ProjectInformationDto.  # noqa: E501
        :rtype: ItemNumberSchemaDto
        """
        return self._item_number_schema

    @item_number_schema.setter
    def item_number_schema(self, item_number_schema):
        """Sets the item_number_schema of this ProjectInformationDto.

        The ItemNumberSchema used in the project.  # noqa: E501

        :param item_number_schema: The item_number_schema of this ProjectInformationDto.  # noqa: E501
        :type: ItemNumberSchemaDto
        """

        self._item_number_schema = item_number_schema

    @property
    def currency_short(self):
        """Gets the currency_short of this ProjectInformationDto.  # noqa: E501

        Short label for the currency used.  # noqa: E501

        :return: The currency_short of this ProjectInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._currency_short

    @currency_short.setter
    def currency_short(self, currency_short):
        """Sets the currency_short of this ProjectInformationDto.

        Short label for the currency used.  # noqa: E501

        :param currency_short: The currency_short of this ProjectInformationDto.  # noqa: E501
        :type: str
        """

        self._currency_short = currency_short

    @property
    def currency_long(self):
        """Gets the currency_long of this ProjectInformationDto.  # noqa: E501

        Full label of the currency used.  # noqa: E501

        :return: The currency_long of this ProjectInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._currency_long

    @currency_long.setter
    def currency_long(self, currency_long):
        """Sets the currency_long of this ProjectInformationDto.

        Full label of the currency used.  # noqa: E501

        :param currency_long: The currency_long of this ProjectInformationDto.  # noqa: E501
        :type: str
        """

        self._currency_long = currency_long

    @property
    def labour_time_label(self):
        """Gets the labour_time_label of this ProjectInformationDto.  # noqa: E501

        Label for the labour time part of prices used in the project.  # noqa: E501

        :return: The labour_time_label of this ProjectInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._labour_time_label

    @labour_time_label.setter
    def labour_time_label(self, labour_time_label):
        """Sets the labour_time_label of this ProjectInformationDto.

        Label for the labour time part of prices used in the project.  # noqa: E501

        :param labour_time_label: The labour_time_label of this ProjectInformationDto.  # noqa: E501
        :type: str
        """

        self._labour_time_label = labour_time_label

    @property
    def price_components(self):
        """Gets the price_components of this ProjectInformationDto.  # noqa: E501

        Labels for the price components used in the project. Caution: Removal of a price component will trigger to have dependent price informations be deleted in IElements that use this property. If this property is changed or altered after the project has already been used, it is strongly advised to do operations step by step, e.g. if renaming and reordering multiple price components, this should be done one by one. Otherwise, a combination of rename and reordering will not be correctly propagated downwards to child objects in this Project.  # noqa: E501

        :return: The price_components of this ProjectInformationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._price_components

    @price_components.setter
    def price_components(self, price_components):
        """Sets the price_components of this ProjectInformationDto.

        Labels for the price components used in the project. Caution: Removal of a price component will trigger to have dependent price informations be deleted in IElements that use this property. If this property is changed or altered after the project has already been used, it is strongly advised to do operations step by step, e.g. if renaming and reordering multiple price components, this should be done one by one. Otherwise, a combination of rename and reordering will not be correctly propagated downwards to child objects in this Project.  # noqa: E501

        :param price_components: The price_components of this ProjectInformationDto.  # noqa: E501
        :type: list[str]
        """

        self._price_components = price_components

    @property
    def price_component_types(self):
        """Gets the price_component_types of this ProjectInformationDto.  # noqa: E501

        This dictionary specifies actual types used for the PriceComponents. For example, a single price component might have the name 'Material' as a string, ans this dictionary would then have a key 'Material' and a value of Materials. You can not add keys here that are not also present in the PriceComponents property, and removing price components will also remove them from this dictionary here.  # noqa: E501

        :return: The price_component_types of this ProjectInformationDto.  # noqa: E501
        :rtype: dict(str, PriceComponentTypeDto)
        """
        return self._price_component_types

    @price_component_types.setter
    def price_component_types(self, price_component_types):
        """Sets the price_component_types of this ProjectInformationDto.

        This dictionary specifies actual types used for the PriceComponents. For example, a single price component might have the name 'Material' as a string, ans this dictionary would then have a key 'Material' and a value of Materials. You can not add keys here that are not also present in the PriceComponents property, and removing price components will also remove them from this dictionary here.  # noqa: E501

        :param price_component_types: The price_component_types of this ProjectInformationDto.  # noqa: E501
        :type: dict(str, PriceComponentTypeDto)
        """

        self._price_component_types = price_component_types

    @property
    def bidder_comment_allowed(self):
        """Gets the bidder_comment_allowed of this ProjectInformationDto.  # noqa: E501

        This bool indicates if this project allows the bidder to add bidder comments. Bidder comments are a way to attach clarifying information when submitting an offer.  # noqa: E501

        :return: The bidder_comment_allowed of this ProjectInformationDto.  # noqa: E501
        :rtype: bool
        """
        return self._bidder_comment_allowed

    @bidder_comment_allowed.setter
    def bidder_comment_allowed(self, bidder_comment_allowed):
        """Sets the bidder_comment_allowed of this ProjectInformationDto.

        This bool indicates if this project allows the bidder to add bidder comments. Bidder comments are a way to attach clarifying information when submitting an offer.  # noqa: E501

        :param bidder_comment_allowed: The bidder_comment_allowed of this ProjectInformationDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and bidder_comment_allowed is None:
            raise ValueError("Invalid value for `bidder_comment_allowed`, must not be `None`")  # noqa: E501

        self._bidder_comment_allowed = bidder_comment_allowed

    @property
    def side_offers_allowed(self):
        """Gets the side_offers_allowed of this ProjectInformationDto.  # noqa: E501

        This property indicates if the project should allow side offers from contractors. In GAEB, a side offer would typically be in exchange phase 85.  # noqa: E501

        :return: The side_offers_allowed of this ProjectInformationDto.  # noqa: E501
        :rtype: bool
        """
        return self._side_offers_allowed

    @side_offers_allowed.setter
    def side_offers_allowed(self, side_offers_allowed):
        """Sets the side_offers_allowed of this ProjectInformationDto.

        This property indicates if the project should allow side offers from contractors. In GAEB, a side offer would typically be in exchange phase 85.  # noqa: E501

        :param side_offers_allowed: The side_offers_allowed of this ProjectInformationDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and side_offers_allowed is None:
            raise ValueError("Invalid value for `side_offers_allowed`, must not be `None`")  # noqa: E501

        self._side_offers_allowed = side_offers_allowed

    @property
    def award_type(self):
        """Gets the award_type of this ProjectInformationDto.  # noqa: E501

        This enumeration describes the type of the award / procurement process. If this is used in a GAEB context, more information about award types can be found in the German VOB/A rules and the GAEB standard  # noqa: E501

        :return: The award_type of this ProjectInformationDto.  # noqa: E501
        :rtype: AwardTypeDto
        """
        return self._award_type

    @award_type.setter
    def award_type(self, award_type):
        """Sets the award_type of this ProjectInformationDto.

        This enumeration describes the type of the award / procurement process. If this is used in a GAEB context, more information about award types can be found in the German VOB/A rules and the GAEB standard  # noqa: E501

        :param award_type: The award_type of this ProjectInformationDto.  # noqa: E501
        :type: AwardTypeDto
        """
        if self._configuration.client_side_validation and award_type is None:
            raise ValueError("Invalid value for `award_type`, must not be `None`")  # noqa: E501

        self._award_type = award_type

    @property
    def special_award_kind(self):
        """Gets the special_award_kind of this ProjectInformationDto.  # noqa: E501

        This enumeration describes awards for project that are not just a regular procurement. For example, it can be used to describe recurring maintenance or an outline contract (German: Rahmenvertrag) which just specifies services and prices but may be requested on demand when necessary  # noqa: E501

        :return: The special_award_kind of this ProjectInformationDto.  # noqa: E501
        :rtype: SpecialAwardKindDto
        """
        return self._special_award_kind

    @special_award_kind.setter
    def special_award_kind(self, special_award_kind):
        """Sets the special_award_kind of this ProjectInformationDto.

        This enumeration describes awards for project that are not just a regular procurement. For example, it can be used to describe recurring maintenance or an outline contract (German: Rahmenvertrag) which just specifies services and prices but may be requested on demand when necessary  # noqa: E501

        :param special_award_kind: The special_award_kind of this ProjectInformationDto.  # noqa: E501
        :type: SpecialAwardKindDto
        """
        if self._configuration.client_side_validation and special_award_kind is None:
            raise ValueError("Invalid value for `special_award_kind`, must not be `None`")  # noqa: E501

        self._special_award_kind = special_award_kind

    @property
    def requesters(self):
        """Gets the requesters of this ProjectInformationDto.  # noqa: E501

        Requesters in a construction project, in German also called 'Bedarfsträger', are parties connected to the building process, e.g. architects or planners.  # noqa: E501

        :return: The requesters of this ProjectInformationDto.  # noqa: E501
        :rtype: list[PartyInformationDto]
        """
        return self._requesters

    @requesters.setter
    def requesters(self, requesters):
        """Sets the requesters of this ProjectInformationDto.

        Requesters in a construction project, in German also called 'Bedarfsträger', are parties connected to the building process, e.g. architects or planners.  # noqa: E501

        :param requesters: The requesters of this ProjectInformationDto.  # noqa: E501
        :type: list[PartyInformationDto]
        """

        self._requesters = requesters

    @property
    def notification_sites(self):
        """Gets the notification_sites of this ProjectInformationDto.  # noqa: E501

        Notification sites are addresses that are used for delivering messages in the context of construction projects.  # noqa: E501

        :return: The notification_sites of this ProjectInformationDto.  # noqa: E501
        :rtype: list[PartyInformationDto]
        """
        return self._notification_sites

    @notification_sites.setter
    def notification_sites(self, notification_sites):
        """Sets the notification_sites of this ProjectInformationDto.

        Notification sites are addresses that are used for delivering messages in the context of construction projects.  # noqa: E501

        :param notification_sites: The notification_sites of this ProjectInformationDto.  # noqa: E501
        :type: list[PartyInformationDto]
        """

        self._notification_sites = notification_sites

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
        if issubclass(ProjectInformationDto, dict):
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
        if not isinstance(other, ProjectInformationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectInformationDto):
            return True

        return self.to_dict() != other.to_dict()

