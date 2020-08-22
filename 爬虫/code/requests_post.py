#coding:utf-8
import sys
import requests
import json

class Trans(object):

    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
        }
        self.data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }
    #   get data from translation site
    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.data, )
        return response.content
    def parse_data(self, data):
        #loads() transform json data to dict data
        dict_data = json.loads(data)
        return  dict_data
    # TODO : update

    def run(self):
        response = self.get_data()

        # print(response.decode())
        # print(self.parse_data(response))

        trans_result_dict = self.parse_data(response)

        # print(trans_result_dict)

        try:
            trans_result = trans_result_dict['content']['out']
        except:
            trans_result = trans_result_dict['content']['word_mean']
        print(trans_result)

if __name__ == '__main__':

    word = sys.argv[1]
    # print(sys.argv)
    King = Trans(word)
    King.run()
