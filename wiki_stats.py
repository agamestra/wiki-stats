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
            self._n = int(file_data[0]) #n - количество статей
            self._nlinks = int(file_data[-1]) #nlinks - количество ссылок во всех статьях
            
            self._titles = [] #titles - названия статей
            self._sizes = array.array('L', [0]*self._n) #sizes - размеры статей
            self._links = array.array('L', [0]*self._nlinks) #links - количество ссылок в статьях
            self._redirect = array.array('B', [0]*self._n) #redirect - флаги перенаправления
            self._offset = array.array('L', [0]*(self._n+1)) # offset - номер статьи, на которую ссылается статья

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

    def get_id(self, title): #индекс статьи в массиве статей
        return self._titles.index(title)

    def get_number_of_links_from(self, _id): #количество статей 
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
        return self._sizes[id]
        
    def get_count_redirection(self): #количество статей с перенаправлением
        count_redirection = 0
        for i in range (n):
            if self._redirect[i]:
                count_redirection += 1
        return count_redirection
        
    def get_minimum_links_count(self): #минимальное количество ссылок из статьи
        minimum_links_count = self._links[0]
        for i in range (n+1):
            if self._links[i] < minimum_links_count:
                minimum_links_count = self._links[i]
        return minimum_links_count
    
    def get_count_articles_with_min_links(self): #количество статей с минимальным количеством ссылок
        min = minimum_links_count()
        count_articles_with_min_links = 0
        for i in range (n):
            if self._links[i] == min:
                count_articles_with_min_links += 1
        return count_articles_with_min_links
    
    def get_maximum_links_count(self): #максимальное количество ссылок из статьи
        maximum_links_count = self._links[0]
        for i in range (n+1):
            if self._links[i] > maximum_links_count:
                maximum_links_count = self._links[i]
        return maximum_links_count
        
    def get_count_articles_with_max_links(self): #количество статей с максимальным количеством ссылок
        max = maximum_links_count()
        count_articles_with_max_links = 0
        for i in range (n):
            if self._links[i] == max:
                count_articles_with_max_links += 1
        return count_articles_with_max_links
        
    def article_with_max_links(self): #статья с наибольшим количеством ссылок
        max = maximum_links_count()
        for i in range (n):
            if self._links[i] == max:
                article_with_max_links = i
                break
        return article_with_max_links
        
    def middle_count_links_in_article(self): #среднее количество ссылок в статье
        return n_links/n
        
    def min_count_links_to_article(self): #минимальное количество ссылок на статью
        for i in range (n):
            for j in range (n):
                pass

def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    print('Использование: wiki_stats.py <файл с графом статей>')
    wg = WikiGraph()
    wg.load_from_file('wiki_small.txt')

    # TODO: статистика и гистограммы
