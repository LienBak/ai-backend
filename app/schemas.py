from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    """LangChain /chat 요청 본문.

    사용자 식별은 Spring 게이트웨이가 JWT로 처리하므로
    Python은 prompt만 받습니다. (Spring이 보내는 user_id 등 추가 필드는
    Pydantic이 기본 무시하므로 호환에 문제 없습니다.)
    """

    prompt: str = Field(..., min_length=1, max_length=2000, description="사용자 질문") # ... - 기본값이 없다는 것. 들어온 것 확인, description - 힌트

    model_config = {
        "json_schema_extra": {
            "example": {"prompt": "안녕하세요"}
        }
    }

class ChatResponse(BaseModel):
    """채팅 응답 본문."""

    answer: str = Field(..., description="모델 응답 본문")          # description - 설명
    model: str = Field(..., description="실제 사용된 모델 식별자")