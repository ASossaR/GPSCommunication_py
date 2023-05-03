from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np
import time

palabras = []
latitud = 0
longitud = 0
latitud_ant = 0
longitud_ant = 0
p_lon = [0,0]
p_lat = [0,0]


archivo = '/home/sossa/Documentos/Taller de Comu/DatosGPS.txt'

fig = plt.figure(figsize = (12,12))

m = Basemap(projection = 'lcc',
			lat_0 = 10.5, 
			lon_0 = -84.5, 
			width = 5E5, 
			height = 5E5, 
			area_thresh = 2000.,
			resolution = 'h')




#abrir un archivo
with open(archivo,"r") as archivo:
	for lineas in archivo:
		#print('lineaa: ', lineas)
		palabras.extend(lineas.split())
		#print (palabras)



m.drawcountries(color='#303338')
m.drawcoastlines()
m.drawmapboundary(color = '#c0eaff', linewidth = 5.0, fill_color = None, zorder = None, ax = None)
m.readshapefile('/home/sossa/Documentos/Taller de Comu/gadm36_CRI_shp/gadm36_CRI_2', 'Provincia', drawbounds = True)
m.fillcontinents(color='#ebe7d5', lake_color='#c0eaff')
m.drawrivers(color='b', linewidth = 1.0)

#m.drawstates()
#m.drawmapscale()
#m.nightshade()

#metodo
for i in range(len(palabras)):
	if i%3 == 0:
		latitud_ant = latitud
		longitud_ant = longitud

		latitud = palabras[i+1]
		longitud = palabras[i+2]

		p_lon[0],p_lat[0] = m(longitud_ant, latitud_ant)
		p_lon[1],p_lat[1] = m(longitud, latitud)

		


		x,y = m(longitud, latitud)
		plt.plot(x, y, 'ok', markersize = 4, color = 'r')
		if i > 2:
			plt.plot(p_lon,p_lat, color ='g', linewidth = 2)


#plt.text(x, y, 'San Carlos', fontsize = 12);
plt.title('Taller de Comu')

plt.show()