# LLM Evaluation & Observability Platform

A small evaluation API for comparing assistant outputs against expected answers. This project demonstrates evaluation-first AI engineering with a transparent baseline, not a production-grade semantic evaluator.

## Features
- Single and batch evaluation endpoints
- Token-overlap baseline score and configurable pass/fail threshold
- Latency and estimated-token reporting
- Golden examples can be supplied as request payloads
- Pytest tests and GitHub Actions CI

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```
Open http://127.0.0.1:8000/docs.

## Example
```json
{"question":"What is RAG?","expected":"retrieval augmented generation","answer":"RAG uses retrieval augmented generation","latency_ms":120,"input_tokens":30,"output_tokens":20}
```
Send this to `POST /evaluate`; use `POST /evaluate/batch` for a list of cases.

## Limitations / next steps
The score is lexical token overlap, not semantic similarity or an LLM judge. Token counts are estimates provided by the caller. There is no persistent run history, model-provider integration, or dashboard yet. Useful next steps are embedding-based metrics, judge calibration, regression gates, and stored evaluation runs.

## Stack
Python, FastAPI, Pydantic, pytest. Dependencies are free/open source.

## Explore more

- [AI Agent Evaluation Platform](https://github.com/HardikPaghdar/ai-agent-evaluation-platform) — recorded-run metrics and errors.
- [LLM Prompt Versioning Playground](https://github.com/HardikPaghdar/llm-prompt-versioning-playground) — immutable prompt versions.
- [LLM Security & Prompt Injection Testing Lab](https://github.com/HardikPaghdar/llm-security-prompt-injection-lab) — deterministic security regression cases.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
