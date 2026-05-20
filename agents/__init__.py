"""JARVIS sub-agents package"""

from .assistant import PersonalAssistantAgent
from .investment import InvestmentAgent
from .lifestyle import LifestyleAgent
from .marketing import MarketingAgent
from .scriptwriter import ScriptWriterAgent
from .software import SoftwareAgent
from .video import AIVideoAgent

__all__ = [
    "PersonalAssistantAgent",
    "InvestmentAgent",
    "LifestyleAgent",
    "MarketingAgent",
    "ScriptWriterAgent",
    "SoftwareAgent",
    "AIVideoAgent",
]