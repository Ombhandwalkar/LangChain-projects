import os 
import pandas as pd
from typing import List
from datetime import datetime,date

""" A class for handling the storage of chatbot conversation history by writing chat logs to csv file """
class Memory:

    # Wite most recent chatbot interaction to csv file
    @staticmethod
    def write_chat_history_to_file(gradio_chatbot:List ,thread_id:str ,folder_path:str )->None:
        """
        The log include thread ID and timestamp of interaction

        Args:
            gradio_chatbot= 
                A list containing tuple of users query and chatbot interactions. 
                The most recent interactions appended to the log.
            thread_id= 
                unique identifier for chat session 
            folder_path= 
                The directory where chat log CSV files should be stored.
        """
        # Convert tuple into list
        temp_list=list(gradio_chatbot[-1])

        # Today's Day
        today_str=date.today().strftime('%Y-%m-%d')
        temp_list.insert(0,thread_id)

        current_time_str=datetime.now().strftime('%H:%M:%S')
        temp_list.insert(1,current_time_str)

        # Today's file name to converastion
        file_path=os.path.join(folder_path,f'{today_str}.csv')
        new_df=pd.DataFrame([temp_list],columns=['thread_id','timestamp','user_query','response'])

        # Store in file directory
        if os.path.exists(file_path):
            new_df.to_csv(file_path,mode='a',header=False,index=False)
        else:
            new_df.to_csv(file_path,mode='w',header=False,index=False)