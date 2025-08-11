import yfinance as yf

def get_stock_price(symbol: str) -> str:
    # 주식 정보 가져오기
    stock = yf.Ticker(symbol)

    # 최근 일일 거래 데이터 불러오기
    hist = stock.history(period="1d")

    # 데이터가 없는 경우 예외 처리
    if hist.empty:
        return f"{symbol} 주가 정보를 찾을 수 없습니다."

    # 가장 최근 종가 가져오기
    price = hist["Close"].iloc[-1]
    return f"{symbol}의 현재 주가는 {price:.2f} USD입니다."
