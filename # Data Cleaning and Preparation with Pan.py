# Data Cleaning and Preparation with Pandas
 # Handling Missing values
    # Why Handle Missing Values? -- Missing data can affect analysis and model performance.
    
    # Methods to handle missing values
      #1) Drop Missing values  
      
    df = df.dropna()   #-- dropna  it drop rows with any missing values 
    df = df.dropna(axis=1)  #-- it drop columns with missing values
     
      #2) FIll Missing Values
    
    df["column_name"] = df["column_name"].fillna(0)  #-- it fill given column with the 0 value 
    
    # 2 types of fill:
        
        #1 forward fill:
        df.fillna(method="ffill")
                
        #2 Backward Fill:
        df.fillna(method="bfill")

    
      
      #3) Interpolation
    
        # liner interpolation:
    
         df["column_name"] = df["column_name"].interpolate()     #-- this will add values based on interpolation         
    

    
    
###  Data Transformation

    # Renaming Columns 
    df = df.rename(columns={"old_name": "new_name"})
    
    # Changing Data Types
    df["column_name"] = df["column_name"].astype("float")
    df["column_name"] = pd.to_datetime(df["column_name"])
           
    # Creating or modifying columns 
    df["new_column"] = df["existing_column"] *2
    
    
## Combining and merging DataFrames

    #1. Concatenation -- Combine dataframs along rows and columns
    
        combined = pd.concat([df1, df2], axis=0)   #-- combine two different datafrems based on rows  
        combined = pd.concat([df1, df2], axis=1)  #-- combine two different datafrems based on columns 


    #2. Merging  -- it merges the dataframe based on key and condition

    merged = pd.merge(df1, df2, on="common_column")  #-- merge with common columns
    merged = pd.merge(df1, df2, how="left", on="common_column")  #-- left join
    merged = pd.merge(df1, df2, how="inner", on="common_column")  #-- Inner join

    #3. Joining  -- 

    joined = df1.join(df2, how="inner")
   
   
    
    