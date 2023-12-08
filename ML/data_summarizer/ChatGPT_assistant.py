import os
import io
import json
import time
from PIL import Image

import pandas as pd
import matplotlib.pyplot as plt

from openai import OpenAI
        
# client = OpenAI(api_key="YOUR_API_KEY")

def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")


# Pretty printing helper
def pretty_print(messages):
    print("# Messages")
    for m in messages:
        try :
            print(f"{m.role}: {m.content[0].text.value}")
        except:
            # print(m.content[0].image_file)
            # print(m.content[0].text.value)
            for content in m.content:
                try:
                    print(content.text.value)
                except:
                    image = client.files.with_raw_response.retrieve_content(content.image_file.file_id)
                    image_bytes = io.BytesIO(image.content)
                    img = Image.open(image_bytes)
                    plt.imshow(img)
                    plt.savefig(f'LlamaVista/ML/data_summarizer/results/visualize_test_{content.image_file.file_id}.png')
                    plt.show()
    print()


# Waiting in a loop
def wait_on_run(run, thread):
    print("Waiting for run to complete...")
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
        
    print("Run completed!")
    return run


def show_json(obj):
    return json.loads(obj.model_dump_json())

def _get_description(df) -> tuple:
    df.dropna(inplace=True)
    
    # info
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    
    # description
    describe_str = df.describe().to_string()

    # unique values
    unique_values = {}
    for col in df.columns:
        if df[col].dtype == 'object':
            if df[col].nunique() < 50:
                unique_values[col] = df[col].unique()

    unique_values_str = ''
    for col in unique_values:
        unique_values_str += f'{col}: {unique_values[col]}\n'
    
    return info_str, describe_str, unique_values_str
    
def get_assistant(client, file_path) -> tuple:
    # size limit
    file = client.files.create(
        file=open(file_path, "rb"),
        purpose='assistants'
    )
    file_id = 'file-YEzilQBW4smW9Duii9VAURSG'
    
    # df = pd.read_csv(file_path)
    # info, description, unique_values = _get_description(df)
    
    new_assistant = client.beta.assistants.create(
        name="CSV interpreter",
        instructions=f"데이터 파일의 형식을 CSV 파일로 제공할 것 입니다. 이 파일을 완전한 설명과 함께 해석해야 합니다. 데이터 처리나 유사한 주제에 대한 지식이 없는 사람이 이해할 수 있도록 노력하세요. 데이터를 설명할 때 몇 가지 시각화를 제시하도록 하세요. 매우 심도 깊은 설명을 제공하면 더 좋습니다. 계속 하는지 묻지 말고, 그냥 할 수 있는 만큼 계속 시각화하면 됩니다",
        tools=[{"type": "code_interpreter"}], # type: code_interpreter, retrieval, function
        model="gpt-4-1106-preview",
        file_ids=[file_id],
    )
    
    print("------new assistant-----")
    print(show_json(new_assistant))
    print()
    
    return new_assistant

def create_thread_and_run(client, assistant, prompt) -> object:
    # without size limit
    thread = client.beta.threads.create()
    run = submit_message(assistant.id, thread, prompt)
    print("------new thread-----")
    print(show_json(thread))
    print()
    return thread, run
    
def run_assistant(client, thread, assistant) -> object:
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    run = wait_on_run(run, thread)
                
    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
        order="asc",
        # after=message.id, # get messages after this message
    )
    return messages
    
if __name__=="__main__":
    client = OpenAI()
    
    # pre-defined assistant
    assistant_id = "asst_JFL5Myn9IWvEIBchIQVojFpo"
    assistant = client.beta.assistants.retrieve(assistant_id)
    # assistant = get_assistant(client, file_path="./ML/data_summarizer/cars.csv")

    prompt = "데이터를 시각화해줘"
    thread, run = create_thread_and_run(client, assistant, prompt)
    run = wait_on_run(run, thread)
    pretty_print(get_response(thread))
    
    # ctrl + c 나오기전 까지 추가로 질문
    while():
        prompt = input("extra input prompt: ")
        run = submit_message(assistant.id, thread, prompt)
        run = wait_on_run(run, thread)
        pretty_print(get_response(thread))