"""JARVIS - AI Assistant with voice I/O and sub-agent orchestration

Quick Start:
    export LLM_API_KEY="your-api-key"
    python -m jarvis.core
    
Features:
    - Voice input/output (gTTS + SpeechRecognition)
    - 7 specialized sub-agents
    - Task routing and orchestration
    - Text and voice interaction modes
"""

from .core import JARVIS
from .voice import VoiceInput, VoiceOutput

__all__ = ["JARVIS", "VoiceInput", "VoiceOutput"]
__version__ = "0.1.0"