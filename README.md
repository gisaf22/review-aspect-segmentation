# Review Aspect Segmentation

## What this repository achieves

This repository performs **sentence-level segmentation of customer reviews**, transforming review-level text into atomic semantic units.

Each sentence is treated as a standalone unit of meaning, providing a fast and reliable proxy for aspect-level analysis without performing full aspect extraction.

---

## Why this exists

Customer reviews frequently contain multiple aspects within a single document (for example: food quality, service speed, ambiance).

Modeling entire reviews as single documents leads to:

- Blended semantic representations
- Overlapping or dominant themes
- Poor lexical interpretability in topic modeling

Sentence-level segmentation enforces a cleaner semantic granularity that better aligns with how opinions are actually expressed.

---

## What this project does

- Splits free-form review text into sentences
- Produces one row per sentence
- Assigns stable sentence identifiers for traceability
- Preserves review-level linkage via `review_id`

This transformation is deterministic and irreversible, making it suitable as a foundational preprocessing step.

---

## What this project does not do

This repository intentionally does **not** perform:

- Clause-level splitting
- Aspect detection or labeling
- Sentiment classification
- Topic modeling or clustering
- Time-based aggregation or trend analysis

Those concerns are handled downstream by consumer pipelines.

---

## Input / Output contract

### Input

- `review_id`
- `review_text`

### Output

- `review_id`
- `sentence_id`
- `sentence_text`

Each row represents a single sentence derived from the original review.

---

## Design principles

- Granularity before intelligence
- Deterministic, testable transformations
- Clear input/output boundaries
- Reusable as a standalone NLP component

---

## Intended usage

This module is designed to be used as a preprocessing stage for downstream NLP tasks such as:

- Topic modeling
- Theme extraction
- Trend analysis
- Aspect-based sentiment analysis

By isolating sentence segmentation, downstream models operate on cleaner, more interpretable text units.

---

## Future extensions (explicitly deferred)

- Clause-level unitization
- Aspect-aware splitting
- Semantic validation of splits
