import sqlite3
import pandas as pd


class database:
    
    
    
    def init_db():
        con = sqlite3.connect('main_db.db')
        print(con)
        # cur=con.cursor()
        # cur.execute()
        return(con)
      
    def import_df(csv):
        df=pd.read_csv(csv)
        # import df inidividually, and then cat all csv to one main
        return(df)
        
    
    # def import_gdf(shpefle):
    #  ##   
        
    def query(con):
        query_df=pd.read_sql_query()
        return(query_df)
    
    def close_db(con):
        con.close()
    

if __name__=="__main__":
    database.init_db()
