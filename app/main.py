import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Backend", version="1.0.0")

from .errors import handle_unexpected
from .middleware import add_process_time
from .routers import chat_crew, chat_langchain
from .schemas import ChatRequest, ChatResponse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
)

# 미들웨어 — 등록 순서 역순으로 실행됩니다
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(add_process_time)

app.add_exception_handler(Exception, handle_unexpected)

@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
    """헬스 체크 - Docker/k8s liveness 용도."""
    return {"status": "ok"}

@app.post("/echo", tags=["meta"])
def echo(req: ChatRequest) -> ChatResponse:             # -> ChatResponse - 이 타입으로 내보낼거야. 지정
    """Pydantic v2 검증 시연용 echo 엔드포인트."""
    return ChatResponse(answer=req.prompt, model="echo-1")

app.include_router(chat_langchain.router)
app.include_router(chat_crew.router)

<<<<<<< HEAD
### ============== api 서버 만들기 완료 ==============
=======
### ============== api 서버 만들기 완료. ==============







# @app.post("/health", tags=["meta"])
# def health_write() -> dict[str, str]:
#     """헬스쓰기 체크 - Docker/k8s liveness 용도."""
#     return {"status": "write"}

# @app.put("/health", tags=["meta"])
# def update_health() -> dict[str, str]:
#     """헬스 업데이트 - Docker/k8s liveness 용도."""
#     return {"status": "update"}

# @app.delete("health", tags=["meta"])
# def delete_health() -> dict[str, str]:
#     """헬스 삭제 - Docker/k8s liveness 용도."""
#     return {"status": "delete"}