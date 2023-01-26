import json
import os
from typing import Optional, Dict
from urllib.parse import urlparse

import requests
from requests_file import FileAdapter
from sphinx.application import Sphinx

from sphinx_ads.logging import get_logger

logger = get_logger(__name__)


def get_json_data_from_path(app: Sphinx) -> Dict:
    ads_json_path = app.config.config.ads_path
    logger.info(f"Importing ads from {ads_json_path}")

    if not os.path.isabs(ads_json_path):
        # Relative path should start from current rst file directory
        curr_dir = os.path.dirname(app.env.docname)
        new_ads_json_path = os.path.join(app.srcdir, curr_dir, ads_json_path)

        correct_ads_json_path = new_ads_json_path

        if not os.path.exists(correct_ads_json_path):
            # Determine relative path by starting from conf.py directory
            check_ads_json_path = os.path.join(app.srcdir, ads_json_path)
            if os.path.exists(check_ads_json_path):
                correct_ads_json_path = check_ads_json_path
    else:
        # Absolute path starts with /, based on the source directory. The / must be striped
        correct_ads_json_path = os.path.join(app.srcdir, ads_json_path[1:])

    if not os.path.exists(correct_ads_json_path):
        raise ReferenceError(f"The path you passed to 'ads_path': {correct_ads_json_path}, does not exist.")

    with open(correct_ads_json_path) as ads_json_file:
        ads_json_file_content = ads_json_file.read()
    try:
        ads_list: Dict = json.loads(ads_json_file_content)
    except json.JSONDecodeError as e:
        raise AdsJSONImportException(
            f"Could not load the JSON file you passed to 'ads_path': {correct_ads_json_path}. Reason: {e}"
        )

    return ads_list


def get_json_data_from_url(app: Sphinx) -> Dict:
    ads_json_url = app.config.ads_url
    # check if given url is downloadable ads.json path
    url = urlparse(ads_json_url)
    if not url.scheme and url.netloc:
        raise AdsJSONImportException(f"The JSON URL given is not downloadable: {url}.")
    # download ads.json
    logger.info(f"Downloading ads.json from url {ads_json_url}")
    s = requests.Session()
    s.mount("file://", FileAdapter())
    try:
        response = s.get(ads_json_url)
        ads_list: Dict = response.json()  # The downloaded file MUST be json. Everything else we do not handle!
    except Exception as e:
        raise AdsJSONImportException(f"Getting {ads_json_url} didn't work. Reason: {e}.")

    return ads_list


class AdsJSONImportException(BaseException):
    pass
