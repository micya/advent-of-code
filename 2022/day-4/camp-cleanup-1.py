class Section:
    def __init__(self, section: str) -> None:
        parts = section.strip().split('-')
        self.start = int(parts[0])
        self.end = int(parts[1])

    def contains(self, other: "Section") -> bool:
        return self.start <= other.start and self.end >= other.end


count = 0

for line in open("input.txt"):
    line = line.strip()
    parts = line.split(',')
    section1 = Section(parts[0])
    section2 = Section(parts[1])

    if section1.contains(section2) or section2.contains(section1):
        count += 1

print(count)
