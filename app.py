from fastapi import FastAPI
from pydantic import BaseModel, Field
from statistics import mean
from time import perf_counter

app = FastAPI(title="LLM Evaluation & Observability Platform", version="0.1.0")

GOLDEN = [
    {"id":"qa-1","question":"What is RAG?","expected":"retrieval augmented generation"},
    {"id":"qa-2","question":"Why cite sources?","expected":"verify claims"},
]

class EvaluationInput(BaseModel):
    question: str
    expected: str
    answer: str
    latency_ms: float = Field(default=0, ge=0)
    input_tokens: int = Field(default=0, ge=0)
    output_tokens: int = Field(default=0, ge=0)

def evaluate(item: EvaluationInput) -> dict:
    expected = set(item.expected.lower().split())
    answer = set(item.answer.lower().split())
    overlap = len(expected & answer) / max(1, len(expected))
    return {"question": item.question, "overlap_score": round(overlap, 3),
            "passed": overlap >= 0.5, "latency_ms": item.latency_ms,
            "estimated_tokens": item.input_tokens + item.output_tokens}

@app.get("/health")
def health(): return {"status":"ok"}

@app.get("/golden-dataset")
def golden_dataset(): return {"items": GOLDEN, "count": len(GOLDEN)}

@app.post("/evaluate")
def run_evaluation(item: EvaluationInput): return evaluate(item)

@app.post("/evaluate/batch")
def batch(items: list[EvaluationInput]):
    results = [evaluate(item) for item in items]
    return {"results": results, "count": len(results),
            "pass_rate": round(mean([r["passed"] for r in results]), 3) if results else 0,
            "avg_latency_ms": round(mean([r["latency_ms"] for r in results]), 2) if results else 0,
            "total_estimated_tokens": sum(r["estimated_tokens"] for r in results)}
