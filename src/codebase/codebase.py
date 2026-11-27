

from pydantic import BaseModel


class Codebase(BaseModel):
    def model_post_init(self) -> "Codebase":
        pass
