import json
import os

from jinja2 import Environment, FileSystemLoader

from media import Movie

SOURCE_FILE = 'source.json'
OUTPUT_FILE = 'index.html'
TEMPLATE_FILE = 'template.html'
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False, loader=FileSystemLoader(os.path.dirname(__file__)),
    trim_blocks=False)


def get_movies_from_source():
    with open(SOURCE_FILE) as f:
        return json.load(f)


def render_template(context):
    return TEMPLATE_ENVIRONMENT.get_template(TEMPLATE_FILE).render(context)


def generate_output(movies):
    html = render_template(context={'movies': movies})
    with open(OUTPUT_FILE, 'w') as f:
        f.write(html)


def main():
    movies = []
    for movie in get_movies_from_source()['movies']:
        movie_obj = Movie(
            title=movie['title'],
            youtube_url=movie['trailer'],
            poster_url=movie['poster_link']
        )
        movies.append(movie_obj)
    generate_output(movies)


if __name__ == '__main__':
    main()
