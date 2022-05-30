"""A python module for very basic APIs of the free dweet service with encryption.

- Author: Quan Lin
- License: MIT
"""

__version__ = "0.1.0"
__all__ = ["CryptoDweet"]

from binascii import hexlify, unhexlify
import basicdweet
from cryptomsg import CryptoMsg


def to_bytes(msg):
    return msg if isinstance(msg, bytes) else msg.encode("utf-8")


def from_bytes(msg):
    return msg.decode("utf-8") if isinstance(msg, bytes) else msg


class CryptoDweet:
    def __init__(self, aes_cbc_key=b"aes_cbc_key", aes_cbc_iv=None):
        self.aes_cbc_key = aes_cbc_key
        if aes_cbc_iv is None:
            self.aes_cbc_iv = self.aes_cbc_key
        else:
            self.aes_cbc_iv = aes_cbc_iv

    def dweet_for(self, thing, content_dict):
        cm = CryptoMsg(to_bytes(self.aes_cbc_key), to_bytes(self.aes_cbc_iv))
        thing_cipher = cm.encrypt_msg(to_bytes(thing))
        thing_cipher_hexlified = from_bytes(hexlify(thing_cipher))

        content_dict_cipher = {
            cm.encrypt_msg(to_bytes(k)): cm.encrypt_msg(to_bytes(v))
            for (k, v) in content_dict.items()
        }
        content_dict_cipher_hexlified = {
            from_bytes(hexlify(k)): from_bytes(hexlify(v))
            for (k, v) in content_dict_cipher.items()
        }

        return basicdweet.dweet_for(
            thing_cipher_hexlified, content_dict_cipher_hexlified
        )

    def get_latest_dweet_for(self, thing):
        cm = CryptoMsg(to_bytes(self.aes_cbc_key), to_bytes(self.aes_cbc_iv))
        thing_cipher = cm.encrypt_msg(to_bytes(thing))
        thing_cipher_hexlified = from_bytes(hexlify(thing_cipher))

        dweets_list_cipher_hexlified = basicdweet.get_latest_dweet_for(
            thing_cipher_hexlified
        )

        dweets_list = []
        for cipher_dweet in dweets_list_cipher_hexlified:
            content_dict_cipher_hexlified = cipher_dweet["content"]
            content_dict_cipher = {
                unhexlify(to_bytes(k)): unhexlify(to_bytes(v))
                for (k, v) in content_dict_cipher_hexlified.items()
            }
            content_dict = {
                from_bytes(cm.decrypt_msg(k)): from_bytes(cm.decrypt_msg(v))
                for (k, v) in content_dict_cipher.items()
            }
            decrypted_dweet = cipher_dweet
            decrypted_dweet["thing"] = from_bytes(thing)
            decrypted_dweet["content"] = content_dict
            dweets_list.append(decrypted_dweet)

        return dweets_list

    def get_dweets_for(self, thing):
        cm = CryptoMsg(to_bytes(self.aes_cbc_key), to_bytes(self.aes_cbc_iv))
        thing_cipher = cm.encrypt_msg(to_bytes(thing))
        thing_cipher_hexlified = from_bytes(hexlify(thing_cipher))

        dweets_list_cipher_hexlified = basicdweet.get_dweets_for(thing_cipher_hexlified)

        dweets_list = []
        for cipher_dweet in dweets_list_cipher_hexlified:
            content_dict_cipher_hexlified = cipher_dweet["content"]
            content_dict_cipher = {
                unhexlify(to_bytes(k)): unhexlify(to_bytes(v))
                for (k, v) in content_dict_cipher_hexlified.items()
            }
            content_dict = {
                from_bytes(cm.decrypt_msg(k)): from_bytes(cm.decrypt_msg(v))
                for (k, v) in content_dict_cipher.items()
            }
            decrypted_dweet = cipher_dweet
            decrypted_dweet["thing"] = from_bytes(thing)
            decrypted_dweet["content"] = content_dict
            dweets_list.append(decrypted_dweet)

        return dweets_list
