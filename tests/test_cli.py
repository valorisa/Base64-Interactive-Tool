from pathlib import Path

from base64_tool.cli import main


def test_cli_encode(capsys):
    assert main(["encode", "hello"]) == 0

    out = capsys.readouterr().out.strip()

    assert out == "aGVsbG8="


def test_cli_decode(capsys):
    assert main(["decode", "aGVsbG8="]) == 0

    out = capsys.readouterr().out.strip()

    assert out == "hello"


def test_cli_invalid_base64(capsys):
    assert main(["decode", "%%%%"]) == 1

    err = capsys.readouterr().err.strip()

    assert "Invalid Base64" in err


def test_cli_encode_file(tmp_path: Path):
    source = tmp_path / "input.txt"
    destination = tmp_path / "output.b64"

    source.write_text("hello", encoding="utf-8")

    assert main(
        [
            "encode-file",
            str(source),
            str(destination),
        ]
    ) == 0

    assert destination.read_text(encoding="ascii") == "aGVsbG8="


def test_cli_decode_file(tmp_path: Path):
    source = tmp_path / "input.b64"
    destination = tmp_path / "output.txt"

    source.write_text("aGVsbG8=", encoding="ascii")

    assert main(
        [
            "decode-file",
            str(source),
            str(destination),
        ]
    ) == 0

    assert destination.read_text(encoding="utf-8") == "hello"


def test_cli_encode_missing_file(capsys, tmp_path: Path):
    destination = tmp_path / "output.b64"

    assert main(
        [
            "encode-file",
            str(tmp_path / "missing.txt"),
            str(destination),
        ]
    ) == 1

    err = capsys.readouterr().err.strip()

    assert err


def test_cli_decode_invalid_file(capsys, tmp_path: Path):
    source = tmp_path / "invalid.b64"
    destination = tmp_path / "output.txt"

    source.write_text("%%%%", encoding="ascii")

    assert main(
        [
            "decode-file",
            str(source),
            str(destination),
        ]
    ) == 1

    err = capsys.readouterr().err.strip()

    assert "Invalid Base64" in err
