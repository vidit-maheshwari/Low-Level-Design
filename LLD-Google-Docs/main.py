from abc import ABC, abstractmethod
from typing import List
import uuid


# ---- Base Abstraction ----
class DocumentElement(ABC):
    def __init__(self):
        self.id = str(uuid.uuid4())

    @abstractmethod
    def render(self) -> str:
        pass


# ---- Editable Capability ----
class Editable(ABC):
    @abstractmethod
    def update(self, new_content: str) -> None:
        pass


# ---- Concrete Elements ----
class TextElement(DocumentElement, Editable):
    def __init__(self, content: str):
        super().__init__()
        self._content = content

    def render(self) -> str:
        return self._content

    def update(self, new_content: str) -> None:
        self._content = new_content


class ImageElement(DocumentElement, Editable):
    def __init__(self, image_path: str):
        super().__init__()
        self._image_path = image_path

    def render(self) -> str:
        return f"[Image: {self._image_path}]"

    def update(self, new_content: str) -> None:
        self._image_path = new_content


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

    def edit_element(self, element_id: str, new_content: str) -> None:
        for element in self._elements:
            if element.id == element_id:
                if isinstance(element, Editable):
                    element.update(new_content)
                    return
                else:
                    raise TypeError("Element is not editable")
        raise ValueError("Element not found")

    def render(self) -> str:
        return "\n".join(element.render() for element in self._elements)

    def save(self, strategy: SaveStrategy) -> None:
        strategy.save(self.render())


# ---- Client Code ----
if __name__ == "__main__":
    doc = Document()

    text = TextElement("Hello World")
    image = ImageElement("image.png")

    doc.add_element(text)
    doc.add_element(image)

    print("Before Edit:\n")
    print(doc.render())

    # Edit using ID
    doc.edit_element(text.id, "Updated Hello World")
    doc.edit_element(image.id, "new_image.png")

    print("\nAfter Edit:\n")
    print(doc.render())

    save_strategy = SaveToDisk("sample_document.txt")
    doc.save(save_strategy)