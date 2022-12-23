import pandas as pd
from datetime import datetime

print(pd.date_range(end = datetime.today(),periods = 3).to_pydatetime().tolist())