import builtins

from base64_tool.interactive import run


def test_encode(monkeypatch, capsys):
    answers = iter([
        "e",
        "",
        "hello",
    ])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(answers),
    )

    assert run() == 0

    out = capsys.readouterr().out

    assert "aGVsbG8=" in out


def test_decode(monkeypatch, capsys):
    answers = iter([
        "d",
        "",
        "aGVsbG8=",
    ])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(answers),
    )

    assert run() == 0

    out = capsys.readouterr().out

    assert "hello" in out


def test_invalid_mode(monkeypatch):
    answers = iter(["x"])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(answers),
    )

    assert run() == 1


def test_invalid_base64(monkeypatch):
    answers = iter([
        "d",
        "",
        "%%%%",
    ])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(answers),
    )

    assert run() == 1
