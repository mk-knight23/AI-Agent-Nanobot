# Use Case: Personal Finance Monitor

Automatically track your expenses and get financial insights via Telegram.

## Goal
To have a 24/7 assistant that monitors bank notification emails/SMS, categorizes spending, and provides weekly budget reports.

## Setup

### 1. Enable Gmail/Email Access
Grant Nanobot read-only access to your financial notification folder using the `add-gmail` skill.

### 2. Configure Categories
Define your budget categories in `use-cases/personal-finance-monitor/budget.json`.
```json
{
  "Dining": 500,
  "Rent": 1500,
  "Utilities": 200,
  "Entertainment": 100
}
```

### 3. Activate Workflow
Enable the `finance-monitor` workflow in `config.json`.
```json
{
  "workflows": ["finance-monitor"],
  "finance_channel": "telegram/@my_private_finance_bot"
}
```

## How It Works
1. **Trigger**: New email arrival.
2. **Action**: Nanobot parses transaction amount and merchant.
3. **Analysis**: AI categorizes the merchant (e.g., "Starbucks" → "Dining").
4. **Storage**: Appends entry to a Supabase table or Notion database.
5. **Alert**: Sends a Telegram message if a category budget is exceeded.

## Benefits
- **Privacy**: Your financial data stays within your controlled Nanobot instance.
- **Natural Language**: Ask "How much did I spend on coffee this month?"
- **Low Cost**: Runs on a $10 board without expensive subscription fees.
