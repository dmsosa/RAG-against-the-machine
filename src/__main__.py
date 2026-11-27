import argparse

from pydantic import ValidationError


def init_argparse() -> argparse.Namespace:
    """Parser of the terminal code """
    parser = argparse.ArgumentParser(
        description="" \
        "RAG: Retrieval from vLLM repository to " \
        "answer questions related to it. "
    )
    parser.add_argument(
        "--chunk_size",
        default=200,
    )

    return parser.parse_args()

def main() -> None:
    # The first step, read the file from repository
    args: argparse.Namespace = init_argparse()
    try:
        chunker = Chunker(chunk_size=args.chunk_size)
    except ValidationError:
        print(f"Error, invalid chunk size {args.chunk_size}")
        return 1
    
    codebase = Codebase(file_path)


if __name__ == "__main__":
    main()