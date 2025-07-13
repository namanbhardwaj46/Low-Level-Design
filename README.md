# Simple Factory Pattern for Document Processing

## Problem Statement

You are designing a document processing application. Depending on the type of document (e.g., text, spreadsheet, presentation), different processing routines are required. You need a way to create document processors without explicitly specifying their classes, ensuring the application is open for future document types.

## Assignment

Your task is to implement the Simple Factory pattern to create document processors in the document processing application. The Simple Factory pattern provides a way to create objects without exposing the instantiation logic, allowing for easy addition of new document processor types.

### Task 1 - Creating Document Processor Classes (Product Hierarchy)

1. **Complete the common product class `DocumentProcessor`**: Start by completing the parent `DocumentProcessor` class. This is going to be the parent class for each supported document type. Each document processor class should implement the same set of methods for processing documents. Additionally, each class should have attributes that store information about the document, such as the `document_name`. **Make sure to use the same names of the methods and attributes in the parent class**. Also, abstract common methods with the same implementation in the parent class.

2. **Modify the concrete product classes** (e.g., `TextDocumentProcessor`, `SpreadsheetDocumentProcessor`, `PresentationDocumentProcessor`): Implement the concrete document processor classes for each supported document type. Each class should inherit from the `DocumentProcessor` class and implement the methods to process documents. It should have methods `process_document` and `supports_type` to process the document and check if the document type is supported respectively. 

### Task 2 - Implementing the Simple Factory

Next, complete the `DocumentFactory` class that follows the Simple Factory pattern. This class should provide a static method `create_document` to create document processor objects based on the document type and relevant arguments. The factory class should take care of instantiating the appropriate document processor class based on the type provided and the relevant arguments. **Remember you have to create the actual concrete document processor objects in the factory class so pass the required arguments to the factory method**.

### Instructions

1. Implement the `DocumentProcessor` class as a common parent class for all document processors. Include attributes and methods that are common to all document processors.

2. Implement the `DocumentFactory` class that implements the Simple Factory pattern. Add a method `create_document` to create document processor objects based on the document type and relevant arguments (`document_name`).

3. Run the provided test cases in the `DocumentProcessorTest` class to verify the correctness of your implementation. The tests will check if all document processor classes are implemented correctly and if the factory class is able to create document processor objects for different document types.