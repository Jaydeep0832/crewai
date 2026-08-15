from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    stream=False
)

researcher = Agent(
    role="AI Researcher",
    goal="Research and analyze information accurately.",
    backstory="You are an experienced AI researcher.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

research_task = Task(
    description="Explain what Generative AI is in simple terms.",
    expected_output="A clear explanation of Generative AI with its key concepts and applications.",
    agent=researcher,
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True,
)

result = crew.kickoff()

print("\nFINAL RESULT:")
print(result)