import requests
from table2ascii import table2ascii as t2a, PresetStyle
from bs4 import BeautifulSoup

class IFPAChampsStandings:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}

  def key_words_search_words(self, user_message):
    self.url = 'https://www.ifpapinball.com/nacs/2021/standings.php?l=PA#rankings'
    words = user_message.split()[1:]
    state = words[0]
    year = words[1]
    #championship = words[2]
    self.url = 'https://www.ifpapinball.com/'
    self.url = self.url + 'nacs'
    self.url = self.url + '/'
    self.url = self.url + year
    self.url = self.url + '/standings.php?l='
    self.url = self.url + state
    self.url = self.url + '#rankings'
    full_url = self.url
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words, full_url

  def key_words_search_wnacs(self, user_message):
    self.url = 'https://www.ifpapinball.com/rankings/custom_view.php?id=325'
    words = user_message.split()[1:]
    #state = words[0]
    #year = words[1]
    #championship = words[2]
    #self.url = 'https://www.ifpapinball.com/'
    #self.url = self.url + 'nacs'
    #self.url = self.url + '/'
    #self.url = self.url + year
    #self.url = self.url + '/standings.php?l='
    #self.url = self.url + state
    #self.url = self.url + '#rankings'
    full_url = self.url
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words, full_url

  def search(self, keywords):

    #try:
    response = requests.get(self.url, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    data = []
    table = soup.find('table', attrs={'class':'table table-striped table-hover table-sm', 'style':'margin-top: 25px'})
    rows = table.find_all('tr')
    row_counter = 0
    for row in rows:
      if row_counter < 33:
        cols = row.find_all(["th", "td"])
        cols = [ele.text.strip() for ele in cols]
        #data.append([ele for ele in cols if ele]) # Get rid of empty values
      row_counter = row_counter + 1
    top_list = []
    for element in data:
      top_list.append([element[0], element[1], element[3]])
    top_table = t2a(
    #header = ["Rank", "Player", "Pts"],
    body = top_list,
    style = PresetStyle.thin_compact)
    #except:
    #  top_table = '''Error: I am not finding standings for what you entered.  Can you try again?
    #  Type $ifpachamps followed by the following two inputs:
    #  * Two-Letter State or Province Code
    #  * Year
    #  Example: $ipfachamps PA 2022'''
      
    return top_table

  def search_wnacs(self, keywords):

    #try:
    response = requests.get(self.url, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    data = []
    table = soup.find('table', attrs={'class':'table table-striped table-hover table-sm'})
    rows = table.find_all('tr')
    row_counter = 0
    for row in rows:
      if row_counter < 33:
        cols = row.find_all(["th", "td"])
        #cols = [ele.text.strip() for ele in cols]
        cols = [ele.text for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
      row_counter = row_counter + 1
    top_list = []
    for element in data:
      top_list.append([element[0], element[1], element[3]])
    top_table_w = t2a(
    #header = ["Rank", "Player", "Pts"],
    body = top_list,
    style = PresetStyle.thin_compact)
    print(data)
    #except:
    #  top_table = '''Error: I am not finding standings for what you entered.  Can you try again?
    #  Type $ifpachamps followed by the following two inputs:
    #  * Two-Letter State or Province Code
    #  * Year
    #  Example: $ipfachamps PA 2022'''
      
    #return top_table_w
    #return top_list