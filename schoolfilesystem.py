
#Libraries you may need:
import csv
import os
import pandas as pd



#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = []


    def process_file(self, file_path):   
        try:
            file_extension = file_path.split('.')[-1]
            
            if file_extension == 'csv':
                self.data = pd.read_csv(file_path)
            elif file_extension == 'xlsx':
                self.data = pd.read_excel(file_path)
            elif file_extension == 'txt':
                with open(file_path, 'r') as file:
                    return file.read()
            else:
                print("Unsupported file format")   

        except Exception as e:
            print(f"Error reading file: {str(e)}")


    def transfer_data(self, old_file_path, new_file_path):
        try:
            with open(new_file_path, 'a') as file:
                file.write(self.process_file(old_file_path))
        except UnicodeDecodeError:
            print("Error: Could not read file")

        
    def fetch_web_data(self):
        pass

    def analyze_content(self):
        pass

    def generate_summary(self):
        pass



if __name__ == "__main__":
    analyzer = SchoolAssessmentSystem()
    
    analyzer.process_file("test.csv")


# Analyze content & display result area

            

