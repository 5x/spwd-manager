from textwrap import wrap


def get_cropped_lines(value, length, delimiter="\n"):
    lines = value.split(delimiter)
    lines_cropped = (delimiter.join(wrap(i, length)) for i in lines)
    return delimiter.join(lines_cropped)
