import pandas as pd
import numpy as np

clusters=pd.read_csv('Data/clusters.csv')
def track_reco(prediction,n):
    # Find the unique clusters and number of tracks in each clusters
    unique,count=np.unique(prediction,return_counts=True)
    t=len(prediction)
    l=len(unique)

    # Claculate the percentage values for each cluster based on count of tracks in each clusters
    p=[]
    for i in range(l):
        p.append(count[i]/t)

    # Predict the tracks based on percentage value of each cluster
    tracks=[]
    tracks_df=pd.DataFrame()
    for i in range(l):
        tracks.append(clusters.track_name[clusters['cluster']==unique[i]].sample(n=int(n*p[i])))
        tracks_df=tracks_df.append(pd.DataFrame(tracks[i]))
        
    return tracks_df
    