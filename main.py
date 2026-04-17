import os
import json
import csv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)

sample_folder = "sample-data"
csv_file = "transactions.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["merchant", "amount", "date"])

    if not file_exists:
        writer.writeheader()

    for filename in os.listdir(sample_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(sample_folder, filename)

            with open(file_path, "r") as email_file:
                email_text = email_file.read()

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"""
Extract the transaction details from this email.

Return ONLY valid JSON in this format:
{{
  "merchant": "",
  "amount": 0,
  "date": "YYYY-MM-DD"
}}

Email:
{email_text}
"""
            )

            output_text = response.output_text.strip()
            cleaned_output = output_text.replace("```json", "").replace("```", "").strip()
            data = json.loads(cleaned_output)

            writer.writerow(data)

            print(f"Processed {filename}: {data}")

print("\nSaved all transactions to transactions.csv")