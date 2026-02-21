from abc import ABC, abstractmethod
from typing import List


# ---- Abstraction for document elements ----
class DocumentElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class TextElement(DocumentElement):
    def __init__(self, content: str):
        self._content = content

    def render(self) -> str:
        return self._content


class ImageElement(DocumentElement):
    def __init__(self, image_path: str):
        self._image_path = image_path

    def render(self) -> str:
        return f"[Image: {self._image_path}]"


# ---- Save Strategy ----
class SaveStrategy(ABC):
    @abstractmethod
    def save(self, content: str) -> None:
        pass


class SaveToDisk(SaveStrategy):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, content: str) -> None:
        with open(self._file_path, "w") as f:
            f.write(content)
        print(f"Document saved to {self._file_path}")


# ---- Document ----
class Document:
    def __init__(self):
        self._elements: List[DocumentElement] = []

    def add_element(self, element: DocumentElement) -> None:
        self._elements.append(element)

    def render(self) -> str:
        return "\n".join(element.render() for element in self._elements)

    def save(self, strategy: SaveStrategy) -> None:
        strategy.save(self.render())


if __name__ == "__main__":
    # Create a document
    doc = Document()
    doc.add_element(TextElement("Hello, this is a sample document."))
    doc.add_element(ImageElement("path/to/image.png"))
    doc.add_element(TextElement("This document demonstrates the Liskov Substitution Principle."))

    # Render and save the document
    print(doc.render())
    save_strategy = SaveToDisk("LLD-Google-Docs/sample_document.txt")
    doc.save(save_strategy)