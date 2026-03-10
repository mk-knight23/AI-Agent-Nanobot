---
name: batch-processor
description: "Parallel processing of large datasets using Python asyncio + Claude AI transforms. Accepts CSV, JSON, Parquet, or JSONL as input. Splits into configurable chunk sizes, processes each chunk concurrently using Haiku (cost-efficient), aggregates results, and writes output. Includes progress tracking, error retry with exponential backoff, and cost estimation before run. Cross-ported from ZeroClaw's Rayon-based batch processor."
---

# batch-processor

Process thousands of records with Claude in parallel. Cost-efficient, resumable, observable.

## Usage
```
@Nanobot batch-processor --input data.csv --task "classify sentiment of the 'review' column"
@Nanobot batch-processor --input records.jsonl --task "extract company names" --output results.jsonl
@Nanobot batch-processor --input large.parquet --chunk-size 50 --concurrency 10 --estimate-cost
@Nanobot batch-processor --resume job_20240310_143022    # Resume an interrupted job
```

## Supported Formats

| Format | Input | Output |
|--------|-------|--------|
| CSV | ✓ | ✓ |
| JSON array | ✓ | ✓ |
| JSONL (newline-delimited) | ✓ | ✓ |
| Parquet | ✓ | ✓ |
| Text files | ✓ (line-by-line) | ✓ |

## Architecture

```python
# Internal execution model
async def run_batch(records, task, concurrency=5):
    semaphore = asyncio.Semaphore(concurrency)
    chunks = list(split(records, chunk_size=50))

    async def process_chunk(chunk):
        async with semaphore:
            return await claude_haiku(task, chunk)

    results = await asyncio.gather(*[process_chunk(c) for c in chunks])
    return aggregate(results)
```

## Cost Estimation
```
@Nanobot batch-processor --input data.csv --task "..." --estimate-cost

Estimated cost breakdown:
  Records: 10,000
  Avg tokens/record: 150 (input) + 50 (output)
  Model: claude-haiku-4-5
  Estimated cost: $0.42
  Estimated time: ~8 minutes at concurrency=10

Proceed? [y/N]
```

## Progress & Resumability
- Real-time progress bar via `rich`
- Checkpoint file written every 100 records
- `--resume <job_id>` skips already-processed records
- Failed records logged to `failed_records.jsonl` for retry

## Output
```
output/
├── results.jsonl           # Processed records (one JSON per line)
├── batch_summary.md        # Stats: total, succeeded, failed, cost, time
├── failed_records.jsonl    # Records that failed after retry
└── job_20240310_143022/    # Checkpoint files for resumability
```

## Philosophy
Large AI jobs should be affordable. Haiku handles the bulk processing at ~15x lower cost than Sonnet. Orchestrator (Sonnet) only aggregates and synthesizes at the end.
