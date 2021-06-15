import sys
import PyPluMA

class ReadingFramePlugin:
    def input(self, inputfile):
       csvfile = open(inputfile, 'r')
       self.firstline = csvfile.readline().strip().split(',')
       self.start_idx = self.firstline.index("start")
       self.end_idx = self.firstline.index("end")
       self.firstline.insert(self.end_idx+1, "readingFrame")
       
       self.data = []
       self.data.append(self.firstline)
       for line in csvfile:
           self.data.append(line.strip().split(','))
       
    def run(self):
       self.data[1].insert(self.end_idx+1, -1)
       for i in range(2, len(self.data)):
           self.data[i].insert(self.end_idx+1, int(self.data[i][self.start_idx])-int(self.data[i-1][self.end_idx]))


    def output(self, filename):
       outfile = open(filename, 'w')
       for element in self.data:
           for i in range(0, len(element)):
              outfile.write(str(element[i]))
              if (i == len(element)-1):
                  outfile.write("\n")
              else:
                  outfile.write(',')


