from src.load_data import load_dataset, basic_info
from src.clean_data import clean_dataset
from src.batting_analysis import batting_analysis
from src.bowling_analysis import bowling_analysis
from src.team_analysis import team_analysis
from src.advanced_analysis import advanced

df = load_dataset("data/cricket_players.csv")
basic_info(df)

df = clean_dataset(df)
batting_analysis(df)
bowling_analysis(df)
team_analysis(df)
advanced(df)