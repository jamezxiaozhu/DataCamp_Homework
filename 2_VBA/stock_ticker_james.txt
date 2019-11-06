Attribute VB_Name = "Module1"
Sub stock_ticker()
 'loop through each sheet
 Dim ws As Worksheet
 
 For Each ws In Worksheets

     ' Set an initial variable for holding the ticker name and next row ticker
     Dim ticker_name As String
     Dim next_row_ticker_name As String
     ' Set an initial variable for holding the open price
     Dim open_price As Double
     open_price = ws.Range("c2").Value
     
     ' Set an initial variable for holding the close price
     Dim close_price As Double
     
     
     ' Set an initial variable for holding the total volume
     Dim total_vol As Variant
     
     'headers for summary table
     ws.Range("I1").Value = "Ticker"
     ws.Range("J1").Value = "Yearly Change"
     ws.Range("K1").Value = "Percentage Change"
     ws.Range("L1").Value = "Total Stock Volume"
     ' Keep track of the location for ticker in the summary table
     Dim Summary_Table_Row As Long
     Summary_Table_Row = 2
    
     ' Loop through all rows
     Dim i, last_row As Long
     last_row = CLng(ws.Cells(Rows.Count, 1).End(xlUp).Row)
    
     For i = CLng(2) To last_row
       ' Check if we are still within the same ticker,
       ticker_name = ws.Cells(i, 1).Value
       next_row_ticker_name = ws.Cells(i + 1, 1).Value
       If next_row_ticker_name = ticker_name Then
         ' Add to the total volume
         total_vol = CDec(total_vol) + CDec(ws.Cells(i, 7).Value)
    
       Else
         ' Add to the total volume
         total_vol = CDec(total_vol) + CDec(ws.Cells(i, 7).Value)
         'close price
         close_price = ws.Cells(i, 6).Value
         ' Print the ticker in the Summary Table
         ws.Range("I" & Summary_Table_Row).Value = ticker_name
         ' Print the change in open and close
         ws.Range("J" & Summary_Table_Row).Value = close_price - open_price
         'ws.Range("J" & Summary_Table_Row) = Format(ws.Range("J" & Summary_Table_Row), "0.0000")
         
         ' check if change is zero, Print the change in open and close difference
         If ws.Range("J" & Summary_Table_Row).Value = 0 Or open_price = 0 Then
         ' Testing:Or IsError((close_price - open_price) / open_price) Or close_price - open_price = 0 Or open_price = 0 Or close_price = 0 Then
            ws.Range("K" & Summary_Table_Row).Value = 0
         Else
            ws.Range("K" & Summary_Table_Row).Value = CDbl(close_price - open_price) / open_price
         
         End If
         
         'Format to %
         ws.Range("K" & Summary_Table_Row) = Format(ws.Range("K" & Summary_Table_Row), "0.00%")
         ' Print the total volume to the Summary Table
         ws.Range("L" & Summary_Table_Row).Value = total_vol
         ' Add one to the summary table row
         Summary_Table_Row = Summary_Table_Row + 1
         ' Reset the total volume, open price and close price
         total_vol = 0
         open_price = ws.Cells(i + 1, 3).Value
         close_price = 0
         
       End If
    
     Next i
     
    'conditional formatting 0< red, >0 green, =0 yellow
    Dim j, last_row_summary_table As Long
    last_row_summary_table = CLng(ws.Cells(Rows.Count, 10).End(xlUp).Row)
    
    For j = CLng(2) To last_row_summary_table
        If ws.Cells(j, 10).Value = 0 Then
            ws.Cells(j, 10).Interior.ColorIndex = 6
        ElseIf ws.Cells(j, 10) > 0 Then
            ws.Cells(j, 10).Interior.ColorIndex = 4
        Else
            ws.Cells(j, 10).Interior.ColorIndex = 3
        End If
    Next j
    last_row_summary_table = 0
    Next
    MsgBox ("Done!")

End Sub

