# PayPilotLabs Telephony

Phone calls, text messages and one-time codes inside PayPilotLabs apps, through Twilio or Exotel.

By [PayPilotLabs](https://paypilotlabs.com). Support and requests: https://paypilotlabs.com/roadmap/

## What it does

- Lets staff call a customer from the app with one click.
- Shows a pop-up when a customer calls in.
- Keeps a log of every call, with its recording.
- Connects to Twilio or Exotel, whichever you use.
- Remembers each person's preferred way to call.
- Sends text messages (SMS) and keeps a log of them.
- Sends one-time login codes (OTP) by SMS or email, with limits to stop abuse.

It has no screens of its own. The product it is installed in shows the buttons and pop-ups.

## How it helps your business

- No call goes unrecorded: every call is logged and linked to the contact.
- Your team stops typing numbers by hand.
- Managers can listen back to a call to settle a doubt.
- Customers can confirm who they are with a code sent to their phone or email.
- You can switch phone provider without changing the rest of the app.

## How it fits with other PayPilotLabs products

It runs on paypilotlabs-framework and is used by PayPilotLabs Helpdesk (optional) and PayPilotLabs CRM. It does not need any other PayPilotLabs app.

## Run it

It is not run on its own. It is installed as part of a product image: the product's `./docker/build.sh` adds it. See that product's README.

## Licence

AGPL-3.0. See [license.txt](license.txt). Based on open-source work by others; see [NOTICE.md](NOTICE.md) for credits.
