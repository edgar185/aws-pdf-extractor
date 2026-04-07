# AWS PDF Extractor 📄🚀

A modular Python automation tool that uses **Amazon Textract** and **AWS S3** to extract text from multi-page PDF documents. 

## Features
- **Modular Design**: Separate functions for S3 uploading, Textract triggering, and result polling.
- **Asynchronous Processing**: Designed to handle large multi-page PDFs via S3.
- **Easy Integration**: Simple setup for any AWS-enabled environment.

## Prerequisites
- Python 3.x
- AWS CLI configured (`aws configure`)
- IAM Permissions: `AmazonS3FullAccess`, `AmazonTextractFullAccess`

## Installation
1. **Clone the repo**:
   ```bash
   git clone [https://github.com](https://github.com/edgar185/aws-pdf-extractor/blob/main/PDFExtracter.py)
   cd aws-pdf-extractor
