import streamlit as st
import requests
import pandas as pd

st.title("🌎 USGS 지진 데이터 테스트")

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

response = requests.get(url)
data = response.json()

rows = []

for feature in data["features"]:
    rows.append({
        "장소": feature["properties"]["place"],
        "규모": feature["properties"]["mag"],
        "시간": pd.to_datetime(
            feature["properties"]["time"],
            unit="ms"
        ),
        "위도": feature["geometry"]["coordinates"][1],
        "경도": feature["geometry"]["coordinates"][0],
        "깊이(km)": feature["geometry"]["coordinates"][2]
    })

df = pd.DataFrame(rows)

st.subheader(f"최근 지진 {len(df)}개")

st.dataframe(df)

st.subheader("지진 발생 위치")

st.map(
    df,
    latitude="위도",
    longitude="경도"
)
