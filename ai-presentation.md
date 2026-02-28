# AI

## 7 Milestones of Agentic AI Evolution

- [Old AI agent milestones](https://medium.com/wonder-think/the-fascinating-history-of-agentic-artificial-intelligence-14c4f3c6b58e)

```
2022-Nov: ChatGPT Launch
          Conversational AI goes mainstream
|
2023-Mar: GPT-4 with Function Calling
          Agents can now interact with external tools and APIs
|
|
|
2023-Nov: Extended Context Windows (128k)
          Agents can maintain coherent plans across large codebases
|
|
2024-Jun: Claude 3.5 Sonnet
          Superior code generation with reasoning traces visible to users
|
|
2024-Nov: Model Context Protocol (MCP)
          Universal tool integration standard; Computer Use API enables autonomous control
|
|
2025-Jun: Test-Driven Agent Workflows
          Integration with linters, type checkers, tests for high-frequency feedback loops
|
2025-Sep: Claude Sonnet 4.5
          Multi-step autonomous "no-hands" coding, completing complex tasks without humans
```

The explosion in utility came from combining **tool access** + **extended context** + **test integration** + **autonomous execution**.

---

- [2025 State of AI-assisted software DORA report (PDF)](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)
- [Paper Jan 2026: AI negatively impacts skill formation](https://x.com/LuizaJarovsky/status/2026653994118984051)
- [Feb 2026 confluence youtube: Context engineering video (aka Prompt engineering is dead)](https://www.youtube.com/watch?v=Cs7QiSi8KLY&list=PLQmImZv_mq3TWN0UhoayCzmEYbWaTcdWu&index=16&t=21s)
- [Jan 2026 youtube: Study 150 Developers Using AI](https://www.youtube.com/watch?v=b9EbCb5A408&list=PLQmImZv_mq3TWN0UhoayCzmEYbWaTcdWu&index=16) which refers to this
- [Paper Jul 2026: Echoes of AI: Investigating the Downstream Effects of AI Assistants on Software Maintainability](https://arxiv.org/abs/2507.00788)
- [Jan 2026 blog: AI-Ready dev – Same Game, Different Dice](https://codemanship.wordpress.com/2026/01/05/the-ai-ready-software-developer-conclusion-same-game-different-dice/)
- [Claude's 5 Levels of AI Coding](https://www.youtube.com/watch?v=bDcgHzCBgmQ)
- [2025 MS study on 300.000 employees deploying *Copilot* on *Microsoft 365* (PDF)](https://www.microsoft.com/insidetrack/blog/uploads/prod/2024/04/10602-Copilot-Deployment_EBOOK.pdf)
- [Author your own LLM Agent from scratch](https://fly.io/blog/everyone-write-an-agent/)
  A simple agent (without tools):

  ```python
  from openai import OpenAI

  client = OpenAI()
  context = []

  def call():
      return client.responses.create(model="gpt-5", input=context)

  def process(line):
      context.append({"role": "user", "content": line})
      response = call()
      context.append({"role": "assistant", "content": response.output_text})
      return response.output_text
  ```

## High-frequency Testing & Feedback
![Claude 5 Levels of AI coding](Claude-5-Levels-of-AI-coding.png)evels-of-AI-coding.png)
AI increases the frequency of the code chunks authored.


- Test statically:
  - use compiler
  - python: use typings & rum [`ty`](https://github.com/astral-sh/ty) (instead of the slow `mypy`)
  - javascript: use TypeScript
  - Lint
- Test runtime:
  - run unit-tests & integration tests
  - Stealth schenarios

## Agents

- ![agent is an llm in a loop with tools](agent-is-an-llm-in-a-loop-with-tools.png)
- [2026 Jan Burke Holland: Level Up Your VS Code Productivity](https://www.youtube.com/watch?v=0XoXNG65rfg)

## Context-size matter, tokens to words

- [2025 Nov: Context rot undrepinings](https://www.understandingai.org/p/context-rot-the-emerging-challenge)
  - ![alt text](time-horizon-of-llm-tasks-vs-humans.png)umans.png)
  - [Paper Sep 2025: SepContext Is What You Need: The Maximum Effective Context Window for Real World Limits of LLMs](https://arxiv.org/abs/2509.21361)
  - [Paper Feb 2025: NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167)

- drift, Attention dilution, [“lost in the middle” effect in RAGs](https://medium.com/@cenghanbayram35/lost-in-the-middle-in-llms-86e461dc7212), or attention sink

- ![my context's sizings 1](my-ctxt-size-1.png), ![my context's sizings 2](my-ctxt-size-2.png), ![my context's sizings 3](my-ctxt-size-3.png)ze-3.png)

General Ratios (1 Token Equals):
- English Prose: ~0.75 words/token (or ~4 characters)
- Code (Python/JS): ~0.5 words / token (or ~2–3 tokens per word)
- Code (Python/JS): 3-10 token / LoC
Detailed Breakdown
- Prose (1,000 Tokens): Approximately 750 words.
- Code (1,000 Tokens): Approximately 500 words or fewer.
- Code (1,000 Tokens): Approximately 500 words or fewer.


## Skills

- [Skills in awesome-copilot](https://github.com/github/awesome-copilot)
- [2026 Feb Burke Holland: Skills tutorial](https://www.youtube.com/watch?v=fabAI1OKKww)

## Payment

- Developers of "popular" FOSS projects get [a free Copilot Pro subscription](https://github.com/orgs/community/discussions/165153)
- [models available to copilot plans](https://docs.github.com/en/copilot/reference/ai-models/supported-models#supported-ai-models-per-copilot-plan)
