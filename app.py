import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from datetime import datetime
from SearchingAlgos import *
from sorting import Sorting
import SearchingAlgos
import pandas as pd
import webbrowser
from pakwheels import get_words_in_page
from Carvago import get_words_in_page
import requests
import time
from bs4 import BeautifulSoup
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from voiceover import voice
import logging

logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s', level=logging.INFO)

counter = False
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    counter = False
    Start = 0
    Start1 = 0
    info= []
    def run(self):
        """Long-running task."""
        self.Start,End = self.pakwheels_paging(self.info)
        self.Start1,End1 = self.Carvago_paging(self.info)
        while (self.Start <= End or self.Start1 < End1) and self.counter == False:
            time.sleep(2)
            if self.counter == False:
                if self.Start1 <= End1 and self.Start <= End:
                    if self.counter == False:
                        data_list = self.Carvago_main(self.Start1 , self.Start1+5 )
                    # all_data.extend(Carvago_main())
                if self.Start <= End:
                    if self.counter == False:
                        data_list.extend(self.Pakwheels_main(self.Start , self.Start+5))
                    # all_data.extend(Carvago_main())
                if self.Start1 <= End1 and self.Start > End:
                    if self.counter == False:
                        data_list = self.Carvago_main(self.Start1 , self.Start1+5)
                self.finished.emit()
                return
                # self.label_12.setText(str(len(data_list)))
            self.Start1 += 5
            self.Start += 5
        self.finished.emit()
    
    def pakwheels_paging(self , info):
        file1 = open("Pause Holding.txt","r") 
        Numbers = file1.read()
        li = list(Numbers.split(' '))
        Start = int(li[0])
        base_url = "https://www.pakwheels.com/used-cars/search/-/?_pjax=%5Bdata-pjax-container%5D"
        soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
            
        for ul in soup.select("ul.search-pagi"):
            info = [i['href'] for i in ul.find_all('a', href=True)]
        value = info[7]
        END=int(value[58:len(value)])
        return Start,END
    def Carvago_paging(self , info):
        file1 = open("Pause Holding.txt","r") 
        Numbers = file1.read()
        li = list(Numbers.split(' '))
        Start = int(li[1])
        base_url = "https://carvago.com/cars?sort=recommended&page=1&limit=20"
        soup = BeautifulSoup(requests.get(base_url ).content, "html.parser")
        
        for ul in soup.select("ul.Pagination-container"):
                info = [li.get_text(strip=True) for li in ul.select("li")]
        
        END = int(info[7])
        return Start,END
    def Pakwheels_main(self , start , end):
        all_data = []
        base_url = "https://www.pakwheels.com/used-cars/search/-/?_pjax=%5Bdata-pjax-container%5D"
        # soup = BeautifulSoup(requests.get(base_url , headers=headers).content, "html.parser")
            
        # for ul in soup.select("ul.search-pagi"):
        #     info = [i['href'] for i in ul.find_all('a', href=True)]
        # value = info[7]
        # END=int(value[58:len(value)])
        START = start
        END = end
        for paging in range(START,END):
            if counter == False:
                print(paging)
                self.Start += 1
                if paging < 2:    
                    all_data = get_words_in_page( base_url ) 
                    base_url = "https://www.pakwheels.com/used-cars/search/-/?_pjax=%5Bdata-pjax-container%5D&page="
                    try:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" ,"Year", "KM", "Type", "CC", "Type 2" , "GRADE" ])
                        df["GRADE"] = df["GRADE"].fillna(0)
                        df.to_csv("data.csv", index=False)
                    except:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" , "Year", "KM", "Type", "CC", "Type 2" ])
                        df.to_csv("data.csv",index=False)
                if paging >= 2: 
                    base_url = "https://www.pakwheels.com/used-cars/search/-/?_pjax=%5Bdata-pjax-container%5D&page="
                    url = base_url+str(paging)
                    all_data = get_words_in_page(url)
                    try:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" ,"Year", "KM", "Type", "CC", "Type 2" , "GRADE" ])
                        df["GRADE"] = df["GRADE"].fillna(0)
                        df.to_csv("data.csv", index=False)
                    except:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" , "Year", "KM", "Type", "CC", "Type 2" ])
                        df.to_csv("data.csv",index=False)
            elif counter == True:
                break
        return all_data
    def Carvago_main(self ,start,end):
        all_data = []
        base_url = "https://carvago.com/cars?sort=recommended&page=1&limit=20"
        # soup = BeautifulSoup(requests.get(base_url , headers=headers).content, "html.parser")
        
        # for ul in soup.select("ul.Pagination-container"):
        #         info = [li.get_text(strip=True) for li in ul.select("li")]
        
        # END = int(info[7])
        START = start
        END = end
        for paging in range(START,END):
            if self.counter == False:
                print(paging)
                self.Start1 += 1
                if paging < 2:    
                    all_data = get_words_in_page( base_url ) 
                    base_url = "https://carvago.com/cars?sort=recommended&page="
                    try:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" ,"Year", "KM", "Type", "CC", "Type 2" , "GRADE" ])
                        df["GRADE"] = df["GRADE"].fillna(0)
                        df.to_csv("data.csv", index=False)
                    except:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" , "Year", "KM", "Type", "CC", "Type 2" ])
                        df.to_csv("data.csv",index=False)
                if paging >= 2:    
                    base_url = "https://carvago.com/cars?sort=recommended&page="
                    url = base_url+str(paging )+ "&limit=20"
                    all_data = get_words_in_page(url)
                    try:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" ,"Year", "KM", "Type", "CC", "Type 2" , "GRADE" ])
                        df["GRADE"] = df["GRADE"].fillna(0)
                        df.to_csv("data.csv", index=False)
                    except:
                        df = pd.DataFrame(all_data, columns=["Car Name","Link" , "Year", "KM", "Type", "CC", "Type 2" ])
                        df.to_csv("data.csv",index=False)
            elif counter == True:
                break

        return all_data
class MainWindow(QMainWindow):
    
    source_list = []
    back_up = []
    attributes = ['Name', 'Year', 'Mileage',
                  'CC', 'Grade', 'Transmission', 'Fuel']

    sort_algorithms = ['Insertion Sort', 'Selection Sort', 'Heap Sort', 'Bubble Sort', 'Tim Sort', 'Quick Sort',
                       'Count Sort', 'Radix Sort', 'Bucket Sort', '3-way Merge Sort', 'Cocktail Sort',
                       'Merge Sort']

    search_algorithms = ['Rabin-Karp Algo']
    def __init__(self):  # Setting up events for clicks
        super(MainWindow, self).__init__()
        loadUi('app.ui', self)
        self.setFixedSize(925, 1000)  # Window Size width x Height
        df =  pd.read_csv("data.csv", encoding='utf8')
        naem = df['Car Name'].values.tolist()
        naem = naem[0:5000]
        link = df['Link'].values.tolist()
        link = link[0:5000]
        year = df['Year'].values.tolist()
        year = year[0:5000]
        km = df['KM'].values.tolist()
        km = km[0:5000]
        type = df['Type'].values.tolist()
        type = type[0:5000]
        cc = df['CC'].values.tolist()
        cc = cc[0:5000]
        type2 = df['Type 2'].values.tolist()
        type2 = type2[0:5000]
        grade = df['GRADE'].values.tolist()
        grade = grade[0:5000]
           
        self.source_list.append(naem)
        self.source_list.append(link)
        self.source_list.append(year)
        self.source_list.append(km)
        self.source_list.append(type)
        self.source_list.append(cc)
        self.source_list.append(type2)
        self.source_list.append(grade)
        # print(self.source_list)
        
        self.back_up = self.source_list.copy()
        self.fill_table(self.source_list)
        # print(self.source_list)
        numbers_string = str(0) +' '+ str(0)
        with open('Pause Holding.txt', 'w') as f:
            f.write(numbers_string)

        # Adding various click events
        self.setWindowTitle('Car Details Platform')
        # self.combo_attribute_sort.addItems(self.attributes)
        self.combo_algo_sort.addItems(self.sort_algorithms)
        self.combo_attribute_search.addItems(self.attributes)
        self.combo_algo_search.addItems(self.search_algorithms)
        self.btn_sort.clicked.connect(self.sort)
        self.btn_search.clicked.connect(self.searchWithAttributes)
        self.btn_clr_search.clicked.connect(self.clear_search)
        self.btn_clr_sort.clicked.connect(self.clear_sort)
        self.btn_reset.clicked.connect(self.resetButton)
        self.btn_car_contains.clicked.connect(self.searchBar)
        self.table_entities.itemDoubleClicked.connect(self.openLink)
        self.btn_scrap.clicked.connect(self.scrape)
        self.btn_resume_scrap.clicked.connect(self.resume)
        self.btn_end_srap.clicked.connect(self.update_scrape)
        self.btn_pause_scrap.clicked.connect(self.pause_scrape)
        
        # Setting up default radio
        self.defaultButtons()     
    @staticmethod
    def loadData():
        df =  pd.read_csv("data.csv", encoding='utf8')
        naem = df['Car Name'].values.tolist()
        link = df['Link'].values.tolist()
        year = df['Year'].values.tolist()
        km = df['KM'].values.tolist()
        type = df['Type'].values.tolist()
        cc = df['CC'].values.tolist()
        type2 = df['Type 2'].values.tolist()
        grade = df['GRADE'].values.tolist()
           
        ap= []
        ap.append(naem)
        ap.append(link)
        ap.append(year)
        ap.append(km)
        ap.append(type)
        ap.append(cc)
        ap.append(type2)
        ap.append(grade)
        
        return ap
    
    def defaultButtons(self):
        self.radio_ascend_sort.setChecked(True)
        # self.radio_search_single.setChecked(True)
    def resetButton(self):
        try:
            self.source_list = []
            self.source_list = self.back_up.copy()
            self.table_entities.setColumnWidth(0, 200)
            self.table_entities.setColumnWidth(1,100)
            self.table_entities.setRowCount(len(self.back_up[0]))

            # row = 0
            for i in range(0, len(self.back_up[0])):
                
                self.table_entities.setItem(i, 0, QTableWidgetItem(str(self.back_up[0][i])))
                self.table_entities.setItem(i, 1, QTableWidgetItem(str(self.back_up[1][i])))
                # print(item[2])
                self.table_entities.setItem(i, 2, QTableWidgetItem(str(self.back_up[2][i])))
                self.table_entities.setItem(i, 3, QTableWidgetItem(str(self.back_up[3][i])))
                self.table_entities.setItem(i, 4, QTableWidgetItem(str(self.back_up[4][i])))
                self.table_entities.setItem(i, 5, QTableWidgetItem(str(self.back_up[5][i])))
                self.table_entities.setItem(i, 6, QTableWidgetItem(str(self.back_up[6][i])))
                self.table_entities.setItem(i, 7, QTableWidgetItem(str(self.back_up[7][i]))) #filling the table with elements from the original load
            
            self.lbl_algo_stat.setText('__________')
            self.lbl_time_stat.setText('__________')
        except:
            pass
        
    def reset(self,list1):  # empties table and fills it again with csv files
        self.table_entities.setRowCount(0)
        self.fill_table(list1)
        # self.fill_table(self.source_list[0:10])
        

    def searchBar(self): #SearchBar Functionality 
        try:
            pattern = self.txt_car_contains.toPlainText()
            # print(pattern)
            # if len(self.txt_car_contains.toPlainText()) == 0:
            #     self.resetButton()
            # else:
            if pattern != None:
                start = datetime.now()
                self.source_list = []
                self.source_list = SearchingAlgos.checkName(self.back_up,0,pattern)
                # print(self.source_list)
                
                end = datetime.now()
                diff = (end-start)
                diff = diff.total_seconds() * 1000
                diff = round(diff,3)
                self.table_entities.setColumnWidth(0, 200)
                self.table_entities.setColumnWidth(1,100)
                self.table_entities.setRowCount(len(self.source_list[0]))

                # row = 0
                for i in range(0, len(self.source_list[0])):
                    
                    self.table_entities.setItem(i, 0, QTableWidgetItem(str(self.source_list[0][i])))
                    self.table_entities.setItem(i, 1, QTableWidgetItem(str(self.source_list[1][i])))
                    # print(item[2])
                    self.table_entities.setItem(i, 2, QTableWidgetItem(str(self.source_list[2][i])))
                    self.table_entities.setItem(i, 3, QTableWidgetItem(str(self.source_list[3][i])))
                    self.table_entities.setItem(i, 4, QTableWidgetItem(str(self.source_list[4][i])))
                    self.table_entities.setItem(i, 5, QTableWidgetItem(str(self.source_list[5][i])))
                    self.table_entities.setItem(i, 6, QTableWidgetItem(str(self.source_list[6][i])))
                    self.table_entities.setItem(i, 7, QTableWidgetItem(str(self.source_list[7][i])))
                        
                self.lbl_algo_stat.setText('Rabin-Karp Algo')
                self.lbl_time_stat.setText(str(diff))
                
            
                self.lbl_algo_stat.setText('Rabin-Karp Algo')
                self.lbl_time_stat.setText(str(diff))
                # self.back_up = self.loadData()
            
            #Play the number of elements in the list using voiceover.py module
                length = len(self.source_list[0])
                length = str(length) + ' elements in the table upcoming'
                voice(length)
        except Exception as e:
            logging.exception(str(e))
        
    def searchWithAttributes(self):
        try:
            attr = str(self.combo_attribute_search.currentText())
            algo = self.combo_algo_search.currentText()
            contains = self.txt_col_contains.toPlainText()
            attr = self.combo_attribute_search.currentText()
            start_as = self.txt_start_search.toPlainText()
            # if start_as == '':
            #     logging.info('Start as is null.')
            end_as = self.txt_end_search.toPlainText()
            and_attr = self.txt_and_col.toPlainText()
            # or_attr = self.txt_or_col.toPlainText()
            not_attr = self.txt_not_col.toPlainText()
            
            dict = {'Name':'0' , 'Link':'1' ,'Year':'2' , 'Mileage':'3' , 'Fuel':'4' , 'CC':'5', 'Transmission':'6', 'Grade':'7'}
            index = int(dict[attr])

            checkBoxes = [self.radio_and, self.radio_or, self.radio_not]
            checked_checkBoxes = [False for i in range(0, 3)]
            
            for i in range(0,3):
                if checkBoxes[i].isChecked():
                    checked_checkBoxes[i] = True
            
            if checked_checkBoxes[0] == False:
                and_attr = ''
            elif checked_checkBoxes[2] == False:
                not_attr = ''
            
            start = datetime.now()
            self.source_list = self.searchFunction(index,contains, start_as, end_as, and_attr,not_attr)
            if len(self.source_list) == 0:
                voice('Sorry, no elements with given data were found.')
            
            end = datetime.now()

            self.table_entities.setColumnWidth(0, 200)
            self.table_entities.setColumnWidth(1,100)
            self.table_entities.setRowCount(len(self.source_list[0]))

                # row = 0
            for i in range(0, len(self.source_list[0])):
                self.table_entities.setItem(i, 0, QTableWidgetItem(str(self.source_list[0][i])))
                self.table_entities.setItem(i, 1, QTableWidgetItem(str(self.source_list[1][i])))
                # print(item[2])
                self.table_entities.setItem(i, 2, QTableWidgetItem(str(self.source_list[2][i])))
                self.table_entities.setItem(i, 3, QTableWidgetItem(str(self.source_list[3][i])))
                self.table_entities.setItem(i, 4, QTableWidgetItem(str(self.source_list[4][i])))
                self.table_entities.setItem(i, 5, QTableWidgetItem(str(self.source_list[5][i])))
                self.table_entities.setItem(i, 6, QTableWidgetItem(str(self.source_list[6][i])))
                self.table_entities.setItem(i, 7, QTableWidgetItem(str(self.source_list[7][i])))
                
            diff = (end - start).total_seconds() * 1000
            diff = round(diff,3)
            
            self.reset(self.source_list)
            self.lbl_algo_stat.setText(str(algo))
            self.lbl_time_stat.setText(str(diff))
            
            length = len(self.source_list[0])
            length = str(length) + ' elements in the table upcoming'
            voice(length)
        
        except Exception as e:
            logging.exception(str(e))
            print(str(e))
            self.lbl_time_stat.setText('Op !exec')

    def openLink(self, item):  # Opens a QTableItem in browser
        if item.column() == 1:
            webbrowser.open(str(item.text()))

    def searchFunction(self, index,contains, start_as, end_as, and_attr, not_attr):
        # logging.info(str(index) + ' of the column')
        
        # print(containing)
        containing = checkName(self.source_list,index,contains)
        # print(containing)
        if len(containing[0]) == 0:
            return containing
            
        if start_as:
            containing = StartsWith(containing[index],start_as, containing)
        if end_as:
            containing = EndsWith(containing[index],end_as,containing)
        if and_attr:
            containing = checkName(containing,index,and_attr)
        if not_attr:
            containing = Not(containing[index],not_attr,containing)
            # print(containing)
        return containing

    def scrape(self):
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        self.worker.counter = False
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()
        
        
        
    
    # def check_condition(self):
    #     if self.btn_pause_scrap.isChecked() == True:
    #        Worker.counter = True
    
    def update_scrape(self):
        numbers_string = str(0) +' '+ str(0)
        with open('Pause Holding.txt', 'w') as f:
            f.write(numbers_string)
        self.source_list = self.loadData()
        self.reset(self.source_list)
        self.lbl_entites_scrapped.setText(str(len(self.source_list[0])))
        self.worker.counter = True
        self.worker.finished.emit()
        
    def pause_scrape(self):
        numbers_string = str(self.worker.Start) +' '+ str(self.worker.Start1)
        with open('Pause Holding.txt', 'w') as f:
            f.write(numbers_string)
        self.source_list = self.loadData()
        self.reset(self.source_list)
        self.lbl_entites_scrapped.setText(str(len(self.source_list[0])))
        self.worker.counter = True
        self.worker.finished.emit()
            
    
    def resume(self):
        file1 = open("Pause Holding.txt","r") 
        Numbers = file1.read()
        li = list(Numbers.split(' '))
        Start = int(li[0])
        Start1 = int(li[1])
        if Start != 0 or Start1 != 0:
            self.scrape()           
    
    def clear_sort(self):  # Clear sorting filters
        pass

    def clear_search(self):  # Clear searching filters
        try:
            column = self.txt_col_contains.setText('')

            start_as = self.txt_start_search.setText('')
        #    print(str(start_as))
            end_as = self.txt_end_search.setText('')
            and_attr = self.txt_and_col.setText('')
            or_attr = self.txt_or_col.setText('')
            not_attr = self.txt_not_col.setText('')
        
        except Exception as e:
            logging.exception(e)

    def sort(self):
        try:
            # attr = self.combo_attribute_sort.currentText()
            algo = self.combo_algo_sort.currentText()
            mode = self.radio_ascend_sort.isChecked()
            isSorted = False
            types = ['ascend', 'descend']
            radios = [self.radio_ascend_sort, self.radio_descend_sort]
            type_to_pass = None
            for i in range(0, 2):
                if radios[i].isChecked() == True:
                    # print(types[i])
                    type_to_pass = types[i]
                    break
            
            
            checkBoxes = [self.col_name,self.col_link, self.col_year, self.col_mileage, self.col_fuel, self.col_cc,
                         self.col_trans ,self.col_grade]
            
            
            checked_checkBoxes = [False for i in range(0, 8)]
            indices = []
            for i in range(0,8):
                
                if checkBoxes[i].isChecked():
                    checked_checkBoxes[i] = True
                    indices.append(i)
                else:
                    checked_checkBoxes[i] = False
                    
            
            if indices[0] in [0,1,4,6,7] and ((str(algo) == 'Count Sort') or (str(algo) == 'Radix Sort') or (str(algo) == 'Bucket Sort')):
                # logging.info(str(indices[0]))
                raise TypeError('On String argument this sorting filter is not applicable.')  

            start_time = datetime.now()
            if str(algo) == 'Insertion Sort':
                    # print(indices[0])
                self.source_list = Sorting.InsertionSort(self.source_list, type_to_pass,indices[0])
                self.reset(self.source_list)
                isSorted = True
            
            elif str(algo) == 'Merge Sort':
                self.source_list = Sorting.mergeSort(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Bubble Sort':
                self.source_list = Sorting.BubbleSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Tim Sort':
                self.source_list = Sorting.TimSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Selection Sort':
                self.source_list = Sorting.SelectionSort(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)    
            
            elif str(algo) == 'Heap Sort':
                self.source_list = Sorting.HeapSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)  
            
            elif str(algo) == '3-way Merge Sort':
                self.source_list = Sorting.ThreeWayMergeF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Quick Sort': #Not Working
                self.source_list = Sorting.QuickSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Cocktail Sort':  #Not Working
                self.source_list = Sorting.CocktailSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
                
            elif str(algo) == 'Count Sort':   
                self.source_list = Sorting.CountingSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Radix Sort':
                self.source_list = Sorting.RadixSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            elif str(algo) == 'Bucket Sort':    #Not Working
                self.source_list = Sorting.BucketSortF(self.source_list,type_to_pass,indices[0])
                self.reset(self.source_list)
            
            end_time = datetime.now()
            time_diff = (end_time - start_time)
            time_diff = time_diff.total_seconds() * 1000
            time_diff = round(time_diff,3)
            # algo = 'Insertion Sort'

            self.lbl_algo_stat.setText(str(algo))
            self.lbl_time_stat.setText(str(time_diff))
            
        except Exception as e:
            logging.exception(str(e))

    def fill_table(self, list):  # Fill Table with entries
        self.table_entities.setColumnWidth(0, 200)
        self.table_entities.setColumnWidth(1,100)
        self.table_entities.setRowCount(len(list[0]))

        # row = 0
        for i in range(0, len(self.source_list[0])):
            
            self.table_entities.setItem(i, 0, QTableWidgetItem(str(self.source_list[0][i])))
            self.table_entities.setItem(i, 1, QTableWidgetItem(str(self.source_list[1][i])))
            # print(item[2])
            self.table_entities.setItem(i, 2, QTableWidgetItem(str(self.source_list[2][i])))
            self.table_entities.setItem(i, 3, QTableWidgetItem(str(self.source_list[3][i])))
            self.table_entities.setItem(i, 4, QTableWidgetItem(str(self.source_list[4][i])))
            self.table_entities.setItem(i, 5, QTableWidgetItem(str(self.source_list[5][i])))
            self.table_entities.setItem(i, 6, QTableWidgetItem(str(self.source_list[6][i])))
            self.table_entities.setItem(i, 7, QTableWidgetItem(str(self.source_list[7][i])))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
