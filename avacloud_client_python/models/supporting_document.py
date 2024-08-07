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


class SupportingDocument(object):
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
        'document_reference': 'str',
        'description': 'str',
        'external_document_url': 'str',
        'document_base64': 'str',
        'file_name': 'str',
        'document_mime_type': 'AttachmentMimeType'
    }

    attribute_map = {
        'document_reference': 'documentReference',
        'description': 'description',
        'external_document_url': 'externalDocumentUrl',
        'document_base64': 'documentBase64',
        'file_name': 'fileName',
        'document_mime_type': 'documentMimeType'
    }

    def __init__(self, document_reference=None, description=None, external_document_url=None, document_base64=None, file_name=None, document_mime_type=None, _configuration=None):  # noqa: E501
        """SupportingDocument - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._document_reference = None
        self._description = None
        self._external_document_url = None
        self._document_base64 = None
        self._file_name = None
        self._document_mime_type = None
        self.discriminator = None

        if document_reference is not None:
            self.document_reference = document_reference
        if description is not None:
            self.description = description
        if external_document_url is not None:
            self.external_document_url = external_document_url
        if document_base64 is not None:
            self.document_base64 = document_base64
        if file_name is not None:
            self.file_name = file_name
        self.document_mime_type = document_mime_type

    @property
    def document_reference(self):
        """Gets the document_reference of this SupportingDocument.  # noqa: E501


        :return: The document_reference of this SupportingDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_reference

    @document_reference.setter
    def document_reference(self, document_reference):
        """Sets the document_reference of this SupportingDocument.


        :param document_reference: The document_reference of this SupportingDocument.  # noqa: E501
        :type: str
        """

        self._document_reference = document_reference

    @property
    def description(self):
        """Gets the description of this SupportingDocument.  # noqa: E501


        :return: The description of this SupportingDocument.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupportingDocument.


        :param description: The description of this SupportingDocument.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_document_url(self):
        """Gets the external_document_url of this SupportingDocument.  # noqa: E501


        :return: The external_document_url of this SupportingDocument.  # noqa: E501
        :rtype: str
        """
        return self._external_document_url

    @external_document_url.setter
    def external_document_url(self, external_document_url):
        """Sets the external_document_url of this SupportingDocument.


        :param external_document_url: The external_document_url of this SupportingDocument.  # noqa: E501
        :type: str
        """

        self._external_document_url = external_document_url

    @property
    def document_base64(self):
        """Gets the document_base64 of this SupportingDocument.  # noqa: E501


        :return: The document_base64 of this SupportingDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_base64

    @document_base64.setter
    def document_base64(self, document_base64):
        """Sets the document_base64 of this SupportingDocument.


        :param document_base64: The document_base64 of this SupportingDocument.  # noqa: E501
        :type: str
        """

        self._document_base64 = document_base64

    @property
    def file_name(self):
        """Gets the file_name of this SupportingDocument.  # noqa: E501


        :return: The file_name of this SupportingDocument.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SupportingDocument.


        :param file_name: The file_name of this SupportingDocument.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def document_mime_type(self):
        """Gets the document_mime_type of this SupportingDocument.  # noqa: E501


        :return: The document_mime_type of this SupportingDocument.  # noqa: E501
        :rtype: AttachmentMimeType
        """
        return self._document_mime_type

    @document_mime_type.setter
    def document_mime_type(self, document_mime_type):
        """Sets the document_mime_type of this SupportingDocument.


        :param document_mime_type: The document_mime_type of this SupportingDocument.  # noqa: E501
        :type: AttachmentMimeType
        """
        if self._configuration.client_side_validation and document_mime_type is None:
            raise ValueError("Invalid value for `document_mime_type`, must not be `None`")  # noqa: E501

        self._document_mime_type = document_mime_type

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
        if issubclass(SupportingDocument, dict):
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
        if not isinstance(other, SupportingDocument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportingDocument):
            return True

        return self.to_dict() != other.to_dict()
