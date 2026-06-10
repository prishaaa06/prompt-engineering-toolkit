# 🧠 Prompt Engineering Toolkit

A Python-based toolkit of **reusable, production-ready prompts** for marketing and content creation — with an interactive terminal runner.

Built by **Prisha Maheshwari** as a practical resource for AI-assisted content workflows.

---

## 📦 What's Inside

| Category | Prompts Included |
|---|---|
| 🎯 Social Media | Product Launch Caption, Engagement Booster, Instagram Story Script |
| 📧 Email Marketing | Subject Line Generator, Welcome Email |
| 📝 Content Strategy | Blog Post Outline, Content Repurposing Plan |
| 📣 Ad Copy | Google Ads Copy, Meta (Facebook/Instagram) Ad |
| 🤖 AI & Productivity | Custom System Prompt Designer, Prompt Chain Builder |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- No external libraries needed — runs on standard Python

### Run the toolkit
```bash
git clone https://github.com/YOUR_USERNAME/prompt-engineering-toolkit.git
cd prompt-engineering-toolkit
python run_prompt.py
```

---

## 🖥️ How It Works

1. **Choose a category** (Social Media, Email, Ad Copy, etc.)
2. **Select a prompt** from the list
3. **Fill in the variables** (brand name, tone, audience, etc.)
4. **Get your filled prompt** — ready to paste into ChatGPT, Claude, or Gemini
5. **Optionally save** the output to a local file

```
=======================================================
   🧠  Prompt Engineering Toolkit  by Prisha M.
=======================================================

📂 Available Categories:
   1. Ad Copy
   2. AI & Productivity
   3. Content Strategy
   4. Email Marketing
   5. Social Media

👉 Select a category number: 5

📝 Prompts in 'Social Media':
   1. [sm_caption_product] Product Launch Caption
        → Write an engaging Instagram/LinkedIn caption for a new product launch.
   ...
```

---

## 📁 Project Structure

```
prompt-engineering-toolkit/
│
├── run_prompt.py      # Interactive CLI runner
├── prompts.py         # Prompt library (add your own here!)
├── outputs/           # Saved prompts are stored here (auto-created)
└── README.md
```

---

## ➕ Adding Your Own Prompts

Open `prompts.py` and add a new entry to `PROMPT_LIBRARY`:

```python
"your_prompt_key": {
    "name": "Your Prompt Name",
    "category": "Your Category",
    "description": "What this prompt does.",
    "template": "Write a {tone} post about {topic} for {audience}.",
    "variables": ["tone", "topic", "audience"],
},
```

That's it — it will automatically appear in the menu.

---

## 💡 Use Cases

- Content creators building AI-assisted workflows
- Marketers who use ChatGPT/Claude/Gemini daily
- Anyone who wants organised, reusable prompts instead of rewriting from scratch

---

## 🛠️ Built With

- Python 3
- Prompt Engineering best practices
- Real-world marketing use cases

---

## 📬 Connect

**Prisha Maheshwari** — [LinkedIn](https://www.linkedin.com/in/prishamaheshwari-4724a7238/) · prishamaheshwari816@gmail.com
