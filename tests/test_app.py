from app import EvaluationInput, evaluate

def test_overlap_and_pass():
    result = evaluate(EvaluationInput(question="q", expected="retrieval augmented generation", answer="RAG means retrieval augmented generation", latency_ms=12, input_tokens=5, output_tokens=8))
    assert result["passed"] is True
    assert result["estimated_tokens"] == 13

def test_unrelated_answer_fails():
    assert evaluate(EvaluationInput(question="q", expected="verify claims", answer="hello world"))["passed"] is False
