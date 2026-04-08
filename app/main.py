import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    directory = os.path.dirname(destination)

    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    if os.path.exists(source):
        shutil.move(source, destination)
