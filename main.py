from exa_py import Exa
exa = Exa('Insert API key here')


query = input('Search here: ')
response = exa.search(
  query,
  num_results=10,
  type='keyword',
  include_domains=['https://www.linkedin.com'],
)
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()



