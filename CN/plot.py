import pandas
import matplotlib
import mpl_finance
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

matplotlib.style.use("ggplot")

def stockPricePlot(ticker):
    # Step 1. Load data
    history = pandas.read_csv("result/"+ticker+".csv",parse_dates=True,index_col=0)
    # Step 2, Data Manipulation
    close = history["close"]
    close = close.reset_index()
    print(close['timestamp'])
    close['timestamp']=close['timestamp'].map(matplotlib.dates.date2num)
    print(close['timestamp'])
#    close['timestamp'] = matplotlib.dates.datestr2num(close['timestamp'])

    ohlc = history[['open','high','low','close']].resample("1H").ohlc()
    ohlc = ohlc.reset_index()
    print(ohlc['timestamp'])
    ohlc['timestamp'] = ohlc['timestamp'].map(matplotlib.dates.date2num)
    print(ohlc['timestamp'])
    # Step 3, Plot figures. Subplot 1: scatter plot. Subplot 2 candlestick plot
    # Step 3.1 subplot 1 : scatter plot
    pdf = PdfPages('cut_figure.pdf')
    plt.figure()
    subplot1 = plt.subplot2grid((2,1),(0,0),rowspan=1,colspan=1)
    subplot1.xaxis_date()
    subplot1.plot(ohlc['timestamp'],ohlc['close'],'b.')

    # Step 3.2
    subplot2 = plt.subplot2grid((2,1),(1,0),rowspan=1,colspan=1,sharex=subplot1)
    mpl_finance.candlestick_ohlc(ax=subplot2,quotes=ohlc.values,width=0.01,colorup="r",colordown="g")
    pdf.savefig()
    plt.show()
    plt.close()
    pdf.close()

stockPricePlot("600031")
