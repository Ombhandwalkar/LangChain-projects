# Intro to Prompt Engineering

**Project overview**

This repository is a hands-on collection of Jupyter notebooks that teach prompt engineering concepts, patterns, and best practices for working with modern LLMs. The materials are organized as modular notebooks (tutorials, examples, exercises). This README provides a recommended study sequence, file structure guidance, and notes about duplicates and renaming.

---

## Recommended learning sequence 

1. `01-intro_to_prompt_engineering.ipynb` — Overview, objectives, and background.
2. `02-basic-prompt-structure.ipynb` — Basic anatomy of a prompt: instructions, context, examples.
3. `03-prompt-formatting-structure.ipynb` — Formatting techniques, templates, and variables.
4. `04-zero-shot-prompting.ipynb` — Zero-shot approaches and when to use them.
5. `05-few-shot-prompting.ipynb` — Few-shot patterns and example selection.
6. `06-transformers_few_shot.ipynb` — Applying few-shot ideas with transformer models.
7. `07-prompt-templates-variables.ipynb` — Template design and variable injection strategies.
8. `08-role_prompting.ipynb` — Role-play prompts and persona conditioning.
9. `09-Task_Decomposition_task.ipynb` — How to break complex tasks into smaller prompts.
10. `10-prompt_chaining_sequencing.ipynb` — Chaining prompts, pipelines, and orchestration.
11. `11-constrain_guided_generation.ipynb` — Constraining outputs and guided generation.
12. `12-specific-task-prompts.ipynb` — Prompts tailored for common tasks (summaries, QA, code, etc.).
13. `13-Negative_Prompting.ipynb` — Negative prompting (what *not* to do) and adversarial cases.
14. `14-prompt_otimization_technique.ipynb` — Optimization techniques and automated tuning.
15. `15-Prompt_Length_and_Complexity_Management.ipynb` — Managing prompt length and complexity tradeoffs.
16. `16-Self_Consistency_check.ipynb` — Self-consistency, sampling strategies, and aggregation.
17. `17-Chain_of_Thoughts_Prompting.ipynb` — Chain-of-thought prompting and stepwise reasoning.
18. `18-Evaluating_prompt.ipynb` — Evaluation metrics and testing prompts.
19. `19-Prompt_Security_and_Safety.ipynb` — Safety, prompt injections, and guardrails.
20. `20-Ethical_Prompt.ipynb` — Ethics, bias, and responsible prompting.
21. `21-Ambiguity_clarity.ipynb` — Handling ambiguity and clarifying questions.
22. `22-Multilingual_Prompting.ipynb` — Working with multiple languages and localization.
23. `23-Instruction_Engineering.ipynb` — Instruction engineering patterns for consistent behavior.

---

## How to run the notebooks locally

1. Create a Python virtual environment (recommended Python 3.8+):

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\.venv\Scripts\activate  # Windows
pip install -U pip
pip install jupyterlab ipykernel numpy pandas transformers
```

2. Start Jupyter Lab or Notebook:

```bash
jupyter lab
```

3. Open notebooks in the order above.

> If your notebooks require API keys (OpenAI, Hugging Face), do **not** hardcode keys in the notebooks. Use environment variables or a `.env` file and a loader (e.g., python-dotenv).

---


