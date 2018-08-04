VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Stock"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Public Ticker As String

Public TotalVolume As Double

Public OpenPrice As Double

Public ClosingPrice As Double

Property Get AbsolutePriceChange() As Double
    AbsolutePriceChange = ClosingPrice - OpenPrice
End Property

Property Get RelativePriceChange() As Double
    If OpenPrice = 0 Then
        RelativePriceChange = 0
    Else
        RelativePriceChange = ClosingPrice / OpenPrice - 1
    End If
End Property




