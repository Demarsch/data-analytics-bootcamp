Attribute VB_Name = "StockStatisticsCalculator"
' Reads the stock data from the specific worksheet a build a collection of stocks
Function ReadStockData(currentWorksheet As Worksheet) As collection
    Dim lastRow as Long
    Dim currentStock As Stock
    Dim currentTicker As String
    Dim lastTicker As String
    Dim result As New collection

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    row = 2
    ' We skip the header line and go until we are out of values
    For row = 2 to lastRow
        currentTicker = currentWorksheet.Cells(row, 1).value
        ' If this is the very first line we process, or this line contains a different ticker than the previous one, we create a new stock
        If lastTicker = "" Or currentTicker <> lastTicker Then
            lastTicker = currentTicker
            Set currentStock = New Stock
            currentStock.Ticker = currentTicker
            currentStock.OpenPrice = currentWorksheet.Cells(row, 3).value
            currentStock.ClosingPrice = currentWorksheet.Cells(row, 6).value
            currentStock.TotalVolume = currentWorksheet.Cells(row, 7).value
            result.Add currentStock
        Else
            ' This is the case when the very first line for this ticker doesn't have open price
            If currentStock.OpenPrice = 0 Then
                currentStock.OpenPrice = currentWorksheet.Cells(row, 3).value
            End If
            ' This is to override current closing price with the last non-zero closing price
            If currentWorksheet.Cells(row, 6) <> 0 Then
                currentStock.ClosingPrice = currentWorksheet.Cells(row, 6)
            End If
            currentStock.TotalVolume = currentStock.TotalVolume + currentWorksheet.Cells(row, 7).value
        End If
        row = row + 1
    Next row
    Set ReadStockData = result
End Function

' Prints the summary of the stocks
Sub PrintStockData(currentWorksheet As Worksheet, stocks As collection, row As Long, column As Integer)
    Dim currentStock As Stock
    Dim i As Long
        
    ' Print the header line
    currentWorksheet.Cells(row, column).value = "Ticker"
    currentWorksheet.Cells(row, column + 1).value = "Yearly Change"
    currentWorksheet.Cells(row, column + 2).value = "Percent Change"
    currentWorksheet.Cells(row, column + 3).value = "Total Stock Volume"
    ' Print the data itself
    row = row + 1
    For i = 1 To stocks.Count
        Set currentStock = stocks(i)
        currentWorksheet.Cells(row, column).value = currentStock.Ticker
        currentWorksheet.Cells(row, column + 1).value = currentStock.AbsolutePriceChange
        currentWorksheet.Cells(row, column + 1).NumberFormat = "0.00"
        If currentStock.AbsolutePriceChange < 0 Then
            currentWorksheet.Cells(row, column + 1).Interior.Color = RGB(255, 199, 206)
            currentWorksheet.Cells(row, column + 1).Font.Color = RGB(156, 0, 6)
        ElseIf currentStock.AbsolutePriceChange > 0 Then
            currentWorksheet.Cells(row, column + 1).Interior.Color = RGB(198, 239, 206)
            currentWorksheet.Cells(row, column + 1).Font.Color = RGB(0, 97, 0)
        ' Strictly speaking this 'else' branch is not required but it is here just in case we decide to print the data
        ' over the range where some other values already reside
        Else
            currentWorksheet.Cells(row, column + 1).Interior.Color = rgbWhite
            currentWorksheet.Cells(row, column + 1).Font.Color = rgbBlack
        End If
        currentWorksheet.Cells(row, column + 2).value = currentStock.RelativePriceChange
        currentWorksheet.Cells(row, column + 2).NumberFormat = "0.00%"
        currentWorksheet.Cells(row, column + 3).value = currentStock.TotalVolume
        currentWorksheet.Cells(row, column + 3).NumberFormat = "General"
        row = row + 1
    Next i
    ' Auto fit all used columns
    For i = 0 To 3
        currentWorksheet.Columns(column + i).AutoFit
    Next i
End Sub

' Calculates stock statistics
Function CalculateStockStatistics(stocks As collection) As StockStatistics
    Dim result As New StockStatistics
    Dim i As Long
    
    For i = 1 To stocks.Count
        If stocks(i).RelativePriceChange > result.MaxIncrease Then
            result.MaxIncrease = stocks(i).RelativePriceChange
            result.MaxIncreaseTicker = stocks(i).Ticker
        End If
        If stocks(i).RelativePriceChange < result.MaxDecrease Then
            result.MaxDecrease = stocks(i).RelativePriceChange
            result.MaxDecreaseTicker = stocks(i).Ticker
        End If
        If stocks(i).TotalVolume > result.MaxTotalVolume Then
            result.MaxTotalVolume = stocks(i).TotalVolume
            result.MaxTotalVolumeTicker = stocks(i).Ticker
        End If
    Next i
    Set CalculateStockStatistics = result
End Function

' Prints stock statistics
Sub PrintStockStatistics(currentWorksheet As Worksheet, statistics As StockStatistics, row As Long, column As Integer)
    currentWorksheet.Cells(row, column).value = ""
    currentWorksheet.Cells(row, column + 1).value = "Ticker"
    currentWorksheet.Cells(row, column + 2).value = "Value"
    
    currentWorksheet.Cells(row + 1, column).value = "Greatest % Increase"
    currentWorksheet.Cells(row + 1, column + 1).value = statistics.MaxIncreaseTicker
    currentWorksheet.Cells(row + 1, column + 2).value = statistics.MaxIncrease
    currentWorksheet.Cells(row + 1, column + 2).NumberFormat = "0.00%"
    
    currentWorksheet.Cells(row + 2, column).value = "Greatest % Decrease"
    currentWorksheet.Cells(row + 2, column + 1).value = statistics.MaxDecreaseTicker
    currentWorksheet.Cells(row + 2, column + 2).value = statistics.MaxDecrease
    currentWorksheet.Cells(row + 2, column + 2).NumberFormat = "0.00%"
    
    currentWorksheet.Cells(row + 3, column).value = "Greatest Total Volume"
    currentWorksheet.Cells(row + 3, column + 1).value = statistics.MaxTotalVolumeTicker
    currentWorksheet.Cells(row + 3, column + 2).value = statistics.MaxTotalVolume
    ' Auto fit all used columns
    For i = 0 To 2
        currentWorksheet.Columns(column + i).AutoFit
    Next i
End Sub


' Performs stock data reading, analyzing and displaying for specific worksheet
Sub ProcessWorksheet(currentWorksheet As Worksheet)
    Dim row As Long
    Dim stocks As collection
    Dim statistics As StockStatistics
    
    Set stocks = ReadStockData(currentWorksheet)
    PrintStockData currentWorksheet, stocks, 1, 9
    
    Set statistics = CalculateStockStatistics(stocks)
    PrintStockStatistics currentWorksheet, statistics, 1, 15
End Sub

' Performs stock data reading, analyzing and displaying for all worksheets of the current workbook
Sub Run()
    Dim startedAt As Date
    
    startedAt = Time
    For i = 1 To Worksheets.Count
        ProcessWorksheet Worksheets(i)
    Next i
    MsgBox ("Done. Time elapsed: " + Format(Time - startedAt, "hh:mm:ss"))
    
End Sub
