import httpx
import pytest

from numbers_api.tools.numbers_api_tool import NumbersAPITool, NumbersAPIToolInput


def test_input_rejects_unknown_fact_type() -> None:
    with pytest.raises(ValueError):
        NumbersAPIToolInput(number=7, type="unknown")


def test_tool_returns_bounded_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    def fail_request(*args: object, **kwargs: object) -> str:
        raise httpx.TimeoutException("timed out")

    monkeypatch.setattr(httpx, "get", fail_request)

    result = NumbersAPITool()._run(7, "trivia")

    assert result == "Numbers API request failed: timed out"
