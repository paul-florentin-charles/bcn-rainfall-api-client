"""
Provides functions parsing the YAML Configuration file to retrieve parameters.
"""

from functools import cached_property
from typing import Optional

from bcn_rainfall_api_client.utils import APIClientSettings, BaseConfig


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
    def get_api_settings(self) -> APIClientSettings:
        """
        Return settings to build base API URL to communicate with using client.

        Example:
        {
            "host": "127.0.0.1",
            "port": 8000,
            "root_path": "/api",
        }

        """

        return APIClientSettings(**self.yaml_config["api"])
