"""from rich import print
from rich.panel import Panel
from rich.layout import Layout
from rich.prompt import Prompt

def rich_ui():
    while True:
        layout = Layout()
        layout.split_column(
            Layout(name="banner"),
            Layout(name="recipe"),
            Layout(name="search")
        )

        layout['banner'].update(Panel('Chocolate cheesecake', padding=1))
        layout['banner'].size = 5

        layout['recipe'].split_row(
            Layout(name="ingredients"),
            Layout(name="method")
        )

        layout['search'].update(Panel(Prompt.ask('> '), title='Search for a recipe'))
        layout['search'].size = 5
        print(layout)

if __name__ == '__main__':
    rich_ui()
"""
"""
import time

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn


def main():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        progress.add_task(description="Preparing...", total=None)
        time.sleep(5)
    print("Done!")


if __name__ == "__main__":
    typer.run(main)
"""


from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
import asyncio
import time


async def echo():
    while True:
        with patch_stdout():
            print(time.time())
            await asyncio.sleep(1)




async def read():
    session = PromptSession()

    while True:
        with patch_stdout():
            line = await session.prompt_async("> ")
            print(line)


loop = asyncio.get_event_loop()
loop.create_task(echo())
loop.create_task(read())
loop.run_forever()


"""
import time
from rich.progress import Progress
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel

console = Console()

# outer status bar and progress bar
status = console.status("Not started")

with Live(status):
    while True:
        print("ciaooo")
        status.update(f"[bold green]Status = TRY")
"""