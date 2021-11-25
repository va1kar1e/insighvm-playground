# coding: utf-8
# Author: Siwanont Sittinam

import os
import base64
from dotenv import load_dotenv
load_dotenv()


class InsightvmAuthentication:
    def getHostname(self):
        HOSTNAME = os.getenv("HOSTNAME")

        return "https://" + HOSTNAME + "/"

    def getRequestHeader(self):
        INSIGHTVM_USER = os.getenv("INSIGHTVM_USER")
        INSIGHTVM_PASSWORD = os.getenv("INSIGHTVM_PASSWORD")
        HOSTNAME = os.getenv("HOSTNAME")

        TOKEN = (INSIGHTVM_USER + ":" + INSIGHTVM_PASSWORD).encode("ascii")
        TOKEN_AUTH = "Basic " + base64.b64encode(TOKEN).decode("utf-8")

        del INSIGHTVM_USER, INSIGHTVM_PASSWORD, TOKEN

        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;',
            "Host": HOSTNAME,
            'Authorization': TOKEN_AUTH
        }
