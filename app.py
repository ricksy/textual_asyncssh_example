import asyncssh
import asyncio

class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn):
        print('Connection made to SSH server.')

    def session_requested(self):
        return MySSHServerSession()

    def begin_auth(self, username):
        # Disable authentication
        return False

class MySSHServerSession(asyncssh.SSHServerSession):
    def shell_requested(self):
        return self

    def connection_made(self, chan):
        self._chan = chan
        self._chan.write('Hello, World\n')
        self._chan.close()

async def start_server():
    await asyncssh.create_server(
        MySSHServer, '', 8022,
        server_host_keys=['ssh_host_key']
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server())
loop.run_forever()

