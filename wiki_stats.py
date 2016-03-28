#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            file_data = f.readline().split()
            self._n = int(file_data[0])
            self._nlinks = int(file_data[-1])
            
            self._titles = []
            self._sizes = array.array('L', [0]*self._n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self._n)
            self._offset = array.array('L', [0]*(self._n+1))

            links_iterator = 0
            for title_number in range(self._n):
                self._titles.append(f.readline())
                title_size, redirect_flag, title_links_number = [int(x) for x in f.readline().split()]
                self._sizes[title_number] = title_size
                self._redirect[title_number] = redirect_flag
                if title_number == 0:
                    self._offset[title_number] = links_iterator
                for link_number in range(title_links_number):
                    self._links[links_iterator] = (int(f.readline()))
                    links_iterator += 1

        print('Граф загружен')

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1]-self._offset[_id]

    def get_links_from(self, _id):
        start_id = self._offset[id]
        end_id = self._offset[id+1]
        return end_id - start_id

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        return self._redirect [id]

    def get_title(self, _id):
        return self._title[id]

    def get_page_size(self, _id):
        pass


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    print('Использование: wiki_stats.py <файл с графом статей>')
    wg = WikiGraph()
    wg.load_from_file('wiki_small.txt')

    # TODO: статистика и гистограммы
