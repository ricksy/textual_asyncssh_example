import asyncio
import asyncssh
from textual.app import App
from textual.widgets import Button, Static

class MyApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(Static("Welcome to My SSH App!"), edge="top")
        await self.view.dock(Button("Click Me"), edge="left")

async def handle_client(process):
    app = MyApp()
    await app.run_async()

async def start_server():
    await asyncssh.create_server(handle_client, '', 2222)

asyncio.run(start_server())

