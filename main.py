import pandas as pd
import numpy as np
import os

class CreateQualityReport():
    def __init__(self):
        self.results_df = pd.read_excel('data/Results.xlsx')
        self.site_list_df = pd.read_excel('data/SiteList.xlsx')
        
        self.merge_dfs()
        self.search_data()
        
        return
    
    def save_csv(self, dataframe):
        if not os.path.exists('results'):
            os.mkdir('results')
            
        dataframe.to_excel('results/quality-report-2023.xlsx')
        
        return
        
    def merge_dfs(self):
        site_name_list = list(self.site_list_df['Site Name'])
        final_df = self.results_df.loc[self.results_df['Site Name'].isin(site_name_list)]
        self.complete_df = final_df
        final_df = final_df.drop(['City', 'Alerts'], axis=1)
        final_df = final_df.set_index('Site ID')
        final_df = final_df.sort_values('State')
        
        self.save_csv(final_df)
        
        return
        
    def search_active_warnings(self):
        active_warnings = self.complete_df[self.complete_df['Alerts'] == 'Yes']
        sites_names = list(active_warnings['Site Name'])
        
        print("Lista de sites com alertas ativos:")
        for site_name in sites_names:
            print(site_name)
            
        return
        
    def get_quality_average(self):
        quality_array = np.array(self.complete_df['Quality (0-10)'])
        average_quality = int(round(np.mean(quality_array), 0))
        
        print(f"A média de qualidade dos sites é: {average_quality}")
        
        return
    
    def get_less_10mbps(self):
        less_10mbps_sites = self.complete_df[self.complete_df['Mbps'] < 10]
        less_10mbps_sites_names = less_10mbps_sites['Site Name']
        
        print("Lista de sites com menos de 10 Mbps:")
        for site_name in less_10mbps_sites_names:
            print(site_name)
        
        return
    
    def search_data(self):
        while True:      
            print("-----------------------")
            print("Selecione a busca que deseja fazer, ou digite 4 para sair:")
            print("1 - Sites com alertas ativos")
            print("2 - Média de qualidade dos sites")
            print("3 - Sites com menos de 10 Mbps")
            print("4 - Sair")
            
            input_value = int(input("Sua escolha: "))
            
            print("-----------------------")            
            
            if input_value == 1:
                self.search_active_warnings()
            elif input_value == 2:
                self.get_quality_average()
            elif input_value == 3:
                self.get_less_10mbps()
            if input_value == 4:
                break
            
if __name__ == '__main__':
    CreateQualityReport()
        
