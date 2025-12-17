import pandas as pd
import re
import streamlit as st

def file_uploader():
    file_data = st.file_uploader("Please upload the media mentions file", type=["xlsx"])
    data_base_raw = st.file_uploader("Please upload the Y/N keyword and Sheet2 file", type=["xlsx"])
    if file_data is not None and data_base_raw is not None:
        st.success("Files uploaded successfully!")
        if st.button("Process File"):
            st.write("Files processing started...")
            
            # Read the Excel file raw data
            data_file = pd.ExcelFile(file_data,engine='openpyxl')
            sheet_names = data_file.sheet_names[0] # We want only the first sheet
            data = pd.read_excel(data_file, sheet_name=sheet_names)
            
            # loading the file for the Y, N, keyword, Sheet2
            
            data_base = pd.ExcelFile(data_base_raw,engine='openpyxl')
            
            # reading the Unique Y sheet
            unique_Y_sheet = data_base.sheet_names[1]
            unique_Y = pd.read_excel(data_base, sheet_name=unique_Y_sheet)
            
            # reading the Unique N sheet
            unique_N_sheet = data_base.sheet_names[3]
            unique_N = pd.read_excel(data_base, sheet_name=unique_N_sheet)
            
            # reading the keywords sheet
            keywords_sheet = data_base.sheet_names[5]
            keywords = pd.read_excel(data_base, sheet_name=keywords_sheet)
            
            # reading the Sheet2 sheet
            Sheet2_sheet = data_base.sheet_names[4]
            Sheet2 = pd.read_excel(data_base, sheet_name=Sheet2_sheet)
            
            # reading the junkwords sheet
            junkwords_sheet = data_base.sheet_names[6]
            junkwords = pd.read_excel(data_base, sheet_name=junkwords_sheet)
            
            # reading the exclude list sheet
            exclude_list_sheet = data_base.sheet_names[7]
            exclude_list_df = pd.read_excel(data_base, sheet_name=exclude_list_sheet)

            # Removing the unwanted columns from the dataframe
            new_file_data = data[[ 'Title','Text','URL', 'Author', 'Nickname','Profile','Subscribers','Source','Resource type','Potential reach']]
            
            # Removing the Blogs and Forums from the Resource type column
            new_file_data = new_file_data[~new_file_data['Resource type'].isin(['Blog','Forum'])]
            
            # Creating the media mention column
            new_file_data.loc[new_file_data['Nickname'].isin(unique_Y['Influencer']), 'media mention'] = 'Y'
            new_file_data.loc[new_file_data['Nickname'].isin(unique_N['Influencer']), 'media mention'] = 'N'
            new_file_data.loc[new_file_data['Nickname'].isin(unique_Y['Influencer']) & new_file_data['Nickname'].isin(unique_N['Influencer']), 'media mention'] = 'Found in both'
            new_file_data['relevant'] = ''

            # Creating the Combine and combine Text columns
            new_file_data['Combine'] = new_file_data['URL'].astype(str) + new_file_data['Author'].astype(str) + new_file_data['Nickname'].astype(str)
            new_file_data['combine Text'] = new_file_data['Title'].astype(str) + new_file_data['Text'].astype(str)
            
            # Converting to set SHHEET CODE
            Sheet2 = Sheet2['User Name'].tolist()
            sheet_2 = set(Sheet2)

            def assign_value(influencer):
                if influencer in sheet_2:
                    return influencer  # or any value you want to assign
                else:
                    return None 

            new_file_data['Sheet2'] = new_file_data['Nickname'].apply(assign_value)


            key_pattern = '|'.join(keywords['Keywords'].tolist())  # 'reporter|journalist|editor'

            # Extract the matched word from the url (if any)
            new_file_data['Keywords'] = new_file_data['Combine'].str.extract(f'({key_pattern})', flags=re.IGNORECASE)
            
            # Adding | operator for the regex 
            junk_pattern = '|'.join(junkwords['Junk'].tolist())

            # creating the Junk column
            new_file_data['Junk'] = new_file_data['combine Text'].str.extract(f'({junk_pattern})',flags=re.IGNORECASE)
            
            # adding the | operator
            exclude_pattern = '|'.join(exclude_list_df['Exclude'].tolist())

            # creating the junk exculde column
            new_file_data['Exclude'] = new_file_data['Combine'].str.extract(f'({exclude_pattern})',flags=re.IGNORECASE)
            
            
            # Rearranging the columns
            new_file_data = new_file_data[['Title','Text','Combine','combine Text','URL','Profile','Subscribers','Source','Resource type','Potential reach','Author', 'Nickname','media mention','relevant','Sheet2','Keywords','Junk','Exclude']]

            
            
            # showing the dataframe
            new_file_data.replace(pd.NA, '', inplace=True)
            st.write("Here is a preview of the uploaded data:")
            st.dataframe(new_file_data)
            
            

col1, col2, col3 = st.columns([0.1,4,1])
with col3:
    st.image('https://www.netimpactlimited.com/wp-content/uploads/2024/04/NetImpact-Logo-Final-Web-2.png')
with col2:
    st.subheader(f'Media Mention Report Generator')

file_uploader()
    
