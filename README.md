# Moving Average 

Moving Average (MA) is a commonly used signal processing technique for time series data. Applying different weightings on current and various past values, it aims to filter/diminish the effect of noises and outlines; and therefore generate a smooth curve describing the long term behaviour.

In this example, we will employ a 3rd party library 'TA-LIB' as illustration. In fact, 'TA-LIB' supports many kind of MAs, including Least Squares MA, Simple MA, Exponential MA, Triangular MA, Welles MA, Variable MA, Volume Adjusted MA, etc. For our example, we arbitrarily choose simple Moving Average (SMA), which applies an equally weighted decay factor. That means, the recent values will carry the same contribution as the past values to the calculation. Besides, the weight function is specified using a time period 'n'. Mathematically,

![formula_SMA](https://github.com/user-attachments/assets/98646d8d-062a-451d-b270-a9bfe9c5e7a7)

Now, we can move to discuss the trading logic. We will firstly construct 2 SMAs with different time period 'n' (i.e. fast and slow) so as to estimate the speed of current trend. If the fast SMA surpass the slow SMA and both SMAs are in upward sloping, in terms of technical analysis, it is named as 'Golden Cross' and suggests a buy signal. On the other hand, if the fast SMA drop below the slow SMA and both SMAs are in downward sloping, it is technically said to be a 'Death Cross' and suggest a sell signal.

![MACross](https://github.com/user-attachments/assets/b2908505-f5f2-412e-9533-c349174d58c0)

The rationale of this strategy is that those 'Crosses' can be mathmatically viewed as turning points indicating the local maximum/minimum of the speed of price change (i.e. f''(x) = 0 ), which therefore provide a high chance to gain a short term profit. Some key points to apply this strategy is summarized below.

'Cross' simply provides an entry signal, think about when to exit
different combination of slow and fast period might provide different prediction results
the entry signal might be enhanced using other smoothing techniques, or multiple MAs cross

In below coding sample, we use 'on_bulkdatafeed' API as demonstration. Suppose we are looking at 1 day bar, and choose the fast and slow period as 7-day and 14-day respectively. Also, we set 10% for both take profit and stop loss. The backtest setting is initialized as follows.

Strategy Name = 'demo_MA' <br>
Backtest Start Month = '2017-01'<br>
Backtest End Month = '2017-12'<br>
Data Interval = 1 day<br>
Initial Capital = 100000<br>
Base Currency = HKD<br>
Leverage = 50<br>
Transaction Cost = 0<br>
Allow Short Sell = True<br>
Instruments = ['HKXHKD']
