import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks/4"

def create_task(summary, description):
    task = {
        "summary": summary,
        "description": description
    }
    response = requests.post(BACKEND_URL, json=task)
    if response.status_code == 201:
        print("Creation succeeded")
    else:
        print("Creation failed")
        
def update_task(summary, description, is_done):
    task = {
        "summary": summary,
        "description": description,
        "is_done": is_done 
    }
    response = requests.put(BACKEND_URL, json=task)
    if response.status_code == 204:
        print("Creation succeeded")
    else:
        print("Creation failed")     
        
from pick import pick

if __name__ == "__main__":
    # print("Fill out the prompts below to create a new task:")
    # summary = input("New task summary: ")
    # description = input("New task description: ")
    # create_task(summary, description)
    print("Fill out the prompts below to create a new task:")
    summary = input("New task summary: ")
    description = input("New task description: ")
    title = 'New task status: '
    options = ['Not done', 'Done']
    is_done, index = pick(options, title, indicator='->')
    print(is_done)
    update_task(summary, description, index)