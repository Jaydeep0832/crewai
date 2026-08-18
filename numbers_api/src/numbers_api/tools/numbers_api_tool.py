from typing import Literal, Type

import httpx
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class NumbersAPIToolInput(BaseModel):
    """Input schema for NumbersAPITool."""
    number: int = Field(..., description="The number to get a fact about.")
    type: Literal["trivia", "math", "date", "year"] = Field(
        default="trivia",
        description="The type of fact to retrieve. Options are 'trivia', 'math', 'date', or 'year'."
    )

class NumbersAPITool(BaseTool):
    name: str = "This is a Numbers API tool"
    description: str = (
        "It takes a number and returns a fact about it based on the type of number (e.g., trivia, math, date, or year)."
    )
    args_schema: Type[BaseModel] = NumbersAPIToolInput

    def _run(self, number: int, type: Literal["trivia", "math", "date", "year"] = "trivia") -> str:
        url = f"https://numbersapi.com/{number}/{type}"
        try:
            response = httpx.get(url, timeout=10.0, follow_redirects=True)
            response.raise_for_status()
            return response.text.strip()
        except httpx.HTTPError as error:
            return f"Numbers API request failed: {error}"

