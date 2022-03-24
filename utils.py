import os
import shutil
import dataclasses
from typing import ClassVar, Text, Type, List

from marshmallow import EXCLUDE, Schema
from marshmallow_dataclass import dataclass


class ObjectWithSchema:
    Schema: ClassVar[Type[Schema]]

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

    def to_json(self) -> Text:
        schema = self.Schema(unknown=EXCLUDE)
        return schema.dumps(self).data


@dataclass
class TestFile(ObjectWithSchema):
    content: str
    name: str


class TempFileManager:
    directory = None
    files = None

    def create_file(self, temp_file: TestFile):
        file_path = f"{self.directory}/{temp_file.name}"

        with open(file_path, 'w') as f:
            f.writelines(temp_file.content)

    def __init__(self, *, files: List[TestFile], directory: str):
        self.files = files or []
        self.directory = directory

        if not os.path.exists(self.directory):
            os.makedirs(self.directory, exist_ok=True)

    def __enter__(self):
        for temp_file in self.files:
            self.create_file(temp_file)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        shutil.rmtree(self.directory)
        if exc_type is not None:
            return False
