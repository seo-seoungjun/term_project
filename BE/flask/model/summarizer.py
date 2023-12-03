import io
import os
import time

import matplotlib.pyplot as plt
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('../env/.env')


class OpenAIManager:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))

    def submit_message(self, assistant_id, thread, user_message):
        self.client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=user_message
        )
        return self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
        )

    def get_response(self, thread):
        return self.client.beta.threads.messages.list(thread_id=thread.id, order="asc")

    def pretty_print(self, messages):
        print("# Messages")
        for m in messages:
            try:
                print(f"{m.role}: {m.content[0].text.value}")
            except:
                for content in m.content:
                    try:
                        print(content.text.value)
                    except:
                        image = self.client.files.with_raw_response.retrieve_content(content.image_file.file_id)
                        image_bytes = io.BytesIO(image.content)
                        img = Image.open(image_bytes)
                        plt.imshow(img)
                        plt.savefig(f'static/images/{content.image_file.file_id}.png')
                        plt.show()
        print()

    def wait_on_run(self, run, thread):
        print("Waiting for run to complete...")
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)

        print("Run completed!")
        return run

    def create_thread_and_run(self, assistant, prompt):
        thread = self.client.beta.threads.create()
        run = self.submit_message(assistant.id, thread, prompt)
        print("New thread created")
        return thread, run

    def run_assistant(self, thread, assistant):
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )
        run = self.wait_on_run(run, thread)

        messages = self.client.beta.threads.messages.list(
            thread_id=thread.id,
            order="asc",
        )
        return messages


if __name__ == "__main__":
    manager = OpenAIManager()
    assistant_id = os.getenv('ASSISTANT_ID')
    assistant = manager.client.beta.assistants.retrieve(assistant_id)
    prompt = "데이터를 시각화해줘"
    thread, run = manager.create_thread_and_run(assistant, prompt)
    run = manager.wait_on_run(run, thread)
    manager.pretty_print(manager.get_response(thread))
