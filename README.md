# JARVIS - AI Assistant with Voice I/O

A JARVIS-like AI Assistant with voice input/output and sub-agent orchestration.

## Features

- 🎙️ **Voice I/O** - Speech-to-text and text-to-speech
- 🤖 **7 Specialized Sub-Agents** - Each handles specific tasks
- 🔀 **Automatic Routing** - Routes tasks to the right agent
- 📝 **Text & Voice modes** - Use whatever is convenient

## Sub-Agents

| Agent | Purpose | Keywords |
|-------|---------|----------|
| `assistant` | General queries, simple tasks | help, question |
| `investment` | Stocks, crypto, portfolio | invest, stock, crypto |
| `lifestyle` | Health, fitness, wellness | health, exercise |
| `software` | Coding, debugging, development | code, program, build |
| `marketing` | Marketing strategies, campaigns | marketing, social media |
| `scriptwriter` | Video scripts, narration | script, youtube |
| `video` | AI video creation | ai video, generate video |

## Installation

```bash
# Navigate to project
cd jarvis

# Install dependencies
uv sync

# Copy and configure environment
cp .env.example .env
# Edit .env with your API key
```

## Get API Key

Get your OpenHands API key from: https://openhands.dev

## Usage

```bash
# Run in text mode
uv run python -m jarvis.main

# Or set API key and run
export LLM_API_KEY="your-key"
uv run python -m jarvis.main
```

## Voice Mode

```python
from jarvis import JARVIS

jarvis = JARVIS(api_key="your-key")
jarvis.run_voice_loop()  # Requires microphone
```

## Example Session

```
JARVIS is ready. Type 'exit' to quit.

You: What's the best way to invest in crypto?
JARVIS: For crypto investment, I recommend starting with...

You: Help me write a youtube video script
JARVIS: I'd be happy to help with your YouTube script. What's the topic?

You: Write code to read a CSV file
JARVIS: Here's a simple Python solution...
```
