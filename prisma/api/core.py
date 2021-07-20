from bs4 import BeautifulSoup

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

  def handle_data(self, data):
    print(data)

def get_summary(htmlfile):
  soup = BeautifulSoup(htmlfile, 'html.parser')
  text = soup.get_text()
  text = text.replace ('Hourly Range:', '\n\nHourly Range: ')
  text = text.replace ('Skills:', '\n\nSkills: ')
  text = text.replace ('Category:', '\n\nCategory:')
  text = text.replace ('Country:', '\nCountry: ')
  text = text.replace ('click to apply', '\n\nWanna claim the bounty? \nClick on the link and start the hunt!')
  return text

class mission:
  def __init__(self,feed_entry):
    self.title = feed_entry.title
    self.timestamp = feed_entry.published
    self.link = feed_entry.link
    self.sum = feed_entry.summary
    self.parsedsum = get_summary(feed_entry.summary)
    self.entry = feed_entry

  def get_cartel(self):
    cartel = (
        '-------------PRISMA BOUNTYHUNTER SYSTEM CARTEL---------------\n'
        +'\n'+
        '                            HELP!!!                          \n'+
        '\n'+
        '- Mission: ' + self.title + '\n' +
        '\n'+
        '- Published on: ' + self.timestamp + '\n' +
        '\n'+
        '- Link: ' + self.link + '\n\n' +
        '- Client Summary: \n\n ' + str(self.parsedsum) +
        '\n\n'+
        '-----------------------END OF CARTEL-------------------------\n\n'
    )
    return cartel


  def print_mission(self):
    print('-------------PRISMA BOUNTYHUNTER SYSTEM CARTEL---------------')
    print('                   WANTED!!!                                 ')
    print('\n')
    print('- Mission: ' + self.title + '\n')
    print('- Published on: ' + self.timestamp + '\n')
    print('- Link: ' + self.link + '\n')
    parser = MyHTMLParser()
    print('- Summary: \n\n ')
    parser.feed(self.sum)
    print('\n\n')
    print('-----------------------END OF CARTEL-------------------------')
    print('\n')


