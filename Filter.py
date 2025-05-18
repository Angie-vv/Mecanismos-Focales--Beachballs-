
#Instalar obspy y pandas
!pip install obspy pandas

import obspy

#Utilizar el link de los datos de mecanismos focales de la Universidad de Harvard
ndk_url = "https://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/jan76_dec20.ndk"
catalog = obspy.read_events(ndk_url)

#Utilizar las corrdenadas de tu zona, por ejemplo Valparaiso
min_lat, max_lat = -34.0, -32.0
min_lon, max_lon = -74.0, -70.0

filtered_events = [
    event for event in catalog
    if min_lat <= event.origins[0].latitude <= max_lat and
       min_lon <= event.origins[0].longitude <= max_lon
]

#Guardar los datos como csv
import pandas as pd

data = []
for event in filtered_events:
    origin = event.origins[0]
    magnitude = event.magnitudes[0]
    focal_mech = event.focal_mechanisms[0]
    mt = focal_mech.moment_tensor.tensor
    data.append({
        "time": origin.time,
        "latitude": origin.latitude,
        "longitude": origin.longitude,
        "depth_km": origin.depth / 1000,
        "magnitude": magnitude.mag,
        "magnitude_type": magnitude.magnitude_type,
        "Mrr": mt.m_rr,
        "Mtt": mt.m_tt,
        "Mpp": mt.m_pp,
        "Mrt": mt.m_rt,
        "Mrp": mt.m_rp,
        "Mtp": mt.m_tp
    })

df = pd.DataFrame(data)
df.to_csv("valparaiso_focal_mechanisms.csv", index=False)