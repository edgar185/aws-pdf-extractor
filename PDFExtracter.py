import pandas as pd
import boto3
import time

def upload_to_s3(file_path, bucket_name):
    """Uploads your local PDF to an S3 bucket."""
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, file_path)
    print(f"✅ Uploaded {file_path} to {bucket_name}")

def save_to_excel(text_lines, filename="results.xlsx"):
    """Converts the extracted list of lines into an Excel spreadsheet."""
    if not text_lines:
        print("⚠️ No text found to save.")
        return
        
    df = pd.DataFrame(text_lines, columns=["Extracted Content"])
    df.to_excel(filename, index_label="Line Number")
    print(f"📊 Spreadsheet saved successfully: {filename}")

def start_text_detection(bucket_name, file_name):
    """Triggers the asynchronous Textract process."""
    textract = boto3.client('textract')
    response = textract.start_document_text_detection(
        DocumentLocation={'S3Object': {'Bucket': bucket_name, 'Name': file_name}}
    )
    return response['JobId']

def get_job_results(job_id):
    """Polls until the job is done and returns the raw results."""
    textract = boto3.client('textract')
    while True:
        response = textract.get_document_text_detection(JobId=job_id)
        status = response['JobStatus']
        
        if status == 'SUCCEEDED':
            return response
        if status == 'FAILED':
            return None
            
        print(f"⏳ Job status: {status}...")
        time.sleep(5)

def main():
    # 1. Config - Update these!
    BUCKET_NAME = 'your-s3-bucket-name'
    FILE_NAME = 'test_document.pdf'

    # 2. Upload
    upload_to_s3(FILE_NAME, BUCKET_NAME)

    # 3. Process
    job_id = start_text_detection(BUCKET_NAME, FILE_NAME)
    print(f"🚀 Started Textract Job ID: {job_id}")

    # 4. Retrieve, Print, and Save
    results = get_job_results(job_id)
    
    if results:
        # Create a clean list of all text lines
        extracted_lines = for block in results['Blocks'] if block['BlockType'] == 'LINE']
        
        print("\n--- Extracted Text ---")
        for line in extracted_lines:
            print(line)
            
        # Save to Excel
        save_to_excel(extracted_lines)
    else:
        print("❌ Extraction failed.")

if __name__ == '__main__':
    main()

