import pandas as pd
import numpy as np


from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello() -> str:
    df = pd.read_csv(
    "../input/datasets/co2.csv",
    index_col='Date',
    parse_dates=['Date'],
)

    df['Time'] = np.arange(len(df.index))   

    df1=df.head()
    
    return df1.to_string() 


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)


