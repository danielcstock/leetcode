def convert(s: str, num_rows: int) -> str:
    # Trivial cases: no zigzag movement needed
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows = [""] * num_rows
    cur = 0
    step = -1  # direction (+1 down, -1 up). Flip at the ends.

    for ch in s:
        print('cur: ', cur, ' step: ', step, ' rows: ', rows)
        rows[cur] += ch
        # Flip direction at top or bottom row
        if cur == 0 or cur == num_rows - 1:
            step *= -1
        cur += step
        

    return "".join(rows)


# Quick tests
if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    # print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    # print(convert("A", 1))               # A