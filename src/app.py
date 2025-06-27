import shutil, uuid, os
from fastapi import FastAPI, Form, WebSocketDisconnect, WebSocket
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import asyncio


app = FastAPI(title="spotGrab")
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
cleanupInterval = int(os.getenv("FILE_CLEANUP_INTERVAL"))
cleanupMaxAge = int(os.getenv("FILE_CLEANUP_MAX_AGE"))


async def download_cleanup():
    while True:
        downloadPath = os.path.join(os.path.dirname(os.getcwd()), "public_downloads")
        for folder in os.listdir(downloadPath):
            folderPath = os.path.join(downloadPath, folder)
            if os.path.isdir(folderPath):
                folderStat = os.stat(folderPath)
                if folderStat.st_mtime > cleanupMaxAge:
                    shutil.rmtree(folderPath)
        await asyncio.sleep(cleanupInterval)


@app.websocket("/ws/downloads/{id}")
async def song_dl(id: str, websocket: WebSocket):
    await websocket.accept()
    musicPath = os.path.join(os.path.dirname(os.getcwd()), "music", id)
    downloadPath = os.path.join(os.path.dirname(os.getcwd()), "public_downloads", id)

    url = await websocket.receive_text()
    process = await asyncio.create_subprocess_exec(
        "spotdl",
        url,
        "--client-id",
        client_id,
        "--client-secret",
        client_secret,
        "--output",
        f"../music/{id}",
        stdout=asyncio.subprocess.PIPE,
    )

    async def read_stdout():
        while True:
            line = await process.stdout.readline()
            if not line:
                break
            await websocket.send_text(line.decode().strip())

    stdout_task = asyncio.create_task(read_stdout())
    process_task = asyncio.create_task(process.wait())

    try:
        await asyncio.gather(stdout_task, process_task)
    except Exception:
        stdout_task.cancel()
        process_task.cancel()

        if process and process.returncode is None:
            process.terminate()
            try:
                await asyncio.wait_for(process.wait(), timeout=10)
            except asyncio.TimeoutError:
                process.kill()
        if os.path.exists(musicPath):
            shutil.rmtree(musicPath)
        if os.path.exists(downloadPath):
            shutil.rmtree(downloadPath)
        return

    shutil.make_archive(os.path.join(downloadPath, "songs"), "zip", musicPath)
    shutil.rmtree(musicPath)

    await websocket.send_json(
        {
            "message": "Download successful via spotGrab!",
            "url":  f"/public_downloads/{id}/songs.zip"
        }
    )


app.mount(
    "/public_downloads",
    StaticFiles(directory="../public_downloads"),
    name="public_downloads",
)


@app.get("/api/download")
async def download():
    id = str(uuid.uuid4())
    return {"message": "WebSocket open for spotGrab", "id": id}


@app.on_event("startup")
async def start_cleanup_task():
    asyncio.create_task(download_cleanup())


app.mount("/", StaticFiles(directory="src", html=True), name="homepage")
