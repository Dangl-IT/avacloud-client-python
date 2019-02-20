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


class HttpStatusCode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CONTINUE = "Continue"
    SWITCHINGPROTOCOLS = "SwitchingProtocols"
    PROCESSING = "Processing"
    EARLYHINTS = "EarlyHints"
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NONAUTHORITATIVEINFORMATION = "NonAuthoritativeInformation"
    NOCONTENT = "NoContent"
    RESETCONTENT = "ResetContent"
    PARTIALCONTENT = "PartialContent"
    MULTISTATUS = "MultiStatus"
    ALREADYREPORTED = "AlreadyReported"
    IMUSED = "IMUsed"
    AMBIGUOUS = "Ambiguous"
    MOVED = "Moved"
    REDIRECT = "Redirect"
    REDIRECTMETHOD = "RedirectMethod"
    NOTMODIFIED = "NotModified"
    USEPROXY = "UseProxy"
    UNUSED = "Unused"
    TEMPORARYREDIRECT = "TemporaryRedirect"
    PERMANENTREDIRECT = "PermanentRedirect"
    BADREQUEST = "BadRequest"
    UNAUTHORIZED = "Unauthorized"
    PAYMENTREQUIRED = "PaymentRequired"
    FORBIDDEN = "Forbidden"
    NOTFOUND = "NotFound"
    METHODNOTALLOWED = "MethodNotAllowed"
    NOTACCEPTABLE = "NotAcceptable"
    PROXYAUTHENTICATIONREQUIRED = "ProxyAuthenticationRequired"
    REQUESTTIMEOUT = "RequestTimeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTHREQUIRED = "LengthRequired"
    PRECONDITIONFAILED = "PreconditionFailed"
    REQUESTENTITYTOOLARGE = "RequestEntityTooLarge"
    REQUESTURITOOLONG = "RequestUriTooLong"
    UNSUPPORTEDMEDIATYPE = "UnsupportedMediaType"
    REQUESTEDRANGENOTSATISFIABLE = "RequestedRangeNotSatisfiable"
    EXPECTATIONFAILED = "ExpectationFailed"
    MISDIRECTEDREQUEST = "MisdirectedRequest"
    UNPROCESSABLEENTITY = "UnprocessableEntity"
    LOCKED = "Locked"
    FAILEDDEPENDENCY = "FailedDependency"
    UPGRADEREQUIRED = "UpgradeRequired"
    PRECONDITIONREQUIRED = "PreconditionRequired"
    TOOMANYREQUESTS = "TooManyRequests"
    REQUESTHEADERFIELDSTOOLARGE = "RequestHeaderFieldsTooLarge"
    UNAVAILABLEFORLEGALREASONS = "UnavailableForLegalReasons"
    INTERNALSERVERERROR = "InternalServerError"
    NOTIMPLEMENTED = "NotImplemented"
    BADGATEWAY = "BadGateway"
    SERVICEUNAVAILABLE = "ServiceUnavailable"
    GATEWAYTIMEOUT = "GatewayTimeout"
    HTTPVERSIONNOTSUPPORTED = "HttpVersionNotSupported"
    VARIANTALSONEGOTIATES = "VariantAlsoNegotiates"
    INSUFFICIENTSTORAGE = "InsufficientStorage"
    LOOPDETECTED = "LoopDetected"
    NOTEXTENDED = "NotExtended"
    NETWORKAUTHENTICATIONREQUIRED = "NetworkAuthenticationRequired"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """HttpStatusCode - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(HttpStatusCode, dict):
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
        if not isinstance(other, HttpStatusCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other