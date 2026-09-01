"""Config loaded from YAML, overridable via environment variables.

Keeps run configuration out of code (per Faz 0: "config'i koddan ayirma").
"""

from pathlib import Path
from typing import Any

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="ML_")

    seed: int = 42
    learning_rate: float = 1e-3
    batch_size: int = 32
    project_name: str = "ml-template"

    @classmethod
    def from_yaml(cls, path: Path) -> "Settings":
        data: dict[str, Any] = yaml.safe_load(path.read_text()) or {}
        return cls(**data)
