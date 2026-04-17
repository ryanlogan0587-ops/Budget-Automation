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

with open("sample-data/example-email.txt", "r") as file:
    email_text = file.read()

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

print("AI output:")
print(output_text)

cleaned_output = output_text.replace("```json", "").replace("```", "").strip()
data = json.loads(cleaned_output)

csv_file = "transactions.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["merchant", "amount", "date"])
    if not file_exists:
        writer.writeheader()
    writer.writerow(data)

print("\nSaved to transactions.csv")