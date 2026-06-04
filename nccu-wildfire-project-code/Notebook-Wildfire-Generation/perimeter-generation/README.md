This folder contains the code for generating a burn perimeter map using the L Band polarizations from the UAVSAR flight paths, POST PROCESSING (RTC and Cropping have been completed).

Data Merging
- Contains a variety of notebooks which can all be used to merge flight paths post processing, depending on the amount of flights needed for the fire and if there are overlapping values or not.
- Inc merge : No merging done, only applying the .inc files to the .tif files
- Weighted Inc Merge x flights : Merging based on the amount of flights done to cover the wildfire area, requires correseponding .inc files for each .tif file. 

Perimeter Evaluation
- Contains the notebook for post perimeter generation based on the offical recorded .shp of the fire, and the burn perimeter map that was generated through perimeter-generation. 

Perimeter Generation
- Contains a variety of notebooks used to generate the burn perimeter of a wildfire through different indices.
- RFDI : Radar Forest Degradation Index uses HH and HV polarizations as log10((HH - HV) / (HV + HH)) to evalute as the name implies the degradation of vegatation in the region. This is done as RFDI(time 1) / RFDI(time 2), as to take into consideration a change from one time into the next.
- RVI : Radar Vegetation Index uses HV and VV polarization as log10(4HV / (HV + VV)) to evaluate the vegetation present in the area. This is done as RVI(time 1) / RVI(time 2), as to take into consideration a change in time.
- HV+HH : Index that was tested to see its individual performance done as log10((HV+HH[time 1]) / (HV+HH[time 2])).
- HV-HH : Index that was tested to see its individual performance done as log10((HV-HH[time 1]) / (HV-HH[time 2])).
- HV logratio : Original index used to evaluate the degradation of the area, done as (hv[time 1] / hv[time 0]). 

Superpixwel Segmentation
- Contains the code for generating the superpixel segmenation map of the fire to decrease overall processing time. 
