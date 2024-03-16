import os
import string

harry_potter_path = "Harry Potter"

os.makedirs(harry_potter_path, exist_ok=True)

films_titles = {
    "results": [
        {"imdb_id": "tt1201607", "title": "Harry Potter and the Deathly Hallows: Part 2"},
        {"imdb_id": "tt0241527", "title": "Harry Potter and the Sorcerer's Stone"},
        {"imdb_id": "tt0926084", "title": "Harry Potter and the Deathly Hallows: Part 1"},
        {"imdb_id": "tt0304141", "title": "Harry Potter and the Prisoner of Azkaban"},
        {"imdb_id": "tt0417741", "title": "Harry Potter and the Half-Blood Prince"},
        {"imdb_id": "tt0295297", "title": "Harry Potter and the Chamber of Secrets"},
        {"imdb_id": "tt0330373", "title": "Harry Potter and the Goblet of Fire"},
        {"imdb_id": "tt0373889", "title": "Harry Potter and the Order of the Phoenix"}
    ]
}

for film in films_titles["results"]:
    film_title = film["title"]
    film_directory = os.path.join(harry_potter_path, film_title)

    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.makedirs(letter_directory, exist_ok=True)



films_awards = [
    {
        'links': {'next': None, 'previous': None},
        'count': 49,
        'results': [
            {
                'movie': {'imdb_id': 'tt1201607', 'title': 'Harry Potter and the Deathly Hallows: Part 2'},
                'series': None,
                'actor': [{'imdb_id': 'nm0240183', 'name': 'Nick Dudman'},
                          {'imdb_id': 'nm0460792', 'name': 'Amanda Knight'},
                          {'imdb_id': 'nm0866566', 'name': 'Lisa Tomblin'}],
                'event_name': 'Academy Awards, USA',
                'year': 2012,
                'type': 'Nominee',
                'award_name': 'Oscar',
                'award': 'Best Achievement in Makeup'
            },
            {
                'movie': {'imdb_id': 'tt1201607', 'title': 'Harry Potter and the Deathly Hallows: Part 2'},
                'series': None,
                'actor': [{'imdb_id': 'nm0121888', 'name': 'Tim Burke'},
                          {'imdb_id': 'nm0724624', 'name': 'John Richardson'},
                          {'imdb_id': 'nm0124935', 'name': 'Greg Butler'},
                          {'imdb_id': 'nm1316134', 'name': 'David Vickery'}],
                'event_name': 'BAFTA Awards',
                'year': 2012,
                'type': 'Winner',
                'award_name': 'BAFTA Film Award',
                'award': 'Best Special Visual Effects'
            },
            {
                'movie': {'imdb_id': 'tt1201607', 'title': 'Harry Potter and the Deathly Hallows: Part 2'},
                'series': None,
                'actor': [{'imdb_id': 'nm0946734', 'name': 'David Yates'},
                          {'imdb_id': 'nm0746830', 'name': 'J.K. Rowling'},
                          {'imdb_id': 'nm0057655', 'name': 'David Barron'},
                          {'imdb_id': 'nm0382268', 'name': 'David Heyman'}],
                'event_name': 'BAFTA Awards',
                'year': 2011,
                'type': 'Winner',
                'award_name': "BAFTA Children's Award",
                'award': 'Best Feature Film'
            },
            {
                'movie': {'imdb_id': 'tt1201607', 'title': 'Harry Potter and the Deathly Hallows: Part 2'},
                'series': None,
                'actor': [{'imdb_id': 'nm1168404', 'name': 'Reg Wayment'},
                          {'imdb_id': 'nm0621178', 'name': 'Daniel Naprous'},
                          {'imdb_id': 'nm2823677', 'name': 'Calvin Warrington-Heasman'}],
                'event_name': 'Academy of Science Fiction, Fantasy & Horror Films, USA',
                'year': 2012,
                'type': 'Winner',
                'award_name': 'Saturn Award',
                'award': 'Best Fantasy Film'
            }
        ]
    }
]
films_awards_list = []

for film_awards in films_awards:
    results = film_awards.get("results", [])
    film_awards_for_movie = []
    for award in results:
        award_info = {
            "type": award.get("type", ""),
            "award_name": award.get("award_name", ""),
            "award": award.get("award", "")
        }
        film_awards_for_movie.append(award_info)
    films_awards_list.append(film_awards_for_movie)

print(films_awards_list)

for film_awards in films_awards_list:
    film_awards.sort(key=lambda x: x["award_name"])

for i, film_awards in enumerate(films_awards_list, 1):
    print(f"Фільм {i}:")
    for award in film_awards:
        print(award)
    print()


def find_starting_letter(award_name):
    return award_name[0].upper()


for film_index, film_awards in enumerate(films_awards_list, 1):
    film_title = films_titles["results"][film_index - 1]["title"]
    film_directory = os.path.join(harry_potter_path, film_title)

    for award in film_awards:
        award_name = award["award_name"]
        award_letter = find_starting_letter(award_name)
        award_file_path = os.path.join(film_directory, award_letter, f"{award_name}.txt")

        with open(award_file_path, "w") as award_file:
            award_file.write(f"Назва нагороди: {award_name}\n")
            award_file.write(f"Тип: {award['type']}\n")
            award_file.write(f"Опис нагороди: {award['award']}\n")
