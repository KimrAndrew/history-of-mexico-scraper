import requests
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

from bs4 import BeautifulSoup


def get_citations_needed(url):
    page = requests.get(url)
    #print(page.content)
    soup = BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())


    results = soup.find_all(title='Wikipedia:Citation needed')
    return len(results)
#list(results)
#print(type(results[0]))

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    results = soup.find_all(title='Wikipedia:Citation needed')
    report = ''
    for i,result in enumerate(results,1):
        # print(i)
        # print('\n')
        # print(result.parent.parent.parent.text)
        report += '\n'
        report += result.parent.parent.parent.text
    report += '\n'
    return report

if __name__ == '__main__':
    print(f'Citations Needed: {get_citations_needed(URL)}')
    print(get_citations_needed_report(URL))