#!/usr/bin/env python
from os import environ
from pathlib import Path
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from sample_flow.crews.poem_crew.poem_crew import PoemCrew


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw
        
    

    @listen(generate_poem)
    def save_poem(self):
        output_dir = Path(environ.get("CREW_OUTPUT_DIR", ".crewai/output"))
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "poem.txt").write_text(self.state.poem, encoding="utf-8")


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
