from llamaviz.config.datamodel import TextGenerationConfig, TextGenerationResponse
from llamaviz.config.generators.text.base_textgen import TextGenerator
from ..scaffold import ChartScaffold
from llamaviz.datamodel import Goal, Summary


system_prompt = """
You are a helpful assistant highly skilled in modifying visualization code based on a summary of a dataset to follow instructions. Your modification should ONLY UPDATE the content of the plot(data) function/method. You MUST return a full program. DO NOT with NO backticks ```. DO NOT include any preamble text. Do not include explanations or prose.
"""


class VizEditor(object):
    """Generate visualizations from prompt"""

    def __init__(
        self,
    ) -> None:
        self.scaffold = ChartScaffold()

    def generate(
            self, code: str, summary: Summary, instructions: list[str],
            textgen_config: TextGenerationConfig, text_gen: TextGenerator, library='altair'):
        """Edit a code spec based on instructions"""

        instructions = [
            {"role": "system", "content": "modify the existing  code to " + i}
            for i in instructions]

        library_template, library_instructions = self.scaffold.get_template(Goal(
            index=0,
            question="",
            visualization="",
            rationale=""), library)
        # print("instructions", instructions)

        messages = [{"role": "system", "content": system_prompt}, {"role": "system", "content": f"The dataset summary is : {summary}"}, {"role": "system",
                                                                                                                                         "content": f"The code to be modified is: {code}.  You MUST use only the {library} library with the following instructions {library_instructions}. The resulting code MUST use the following template {library_template}"}]
        messages.extend(instructions)
        messages.append({"role": "user", "content": "The resulting code is: \n"})

        completions: TextGenerationResponse = text_gen.generate(
            messages=messages, config=textgen_config)
        return [x['content'] for x in completions.text]
