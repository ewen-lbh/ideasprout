from __future__ import annotations

from typing import Any, Optional, Union

from semantic_version import Version

VERSION = Version("0.11.0")

RELEASES_RSS_URL = "https://pypi.org/rss/project/ideaseed/releases.xml"

COLOR_NAME_TO_HEX_MAP: dict[str, int] = {
    "Blue": 0xAECBFA,
    "Brown": 0xE6C9A8,
    "DarkBlue": 0xAECBFA,
    "Gray": 0xE8EAED,
    "Green": 0xCCFF90,
    "Orange": 0xFBBC04,
    "Pink": 0xFDCFE8,
    "Purple": 0xD7AEFB,
    "Red": 0xF28B82,
    "Teal": 0xA7FFEB,
    "White": 0xFFFFFF,
    "Yellow": 0xFFF475,
}

COLOR_ALIASES = {
    "Cyan": "Teal",
    "Indigo": "DarkBlue",
    "Grey": "Gray",
    "Magenta": "Purple",
}

VALID_COLOR_NAMES = list(COLOR_ALIASES.keys()) + list(COLOR_NAME_TO_HEX_MAP.keys())

# colors
C_PRIMARY = "blue"
