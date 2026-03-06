---
name: data-pipeline
description: "Builds ETL pipelines for CSV, JSON, Parquet, or database sources. Describe your transformation in natural language; Nanobot generates a Python pipeline using pandas/polars, runs it, validates the output schema, and writes PIPELINE_REPORT.md. Use when you need to transform, clean, or migrate data between formats or systems. Works with local files or database connections (Postgres, SQLite, Supabase)."
---

# data-pipeline

Describe your data transformation. Nanobot writes the ETL pipeline, runs it, and validates output.

## Usage
```
@Nanobot data-pipeline --input users.csv --describe "parse signup_date as datetime UTC, normalize email to lowercase, remove rows with null revenue, output parquet"
@Nanobot data-pipeline --source postgres://localhost/prod --table orders --describe "deduplicate by order_id keeping latest, join with customers on customer_id, output CSV"
@Nanobot data-pipeline --input raw/*.json --describe "flatten nested items array, extract product_id and quantity, write to SQLite"
```

## What It Does

1. **Profile**: Samples the input to infer schema (column names, types, null percentages, cardinality)
2. **Plan**: Describes transformation steps and asks for confirmation on ambiguous decisions
3. **Generate**: Writes `pipeline_<input_name>.py` using pandas or polars (chosen by data size)
4. **Run**: Executes with progress tracking (tqdm)
5. **Validate**: Checks output schema, null rates, row counts against expectations
6. **Report**: Writes `PIPELINE_REPORT.md`

## Files Created
```
pipeline_<name>.py              # Standalone, reusable pipeline script
PIPELINE_REPORT.md              # Before/after schema, row counts, validation results
```

## Pipeline Selection Logic
- **pandas**: <10M rows, complex transformations, wide compatibility
- **polars**: >1M rows, performance-critical, columnar operations

## PIPELINE_REPORT.md Contents
- Input: schema, rows, file size
- Transformations applied
- Output: schema, rows, validation passed/failed
- Performance: rows/second, total duration

## Philosophy
Generated pipelines are self-contained Python scripts — you can run them independently of Nanobot, schedule them in cron, or commit them to version control. No lock-in.
