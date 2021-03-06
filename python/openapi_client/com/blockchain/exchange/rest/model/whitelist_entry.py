# coding: utf-8

"""
    Blockchain.com Exchange REST API

    ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client).   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class WhitelistEntry(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'whitelist_id': 'str',
        'name': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'whitelist_id': 'whitelistId',
        'name': 'name',
        'currency': 'currency'
    }

    def __init__(self, whitelist_id=None, name=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """WhitelistEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._whitelist_id = None
        self._name = None
        self._currency = None
        self.discriminator = None

        if whitelist_id is not None:
            self.whitelist_id = whitelist_id
        if name is not None:
            self.name = name
        if currency is not None:
            self.currency = currency

    @property
    def whitelist_id(self):
        """Gets the whitelist_id of this WhitelistEntry.  # noqa: E501

        Unique ID for each whitelist entry  # noqa: E501

        :return: The whitelist_id of this WhitelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._whitelist_id

    @whitelist_id.setter
    def whitelist_id(self, whitelist_id):
        """Sets the whitelist_id of this WhitelistEntry.

        Unique ID for each whitelist entry  # noqa: E501

        :param whitelist_id: The whitelist_id of this WhitelistEntry.  # noqa: E501
        :type: str
        """

        self._whitelist_id = whitelist_id

    @property
    def name(self):
        """Gets the name of this WhitelistEntry.  # noqa: E501

        User specified name for this entry  # noqa: E501

        :return: The name of this WhitelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WhitelistEntry.

        User specified name for this entry  # noqa: E501

        :param name: The name of this WhitelistEntry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def currency(self):
        """Gets the currency of this WhitelistEntry.  # noqa: E501


        :return: The currency of this WhitelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this WhitelistEntry.


        :param currency: The currency of this WhitelistEntry.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and not re.search(r'^[A-Z]{3,5}$', currency)):  # noqa: E501
            raise ValueError(r"Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Z]{3,5}$/`")  # noqa: E501

        self._currency = currency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhitelistEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhitelistEntry):
            return True

        return self.to_dict() != other.to_dict()
