# Wegram
A message bridge

## What is this
I'm a big fan of [Telegram][telegram_link], but I have to use WeChat in
order to receive messages from some friends / relatives. WeChat was not really
designed for pure messaging, and does too much as an IM software. So why not forward
all WeChat messges to Telegram?

## How to use
* Clone this repo, checkout the `develop` branch
* Install all requirements via `pip install -r requirements.txt`
* Talk to [eth0][eth0_link] and use `/push` to get a push
  code
* Start the bridge: `ETH0_PUSH_CODE=your_push_code_here python -m wegram.cli`
* Scan the QRCode in WeChat mobile app, and you're in

## Notice
* This thing is far from stable (internally it uses a communication library
  based on the work of reverse-engineering the protocol of WeChat), use at your
  own risk.
* [Eth0][eth0_link] is not yet open sourced, but I can promise you that it will
  not store any message pushed. If you don't trust me, do not use this bridge.
* A standalone Telegram bot adapter is in development. You can use your own
  Telegram bot to forward the message once it's done, but that requires a
  machine on which you can communicate with Telegram's API server.

## License
MIT license, see LICENSE file for details.

## Used software components
* A modified version of [WeixinBot][weixinbot_link], original written by Urinx,
  licensed under Apache License 2.0. See README.md and LICENSE file inside
  `weixinbot` for details.

  [telegram_link]: https://telegram.org
  [eth0_link]: https://telegram.me/eth0_bot
  [weixinbot_link]: https://github.com/Urinx/WeixinBot
