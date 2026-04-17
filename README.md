# Budget Automation (AI-Powered Email Parser)

This project is an AI-powered system that extracts and categorizes financial transaction data from email alerts and prepares it for use in an existing budgeting workflow.

It is designed to turn unstructured transaction emails into structured data that can be mapped into a real budget sheet, reducing manual entry and improving financial organization.

---

## Features

* Extracts merchant, amount, and date from transaction emails
* Classifies transactions into budget-specific sections and categories
* Processes multiple email inputs automatically
* Converts unstructured email text into structured JSON
* Exports cleaned transaction data for integration into an existing budget sheet

---

## How It Works

1. Transaction email text is loaded from input files
2. The text is sent to the OpenAI API
3. AI extracts the key transaction details
4. The response is cleaned and parsed into structured JSON
5. Transactions are mapped into predefined budget sections and categories
6. The processed data is exported in a format that can be used in a connected budgeting system

---

## Example

### Input

```text
Bank of America Alert:
You spent $23.75 at Chipotle on April 14 using your debit card.
```

### Output

```json
{
  "merchant": "Chipotle",
  "amount": 23.75,
  "date": "2024-04-14",
  "section": "Gasto",
  "category": "Comida/Bebida"
}
```

---

## Tech Stack

* Python
* OpenAI API
* python-dotenv
* CSV export for structured output
* Make.com for workflow automation
* Existing custom budget sheet for final organization and tracking

---

## Project Purpose

This project was built to support a real budgeting system by automating one of the most repetitive parts of personal finance tracking: extracting and classifying transaction data from email alerts.

Rather than replacing the budget sheet, it works alongside it by preparing transaction data so it can be integrated into an already established budgeting structure.

---

## Current Status

Working prototype:

* AI extraction implemented
* Budget category mapping implemented
* Multi-email processing supported
* Structured export completed
* Designed to connect into an existing budget sheet workflow

---

## Future Improvements

* Connect directly to real email inbox data
* Integrate more tightly with the budget sheet
* Improve category accuracy with hybrid AI + rule-based logic
* Add summaries by category and section
* Expand support for more transaction formats and merchants
