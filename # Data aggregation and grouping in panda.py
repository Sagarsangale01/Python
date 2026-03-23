# Data aggregation and grouping in pandas

# Grouping Data by Categories
    # Why group Data? -- Grouping of data allows you to perform operation on subsets of data based on shared categories
    # goupby in pandas
    # Syntax
    grouped = df.groupby("column_name")
    
    # Operations 
       #1. Iterate over groups
        for name, group in grouped:
            print(name)
            print(group)

        #2. Apply aggregation
            grouped.mean()
            grouped.sum()
            
    ## Aggregation Functions :
        #1. Using groupby: we can combine grouping with aggregation methods
        
        df.groupby("category_column")["numeric_column"].mean()
        df.groupby("category_column").agg({"numeric_column": ["mean", "max", "min"]})

        #2.   Using pivot_table: reshape the data with aggregation 
        pivot = df.pivot_table(
            values="numeric_column",
            index = "category_column",
            aggfunc ="mean"
        )   

        #3. Custom Aggregation: apply custom functions using agg function 
            # Apply custom functions using .agg()
        def rang_function(x):
            return x.max()-x.min()
        
        df.groupby("category_column")["numeric_column"].agg(rang_function)
        
## Calculating summary statistics for Grouped Data
    # Common Statistics:
        # Mean
        df.groupby("category_column")["numeric_column"].mean()
        # Max
        df.groupby("category_column")["numeric_column"].max()
        # Min 
        df.groupby("category_column")["numeric_column"].min()
    
    # Multi Aggregation 
    df.groupby("category_column").agg(
        {"numeric_column":["mean","max","min"]}
        )    

