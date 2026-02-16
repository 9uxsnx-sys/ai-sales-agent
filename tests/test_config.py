"""
Mock LLM service for testing without API calls.
"""
import sys
import types

async def mock_generate_response(message: str, system_instruction: str = None) -> str:
    message_lower = message.lower()
    instruction_lower = system_instruction.lower() if system_instruction else ""
    
    if "intent" in instruction_lower:
        if any(word in message_lower for word in ["hello", "hi"]):
            return "OTHER"
        elif "buy" in message_lower or "order" in message_lower:
            return "NEW_ORDER"
        elif "status" in message_lower:
            return "CHECK_ORDER"
        return "OTHER"
    
    if "extract" in instruction_lower:
        import json
        return json.dumps({"product": None, "quantity": None, "customer_type": None})
    
    if "goal" in instruction_lower:
        if "greeting" in instruction_lower:
            return "Hello! How can I help you?"
        elif "ask_product" in instruction_lower:
            return "What product are you interested in?"
        return "I'm here to help!"
    
    return "OK"

mock_llm_module = types.ModuleType("services.llm_service")
mock_llm_module.generate_response = mock_generate_response
sys.modules["services.llm_service"] = mock_llm_module
