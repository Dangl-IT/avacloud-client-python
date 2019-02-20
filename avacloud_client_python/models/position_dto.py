# coding: utf-8

"""
    AVACloud API 1.5.3

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from avacloud_client_python.models.addition_type_dto import AdditionTypeDto  # noqa: F401,E501
from avacloud_client_python.models.calculation_dto import CalculationDto  # noqa: F401,E501
from avacloud_client_python.models.comission_status_dto import ComissionStatusDto  # noqa: F401,E501
from avacloud_client_python.models.commerce_properties_dto import CommercePropertiesDto  # noqa: F401,E501
from avacloud_client_python.models.i_element_dto import IElementDto  # noqa: F401,E501
from avacloud_client_python.models.item_number_dto import ItemNumberDto  # noqa: F401,E501
from avacloud_client_python.models.labour_price_component_dto import LabourPriceComponentDto  # noqa: F401,E501
from avacloud_client_python.models.position_type_dto import PositionTypeDto  # noqa: F401,E501
from avacloud_client_python.models.price_component_dto import PriceComponentDto  # noqa: F401,E501
from avacloud_client_python.models.price_type_dto import PriceTypeDto  # noqa: F401,E501
from avacloud_client_python.models.quantity_assignment_dto import QuantityAssignmentDto  # noqa: F401,E501
from avacloud_client_python.models.service_type_dto import ServiceTypeDto  # noqa: F401,E501
from avacloud_client_python.models.sub_description_dto import SubDescriptionDto  # noqa: F401,E501


class PositionDto(IElementDto):
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
        'unit_price': 'float',
        'quantity': 'float',
        'unit_tag': 'str',
        'labour_components': 'LabourPriceComponentDto',
        'price_components': 'list[PriceComponentDto]',
        'quantity_components': 'list[CalculationDto]',
        'sub_descriptions': 'list[SubDescriptionDto]',
        'comission_status': 'ComissionStatusDto',
        'complemented_by': 'list[str]',
        'complemented': 'bool',
        'amount_to_be_entered_by_bidder': 'bool',
        'price_composition_required': 'bool',
        'use_different_tax_rate': 'bool',
        'tax_rate': 'float',
        'item_number': 'ItemNumberDto',
        'deduction_factor': 'float',
        'total_price': 'float',
        'total_price_gross': 'float',
        'total_price_gross_deducted': 'float',
        'deducted_price': 'float',
        'position_type': 'PositionTypeDto',
        'price_type': 'PriceTypeDto',
        'service_type': 'ServiceTypeDto',
        'short_text': 'str',
        'long_text': 'str',
        'html_long_text': 'str',
        'addition_type': 'AdditionTypeDto',
        'element_type': 'str',
        'quantity_assignments': 'list[QuantityAssignmentDto]',
        'commerce_properties': 'CommercePropertiesDto',
        'alternative_to': 'str',
        'is_lump_sum': 'bool',
        'repetition_to': 'str',
        'type': 'str'
    }

    attribute_map = {
        'unit_price': 'unitPrice',
        'quantity': 'quantity',
        'unit_tag': 'unitTag',
        'labour_components': 'labourComponents',
        'price_components': 'priceComponents',
        'quantity_components': 'quantityComponents',
        'sub_descriptions': 'subDescriptions',
        'comission_status': 'comissionStatus',
        'complemented_by': 'complementedBy',
        'complemented': 'complemented',
        'amount_to_be_entered_by_bidder': 'amountToBeEnteredByBidder',
        'price_composition_required': 'priceCompositionRequired',
        'use_different_tax_rate': 'useDifferentTaxRate',
        'tax_rate': 'taxRate',
        'item_number': 'itemNumber',
        'deduction_factor': 'deductionFactor',
        'total_price': 'totalPrice',
        'total_price_gross': 'totalPriceGross',
        'total_price_gross_deducted': 'totalPriceGrossDeducted',
        'deducted_price': 'deductedPrice',
        'position_type': 'positionType',
        'price_type': 'priceType',
        'service_type': 'serviceType',
        'short_text': 'shortText',
        'long_text': 'longText',
        'html_long_text': 'htmlLongText',
        'addition_type': 'additionType',
        'element_type': 'elementType',
        'quantity_assignments': 'quantityAssignments',
        'commerce_properties': 'commerceProperties',
        'alternative_to': 'alternativeTo',
        'is_lump_sum': 'isLumpSum',
        'repetition_to': 'repetitionTo',
        'type': 'type'
    }

    def __init__(self, unit_price=None, quantity=None, unit_tag=None, labour_components=None, price_components=None, quantity_components=None, sub_descriptions=None, comission_status=None, complemented_by=None, complemented=None, amount_to_be_entered_by_bidder=None, price_composition_required=None, use_different_tax_rate=None, tax_rate=None, item_number=None, deduction_factor=None, total_price=None, total_price_gross=None, total_price_gross_deducted=None, deducted_price=None, position_type=None, price_type=None, service_type=None, short_text=None, long_text=None, html_long_text=None, addition_type=None, element_type=None, quantity_assignments=None, commerce_properties=None, alternative_to=None, is_lump_sum=None, repetition_to=None, type=None):  # noqa: E501
        """PositionDto - a model defined in Swagger"""  # noqa: E501

        self._unit_price = None
        self._quantity = None
        self._unit_tag = None
        self._labour_components = None
        self._price_components = None
        self._quantity_components = None
        self._sub_descriptions = None
        self._comission_status = None
        self._complemented_by = None
        self._complemented = None
        self._amount_to_be_entered_by_bidder = None
        self._price_composition_required = None
        self._use_different_tax_rate = None
        self._tax_rate = None
        self._item_number = None
        self._deduction_factor = None
        self._total_price = None
        self._total_price_gross = None
        self._total_price_gross_deducted = None
        self._deducted_price = None
        self._position_type = None
        self._price_type = None
        self._service_type = None
        self._short_text = None
        self._long_text = None
        self._html_long_text = None
        self._addition_type = None
        self._element_type = None
        self._quantity_assignments = None
        self._commerce_properties = None
        self._alternative_to = None
        self._is_lump_sum = None
        self._repetition_to = None
        self._type = None
        self.discriminator = None

        self.unit_price = unit_price
        self.quantity = quantity
        if unit_tag is not None:
            self.unit_tag = unit_tag
        if labour_components is not None:
            self.labour_components = labour_components
        if price_components is not None:
            self.price_components = price_components
        if quantity_components is not None:
            self.quantity_components = quantity_components
        if sub_descriptions is not None:
            self.sub_descriptions = sub_descriptions
        self.comission_status = comission_status
        if complemented_by is not None:
            self.complemented_by = complemented_by
        self.complemented = complemented
        self.amount_to_be_entered_by_bidder = amount_to_be_entered_by_bidder
        self.price_composition_required = price_composition_required
        self.use_different_tax_rate = use_different_tax_rate
        self.tax_rate = tax_rate
        if item_number is not None:
            self.item_number = item_number
        self.deduction_factor = deduction_factor
        self.total_price = total_price
        self.total_price_gross = total_price_gross
        self.total_price_gross_deducted = total_price_gross_deducted
        self.deducted_price = deducted_price
        self.position_type = position_type
        self.price_type = price_type
        self.service_type = service_type
        if short_text is not None:
            self.short_text = short_text
        if long_text is not None:
            self.long_text = long_text
        if html_long_text is not None:
            self.html_long_text = html_long_text
        self.addition_type = addition_type
        if element_type is not None:
            self.element_type = element_type
        if quantity_assignments is not None:
            self.quantity_assignments = quantity_assignments
        if commerce_properties is not None:
            self.commerce_properties = commerce_properties
        if alternative_to is not None:
            self.alternative_to = alternative_to
        self.is_lump_sum = is_lump_sum
        if repetition_to is not None:
            self.repetition_to = repetition_to
        if type is not None:
            self.type = type

    @property
    def unit_price(self):
        """Gets the unit_price of this PositionDto.  # noqa: E501


        :return: The unit_price of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this PositionDto.


        :param unit_price: The unit_price of this PositionDto.  # noqa: E501
        :type: float
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def quantity(self):
        """Gets the quantity of this PositionDto.  # noqa: E501


        :return: The quantity of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PositionDto.


        :param quantity: The quantity of this PositionDto.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def unit_tag(self):
        """Gets the unit_tag of this PositionDto.  # noqa: E501


        :return: The unit_tag of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._unit_tag

    @unit_tag.setter
    def unit_tag(self, unit_tag):
        """Sets the unit_tag of this PositionDto.


        :param unit_tag: The unit_tag of this PositionDto.  # noqa: E501
        :type: str
        """

        self._unit_tag = unit_tag

    @property
    def labour_components(self):
        """Gets the labour_components of this PositionDto.  # noqa: E501


        :return: The labour_components of this PositionDto.  # noqa: E501
        :rtype: LabourPriceComponentDto
        """
        return self._labour_components

    @labour_components.setter
    def labour_components(self, labour_components):
        """Sets the labour_components of this PositionDto.


        :param labour_components: The labour_components of this PositionDto.  # noqa: E501
        :type: LabourPriceComponentDto
        """

        self._labour_components = labour_components

    @property
    def price_components(self):
        """Gets the price_components of this PositionDto.  # noqa: E501


        :return: The price_components of this PositionDto.  # noqa: E501
        :rtype: list[PriceComponentDto]
        """
        return self._price_components

    @price_components.setter
    def price_components(self, price_components):
        """Sets the price_components of this PositionDto.


        :param price_components: The price_components of this PositionDto.  # noqa: E501
        :type: list[PriceComponentDto]
        """

        self._price_components = price_components

    @property
    def quantity_components(self):
        """Gets the quantity_components of this PositionDto.  # noqa: E501


        :return: The quantity_components of this PositionDto.  # noqa: E501
        :rtype: list[CalculationDto]
        """
        return self._quantity_components

    @quantity_components.setter
    def quantity_components(self, quantity_components):
        """Sets the quantity_components of this PositionDto.


        :param quantity_components: The quantity_components of this PositionDto.  # noqa: E501
        :type: list[CalculationDto]
        """

        self._quantity_components = quantity_components

    @property
    def sub_descriptions(self):
        """Gets the sub_descriptions of this PositionDto.  # noqa: E501


        :return: The sub_descriptions of this PositionDto.  # noqa: E501
        :rtype: list[SubDescriptionDto]
        """
        return self._sub_descriptions

    @sub_descriptions.setter
    def sub_descriptions(self, sub_descriptions):
        """Sets the sub_descriptions of this PositionDto.


        :param sub_descriptions: The sub_descriptions of this PositionDto.  # noqa: E501
        :type: list[SubDescriptionDto]
        """

        self._sub_descriptions = sub_descriptions

    @property
    def comission_status(self):
        """Gets the comission_status of this PositionDto.  # noqa: E501


        :return: The comission_status of this PositionDto.  # noqa: E501
        :rtype: ComissionStatusDto
        """
        return self._comission_status

    @comission_status.setter
    def comission_status(self, comission_status):
        """Sets the comission_status of this PositionDto.


        :param comission_status: The comission_status of this PositionDto.  # noqa: E501
        :type: ComissionStatusDto
        """
        if comission_status is None:
            raise ValueError("Invalid value for `comission_status`, must not be `None`")  # noqa: E501

        self._comission_status = comission_status

    @property
    def complemented_by(self):
        """Gets the complemented_by of this PositionDto.  # noqa: E501


        :return: The complemented_by of this PositionDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._complemented_by

    @complemented_by.setter
    def complemented_by(self, complemented_by):
        """Sets the complemented_by of this PositionDto.


        :param complemented_by: The complemented_by of this PositionDto.  # noqa: E501
        :type: list[str]
        """

        self._complemented_by = complemented_by

    @property
    def complemented(self):
        """Gets the complemented of this PositionDto.  # noqa: E501


        :return: The complemented of this PositionDto.  # noqa: E501
        :rtype: bool
        """
        return self._complemented

    @complemented.setter
    def complemented(self, complemented):
        """Sets the complemented of this PositionDto.


        :param complemented: The complemented of this PositionDto.  # noqa: E501
        :type: bool
        """
        if complemented is None:
            raise ValueError("Invalid value for `complemented`, must not be `None`")  # noqa: E501

        self._complemented = complemented

    @property
    def amount_to_be_entered_by_bidder(self):
        """Gets the amount_to_be_entered_by_bidder of this PositionDto.  # noqa: E501


        :return: The amount_to_be_entered_by_bidder of this PositionDto.  # noqa: E501
        :rtype: bool
        """
        return self._amount_to_be_entered_by_bidder

    @amount_to_be_entered_by_bidder.setter
    def amount_to_be_entered_by_bidder(self, amount_to_be_entered_by_bidder):
        """Sets the amount_to_be_entered_by_bidder of this PositionDto.


        :param amount_to_be_entered_by_bidder: The amount_to_be_entered_by_bidder of this PositionDto.  # noqa: E501
        :type: bool
        """
        if amount_to_be_entered_by_bidder is None:
            raise ValueError("Invalid value for `amount_to_be_entered_by_bidder`, must not be `None`")  # noqa: E501

        self._amount_to_be_entered_by_bidder = amount_to_be_entered_by_bidder

    @property
    def price_composition_required(self):
        """Gets the price_composition_required of this PositionDto.  # noqa: E501


        :return: The price_composition_required of this PositionDto.  # noqa: E501
        :rtype: bool
        """
        return self._price_composition_required

    @price_composition_required.setter
    def price_composition_required(self, price_composition_required):
        """Sets the price_composition_required of this PositionDto.


        :param price_composition_required: The price_composition_required of this PositionDto.  # noqa: E501
        :type: bool
        """
        if price_composition_required is None:
            raise ValueError("Invalid value for `price_composition_required`, must not be `None`")  # noqa: E501

        self._price_composition_required = price_composition_required

    @property
    def use_different_tax_rate(self):
        """Gets the use_different_tax_rate of this PositionDto.  # noqa: E501


        :return: The use_different_tax_rate of this PositionDto.  # noqa: E501
        :rtype: bool
        """
        return self._use_different_tax_rate

    @use_different_tax_rate.setter
    def use_different_tax_rate(self, use_different_tax_rate):
        """Sets the use_different_tax_rate of this PositionDto.


        :param use_different_tax_rate: The use_different_tax_rate of this PositionDto.  # noqa: E501
        :type: bool
        """
        if use_different_tax_rate is None:
            raise ValueError("Invalid value for `use_different_tax_rate`, must not be `None`")  # noqa: E501

        self._use_different_tax_rate = use_different_tax_rate

    @property
    def tax_rate(self):
        """Gets the tax_rate of this PositionDto.  # noqa: E501


        :return: The tax_rate of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this PositionDto.


        :param tax_rate: The tax_rate of this PositionDto.  # noqa: E501
        :type: float
        """
        if tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")  # noqa: E501

        self._tax_rate = tax_rate

    @property
    def item_number(self):
        """Gets the item_number of this PositionDto.  # noqa: E501


        :return: The item_number of this PositionDto.  # noqa: E501
        :rtype: ItemNumberDto
        """
        return self._item_number

    @item_number.setter
    def item_number(self, item_number):
        """Sets the item_number of this PositionDto.


        :param item_number: The item_number of this PositionDto.  # noqa: E501
        :type: ItemNumberDto
        """

        self._item_number = item_number

    @property
    def deduction_factor(self):
        """Gets the deduction_factor of this PositionDto.  # noqa: E501


        :return: The deduction_factor of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._deduction_factor

    @deduction_factor.setter
    def deduction_factor(self, deduction_factor):
        """Sets the deduction_factor of this PositionDto.


        :param deduction_factor: The deduction_factor of this PositionDto.  # noqa: E501
        :type: float
        """
        if deduction_factor is None:
            raise ValueError("Invalid value for `deduction_factor`, must not be `None`")  # noqa: E501

        self._deduction_factor = deduction_factor

    @property
    def total_price(self):
        """Gets the total_price of this PositionDto.  # noqa: E501


        :return: The total_price of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this PositionDto.


        :param total_price: The total_price of this PositionDto.  # noqa: E501
        :type: float
        """
        if total_price is None:
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501

        self._total_price = total_price

    @property
    def total_price_gross(self):
        """Gets the total_price_gross of this PositionDto.  # noqa: E501


        :return: The total_price_gross of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._total_price_gross

    @total_price_gross.setter
    def total_price_gross(self, total_price_gross):
        """Sets the total_price_gross of this PositionDto.


        :param total_price_gross: The total_price_gross of this PositionDto.  # noqa: E501
        :type: float
        """
        if total_price_gross is None:
            raise ValueError("Invalid value for `total_price_gross`, must not be `None`")  # noqa: E501

        self._total_price_gross = total_price_gross

    @property
    def total_price_gross_deducted(self):
        """Gets the total_price_gross_deducted of this PositionDto.  # noqa: E501


        :return: The total_price_gross_deducted of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._total_price_gross_deducted

    @total_price_gross_deducted.setter
    def total_price_gross_deducted(self, total_price_gross_deducted):
        """Sets the total_price_gross_deducted of this PositionDto.


        :param total_price_gross_deducted: The total_price_gross_deducted of this PositionDto.  # noqa: E501
        :type: float
        """
        if total_price_gross_deducted is None:
            raise ValueError("Invalid value for `total_price_gross_deducted`, must not be `None`")  # noqa: E501

        self._total_price_gross_deducted = total_price_gross_deducted

    @property
    def deducted_price(self):
        """Gets the deducted_price of this PositionDto.  # noqa: E501


        :return: The deducted_price of this PositionDto.  # noqa: E501
        :rtype: float
        """
        return self._deducted_price

    @deducted_price.setter
    def deducted_price(self, deducted_price):
        """Sets the deducted_price of this PositionDto.


        :param deducted_price: The deducted_price of this PositionDto.  # noqa: E501
        :type: float
        """
        if deducted_price is None:
            raise ValueError("Invalid value for `deducted_price`, must not be `None`")  # noqa: E501

        self._deducted_price = deducted_price

    @property
    def position_type(self):
        """Gets the position_type of this PositionDto.  # noqa: E501


        :return: The position_type of this PositionDto.  # noqa: E501
        :rtype: PositionTypeDto
        """
        return self._position_type

    @position_type.setter
    def position_type(self, position_type):
        """Sets the position_type of this PositionDto.


        :param position_type: The position_type of this PositionDto.  # noqa: E501
        :type: PositionTypeDto
        """
        if position_type is None:
            raise ValueError("Invalid value for `position_type`, must not be `None`")  # noqa: E501

        self._position_type = position_type

    @property
    def price_type(self):
        """Gets the price_type of this PositionDto.  # noqa: E501


        :return: The price_type of this PositionDto.  # noqa: E501
        :rtype: PriceTypeDto
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this PositionDto.


        :param price_type: The price_type of this PositionDto.  # noqa: E501
        :type: PriceTypeDto
        """
        if price_type is None:
            raise ValueError("Invalid value for `price_type`, must not be `None`")  # noqa: E501

        self._price_type = price_type

    @property
    def service_type(self):
        """Gets the service_type of this PositionDto.  # noqa: E501


        :return: The service_type of this PositionDto.  # noqa: E501
        :rtype: ServiceTypeDto
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this PositionDto.


        :param service_type: The service_type of this PositionDto.  # noqa: E501
        :type: ServiceTypeDto
        """
        if service_type is None:
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501

        self._service_type = service_type

    @property
    def short_text(self):
        """Gets the short_text of this PositionDto.  # noqa: E501


        :return: The short_text of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._short_text

    @short_text.setter
    def short_text(self, short_text):
        """Sets the short_text of this PositionDto.


        :param short_text: The short_text of this PositionDto.  # noqa: E501
        :type: str
        """

        self._short_text = short_text

    @property
    def long_text(self):
        """Gets the long_text of this PositionDto.  # noqa: E501


        :return: The long_text of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._long_text

    @long_text.setter
    def long_text(self, long_text):
        """Sets the long_text of this PositionDto.


        :param long_text: The long_text of this PositionDto.  # noqa: E501
        :type: str
        """

        self._long_text = long_text

    @property
    def html_long_text(self):
        """Gets the html_long_text of this PositionDto.  # noqa: E501


        :return: The html_long_text of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._html_long_text

    @html_long_text.setter
    def html_long_text(self, html_long_text):
        """Sets the html_long_text of this PositionDto.


        :param html_long_text: The html_long_text of this PositionDto.  # noqa: E501
        :type: str
        """

        self._html_long_text = html_long_text

    @property
    def addition_type(self):
        """Gets the addition_type of this PositionDto.  # noqa: E501


        :return: The addition_type of this PositionDto.  # noqa: E501
        :rtype: AdditionTypeDto
        """
        return self._addition_type

    @addition_type.setter
    def addition_type(self, addition_type):
        """Sets the addition_type of this PositionDto.


        :param addition_type: The addition_type of this PositionDto.  # noqa: E501
        :type: AdditionTypeDto
        """
        if addition_type is None:
            raise ValueError("Invalid value for `addition_type`, must not be `None`")  # noqa: E501

        self._addition_type = addition_type

    @property
    def element_type(self):
        """Gets the element_type of this PositionDto.  # noqa: E501


        :return: The element_type of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this PositionDto.


        :param element_type: The element_type of this PositionDto.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

    @property
    def quantity_assignments(self):
        """Gets the quantity_assignments of this PositionDto.  # noqa: E501


        :return: The quantity_assignments of this PositionDto.  # noqa: E501
        :rtype: list[QuantityAssignmentDto]
        """
        return self._quantity_assignments

    @quantity_assignments.setter
    def quantity_assignments(self, quantity_assignments):
        """Sets the quantity_assignments of this PositionDto.


        :param quantity_assignments: The quantity_assignments of this PositionDto.  # noqa: E501
        :type: list[QuantityAssignmentDto]
        """

        self._quantity_assignments = quantity_assignments

    @property
    def commerce_properties(self):
        """Gets the commerce_properties of this PositionDto.  # noqa: E501


        :return: The commerce_properties of this PositionDto.  # noqa: E501
        :rtype: CommercePropertiesDto
        """
        return self._commerce_properties

    @commerce_properties.setter
    def commerce_properties(self, commerce_properties):
        """Sets the commerce_properties of this PositionDto.


        :param commerce_properties: The commerce_properties of this PositionDto.  # noqa: E501
        :type: CommercePropertiesDto
        """

        self._commerce_properties = commerce_properties

    @property
    def alternative_to(self):
        """Gets the alternative_to of this PositionDto.  # noqa: E501


        :return: The alternative_to of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._alternative_to

    @alternative_to.setter
    def alternative_to(self, alternative_to):
        """Sets the alternative_to of this PositionDto.


        :param alternative_to: The alternative_to of this PositionDto.  # noqa: E501
        :type: str
        """

        self._alternative_to = alternative_to

    @property
    def is_lump_sum(self):
        """Gets the is_lump_sum of this PositionDto.  # noqa: E501


        :return: The is_lump_sum of this PositionDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_lump_sum

    @is_lump_sum.setter
    def is_lump_sum(self, is_lump_sum):
        """Sets the is_lump_sum of this PositionDto.


        :param is_lump_sum: The is_lump_sum of this PositionDto.  # noqa: E501
        :type: bool
        """
        if is_lump_sum is None:
            raise ValueError("Invalid value for `is_lump_sum`, must not be `None`")  # noqa: E501

        self._is_lump_sum = is_lump_sum

    @property
    def repetition_to(self):
        """Gets the repetition_to of this PositionDto.  # noqa: E501


        :return: The repetition_to of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._repetition_to

    @repetition_to.setter
    def repetition_to(self, repetition_to):
        """Sets the repetition_to of this PositionDto.


        :param repetition_to: The repetition_to of this PositionDto.  # noqa: E501
        :type: str
        """

        self._repetition_to = repetition_to

    @property
    def type(self):
        """Gets the type of this PositionDto.  # noqa: E501


        :return: The type of this PositionDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PositionDto.


        :param type: The type of this PositionDto.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(PositionDto, dict):
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
        if not isinstance(other, PositionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
