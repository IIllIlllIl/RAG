import os


def run_llm(prompt):
    cmd = "ollama run llama3 " + prompt
    os.system(cmd)



