from unittest.mock import patch

from ml_template.config import Settings
from ml_template.tracking import init_run


def test_init_run_logs_config_and_git_commit() -> None:
    settings = Settings()

    with patch("ml_template.tracking.wandb.init") as mock_init:
        init_run(settings)

    _, kwargs = mock_init.call_args
    assert kwargs["project"] == settings.project_name
    assert kwargs["config"]["seed"] == settings.seed
    assert "git_commit" in kwargs["config"]
