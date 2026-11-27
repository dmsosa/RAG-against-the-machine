from pydantic import BaseModel


TARGET_FILES = [".txt", ".md", ".py"]

class DataStorage(BaseModel):
	storage: dict[str, ]