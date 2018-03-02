import json

from discord.ext import commands


def fetchFromDisk(filename):
    try:
        with open(f"{filename}.json") as file:
            return json.load(file)
    except FileNotFoundError:
        return dict()


def saveToDisk(filename, dict):
    with open(f"{filename}.json") as file:
        json.dump(dict, file, indent=4, skipkeys=True, sort_keys=True)


def convertToSeconds(value: int, type: str):
    type = type.lower()
    if type[-1:] == 's': # plural -> singular
        type = type[:-1]
    if type == 'w' or type == 'week':
        value = value * 7
        type = 'd'
    if type == 'd' or type == 'day':
        value = value * 24
        type = 'h'
    if type == 'h' or type == 'hour':
        value = value * 60
        type = 'm'
    if type == 'm' or type == 'minute':
        value = value * 60
        type = 's'
    if type != 's' and type != 'second':
        raise commands.BadArgument(f"Invalid duration: `{type}`\nValid identifiers: week(s), day(s), hour(s), minute(s), second(s)")
    else:
        return value

