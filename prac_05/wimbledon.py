"""
CP1404/CP5632 Practical
Finding color code
Wimbledon
Estimate: 30 minutes
Actual:   35 minutes
"""
CHAMPION_INDEX = 2
COUNTRY_INDEX = 3
FILENAME = "wimbledon.csv"


def main():
    records = get_record(FILENAME)
    champion_to_count, countries = process_records(records)
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(champion, count)

    sorted_countries = sorted(countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted_countries))


def get_record(filename):
    """get the record list from the wimbledon.csv"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    countries = set()
    champion_to_count = {}

    for record in records:
        countries.add(record[COUNTRY_INDEX])
        champion = record[CHAMPION_INDEX]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count, countries


main()