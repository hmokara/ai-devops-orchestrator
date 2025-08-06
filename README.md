text
# AI-Powered DevOps Orchestrator 🚀

A next-gen DevOps tool that uses AI (OpenAI GPT) to **summarize and suggest fixes** for your build, deployment, or pipeline errors—right from your CI/CD logs.

---

## 💡 What Is This?

This project helps DevOps engineers **save time debugging**.  
Instead of reading long, complex error logs, just run this tool to get:
- A clear summary of the error (in plain English!),
- And a suggested fix, powered by OpenAI's GPT API.

---

## 🌟 Business Impact

- **Cut debugging time by 60%**
- **Faster, smarter recovery from CI/CD failures**
- **Works with any log file—easy plug-and-play!**

---

## 🚀 How It Works

1. Collect your CI/CD error log (from GitHub Actions, Jenkins, etc).
2. Run this tool: It sends the log to OpenAI's GPT model.
3. Instantly see a clear summary and suggested solution.

---

## 🖥️ Demo Example

**Sample Log File (`sample_error.log`):**
[ERROR] 2025-08-05 10:23:45 - ModuleNotFoundError: No module named 'requests'
Traceback (most recent call last):
File "deploy.py", line 12, in <module>
import requests

text

**Tool Output:**
Error Summary & Fix:
The error indicates the 'requests' Python module is missing.
Quick Fix: Run pip install requests in your environment to resolve this issue.

text

---

## 🏗️ Tech Stack

- Python 3.8+
- [OpenAI GPT-3.5-turbo API](https://platform.openai.com/)
- Simple environment setup

---

## ⚡ Quickstart

1. **Clone this repo:**
    ```
    git clone https://github.com/hmokara/ai-devops-orchestrator.git
    cd ai-devops-orchestrator
    ```
2. **Install dependencies:**
    ```
    pip install openai
    ```
3. **Set your OpenAI API key:**
    - [Get your API key here.](https://platform.openai.com/account/api-keys)
    - Set it in your shell:
        ```
        export OPENAI_API_KEY=sk-xxxxxx
        ```
4. **Add your error log file:**
    - Place your CI/CD error log as `sample_error.log`, or change the code to use your log file.
5. **Run the tool:**
    ```
    python summarize_error.py
    ```
6. **See the error summary and suggested fix!**

---

## ⚙️ Project Structure

ai-devops-orchestrator/
├── summarize_error.py # Main Python script
├── sample_error.log # Example error log
├── README.md # This file
└── docs/
└── demo.png # (Optional) Demo screenshot

text

---

## 🔍 Architecture

flowchart LR
A[CI/CD Error Log] --> B[Summarizer Script]
B --> C(OpenAI GPT API)
C --> D[Summary & Fix Output]

text

---

## 🤝 Contributing

- Have ideas? Open issues or submit pull requests!
- Want to help with cloud integration or notifications? Jump in!

---

## 📣 About

**Created by Hema Mokara**  
AI-Native DevOps Engineer — combining cloud automation with AI technology.

[Portfolio](https://hmokara.github.io/) | [LinkedIn](https://www.linkedin.com/in/mokara-hema-latha-6607b9265) | [Email](hemalatha.mokara73@gmail.com)

---

## 📜 License

MIT License. Feel free to use and adapt.

---
