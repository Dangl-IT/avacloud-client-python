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


class ServiceSpecificationCommercePropertiesDto(object):
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
        'fixed_price_date': 'datetime',
        'delivery_voucher_date': 'datetime',
        'delivery_date': 'datetime',
        'inquiry_number': 'str',
        'offer_number': 'str',
        'order_number': 'str',
        'order_confirmation_number': 'str',
        'delivery_number': 'str',
        'customer_reference_number': 'str',
        'supplier_reference_number': 'str',
        'shipping_type': 'str',
        'inquiry_type': 'CommerceInquiryTypeDto'
    }

    attribute_map = {
        'fixed_price_date': 'fixedPriceDate',
        'delivery_voucher_date': 'deliveryVoucherDate',
        'delivery_date': 'deliveryDate',
        'inquiry_number': 'inquiryNumber',
        'offer_number': 'offerNumber',
        'order_number': 'orderNumber',
        'order_confirmation_number': 'orderConfirmationNumber',
        'delivery_number': 'deliveryNumber',
        'customer_reference_number': 'customerReferenceNumber',
        'supplier_reference_number': 'supplierReferenceNumber',
        'shipping_type': 'shippingType',
        'inquiry_type': 'inquiryType'
    }

    def __init__(self, fixed_price_date=None, delivery_voucher_date=None, delivery_date=None, inquiry_number=None, offer_number=None, order_number=None, order_confirmation_number=None, delivery_number=None, customer_reference_number=None, supplier_reference_number=None, shipping_type=None, inquiry_type=None, _configuration=None):  # noqa: E501
        """ServiceSpecificationCommercePropertiesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fixed_price_date = None
        self._delivery_voucher_date = None
        self._delivery_date = None
        self._inquiry_number = None
        self._offer_number = None
        self._order_number = None
        self._order_confirmation_number = None
        self._delivery_number = None
        self._customer_reference_number = None
        self._supplier_reference_number = None
        self._shipping_type = None
        self._inquiry_type = None
        self.discriminator = None

        if fixed_price_date is not None:
            self.fixed_price_date = fixed_price_date
        if delivery_voucher_date is not None:
            self.delivery_voucher_date = delivery_voucher_date
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if inquiry_number is not None:
            self.inquiry_number = inquiry_number
        if offer_number is not None:
            self.offer_number = offer_number
        if order_number is not None:
            self.order_number = order_number
        if order_confirmation_number is not None:
            self.order_confirmation_number = order_confirmation_number
        if delivery_number is not None:
            self.delivery_number = delivery_number
        if customer_reference_number is not None:
            self.customer_reference_number = customer_reference_number
        if supplier_reference_number is not None:
            self.supplier_reference_number = supplier_reference_number
        if shipping_type is not None:
            self.shipping_type = shipping_type
        self.inquiry_type = inquiry_type

    @property
    def fixed_price_date(self):
        """Gets the fixed_price_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The date until the price is valid or fixed.  # noqa: E501

        :return: The fixed_price_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: datetime
        """
        return self._fixed_price_date

    @fixed_price_date.setter
    def fixed_price_date(self, fixed_price_date):
        """Sets the fixed_price_date of this ServiceSpecificationCommercePropertiesDto.

        The date until the price is valid or fixed.  # noqa: E501

        :param fixed_price_date: The fixed_price_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: datetime
        """

        self._fixed_price_date = fixed_price_date

    @property
    def delivery_voucher_date(self):
        """Gets the delivery_voucher_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The date of the delivery voucher note.  # noqa: E501

        :return: The delivery_voucher_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: datetime
        """
        return self._delivery_voucher_date

    @delivery_voucher_date.setter
    def delivery_voucher_date(self, delivery_voucher_date):
        """Sets the delivery_voucher_date of this ServiceSpecificationCommercePropertiesDto.

        The date of the delivery voucher note.  # noqa: E501

        :param delivery_voucher_date: The delivery_voucher_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: datetime
        """

        self._delivery_voucher_date = delivery_voucher_date

    @property
    def delivery_date(self):
        """Gets the delivery_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The actual date of delivery.  # noqa: E501

        :return: The delivery_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: datetime
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this ServiceSpecificationCommercePropertiesDto.

        The actual date of delivery.  # noqa: E501

        :param delivery_date: The delivery_date of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: datetime
        """

        self._delivery_date = delivery_date

    @property
    def inquiry_number(self):
        """Gets the inquiry_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The number of the inquiry, usually in a context of offer requests.  # noqa: E501

        :return: The inquiry_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_number

    @inquiry_number.setter
    def inquiry_number(self, inquiry_number):
        """Sets the inquiry_number of this ServiceSpecificationCommercePropertiesDto.

        The number of the inquiry, usually in a context of offer requests.  # noqa: E501

        :param inquiry_number: The inquiry_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._inquiry_number = inquiry_number

    @property
    def offer_number(self):
        """Gets the offer_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The number of the offer, usually in a context of an offer.  # noqa: E501

        :return: The offer_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._offer_number

    @offer_number.setter
    def offer_number(self, offer_number):
        """Sets the offer_number of this ServiceSpecificationCommercePropertiesDto.

        The number of the offer, usually in a context of an offer.  # noqa: E501

        :param offer_number: The offer_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._offer_number = offer_number

    @property
    def order_number(self):
        """Gets the order_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The order number, usually in the context of a grant or contract.  # noqa: E501

        :return: The order_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this ServiceSpecificationCommercePropertiesDto.

        The order number, usually in the context of a grant or contract.  # noqa: E501

        :param order_number: The order_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def order_confirmation_number(self):
        """Gets the order_confirmation_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The order confirmation number  # noqa: E501

        :return: The order_confirmation_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._order_confirmation_number

    @order_confirmation_number.setter
    def order_confirmation_number(self, order_confirmation_number):
        """Sets the order_confirmation_number of this ServiceSpecificationCommercePropertiesDto.

        The order confirmation number  # noqa: E501

        :param order_confirmation_number: The order_confirmation_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._order_confirmation_number = order_confirmation_number

    @property
    def delivery_number(self):
        """Gets the delivery_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The number of the delivery, e.g. on the delivery note voucher.  # noqa: E501

        :return: The delivery_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._delivery_number

    @delivery_number.setter
    def delivery_number(self, delivery_number):
        """Sets the delivery_number of this ServiceSpecificationCommercePropertiesDto.

        The number of the delivery, e.g. on the delivery note voucher.  # noqa: E501

        :param delivery_number: The delivery_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._delivery_number = delivery_number

    @property
    def customer_reference_number(self):
        """Gets the customer_reference_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The reference number of the customer / buyer.  # noqa: E501

        :return: The customer_reference_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference_number

    @customer_reference_number.setter
    def customer_reference_number(self, customer_reference_number):
        """Sets the customer_reference_number of this ServiceSpecificationCommercePropertiesDto.

        The reference number of the customer / buyer.  # noqa: E501

        :param customer_reference_number: The customer_reference_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._customer_reference_number = customer_reference_number

    @property
    def supplier_reference_number(self):
        """Gets the supplier_reference_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The reference number of the supplier / bidder.  # noqa: E501

        :return: The supplier_reference_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_reference_number

    @supplier_reference_number.setter
    def supplier_reference_number(self, supplier_reference_number):
        """Sets the supplier_reference_number of this ServiceSpecificationCommercePropertiesDto.

        The reference number of the supplier / bidder.  # noqa: E501

        :param supplier_reference_number: The supplier_reference_number of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._supplier_reference_number = supplier_reference_number

    @property
    def shipping_type(self):
        """Gets the shipping_type of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The type of shippment.  # noqa: E501

        :return: The shipping_type of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: str
        """
        return self._shipping_type

    @shipping_type.setter
    def shipping_type(self, shipping_type):
        """Sets the shipping_type of this ServiceSpecificationCommercePropertiesDto.

        The type of shippment.  # noqa: E501

        :param shipping_type: The shipping_type of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: str
        """

        self._shipping_type = shipping_type

    @property
    def inquiry_type(self):
        """Gets the inquiry_type of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501

        The type of the price inquiry.  # noqa: E501

        :return: The inquiry_type of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :rtype: CommerceInquiryTypeDto
        """
        return self._inquiry_type

    @inquiry_type.setter
    def inquiry_type(self, inquiry_type):
        """Sets the inquiry_type of this ServiceSpecificationCommercePropertiesDto.

        The type of the price inquiry.  # noqa: E501

        :param inquiry_type: The inquiry_type of this ServiceSpecificationCommercePropertiesDto.  # noqa: E501
        :type: CommerceInquiryTypeDto
        """
        if self._configuration.client_side_validation and inquiry_type is None:
            raise ValueError("Invalid value for `inquiry_type`, must not be `None`")  # noqa: E501

        self._inquiry_type = inquiry_type

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
        if issubclass(ServiceSpecificationCommercePropertiesDto, dict):
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
        if not isinstance(other, ServiceSpecificationCommercePropertiesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceSpecificationCommercePropertiesDto):
            return True

        return self.to_dict() != other.to_dict()
