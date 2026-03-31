# Semantic-PDF-Explorer
A simple AI-powered search tool for PDFs. 

*Approach:*
This project was built using Hugging Face Zero Shot Classification. The chunks with a confidence score of more than 50% are displayed.
Text of the PDF is extracted using the PyPDF2 library. The chunks whose size is less than 300 are considered, and any exceptions that arise are also handled effectively. 

*Difficulties faced:*
The code initially threw a lot of errors, which were quite frustrating. Debugging was the major challenge in this project.

*Results:* 
This system successfully extracts text from the user-provided PDF and uses Zero-Shot Classification to identify content relevant to the user's query. Relevant texts/chunks having a confidence score greater than or equal to 50% are displayed. 

*Key Learning:*
This was my first project. Hugging Face transformer was a new topic for me. Also learnt how to integrate Zero-Shot Classification in this system.

*How to run this assignment?*
The program will easily run on VS Code. Transformers, PyPDF2 and PyTorch have to be installed before running the program on VS Code. Also, the PDF provided by the user MUST lie in the same directory as the code file.
