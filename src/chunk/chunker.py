from typing import Any

from pydantic import BaseModel, Field


class Chunk(BaseModel):
    id: int
    content: str
    file_path: str
    first_character_index: str
    last_character_index: str
    file_type: str

class Chunker(BaseModel):
    """
    The goal and purpose of this class is to read the documents that are
    relevant for our Context-Enrichment process. We are going to focus only on
    .txt, .md, and .py files for now.
    """
    chunk_size: int = Field(gt=1, lt=2001, default=200)

    def load_sources(data_path: str) -> None:
        pass

    def create_chunk(kwargs: dict[str, Any]) -> Chunk:
        return Chunk(
            **kwargs
        )

def create_all_chunks() -> None:
    pass