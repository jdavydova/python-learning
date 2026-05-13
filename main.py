import requests

response = requests.get("https://gitlab.com/api/v4/users/juliada888/projects")
print(response.json())
print(type(response.json()))

my_project = response.json()

for project in my_project:
    print(f"Project Name {project['name']}\nProject URL {project['web_url']}")