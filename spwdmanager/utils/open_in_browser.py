import webbrowser


def open_in_browser(url, exception=False):
    if url:
        webbrowser.open(url, new=0, autoraise=True)
    elif exception:
        raise ValueError("URL not specified.")
