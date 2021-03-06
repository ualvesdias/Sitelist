import requests as r
from bs4 import BeautifulSoup as bs
import argparse as ap


def wordListGen(url,minlen,depth,leet):
    try:
        req = r.get(url, verify=False)
    except:
        print('Can\'t connect to '+url+'. Check the URL and your connection.')
        return
    html = req.text
    soup = bs(html, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    words = []
    wordcount = 0
    for word in text.split():
        if len(word) >= minlen:
            words.append(word.strip('.,:!;"?@#$%&*()'))
            wordcount += 1
    if depth > 0:
        depth -= 1
        for link in list(set(soup.find_all('a'))):
            if link.get('href').startswith('http'):
                continue
            words2, wordcount2 = wordListGen(url+'/'+link.get('href'),minlen,depth,leet)
            wordcount += wordcount2
            if words2 != None:
                for word2 in words2:
                    words.append(word2)
                    wordcount += 1
    if leet:
        leetwords = leetMode(words)
        for leetword in leetwords:
            words.append(leetword)
            wordcount += 1
    return list(set(words)), wordcount


def leetMode(wordlist):
    # a=4, e=3, o=0, l=1, s=5, t=7
    leetlist = []
    for word in wordlist:
        newword = ''
        for char in word:
            if char.lower() in 'aeolst':
                    newword += '430157'['aeolst'.find(char.lower())]
            else:
                newword += char

        leetlist.append(newword)
    return leetlist


if __name__ == '__main__':
    parser = ap.ArgumentParser(description="Generate a wordlist from the contents of a URL.")
    parser.add_argument('-u', '--url', help='The target site address.', required=True)
    parser.add_argument('-m', '--minlen', default=4, help='The minimum length for a word to be in the wordlist.', type=int)
    parser.add_argument('-d', '--depth', default=1, help='The maximum depth of links to parse.', type=int)
    parser.add_argument('-l', '--leet',  help='Generate modified words from the existing ones using leet substitution.', action='store_true')
    parser.add_argument('-o', '--output',  help='Save wordlist to a file.')
    args = parser.parse_args()

    if args.url.startswith('http'):
        pass
    else:
        args.url = 'http://'+args.url

    wordlist, wordcount = wordListGen(args.url,args.minlen,args.depth,args.leet)

    if args.output:
        with open(args.output,'w') as file:
            for word in wordlist:
                file.write(word+'\n')
            print('Wordlist created with success in %s. %i words were collected.' % (args.output,wordcount))
    else:
        for word in wordlist:
            print(word)
        print('\nWordlist created with success. %i words were collected.' % wordcount)

