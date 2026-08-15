import crewai.llms.cache

# CrewAI 1.15.16 adds cache_breakpoint to messages.
# Groq rejects this field.
def no_cache_breakpoint(message):
    return message

crewai.llms.cache.mark_cache_breakpoint = no_cache_breakpoint


# Now import your generated crew.
from basic_crewai.crew import BasicCrewaiCrew

crew = BasicCrewaiCrew()
result = crew.crew().kickoff()

print("\n\nFINAL RESULT:\n")
print(result)