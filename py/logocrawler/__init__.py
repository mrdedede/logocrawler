"""
LogoCrawler Project

This project aims to:
- Catch entries with domain names and queries them
- Output the logo of each domain name with them
- Use only standard Python libraries

What else could be done:
- The project does not have a resistancy case for when every possible query is exhausted for a
    domain, with lots of HTTP Errors that could be solved with dynamic header configuration
    for GET requests not being implemented for now
- Some websites reference their logos in their CSS files and, if we could query specifically
    them after failing to retrieve the right images from the HTML we could achieve better
    results
- Our way of filtering image files found in the HTML pages is not working the best as it could,
    being pretty much a filter that only works in a limited number of entries
- Instead of "threading", we could use a library that uses a multiprocessing pool to do more
    http requests and treat their data faster
- We could transform this task in a proper ETL pipeline, in which the first step could be
    implemented using a more rebust requests and scraping library as `requests` or `selenium``
    in order to get as close as possible to a browser in the interpretation of the webpage,
    however, this would make the script slower

Scaling this program to millions of entries:
- Maybe the usage of native Python lists are not indicated for these cases, the usage of a
    C-interface iterable for this data such as Numpy Arrays are a good substitute for faster tracking
- Using distributed computing in an interface such as Apache Spark could help us level up our
    parallelization and multithreading already implemented
- Using caching and databases could help us achieve better results as we need to scale
"""

from main import main_lifecycle

main_lifecycle()