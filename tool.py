"""Recommend lossless telemetry encodings from simple signal traits."""
from __future__ import annotations


def recommend(values: list[int | float]) -> str:
    """Suggest run-length, delta, or plain encoding based on observed values."""
    if len(values) < 2:
        return "plain"
    repeats = sum(left == right for left, right in zip(values, values[1:]))
    deltas = [right - left for left, right in zip(values, values[1:])]
    if repeats / (len(values) - 1) >= 0.5:
        return "run_length"
    if len(set(deltas)) <= max(1, len(deltas) // 3):
        return "delta"
    return "plain"
