"""
Provides functions parsing the YAML Configuration file to retrieve parameters.
"""

from functools import cached_property
from typing import Optional

from bcn_rainfall_api_client.utils import APIServerSettings, BaseConfig


class Config(BaseConfig):
    """
    Provides function to retrieve fields from YAML configuration.
    It needs to be instantiated first to be loaded.
    Configuration is cached but can be reloaded if needed.
    """

    _instance: Optional["Config"] = None

    def __new__(cls, *, path: str):
        return super().__new__(cls, path=path)

    @cached_property
    def get_api_server_settings(self) -> APIServerSettings:
        """
        Return API server settings to communicate with using client.

        Example:
        {
            "api": {
                "base_url": "http://127.0.0.1:8000/rest",
            },
        }
        """

        return APIServerSettings(**self.yaml_config["api"])
