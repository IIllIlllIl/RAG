import os

prompts = []


def run_llm(prompt):
    cmd = "ollama run llama3 " + prompt
    os.system(cmd)


def template_init():
    prompts.append("What are the functions in $(cat {file})?")


def build_prompt(pid, file):
    return prompts[pid].format(file=file)


template_init()
print(build_prompt(0, "class"))
