from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

# ✅ Keep only stable tools
web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()

toolkit = [web_search_tool, web_scraping_tool]

@CrewBase
class MarketIntelligenceAi():
    """Market Intelligence AI crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ---------------- AGENTS ---------------- #

    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_specialist"],
            tools=toolkit
        )

    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitive_intelligence_analyst"],
            tools=toolkit
        )

    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["customer_insights_researcher"],
            tools=toolkit
        )

    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["product_strategy_advisor"],
            tools=toolkit
        )

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["business_analyst"],
            tools=toolkit
        )

    # ---------------- TASKS ---------------- #

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"]
        )

    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitive_intelligence_task"],
            context=[self.market_research_task()]
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config["customer_insights_task"],
            context=[
                self.market_research_task(),
                self.competitive_intelligence_task()
            ]
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["product_strategy_task"],
            context=[
                self.market_research_task(),
                self.competitive_intelligence_task(),
                self.customer_insights_task()
            ]
        )

    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_analyst_task"],
            context=[
                self.market_research_task(),
                self.competitive_intelligence_task(),
                self.customer_insights_task(),
                self.product_strategy_task()
            ]
        )

    # ---------------- CREW ---------------- #

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True   # 👈 add this for debugging
        )