"""W&B run initialization, wired to reproducibility metadata.

Every run's config is logged alongside the git commit hash that produced it
(per Faz 0: "her run'da git commit hash'i loglanır"). Requires `wandb login`
to have been run once on this machine.
"""

from typing import Any

import wandb

from ml_template.config import Settings
from ml_template.repro import get_git_commit_hash


def init_run(settings: Settings, **wandb_kwargs: Any) -> Any:
    config = settings.model_dump()
    config["git_commit"] = get_git_commit_hash()

    return wandb.init(
        project=settings.project_name,
        config=config,
        **wandb_kwargs,
    )
