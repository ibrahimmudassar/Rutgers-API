import plotly.express as px
import requests
from os import path
import pandas as pd
from datetime import datetime

year = str(datetime.today().year)

# for new brunswick
url = f"https://sis.rutgers.edu/soc/api/courses.json?year={year}&term=1&campus=NB"

# for newark
#url = "https://sis.rutgers.edu/soc/api/courses.json?year=2023&term=1&campus=NK"

# for camden
#url = "https://sis.rutgers.edu/soc/api/courses.json?year=2023&term=1&campus=CM"


if not path.exists('courses.json'):
    response = requests.get(url)
    courses = response.content
    with open('courses.json', 'wb') as f:
        f.write(courses)

df = pd.read_json('courses.json')


# each of the sections in the course has its own metadata but i only want the amount of sections within the course
df["numOfSections"] = [len(section) for section in df["sections"]]

# filter only by classes with > 1 section
# df = df[df["numOfSections"] > 40]

fig = px.treemap(df,
                 path=[px.Constant("01"), 'subject', 'courseNumber'],
                 values="numOfSections",
                 color="numOfSections",
                 color_continuous_scale='Reds',
                 hover_data=['subjectDescription', 'title'],
                 )
fig.update_traces(root_color="grey")
#fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Labels
fig.update_layout(title={
                  'text': 'Rutgers Classes Sorted by Section Size', 'x': 0.5, 'xanchor': 'center'})

# Attribution
fig.add_annotation(text="By: Ibrahim Mudassar",
                   xref="paper", yref="paper",
                   x=1, y=1,
                   showarrow=False,
                   align="center",
                   font=dict(size=9, color='white'))

fig.show()
