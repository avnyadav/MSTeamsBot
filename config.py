#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv
load_dotenv()
""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """
    HOST = os.environ.get("HOST","localhost")
    PORT = os.environ.get("PORT", "8080")
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    WEB_CHAT_SECRET= os.environ.get("WebChatSecret","")