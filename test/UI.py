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

"""
import time
import threading
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout


def main():
    session = PromptSession()

    # Start a separate thread to print time every 3 seconds
    time_thread = threading.Thread(target=print_time_continuously)
    time_thread.daemon = True
    time_thread.start()

    with patch_stdout():
        while True:
            try:
                text = session.prompt('Enter your input: ')
                if text.lower() == 'exit':
                    print('Exiting...')
                    break
                else:
                    print_custom_message(text)
            except KeyboardInterrupt:
                print('KeyboardInterrupt: Press "exit" to quit.')


def print_time_continuously():
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'Current Time: {current_time}')
        time.sleep(1)


def print_custom_message(text):
    # Add your custom messages logic here
    if text.lower() == 'hello':
        print('Hello! How are you?')
    elif text.lower() == 'how are you?':
        print('I am just a computer program. I am always fine!')
    else:
        print('You said:', text)


if __name__ == '__main__':
    main()
"""

"""
import threading
import time
import time
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout
import sys
import time

from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter

print = print_formatted_text


def get_toolbar():
    return "Bottom toolbar: time=%r" % time.time()

def get_rprompt_text():
    return [
        ("", " "),
        ("underline", "<rprompt>"),
        ("", " "),
    ]

example_style = Style.from_dict(
    {
        # The 'rprompt' gets by default the 'rprompt' class. We can use this
        # for the styling.
        "rprompt": "bg:#ff0066 #ffffff",
    }
)


def print_found_urls(running):
    i = 0
    while running:
        i += 1
        print("i=%i" % i)
        time.sleep(1)


def main():
    # Print a counter every second in another thread.
    running = True

    print_thread = threading.Thread(target=print_found_urls, args=(True,))
    print_thread.daemon = True
    print_thread.start()
    history = InMemoryHistory()
    completer_commands = WordCompleter(['SWITCH', 'EXIT', 'SAVE', 'VIEW', 'SKIP', 'REGEX', 'HELP'])
    session = PromptSession(history=history, enable_history_search=True)

    while True:
        with patch_stdout():
            command = session.prompt(">", placeholder=HTML('<style color="#888888">(please type something)</style>'),
             rprompt=get_rprompt_text, bottom_toolbar=get_toolbar, refresh_interval=0.5, style=example_style, completer=completer_commands)
        print("> %s" % command)
        history.append_string(command)
        # execute_command()


if __name__ == "__main__":
    main()
"""


#!/usr/bin/env python
"""
Example of a radio list box dialog.
"""
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog


def main():
    result = radiolist_dialog(
        values=[
            ("red", "Red"),
            ("green", "Green"),
            ("blue", "Blue"),
            ("orange", "Orange"),
        ],
        title="Radiolist dialog example",
        text="Please select a color:",
    ).run()

    print(f"Result = {result}")

    # With HTML.
    result = radiolist_dialog(
        values=[
            ("red", HTML('<style bg="red" fg="white">Red</style>')),
            ("green", HTML('<style bg="green" fg="white">Green</style>')),
            ("blue", HTML('<style bg="blue" fg="white">Blue</style>')),
            ("orange", HTML('<style bg="orange" fg="white">Orange</style>')),
        ],
        title=HTML("Radiolist dialog example <reverse>with colors</reverse>"),
        text="Please select a color:",
    ).run()

    print(f"Result = {result}")


if __name__ == "__main__":
    main()