# 🧠 Market Intelligence AI
**Market Intelligence AI** is a multi-agent AI system built using **CrewAI** that analyzes startup ideas and generates comprehensive market research reports — covering trends, competitors, target audience, and growth opportunities.

## Overview
Market Intelligence AI orchestrates a crew of specialized AI agents that collaboratively research and synthesize market data for any given startup idea. Each agent owns a distinct area of analysis, and their outputs are combined into a structured, actionable intelligence report — fully automated using CrewAI's sequential multi-agent workflow.

## Key Features
- Multi-agent system for end-to-end market research automation
- Dedicated agents for trends, competitors, target audience, and opportunities
- Structured report generation saved as `report.md`
- YAML-driven agent and task configuration for easy customization
- Knowledge base support for domain-specific grounding
- Built on CrewAI with UV for fast, reproducible dependency management

## Tech Stack
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/CrewAI-F55036?style=for-the-badge&logo=crewai&logoColor=white" alt="CrewAI"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI"/>
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"/>
  <img src="https://img.shields.io/badge/LiteLLM-000000?style=for-the-badge&logo=literalai&logoColor=white" alt="LiteLLM"/>
  <img src="https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white" alt="YAML"/>
</p>

## Installation

Install:
- **Git**: [Download](https://git-scm.com/download/win)
- **Python 3.10–3.13**: [Download](https://www.python.org/downloads/)
- **UV** (dependency manager):
  ```bash
  pip install uv
  ```

### Clone Repository
1. Open CLI.
2. Run:
   ```bash
   git clone https://github.com/KaustubhMestri/Market-Intelligence-AI
   cd Market-Intelligence-AI
   ```

### Install Dependencies
```bash
crewai install
```

### Set Up `.env`
Create a `.env` file in the root directory and add your API key:
```env
OPENAI_API_KEY=your_api_key_here
```

> Supports OpenAI or Groq (via LiteLLM). Replace the key accordingly.

### Run the Project
```bash
crewai run
```

The generated market intelligence report will be saved at:
```
report.md
```

## How It Works
1. User provides a startup idea as input
2. **Market Trends Agent** researches current industry trends and future outlook
3. **Competitor Analysis Agent** identifies key players, their strengths and weaknesses
4. **Target Audience Agent** defines the ideal customer segments and pain points
5. **Opportunities Agent** synthesizes findings and identifies growth opportunities
6. All agent outputs are compiled into a structured report saved to `report.md`

## Agent Configuration
Agents and tasks are defined via YAML files for easy customization:
- `src/market_intelligence_ai/config/agents.yaml` → Define agent roles, goals, and backstories
- `src/market_intelligence_ai/config/tasks.yaml` → Define tasks, expected outputs, and agent assignments
- `src/market_intelligence_ai/crew.py` → Core crew logic and tool integrations
- `src/market_intelligence_ai/main.py` → Entry point with input configuration
- `knowledge/` → Domain knowledge sources for agent grounding

## Contributing
1. Create an [issue](https://github.com/KaustubhMestri/Market-Intelligence-AI/issues).
2. Branch: `feature/<n>` or `bugfix/<n>`
   ```bash
   git checkout -b feature/<n>
   ```
3. Commit:
   ```bash
   git add .
   git commit -m "#<issue> message"
   ```
4. Push:
   ```bash
   git push origin feature/<n>
   ```
5. Submit PR to `main`.

## Resources
- CrewAI Docs: https://docs.crewai.com
- CrewAI GitHub: https://github.com/joaomdmoura/crewai

## License
MIT License. See [LICENSE](LICENSE).
