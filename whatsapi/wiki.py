import wikipedia
from wikipedia.exceptions import DisambiguationError
from wikipedia.exceptions import PageError
from wikipedia.exceptions import HTTPTimeoutError
import sys

wikipedia.set_lang('en')


def wiki_queries(queries):
    try:
        summary = wikipedia.summary(queries)
        return summary
    except DisambiguationError as e:
        return f'{list(sys.exc_info())[1]}'
    except PageError:
        return 'The page you are requesting does not exist'
    except HTTPTimeoutError:
        return 'Http Time Error'


if __name__ == '__main__':
    print(wiki_queries('netflix'))
