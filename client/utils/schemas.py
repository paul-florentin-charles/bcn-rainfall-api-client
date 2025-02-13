"""
Provides a Pydantic model to initiate API client with a custom configuration.
"""

from pydantic import BaseModel


class APIClientSettings(BaseModel):
    """Type definition for API Client settings."""

    host: str
    port: int
    root_path: str
