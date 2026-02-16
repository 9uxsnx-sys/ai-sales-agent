import pytest
from tests import test_config
from tests.fixtures import tshirt_product
from app.state_manager import clear_session
from logic.conversation_engine import handle_message

@pytest.mark.asyncio
async def test_conversation_flow(db_session):
    user_id = "test_user_001"
    await clear_session(user_id)
    
    response = await handle_message(user_id, "Hello!", "whatsapp", db_session)
    assert "hello" in response.lower() or "help" in response.lower()
    
    await clear_session(user_id)
    
    response = await handle_message(user_id, "I want to buy a t-shirt", "whatsapp", db_session)
    assert "buyer" in response.lower() or "type" in response.lower()
    
    response = await handle_message(user_id, "I'm a retailer", "whatsapp", db_session)
    assert "how many" in response.lower() or "quantity" in response.lower()
    
    response = await handle_message(user_id, "I want 2", "whatsapp", db_session)
    assert "order" in response.lower() or "confirm" in response.lower()
    
    await clear_session(user_id)
