# coding: utf-8

"""
    AVACloud API 1.12.0

    AVACloud API specification  # noqa: E501

    OpenAPI spec version: 1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PartyInformationDto(object):
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
        'street': 'str',
        'zip_code': 'str',
        'city': 'str',
        'country': 'str',
        'identifier': 'str',
        'remarks': 'str',
        'email': 'str',
        'phone': 'str',
        'contact_person_name': 'str',
        'award_identifier': 'str'
    }

    attribute_map = {
        'name': 'name',
        'street': 'street',
        'zip_code': 'zipCode',
        'city': 'city',
        'country': 'country',
        'identifier': 'identifier',
        'remarks': 'remarks',
        'email': 'email',
        'phone': 'phone',
        'contact_person_name': 'contactPersonName',
        'award_identifier': 'awardIdentifier'
    }

    def __init__(self, name=None, street=None, zip_code=None, city=None, country=None, identifier=None, remarks=None, email=None, phone=None, contact_person_name=None, award_identifier=None):  # noqa: E501
        """PartyInformationDto - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._street = None
        self._zip_code = None
        self._city = None
        self._country = None
        self._identifier = None
        self._remarks = None
        self._email = None
        self._phone = None
        self._contact_person_name = None
        self._award_identifier = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if street is not None:
            self.street = street
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if identifier is not None:
            self.identifier = identifier
        if remarks is not None:
            self.remarks = remarks
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if contact_person_name is not None:
            self.contact_person_name = contact_person_name
        if award_identifier is not None:
            self.award_identifier = award_identifier

    @property
    def name(self):
        """Gets the name of this PartyInformationDto.  # noqa: E501

        This party's name.  # noqa: E501

        :return: The name of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartyInformationDto.

        This party's name.  # noqa: E501

        :param name: The name of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def street(self):
        """Gets the street of this PartyInformationDto.  # noqa: E501

        This party's street.  # noqa: E501

        :return: The street of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this PartyInformationDto.

        This party's street.  # noqa: E501

        :param street: The street of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def zip_code(self):
        """Gets the zip_code of this PartyInformationDto.  # noqa: E501

        This party's ZipCode.  # noqa: E501

        :return: The zip_code of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this PartyInformationDto.

        This party's ZipCode.  # noqa: E501

        :param zip_code: The zip_code of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this PartyInformationDto.  # noqa: E501

        This party's City.  # noqa: E501

        :return: The city of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PartyInformationDto.

        This party's City.  # noqa: E501

        :param city: The city of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this PartyInformationDto.  # noqa: E501

        This party's Country.  # noqa: E501

        :return: The country of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PartyInformationDto.

        This party's Country.  # noqa: E501

        :param country: The country of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def identifier(self):
        """Gets the identifier of this PartyInformationDto.  # noqa: E501

        This party's Identifier.  # noqa: E501

        :return: The identifier of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PartyInformationDto.

        This party's Identifier.  # noqa: E501

        :param identifier: The identifier of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def remarks(self):
        """Gets the remarks of this PartyInformationDto.  # noqa: E501

        Remarks for this party.  # noqa: E501

        :return: The remarks of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this PartyInformationDto.

        Remarks for this party.  # noqa: E501

        :param remarks: The remarks of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._remarks = remarks

    @property
    def email(self):
        """Gets the email of this PartyInformationDto.  # noqa: E501

        An email address for this party.  # noqa: E501

        :return: The email of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PartyInformationDto.

        An email address for this party.  # noqa: E501

        :param email: The email of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this PartyInformationDto.  # noqa: E501

        A phone number for this party.  # noqa: E501

        :return: The phone of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PartyInformationDto.

        A phone number for this party.  # noqa: E501

        :param phone: The phone of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def contact_person_name(self):
        """Gets the contact_person_name of this PartyInformationDto.  # noqa: E501

        The name of a contact person.  # noqa: E501

        :return: The contact_person_name of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._contact_person_name

    @contact_person_name.setter
    def contact_person_name(self, contact_person_name):
        """Sets the contact_person_name of this PartyInformationDto.

        The name of a contact person.  # noqa: E501

        :param contact_person_name: The contact_person_name of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._contact_person_name = contact_person_name

    @property
    def award_identifier(self):
        """Gets the award_identifier of this PartyInformationDto.  # noqa: E501

        This is an identifier related to this PartyInformation and their internal reference of the tender (or award). This might be used to assign an identifier (German \"Vergabenummer\") for the current project. This is typically only used in Buyer and Bidder representations and should map to the concept of \"Vergabenummer\" or \"AwardNo\" in GAEB.  # noqa: E501

        :return: The award_identifier of this PartyInformationDto.  # noqa: E501
        :rtype: str
        """
        return self._award_identifier

    @award_identifier.setter
    def award_identifier(self, award_identifier):
        """Sets the award_identifier of this PartyInformationDto.

        This is an identifier related to this PartyInformation and their internal reference of the tender (or award). This might be used to assign an identifier (German \"Vergabenummer\") for the current project. This is typically only used in Buyer and Bidder representations and should map to the concept of \"Vergabenummer\" or \"AwardNo\" in GAEB.  # noqa: E501

        :param award_identifier: The award_identifier of this PartyInformationDto.  # noqa: E501
        :type: str
        """

        self._award_identifier = award_identifier

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
        if issubclass(PartyInformationDto, dict):
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
        if not isinstance(other, PartyInformationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
