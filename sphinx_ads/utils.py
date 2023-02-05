import json
from pathlib import Path
from typing import Dict, Optional
from urllib.parse import urlparse

import requests
from requests_file import FileAdapter
from sphinx.application import Sphinx

from sphinx_ads.logging import get_logger

logger = get_logger(__name__)


def get_json_data_from_path(app: Sphinx) -> Dict:
    ads_json_path = Path(app.config.advertisement_path)
    logger.info(f"Importing ads from {ads_json_path}")

    conf_dir = Path(app.confdir)

    if not ads_json_path.is_absolute():
        # # Relative path should start from current rst file directory
        # curr_dir = os.path.dirname(app.env.docname)
        # new_ads_json_path = os.path.join(app.srcdir, curr_dir, ads_json_path)
        #
        correct_ads_json_path = ""

        # if not os.path.exists(ads_json_path):
        # Determine relative path by starting from conf.py directory
        check_ads_json_path = conf_dir.joinpath(ads_json_path)
        if not check_ads_json_path.exists():
            raise ReferenceError(
                f"The path you passed to 'advertisement_path': {app.config.advertisement_path}, does not exist."
            )
        correct_ads_json_path = check_ads_json_path
    else:
        # Absolute path starts with /, based on the source directory. The / must be striped
        correct_ads_json_path = conf_dir.joinpath(ads_json_path[1:])

    if not correct_ads_json_path.exists():
        raise ReferenceError(
            f"The path you passed to 'advertisement_path': {app.config.advertisement_path}, does not exist."
        )

    ads_json_file_content = correct_ads_json_path.read_text(encoding="utf8")
    # with open(correct_ads_json_path) as ads_json_file:
    #     ads_json_file_content = ads_json_file.read()
    try:
        ads_list: Dict = json.loads(ads_json_file_content)
    except json.JSONDecodeError as e:
        raise AdsJSONImportException(
            f"Could not load the JSON file you passed to 'advertisement_path': {correct_ads_json_path}. Reason: {e}"
        )

    return ads_list


def get_json_data_from_url(app: Sphinx) -> Dict:
    ads_json_url = app.config.advertisement_url
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


def load_data(app: Sphinx) -> None:
    if app.config.advertisement_path is not None and len(app.config.advertisement_path) != 0:
        ads_json_data: Dict = get_json_data_from_path(app)
        app.env.sphinx_ads_data.update(ads_json_data)

    if app.config.advertisement_url is not None and len(app.config.advertisement_url) != 0:
        ads_json_data: Dict = get_json_data_from_url(app)
        app.env.sphinx_ads_data.update(ads_json_data)


class AdsJSONImportException(BaseException):
    pass
