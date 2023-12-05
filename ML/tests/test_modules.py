import sys
sys.path.append("..") # Adds higher directory to python modules path.
print(sys.path)

from llamaviz.config import TextGenerationConfig, llm #TODO: fix relative import
from llamaviz.components import Manager

llamavista = Manager(text_gen=llm("huggingface"))

cars_data_url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"


def test_summarizer():
    textgen_config = TextGenerationConfig(n=1, temperature=0.5, use_cache=False, max_tokens=None)
    summary_no_enrich = llamavista.summarize(cars_data_url, summary_method="default")
    summary = llamavista.summarize(
        "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv",
        textgen_config=textgen_config, summary_method="llm")

    assert summary_no_enrich != summary
    assert "dataset_description" in summary and len(summary["dataset_description"]) > 0


def test_goals():
    textgen_config = TextGenerationConfig(n=1, temperature=0.5, use_cache=False, max_tokens=None)
    summary = llamavista.summarize(
        cars_data_url,
        textgen_config=textgen_config, summary_method="default")

    goals = llamavista.goals(summary, n=2, textgen_config=textgen_config)
    assert len(goals) == 2
    assert len(goals[0].question) > 0


def test_vizgen():
    textgen_config = TextGenerationConfig(
        n=1,
        temperature=0.1,
        use_cache=True,
        max_tokens=None)
    summary = llamavista.summarize(
        cars_data_url,
        textgen_config=textgen_config, summary_method="default")

    goals = llamavista.goals(summary, n=2, textgen_config=textgen_config)
    charts = llamavista.visualize(
        summary=summary,
        goal=goals[0],
        textgen_config=textgen_config,
        library="seaborn")

    assert len(charts) > 0
    assert len(charts[0].raster) > 0
    
    
if __name__ == "__main__":
    test_summarizer()
    print("passed summarizer")
    print("-"*20)
    test_goals()
    print("passed goals")
    print("-"*20)
    test_vizgen()
    print("passed vizgen")
    print("-"*20)