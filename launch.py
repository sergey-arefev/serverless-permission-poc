import os
import subprocess
from types import SimpleNamespace
from aiohttp import web

from utils import TempFileManager

AGENT_PORT = os.getenv("PORT")
TESTS_PATH = "/home/student"


async def run(request: web.Request) -> web.Response:
    body = await request.json()
    files = [SimpleNamespace(name=f["name"], content=f["content"]) for f in body["files"]]

    # Сохраняем файлы для запуска
    with TempFileManager(directory=TESTS_PATH, files=files):
        proc = subprocess.run(
            (
                f"cd {TESTS_PATH} && chown -R student {TESTS_PATH} "
                f"&& su - student -c \"{body['command']}\""
            ),
            capture_output=True,
            shell=True,
        )

    return web.json_response({
        "stdout": proc.stdout.decode(),
        "stderr": proc.stderr.decode(),
    })


def setup_routes(app: web.Application) -> None:
    app.router.add_post("/run/", run)


# Fix file permission
# os.system("chmod a=rx /data && chmod a=r /data/*")

app = web.Application()
setup_routes(app)

web.run_app(
    app,
    host="0.0.0.0",
    port=AGENT_PORT,
)
