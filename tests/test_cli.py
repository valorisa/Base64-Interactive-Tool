from base64_tool.cli import main


def test_cli_encode(capsys):
    assert main(["encode", "hello"]) == 0

    out = capsys.readouterr().out.strip()

    assert out == "aGVsbG8="


def test_cli_decode(capsys):
    assert main(["decode", "aGVsbG8="]) == 0

    out = capsys.readouterr().out.strip()

    assert out == "hello"


def test_cli_invalid_base64():
    assert main(["decode", "%%%%"]) == 1
