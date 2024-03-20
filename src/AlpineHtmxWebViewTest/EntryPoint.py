# ----------------------------------------------------------------------
# |
# |  Copyright (c) 2024 David Brownell
# |  Distributed under the MIT License.
# |
# ----------------------------------------------------------------------
"""This file serves as an example of how to create scripts that can be invoked from the command line once the package is installed."""

import webview
from AlpineHtmxWebViewTest.Server import app


if __name__ == "__main__":
    webview.create_window("AlpineHtmxWebViewTest", app)

    webview.start(
        # debug=True,
        ssl=True,
    )
