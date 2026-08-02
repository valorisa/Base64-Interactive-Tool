#!/usr/bin/env python3
"""CLI interactif & hybride de conversion Base64 (Texte UTF-8)."""

import base64
import binascii
import sys


# --- NOYAU DE TRAITEMENT (Pure Logic) ---


def encode_base64(data: str) -> str:
    """Encode une chaîne UTF-8 en Base64."""
    encoded_bytes = base64.b64encode(data.encode("utf-8"))
    return encoded_bytes.decode("ascii")


def decode_base64(data: str) -> str:
    """Décode une chaîne Base64 vers du texte UTF-8.

    Nettoie tous les espaces et retours à la ligne internes/externes
    avant décodage.

    Raises:
        ValueError:
            Si le payload n'est pas du Base64 valide ou n'est pas
            du texte UTF-8.
    """
    cleaned_data = "".join(data.split())

    try:
        decoded_bytes = base64.b64decode(cleaned_data, validate=True)
        return decoded_bytes.decode("utf-8")
    except (binascii.Error, UnicodeDecodeError, ValueError) as error:
        raise ValueError(
            f"Impossible de décoder le payload en texte UTF-8 : {error}"
        ) from error


# --- ANALYSE DES ARGUMENTS (Strict Mode Parser) ---


def parse_mode(args: list[str]) -> str | None:
    """Retourne 'encode', 'decode' ou None (si aucun flag fourni).

    Raises:
        ValueError:
            Si des options inconnues ou contradictoires sont fournies.
    """
    valid_encode = {"-e", "--encode"}
    valid_decode = {"-d", "--decode"}
    provided = set(args)

    if not provided:
        return None

    unknown = provided - valid_encode - valid_decode
    if unknown:
        raise ValueError(f"Option(s) inconnue(s) : {', '.join(sorted(unknown))}")

    if (provided & valid_encode) and (provided & valid_decode):
        raise ValueError("Les options -e/--encode et -d/--decode sont incompatibles.")

    if provided & valid_decode:
        return "decode"

    return "encode"


# --- INTERFACE UTILISATEUR (CLI & Mode Hybride) ---


def run_cli() -> None:
    """Point d'entrée principal."""

    try:
        explicit_mode = parse_mode(sys.argv[1:])
    except ValueError as error:
        print(f"Erreur : {error}", file=sys.stderr)
        sys.exit(2)

    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
        mode = explicit_mode or "encode"

        try:
            if mode == "decode":
                print(decode_base64(input_data), end="")
            else:
                print(encode_base64(input_data), end="")
        except ValueError as err:
            print(f"Erreur : {err}", file=sys.stderr)
            sys.exit(1)

        return

    mode = explicit_mode

    if mode is None:
        print("=== Base64 Interactive Tool (Text UTF-8) ===")
        print("1. Encoder du texte en Base64")
        print("2. Décoder du Base64 en texte")
        print("q. Quitter")

        choice = input("\nChoix (1/2/q) : ").strip().lower()

        if choice == "q":
            sys.exit(0)
        if choice == "1":
            mode = "encode"
        elif choice == "2":
            mode = "decode"
        else:
            print("Choix invalide.", file=sys.stderr)
            sys.exit(1)

    text = input("Entrez la chaîne à traiter : ")

    try:
        if mode == "encode":
            result = encode_base64(text)
            print(f"\nRésultat (Base64) :\n{result}")
        else:
            result = decode_base64(text)
            print(f"\nRésultat (Texte UTF-8) :\n{result}")
    except ValueError as err:
        print(f"\nErreur : {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run_cli()
