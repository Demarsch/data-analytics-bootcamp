# Stock Performance Analysis

## What is this about?

In this assignment I'm going to analyze 90 Mb of the stock exchange data that contain daily information on stocks prices (open, close, high, low) and trade volumes for three years (2014 - 2016). My goal is to find the best and the worst performers among all tickers and the one that has accumulated the largest trade volume.

## What is Inside

- The original file with stock data is too large so it makes no sense to keep it here. Instead I have the VB loose files that can be imported into Excel spreadsheet with the stock data and then a macros inside it can be executed to achieve the desired result. 

- Also you can find here the screenshots with the actual statistics (the results of running this macros) for each year for the original 90Mb file.

### Statistics for 2014

![Statistics for 2014](Screenshots/Statistics%202014.png)

### Statistics for 2015

![Statistics for 2015](Screenshots/Statistics%202015.png)

### Statistics for 2016

![Statistics for 2016](Screenshots/Statistics%202016.png)

## Performance Considerations

Since the stock data inside published Excel spreadsheet is already sorted first by ticker and then by trade date, this solution doesn't invole manual sorting and using of map (dictionary) data structure thus its complexity is at its theoretical limit of __O(n)__. 

On my machine (Intel Core I5-7400, 8 GB RAM, Win10 x64) a 90 Mb file is processed in 35-38 seconds.
