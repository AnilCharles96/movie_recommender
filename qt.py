import sys
from PySide2.QtWidgets import QApplication, QMainWindow
#from PySide2.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow
import findspark
findspark.init('C:/spark')
from pyspark.sql import SparkSession,Row
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import lit
from PySide2.QtCore import Slot




class MainWindow(QMainWindow):
    
    def __init__(self):
        
        super(MainWindow,self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)       
        self.combobox = self.ui.comboBox 
        self.combobox_2 = self.ui.comboBox_2
        self.textedit = self.ui.textEdit
        self.pushbutton = self.ui.pushButton
        self.pushbutton_2 = self.ui.pushButton_2
        self.textedit_2 = self.ui.textEdit_2
        
        
        spark = SparkSession.builder.appName('movierecommed').getOrCreate()
    
        def parsemoviedata(line):
          
            fields = line.split()
            return Row(userid = int(fields[0]),movieid = int(fields[1]),rating = float(fields[2]))    
                    
        def submit():
            
            self.textedit.append(self.combobox.currentText())   
            self.textedit_2.append(self.combobox_2.currentText())
            
        def recommend():
             
            movie_set = self.textedit.toPlainText().split('\n')            
            rating_set = self.textedit_2.toPlainText().split('\n')                      
            movie_set = set(movie_set)
            rating_set = set(rating_set)
                       
            with open('ml-100k/u.useritem','w') as f:
                 for movieid,rating in zip(movie_set,rating_set):
                     f.write('{0}\t{1}\t{2}\t{3}\n'.format(0,self.movie_title_id[movieid],rating,881250949))
                 with open('ml-100k/u.data') as s:             
                     f.write(s.read())
                
            
            moviedata = spark.sparkContext.textFile('ml-100k/u.useritem')
            movieparsed = moviedata.map(parsemoviedata)            
            df = spark.createDataFrame(movieparsed)
            
    
            als = ALS(maxIter=5,regParam=0.01,userCol='userid',itemCol='movieid',ratingCol='rating')
            model = als.fit(df)

            moviecount = df.groupBy('movieid').count().filter('count>100')
            popularmovies = moviecount.select('movieid').withColumn('userid',lit(0))
    
            recommendation = model.transform(popularmovies)
    
            spark.conf.set('spark.sql.crossJoin.enabled','true')
            top10 = recommendation.sort(recommendation.prediction.desc()).take(10)         
            self.top_recommendation(top10)
                    

        # submit button
        self.pushbutton_2.clicked.connect(submit)
        # recommend button
        self.pushbutton.clicked.connect(recommend)
        
    def select_movies(self,moviedict):       
        self.movie_title_id = {value:key for key,value in moviedict.items()}
        self.moviedict = moviedict
        for moviename in moviedict.items():
            self.combobox.addItem(moviename[1])
            
    def select_ratings(self,ratings):
             
        for items in ratings:
            self.combobox_2.addItem(items)
            
    def top_recommendation(self,top10):
        self.textedit.clear()
        self.textedit_2.clear()
        print(top10)
        for recommend in top10:
            #print(moviedict[recommend['movieid']])
            self.textedit.append(self.moviedict[recommend['movieid']])
            self.textedit_2.append('{:.1f}'.format(recommend['prediction']))
                    
        
if __name__ == '__main__':
    
    moviedict = {}
    with open('ml-100k/u.item',encoding='ISO-8859-1') as f: 
        for line in f:     
            fields = line.split('|')    
            #print(fields[1])
            moviedict[int(fields[0])] = fields[1]  
        
     
    items = []
    sum = 1.0
    for i in range(41):
        items.append('{:0.2}'.format(sum))
        sum += float(0.1)    
        
    items = items[::-1]
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
      
    window.select_movies(moviedict)
    window.select_ratings(items)
    
    window.show()    
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    