# Capital Markets Loan-Cash-Flow-Model

The goal of this application is to automate the forecasted cash flow from the monthly sale of loans generated from a sales center. It was written in python and built with tkinter, pandas, and numpy_financial libraries. 

Below is the opening interface of the app. First, click on View Menu to view the optional length of the models. 

![image](https://user-images.githubusercontent.com/44985594/230700094-3938ab18-496e-46dd-8da9-0c80b439a8e3.png)

Next, The user selects model desired by length of month - 12 months, 24 months, etc. 

![image](https://user-images.githubusercontent.com/44985594/230701026-07cd80d3-28b9-4a59-8630-32d30c854710.png)

Next, they input the forecasted loan amounts for each month, the interest rate for the loans, the term length of the loans, the SMM (single monthly mortality) rate, along with the assumed default rate. Once these have been inputted, click calculate to receive the generated results.

![image](https://user-images.githubusercontent.com/44985594/230701271-ffb9325e-7435-4641-b4ce-bfc88983ce0c.png)

This will generate an excel file that will create individual tabs for each month of forecasted loan sales - 12 months model will have an excel file with 12 tabs and the loan amortization schdule for this group of loans. The generated fields are beginning balance, payment, interest, principal, scheduled principal received, prepaid principal, charge-off principal, total principal collections, net outstanding balance, and ending balance.

These fields and metrics are relevant to us when conducting forecasted loan sales growth for sales centers and their potential cash flow.
