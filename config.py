#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv
load_dotenv()
""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """
    HOST = os.environ.get("HOST","")
    PORT = os.environ.get("PORT", "")
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
