import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tabulate

class HeartAttackAnalyzer:
    def __init__(self, patient_info_path, diagnosis_info_path):
        self.patient_info_path = patient_info_path
        self.diagnosis_info_path = diagnosis_info_path
        self.df = None

    def load_and_merge(self):
        """Loads and merges patient and diagnosis data"""
        patient_info = pd.read_csv(self.patient_info_path)
        diagnosis_info = pd.read_csv(self.diagnosis_info_path)
        self.df = pd.merge(patient_info, diagnosis_info, on='Patient_ID')
        print("✅ Data loaded and merged successfully.")
        print(tabulate(self.head(10), headers='keys', tablefmt='fancy_grid'))

    def plot_risk_distribution(self):
        """Plots count of patients by risk level"""
        if self.df is None:
            print("❌ Data not loaded. Call load_and_merge() first.")
            return
        sns.set(style='whitegrid')
        plt.figure(figsize=(6, 4))
        sns.countplot(data=self.df, x='Risk_Level', palette='Blues')
        plt.title('Number of Patients by Risk Level')
        plt.xlabel('Risk Level')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()

    def plot_blood_sugar_by_risk(self):
        """Plots boxplot of blood sugar levels per risk level"""
        if self.df is None:
            print("❌ Data not loaded. Call load_and_merge() first.")
            return
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=self.df, x='Risk_Level', y='Blood sugar', palette='Blues')
        plt.title('Blood Sugar Distribution Across Risk Levels')
        plt.xlabel('Risk Level')
        plt.ylabel('Blood Sugar (mg/dL)')
        plt.tight_layout()
        plt.show()