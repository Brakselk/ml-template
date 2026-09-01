import random

from ml_template.seed import set_seed


def test_set_seed_is_deterministic() -> None:
    set_seed(42)
    first = [random.random() for _ in range(5)]

    set_seed(42)
    second = [random.random() for _ in range(5)]

    assert first == second
