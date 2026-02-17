import pandas as pandas
import pydytuesday
from .utils import count

# Download files from the week, which you can then read in locally
pydytuesday.get_date('2025-06-03')

# Option 2: Read directly from GitHub and assign to an object

gutenberg_authors = pandas.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')



def list_authors(by_languages=True, alias=True):

    # This module 'references' a function in a different module
    authors_list = count()
    return authors_list


