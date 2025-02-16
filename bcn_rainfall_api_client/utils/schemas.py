"""
Provides the API server settings to initiate API client.
"""

from pydantic import BaseModel, Field


class APIServerSettings(BaseModel):
    """Type definition for API server settings."""

    host: str
    port: int
    root_path: str | None = Field(None)
