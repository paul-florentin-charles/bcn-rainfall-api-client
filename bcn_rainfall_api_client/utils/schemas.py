"""
Provides the API server settings to initiate API client.
"""

from pydantic import BaseModel


class APIServerSettings(BaseModel):
    """Type definition for API server settings."""

    base_url: str
