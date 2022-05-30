# micropython-cryptodweet
[![PayPal Donate][paypal_img]][paypal_link]
[![PyPI version][pypi_img]][pypi_link]
[![Downloads][downloads_img]][downloads_link]

  [paypal_img]: https://github.com/jacklinquan/images/blob/master/paypal_donate_badge.svg
  [paypal_link]: https://www.paypal.me/jacklinquan
  [pypi_img]: https://badge.fury.io/py/micropython-cryptodweet.svg
  [pypi_link]: https://badge.fury.io/py/micropython-cryptodweet
  [downloads_img]: https://pepy.tech/badge/micropython-cryptodweet
  [downloads_link]: https://pepy.tech/project/micropython-cryptodweet

A python module for very basic APIs of the free dweet service with encryption.
Dweet is a simple machine-to-machine (M2M) service from [dweet.io](https://dweet.io).

This module only supports these dweet APIs of the free dweet service:

- `dweet for`
- `get latest dweet for`
- `get dweets for`

This module works under MicroPython and it is tested with MicroPython V1.18.
It requires [micropython-basicdweet](https://github.com/jacklinquan/micropython-basicdweet)
and [micropython-cryptomsg](https://github.com/jacklinquan/micropython-cryptomsg).

For a compatible CPython version, please find [Python package cryptodweet](https://github.com/jacklinquan/cryptodweet).

## Installation
``` Python
>>> import upip
>>> upip.install('micropython-cryptodweet')
```
Alternatively just copy cryptodweet.py and its dependency to the MicroPython device.

## Usage
``` python
>>> from cryptodweet import CryptoDweet
>>> cd = CryptoDweet('YOUR KEY')
>>> cd.dweet_for('YOUR THING', {'YOUR DATA': 'YOUR VALUE'})
{'content': {'8c94428bc640de621c7c3ceea1d00b96': '05d6f2dbc1ce3afa7e6072c0c4c6f6a7'}, 'created': '2022-05-30T00:13:24.215Z', 'thing': '9ee9b47833d5a13043c5f47e8802596a', 'transaction': 'ae80796e-4c3e-4237-bd2f-c5e040ff4b68'}
>>> cd.get_latest_dweet_for('YOUR THING')
[{'content': {'YOUR DATA': 'YOUR VALUE'}, 'created': '2022-05-30T00:13:24.215Z', 'thing': 'YOUR THING'}]
>>> cd.dweet_for('YOUR THING', {'YOUR DATA': 'YOUR VALUE 2'})
{'content': {'8c94428bc640de621c7c3ceea1d00b96': 'b9ed6b3c229ae62ea30f134f9332b5bf'}, 'created': '2022-05-30T00:16:20.835Z', 'thing': '9ee9b47833d5a13043c5f47e8802596a', 'transaction': 'b1f22bfc-8571-4798-a600-56c36288344e'}
>>> cd.get_latest_dweet_for('YOUR THING')
[{'content': {'YOUR DATA': 'YOUR VALUE 2'}, 'created': '2022-05-30T00:16:20.835Z', 'thing': 'YOUR THING'}]
>>> cd.get_dweets_for('YOUR THING')
[{'content': {'YOUR DATA': 'YOUR VALUE 2'}, 'created': '2022-05-30T00:16:20.835Z', 'thing': 'YOUR THING'}, {'content': {'YOUR DATA': 'YOUR VALUE'}, 'created': '2022-05-30T00:13:24.215Z', 'thing': 'YOUR THING'}]
```
