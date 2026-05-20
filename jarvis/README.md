# JARVIS - AI Assistant with Voice I/O

A JARVIS-like AI Assistant with voice input/output and sub-agent orchestration.

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/sampreethD/Jarvis.git
cd Jarvis

# Install
uv sync

# Run web app
uv run python -m jarvis.web
# Open http://localhost:8000
```

## Features

- 🎙️ **Voice I/O** - Speech-to-text and text-to-speech
- 🤖 **7 Specialized Sub-Agents** - Each handles specific tasks
- 🔀 **Automatic Routing** - Routes tasks to the right agent
- 💬 **Web UI** - Real-time chat with WebSocket
- 🌐 **GitHub Pages** - Static demo deployed

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

## Get API Key

1. Get free key from: https://openhands.dev
2. Set as environment variable:
   ```bash
   export LLM_API_KEY="sk-oh-..."
   ```

Or create `.env` file:
```
LLM_API_KEY=your-api-key
LLM_MODEL=openai/gpt-4o
```

## Usage

### Web UI
```bash
uv run python -m jarvis.web
# Open http://localhost:8000
```

### Voice Mode (requires microphone)
```bash
uv run python -m jarvis.main
```

### Python API
```python
from jarvis import JARVIS

jarvis = JARVIS(api_key="your-key")
response = await jarvis.process("Hello!")
print(response)
```

## GitHub Pages Deployment

1. Merge PR to master
2. Go to Settings → Pages
3. Source: Deploy from a branch
4. Branch: `master`, folder: `/docs`
5. Add `LLM_API_KEY` secret in Actions settings

Your URL: `https://sampreethD.github.io/Jarvis/`

## Tech Stack

- **OpenHands SDK** - AI agent framework
- **FastAPI** - Web server
- **WebSocket** - Real-time chat
- **gTTS** - Text-to-speech
- **SpeechRecognition** - Voice input
- **uv** - Package manager

## License

MIT
