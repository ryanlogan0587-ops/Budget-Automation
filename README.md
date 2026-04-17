# Budget Automation (AI-Powered Email Parser)

This project is an AI-powered system that extracts, categorizes, and organizes financial transaction data from email alerts.

It converts unstructured email text into structured data that can be used for budgeting, tracking, and analysis.

---

## Features

* Extracts merchant, amount, and date from transaction emails
* Classifies transactions into real budgeting categories (Gasto, Factura, etc.)
* Processes multiple emails automatically
* Converts unstructured text into structured JSON
* Saves results into a CSV file for tracking and analysis

---

## How It Works

1. Email text is loaded from input files
2. The text is sent to the OpenAI API
3. AI extracts structured transaction data
4. The response is cleaned and parsed into JSON
5. Transactions are categorized based on a predefined budget system
6. Results are saved into a CSV file

---

## Example

### Input

```
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
* CSV (data storage)
* Make.com (automation layer)

---

## Project Purpose

This project demonstrates how AI can be used to transform unstructured financial data into structured, actionable information.

It is part of a larger system that combines automation tools and custom logic to streamline personal finance tracking.

---

## Current Status

Working prototype:

* AI extraction and categorization implemented
* Multi-email processing supported
* Data export to CSV completed

---

## Future Improvements

* Connect directly to Gmail API for real-time processing
* Integrate with automation workflows (Make.com)
* Add spending summaries by category
* Improve categorization accuracy with hybrid rules + AI
* Build a dashboard for financial insights

---
