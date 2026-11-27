import ast

from pydantic import BaseModel

from chunk.chunker import Chunk


class ChunkerPy(BaseModel):

	def chunk_file(file_name: str) -> Chunk:
		chunk_info = {
			"id": 0
		}
		try:
			with open(file_name, 'r') as f:
				data = ast.parse(f.read())
				
		except Exception as e:
			raise e

		return Chunk(**chunk_info)