"""Executable checks for the vector-ui-timeline-bench casebook."""

from __future__ import annotations

from collections import Counter

from . import vector_ui_timeline_bench_segment_00
from . import vector_ui_timeline_bench_segment_01
from . import vector_ui_timeline_bench_segment_02
from . import vector_ui_timeline_bench_segment_03
from . import vector_ui_timeline_bench_segment_04
from . import vector_ui_timeline_bench_segment_05
from . import vector_ui_timeline_bench_segment_06
from . import vector_ui_timeline_bench_segment_07
from . import vector_ui_timeline_bench_segment_08
from . import vector_ui_timeline_bench_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from vector_ui_timeline_bench_segment_00.iter_vector_ui_timeline_bench_00()
    yield from vector_ui_timeline_bench_segment_01.iter_vector_ui_timeline_bench_01()
    yield from vector_ui_timeline_bench_segment_02.iter_vector_ui_timeline_bench_02()
    yield from vector_ui_timeline_bench_segment_03.iter_vector_ui_timeline_bench_03()
    yield from vector_ui_timeline_bench_segment_04.iter_vector_ui_timeline_bench_04()
    yield from vector_ui_timeline_bench_segment_05.iter_vector_ui_timeline_bench_05()
    yield from vector_ui_timeline_bench_segment_06.iter_vector_ui_timeline_bench_06()
    yield from vector_ui_timeline_bench_segment_07.iter_vector_ui_timeline_bench_07()
    yield from vector_ui_timeline_bench_segment_08.iter_vector_ui_timeline_bench_08()
    yield from vector_ui_timeline_bench_segment_09.iter_vector_ui_timeline_bench_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def vector_ui_timeline_bench_summary() -> dict:
    return assert_expected()
