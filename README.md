# Semantic-PDF-Explorer
A simple AI-powered search tool for PDFs. 

*Approach*
This project was built using Hugging Face Zero Shot Classification. The chunks with a confidence score of more than 50% are displayed.
Text of the PDF is extracted using the PyPDF2 library. The chunks whose size is less than 300 are considered, and any exceptions that arise are also handled effectively. 

*Difficulties faced*
The code threw a lot of errors initially, 
