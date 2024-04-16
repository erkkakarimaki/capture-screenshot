from __future__ import annotations
from robot.libraries.BuiltIn import BuiltIn
import base64

class Capture:
    def __init__(self) -> None:
        self.qweb = BuiltIn().get_library_instance("QWeb")

    def capture_screenshot(self, path: str) -> None:
        driver = self.qweb.return_browser()
        page_rect = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
        screenshot = driver.execute_cdp_cmd(
            "Page.captureScreenshot",
            {
                "format": "png",
                "captureBeyondViewport": True,
                "clip": {
                    "width": page_rect["contentSize"]["width"],
                    "height": page_rect["contentSize"]["height"],
                    "x": 0,
                    "y": 0,
                    "scale": 1
                }
            })

        with open(path, "wb") as file:
            file.write(base64.urlsafe_b64decode(screenshot["data"]))
