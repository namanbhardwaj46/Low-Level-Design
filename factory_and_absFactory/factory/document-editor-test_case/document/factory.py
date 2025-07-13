from .products import *


class DocumentFactory:

    @staticmethod
    def create_document(type: DocumentType, document_name: str) -> DocumentProcessor:
        return {
            DocumentType.PRESENTATION: PresentationDocumentProcessor(document_name),
            DocumentType.SPREADSHEET: SpreadsheetDocumentProcessor(document_name),
            DocumentType.TEXT: TextDocumentProcessor(document_name),
        }.get(type, None)
