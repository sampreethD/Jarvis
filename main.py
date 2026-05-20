"""JARVIS CLI Entry Point"""

import asyncio
import os

import dotenv


async def main():
    """Main entry point for JARVIS"""
    # Load environment variables
    dotenv.load_dotenv()
    
    # Check for API key
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        print("Error: LLM_API_KEY is required.")
        print("Set it as environment variable or create a .env file with LLM_API_KEY=your-key")
        print("\nGet your API key from: https://openhands.dev")
        return
    
    from jarvis import JARVIS
    
    # Create JARVIS instance
    jarvis = JARVIS(api_key=api_key)
    
    # Run in text mode
    await jarvis.run_text_loop()


if __name__ == "__main__":
    asyncio.run(main())
