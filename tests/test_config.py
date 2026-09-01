from pathlib import Path

from ml_template.config import Settings


def test_settings_defaults() -> None:
    settings = Settings()
    assert settings.seed == 42
    assert settings.batch_size == 32


def test_settings_from_yaml() -> None:
    config_path = Path(__file__).parent.parent / "configs" / "example.yaml"
    settings = Settings.from_yaml(config_path)
    assert settings.project_name == "ml-template"
