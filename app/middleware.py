import time

from fastapi import Request
from starlette.middleware.base import RequestResponseEndpoint


async def add_process_time(request: Request, call_next: RequestResponseEndpoint):
    """요청 처리 시간을 측정하여 응답 헤더에 기록합니다."""
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{elapsed:.4f}"
    return response
