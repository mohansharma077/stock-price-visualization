import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def main():
    # Load the custom CSS

    st.title("Real-time Stock Price Data")
    a = st.text_input("Enter Company Symbol:")
    b = st.text_input("Enter the range in month(e.g. 1 month, 2 month) ")

    if a and b:
        try:
            stock = yf.Ticker(a)
            stock_info = stock.info

            st.subheader("Stock Information:")
            st.write(f"Company Name: {stock_info.get('longName', 'N/A')}")
            st.write(f"Ticker Symbol: {stock_info.get('symbol', 'N/A')}")
            st.write(f"Exchange: {stock_info.get('exchange', 'N/A')}")
            st.write(f"Industry: {stock_info.get('industry', 'N/A')}")
            st.write(f"Website: {stock_info.get('website', 'N/A')}")
            st.write("---")

            hist = stock.history(period=b+"mo")
            if not hist.empty:
                # Customize plot colors and styles
                fig, ax = plt.subplots(figsize=(12, 8))
                ax.plot(hist.index, hist["Close"], color='blue', linestyle='-', linewidth=2, label="Close Price")
                ax.set_title("Stock Prices", fontsize=20)
                ax.legend()
                ax.grid()

                # Format x-axis dates to show month and day
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

                # Display the plot using st.pyplot()
                st.pyplot(fig)

            else:
                st.write(f"No historical data available for '{a}'. Please enter a valid company name.")

            # Show additional data in a user-friendly format
            st.subheader("History Metadata:")
            st.table(stock.history_metadata)

            st.subheader("Actions (Dividends, Splits, Capital Gains):")
            st.table(stock.actions)

            st.subheader("Dividends:")
            st.table(stock.dividends)

            st.subheader("Splits:")
            st.table(stock.splits)

            st.subheader("Financials (Income Statement):")
            st.table(stock.income_stmt)

            st.subheader("Balance Sheet:")
            st.table(stock.balance_sheet)

            st.subheader("Cash Flow Statement:")
            st.table(stock.cashflow)

            st.subheader("Major Holders:")
            st.table(stock.major_holders)

            st.subheader("Institutional Holders:")
            st.table(stock.institutional_holders)

            st.subheader("Mutual Fund Holders:")
            st.table(stock.mutualfund_holders)

            st.subheader("Earnings Dates:")
            st.table(stock.earnings_dates)

            st.subheader("ISIN code:")
            st.write(stock.isin)

            st.subheader("Options Expirations:")
            st.write(stock.options)

            st.subheader("News:")

            for news_info in stock.news:
                # Show the title as a subheader
                st.subheader(news_info["title"])
                # Show the clickable link to the full news article
                st.markdown(f"[Read More]({news_info['link']})")

                # Add a horizontal line to separate news items
                st.markdown("---")

        except Exception as e:
            st.write(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()

