import crewai.llms.cache


_original_mark_cache_breakpoint = crewai.llms.cache.mark_cache_breakpoint


def mark_cache_breakpoint(message):
    # Groq does not support CrewAI's cache_breakpoint message field.
    return message


crewai.llms.cache.mark_cache_breakpoint = mark_cache_breakpoint