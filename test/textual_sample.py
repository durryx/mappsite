import time

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.widgets import Tree
from textual.widgets import Header, Footer
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from time import monotonic
import os
from textual.app import App, ComposeResult
from textual import events
from textual.widgets import TextLog, ProgressBar
from textual.binding import Binding
from textual.widgets import Label
from textual.timer import Timer

website = f"google.com/ciao/"


class AlternativeHeader(Static):
    """A widget to display elapsed time."""

    start_time = reactive(monotonic)
    time = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.set_interval(1 / 60, self.update_time)

    def update_time(self) -> None:
        """Method to update the time to the current time."""
        self.time = monotonic() - self.start_time

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        padding = os.get_terminal_size().columns - len(website) - 24
        line = f"target website: {website: <{padding}} TT:{hours:02,.0f} h :{minutes:02.0f} min :{seconds:04.1f} s"
        self.update(line)

    def start(self) -> None:
        """Method to start (or resume) time updating."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self):
        """Method to stop the time display updating."""
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total


class TreeApp(Static):
    def compose(self) -> ComposeResult:
        tree: Tree[dict] = Tree("Dune")
        tree.root.expand()
        characters = tree.root.add("Characters", expand=True)
        characters.add_leaf("Paul")
        characters.add_leaf("Jessica")
        characters.add_leaf("Chani")
        yield tree


class VerticalLayoutExample(App):
    CSS_PATH = "vertical_layout.css"


    progress_timer: Timer

    BINDINGS = [
        Binding(key="shift+s", action="save()", description="Save"),
        Binding(key="e", action="expand_tree()", description="View website"),
        Binding(key="k", action="performance_window()", description="Performance"),
        Binding(key="p", action="pause_scan()", description="Pause"),
        Binding(key="t", action="continue_scan()", description="Continue"),
        Binding(key="s", action="shutdown()", description="Shutdown"),
    ]

    def action_shutdown(self) -> None:
        pass

    def action_continue_scan(self) -> None:
        pass

    def action_performance_window(self) -> None:
        pass

    def action_expand_tree(self) -> None:
        pass

    def action_save(self) -> None:
        pass

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        yield AlternativeHeader()
        yield TreeApp()
        yield TextLog(highlight=True, markup=True)
        # rich status spinner -- feature will be added to textual
        with Horizontal(classes="alternative_footer"):
            yield Label("active mode bla bla  ", classes="box")
            yield ProgressBar()
        yield Footer()

    def on_mount(self) -> None:
        """Set up a timer to simulate progess happening."""
        self.progress_timer = self.set_interval(1 / 10, self.make_progress, pause=True)

        text_log = self.query_one(TextLog)
        text_log.border_title = "last found links"

    def make_progress(self) -> None:
        """Called automatically to advance the progress bar."""
        self.query_one(ProgressBar).advance(1)

    def action_start(self) -> None:
        """Start the progress tracking."""
        self.query_one(ProgressBar).update(total=100)
        self.progress_timer.resume()

    def on_ready(self) -> None:
        """Called  when the DOM is ready."""

        text_log = self.query_one(TextLog)
        text_log.write("[bold magenta]Write text or any Rich renderable!")
        # for _ in range(20):
        #    time.sleep(1)
        #    text_log.write("[bold magenta]Write text or any Rich renderable!")

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        text_log = self.query_one(TextLog)
        text_log.write(event)


if __name__ == "__main__":
    app = VerticalLayoutExample()
    app.run()
