import sqlite3
import pandas as pd


class database:
    
    con = init_db()
    
    def init_db():
        con = sqlite3.connect('main_db.db')
        # cur=con.cursor()
        # cur.execute()
        
    def import_df(csv):
        df=pd.read_csv(csv)
        # import df inidividually, and then cat all csv to one main
        
    
    def import_gdf(shpefle):
        
        
    def query(con):
        query_df=pd.read_sql_query()
        return(con, cur)
    
    def close_db(con):
        con.close()
    
    

