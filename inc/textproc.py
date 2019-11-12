import html.parser
from bs4 import BeautifulSoup


class extractText(html.parser.HTMLParser):
    def __init__(self):
        super(extractText, self).__init__()
        self.result = []

    def handle_data(self, data):
        self.result.append(data)

    def text_in(self):
        return ''.join(self.result)


def html2text(html):
    k = extractText()
    k.feed(html)
    return k.text_in()


def cut_text(filename, count):
    with open(filename) as html:
        soup = BeautifulSoup(html, features="lxml")
        for script in soup(["script", "style"]):
            script.extract()
        k = []
        for i in soup.findAll('p')[1]:
            k.append(i)
        b = ''.join(str(e) for e in k)
        text = html2text(b.replace("\n", ""))
        textreduced = (text[:count] + '...') if len(text) > count else (text +
                                                                        '..')
        return (textreduced)


def cut_news_text(filename, count):
    return cut_text("news/" + filename + ".j2", count)
