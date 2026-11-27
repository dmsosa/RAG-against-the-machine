from pydantic import BaseModel, Field


class Loader(BaseModel):
    """
    The goal and purpose of this class is to read the documents that are
    relevant for our Context-Enrichment process. We are going to focus only on
    .txt, .md, and .py files for now.
    """
    py_files: dict[str, str] = Field(default_factory=dict)
    md_files: dict[str, str] = Field(default_factory=dict)
    txt_files: dict[str, str] = Field(default_factory=dict)

    def load_sources(data_path: str) -> None:
        pass