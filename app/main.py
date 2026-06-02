from fastapi import FastAPI

app = FastAPI(title="AI Backend", version="1.0.0")

from .schemas import ChatRequest, ChatResponse


@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
    """헬스 체크 - Docker/k8s liveness 용도."""
    return {"status": "ok"}

@app.post("/echo", tags=["meta"])
def echo(req: ChatRequest) -> ChatResponse:             # -> ChatResponse - 이 타입으로 내보낼거야. 지정
    """Pydantic v2 검증 시연용 echo 엔드포인트."""
    return ChatResponse(answer=req.prompt, model="echo-1")


### ============== api 서버 만들기 완료. ==============
