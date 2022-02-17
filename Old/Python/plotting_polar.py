#change the colour background - see whats apps
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

#empty list to store variable
angle = []
angle1=[]
angle2=[]
angle3=[]
angle4=[]
angle5=[]
angle6=[]
angle7=[]
angle8=[]
distance = []
distance1 = []
distance2 = []
distance3 = []
distance4 = []
distance5 = []
distance6 = []
distance7 = []
distance8 = []

while True:
  try:
    data = pd.read_csv('S1.csv').values 
    for n in range(len(data)): #for angle data format to int
      new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
      angle.append(new_string) #make a list from it
    angle1 = list(map(int, angle)) #transfer to int for graph plotting
    for n in range(len(data)): #for distance (the same thing)
      new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
      distance.append(new_string)
    distance1 = list(map(int, distance))
  except:
    print(" S1.csv is empty and has been skipped.")

  #fig = make_subplots(rows=3, cols=2, specs=[[{'type': 'polar'}]*2]*3)
  fig = make_subplots(rows=2, cols=4, specs=[[{'type': 'polar'}]*4]*2)

  fig.add_trace(go.Scatterpolar(
    name = "Sensor 1",
    r = distance1,
    theta = angle1,
    ), 1, 1)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 2",
    r = distance2,
    theta = angle2,
    ), 1, 2)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 3",
    r = distance3,
    theta = angle3,
    ), 1, 3)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 4",
    r = distance4,
    theta = angle4,
    ), 1, 4)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 5",
    r = distance5,
    theta = angle5,
    ), 2, 1)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 6",
    r = distance6,
    theta = angle6,
    ), 2, 2)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 7",
    r = distance7,
    theta = angle7,
    ), 2, 3)
  fig.add_trace(go.Scatterpolar(
    name = "Sensor 8",
    r = distance8,
    theta = angle8,
    ), 2, 4)


  fig.update_traces(fill='toself')
  fig.update_layout(
    title="Sensor polar plot",
    xaxis_title="Distance (cm)",
    yaxis_title="Angle (deg)",
    polar = dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
    polar2 = dict(
      sector = [0, 180],
      radialaxis = dict(
        angle = 180,
        tickangle = -180 # so that tick labels are not upside down
        )
      ),
    polar3 = dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
    polar4= dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
    polar5= dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
    polar6= dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
    polar7= dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
    polar8= dict(
      sector = [0, 180],
      angularaxis = dict(    
      )
      ),
  )

  '''
      polar3 = dict(
        sector = [80, 400],
        radialaxis_angle = -45,
        angularaxis_categoryarray = ["d", "a", "c", "b"]
      ),
      polar4 = dict(
        radialaxis_categoryorder = "category descending",
        angularaxis = dict(
          thetaunit = "radians",
          dtick = 0.3141592653589793
        ))
      '''

  fig.show()
  time.sleep(10) #10s
