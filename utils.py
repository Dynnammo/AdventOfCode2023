def extract_lines(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]