import os

from llama_cloud_services import LlamaParse
from llama_cloud_services.parse.types import JobResult


class LlammaParser:
    def __init__(self) -> None:
        api_key = os.getenv("LLAMA_CLOUD_API_KEY")
        if (api_key is None) or (api_key == ""):
            raise ValueError(
                "LLAMA_CLOUD_API_KEY environment variable is not set."
            )

        self.parser = LlamaParse(
            api_key=api_key,
            num_workers=1,
            verbose=True,
            language="pt"
        )

    def parse(self, file_path: str) -> JobResult:
        result = self.parser.parse(file_path)
        assert not isinstance(
            result, list), "Expected single JobResult, got list"
        return result
