# LLM Evaluation Scripts

This repository contains a collection of **OpenEvals**- evaluator examples that you can plug into your experimentation pipeline. Each script focuses on a single evaluation dimension—​from basic correctness checks to RAG-specific and sandboxed code execution based evaluations.

| Filename | What it Evaluates | Method / Notes |
|----------|------------------|----------------|
| **`evaluating_conciseness.py`** | *Conciseness* – how concise the LLM answers the user’s question. | Uses `create_llm_as_judge` with a conciseness prompt. |
| **`evaluating_correctness.py`** | *Correctness* – compares the LLM output against a reference answer. | Uses `create_llm_as_judge` with a correctness prompt.|
| **`evaluating_hallucinations.py`** | *Hallucination* – detects unsupported claims in the LLM output. | Uses `create_llm_as_judge` with a hallucination prompt. |
| **`custom_evaluator_prompt.py`** | Demonstrates how to **inject a custom prompt** into `create_llm_as_judge`. | Uses `create_llm_as_judge`. Handy for domain-specific rubrics. |
| **`customizing_output_schema.py`** | Supplies a **custom pydantic output schema** to the evaluator. | Ensures structured, type-safe results. Uses `create_llm_as_judge` |
| **`evaluating_correctness_with_system_parameter.py`** | Adds an *additional system prompt* on top of the correctness prompt. | Good for extra evaluator context. Uses `create_llm_as_judge` |
| **`evaluating_correctness_custom_output_values_custom.py`** | Correctness with a **custom 0-to-1 score** instead of boolean. | Float score lets you weight partial credit. Uses `create_llm_as_judge` |
| **`evaluating_correctness_custom_output_values_choices.py`** | Correctness with a **pre-defined list of choices**. | E.g., `[0.0, 0.5,1.0]` Uses `create_llm_as_judge`|
| **`evaluate_structured_output_with_exact_match.py`** | *Exact-match* evaluation for structured outputs. | Uses `create_json_match_evaluator` |
| **`evaluate_structured_output_with_llm_as_judge.py`** | evaluates structured outputs by using llm as judge. | Uses `create_llm_as_judge` |
| **`rag_groundedness.py`** | RAG *Groundedness* – how well the answer aligns with retrieved context. | Uses `create_llm_as_judge` with groundedness prompt |
| **`rag_helpfulness.py`** | RAG *Helpfulness* – how well the answer addresses the original query. | Uses `create_llm_as_judge` with helpfulness prompt |
| **`rag_retrieval_relevance.py`** | RAG *Retrieval Relevance* – quality of the retrieved results for user query. | Uses `create_llm_as_judge` with retrieval_relevance prompt |
| **`code_pyright.py`** | Type-checks generated Python code with **Pyright**. | Static analysis, no execution. Uses `create_pyright_evaluator` |
| **`code_llm_as_judge.py`** | Uses an LLM to judge code quality / correctness. | Uses `create_code_llm_as_judge` |
| **`code_sandbox_pyright.py`** | Runs Pyright **inside an E2B sandbox** | Keeps your system safe from untrusted code. Uses `create_e2b_pyright_evaluator` |
| **`code_sandbox_execution.py`** | Fully **executes** generated code in an E2B sandbox. | Captures runtime errors and outputs. Uses `create_e2b_execution_evaluator` |


for detailed documentation, refer https://github.com/langchain-ai/openevals
