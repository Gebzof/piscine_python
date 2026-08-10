import os
import time

def format_time(seconds: float) -> str:
    """function format_time:
    Format seconds as MM:SS, always fixed width."""
    seconds = max(0, int(seconds))
    minutes, secs = divmod(seconds, 60)
    return f"{minutes:02d}:{secs:02d}"


def ft_tqdm(lst: range) -> None:
    """
    function ft_tqdm:
    Creates a progress bar like tqdm with the yield operator
    """
    total = len(lst)
    start = time.time()
    n_width = len(str(total))

    last_line_len = 0

    for i, item in enumerate(lst):
        yield item
        n = i + 1
        frac = n / total
        elapsed = time.time() - start
        if elapsed > 0:
            rate = n / elapsed
        else:
            rate = 0
        if rate > 0:
            eta = (total - n) / rate
        else:
            eta = 0

        try:
            term_width = os.get_terminal_size().columns
        except OSError:
            term_width = 80

        suffix = (f"| {n:>{n_width}}/{total} " f"[{format_time(elapsed)}<{format_time(eta)}, {rate:6.2f}it/s]")
        prefix = f"{frac * 100:3.0f}%|"

        width = max(10, term_width - len(prefix) - len(suffix) - 1)
        filled = int(width * frac)
        bar = "=" * filled + " " * (width - filled)

        line = f"{prefix}{bar}{suffix}"
        pad = max(0, last_line_len - len(line))
        if n == total:
            end = "\n"
        else:
            end = ""
        print(f"\r{line}{' ' * pad}", end=end, flush=True)
        last_line_len = len(line)