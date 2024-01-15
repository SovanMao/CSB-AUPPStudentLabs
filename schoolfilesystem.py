
#Libraries you may need:
import csv
import os
import pandas as pd
import openpyxl


#classes and Functions to implement
class SchoolAssessmentSystem:

    def __init__(self):
        self.data = pd.DataFrame()


    def process_file(self, file_path):   
        try:
            file_extension = file_path.split('.')[-1]
            
            if file_extension == 'csv':
                self.data = pd.read_csv(file_path)
            elif file_extension == 'xlsx':
                self.data = pd.read_excel(file_path)
            elif file_extension == 'txt':
                with open(file_path, 'r') as file:
                    self.data = file.read()
            else:
                print("Unsupported file format")   

        except Exception as e:
            print(f"Error reading file: {str(e)}")

    def transfer_data(self, input_file_path, output_file_path, criteria):
        # Load data from input file
        self.process_file(input_file_path)

        # Filter data based on criteria
        filtered_data = self.data[self.data[criteria['column']] == criteria['value']]

        # Transfer filtered data to output file
        filtered_data.to_excel(output_file_path, index=False)
    

        
    # def fetch_web_data(self):
    #     pass

    # def analyze_content(self):
    #     pass

    # def generate_summary(self):
    #     pass




run = SchoolAssessmentSystem()
run.process_file("te1.csv")
print(run.data)

run.transfer_data('te1.csv',  'output.xlsx', {'column': 'ID', 'value': 'A'})

# Analyze content & display result area

            

