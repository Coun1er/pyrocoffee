#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import raw
from ..object import Object


class Invoice(Object):
    """Contains information about an Invoice.

    Parameters:
        title (``str``):
            Product name.

        description (``str``):
            Product description.

        currency (``str``):
            Currency code.

        total_amount (``int``):
            Total price in the smallest units of the currency.

        start_parameter (``str``):
            Unique bot deep-linking parameter that can be used to generate this invoice.

        shipping_address_requested (``bool``, *optional*):
            True, if the the shipping address is requested.

        test (``bool``, *optional*):
            True, if the invoice is a test invoice.

        receipt_message_id (``int``, *optional*):
            The message_id of the message sent to the chat when the invoice is paid.
    """

    def __init__(
        self,
        *,
        currency: str,
        prices: list,
        test: bool = None,
        name_requested: bool = None,
        phone_requested: bool = None,
        email_requested: bool = None,
        shipping_address_requested: bool = None,
        flexible: bool = None,
        phone_to_provider: bool = None,
        email_to_provider: bool = None,
        recurring: bool = None,
        suggested_tip_amounts: list = None
        # TODO: Implement photo, extended_media parameters
    ):
        super().__init__()

        self.currency = currency
        self.prices = prices
        self.test = test
        self.name_requested = name_requested
        self.phone_requested = phone_requested
        self.email_requested = email_requested
        self.shipping_address_requested = shipping_address_requested
        self.flexible = flexible
        self.phone_to_provider = phone_to_provider
        self.email_to_provider = email_to_provider
        self.recurring = recurring
        self.suggested_tip_amounts = suggested_tip_amounts

    @staticmethod
    def _parse(
        message_invoice: "raw.types.MessageMediaInvoice"
    ) -> "Invoice":
        return Invoice(
            currency=message_invoice.currency,
            prices=message_invoice.prices,
            test=message_invoice.test,
            name_requested=message_invoice.name_requested,
            phone_requested=message_invoice.phone_requested,
            email_requested=message_invoice.email_requested,
            shipping_address_requested=message_invoice.shipping_address_requested,
            flexible=message_invoice.flexible,
            phone_to_provider=message_invoice.phone_to_provider,
            email_to_provider=message_invoice.email_to_provider,
            recurring=message_invoice.recurring,
            suggested_tip_amounts=message_invoice.suggested_tip_amounts
        )
