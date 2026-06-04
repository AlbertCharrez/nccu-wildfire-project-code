# radiometric_terrain_correction
This product applies radiometric terrain correction to UAVSAR image to reduce geometric distortions caused by the side-looking SAR and terrain features. The product also generates HDR environment for incidence angle files. This product should be used before the [`uavsar_wildfire_classification`](https://github.jpl.nasa.gov/UAVSAR-Fire-Research/uavsar_wildfire_classification) repository. 

Data can be downloaded from the following sources:
- [UAVSAR](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl)
- [Alaska Satellite Facility](https://search.asf.alaska.edu/#/?dataset=UAVSAR)

Download the following four type of data assoicated with the flight:
- `(.mlc)` multi look cross product slant range image
- `(.hgt)` digital elevation model (DEM) used during processing and ground projection
- `(.ann)` annotation file
- `(.inc)` incidence angle


Make sure conda is set up prior to use. Else, mambaforge can be installed [here](https://github.com/conda-forge/miniforge#mambaforge)

## Setup (Mac)
1. Open terminal
2. Clone this repository: 

    `git clone git@github.jpl.nasa.gov:UAVSAR-Fire-Research/radiometric_terrain_correction.git`
    
    or `git clone https://github.jpl.nasa.gov/UAVSAR-Fire-Research/radiometric_terrain_correction.git`
  
3. Create a virtual environment using conda via:

    `conda create --name rtc python=3.11`
	
	  Make sure to hit `y` to confirm that the listed packages can be downloaded for this environment.
    
4. Activate the virtual environment: 

	  `conda activate rtc`.

5. Install requirements: (Note: this will take a while)

	`conda env update -f environment.yml`
  
6. Create a new jupyter kernel: 

	`python -m ipykernel install --user --name rtc`
	
Make sure the kernel is `rtc` when using jupyter-notebook.

This has not been tested for windows OS but, the setup steps should be similiar to that of Mac except the steps are ran on Anaconda Prompt.
Check [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) for more information about setup.
  
## Products
Activate the jupyter-notebook by going to the `notebook` folder and run `jupyter-notebook` from there.

After downloading the UAVSAR data, organize them into different folders by flight line. 

### For RTC:
Follow the instructions in `RTC_notebook.ipynb`. RTC requires `.mlc`, `.hgt`, `.ann` files

### For HDR - incidence angle:
Follow the instruction in `incidence_angle.ipynb`. This requires `.inc`, `.ann` files. It is done using the `buildUAVSARhdr.py` script created by Nathan Thomas.

## Reference
The code in the notebook is entirely sourced from JPL's Simard Landscape Lab's [UAVSAR-Radiometric-Calibration](https://github.com/simard-landscape-lab/UAVSAR-Radiometric-Calibration/tree/master) repository.

Their paper is linked below:
M. Simard, B. V. Riel, M. Denbina and S. Hensley, "Radiometric Correction of Airborne Radar Images Over Forested Terrain With Topography," in IEEE Transactions on Geoscience and Remote Sensing, vol. 54, no. 8, pp. 4488-4500, Aug. 2016. doi: 10.1109/TGRS.2016.2543142 URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7447752&isnumber=7482858

##

Copyright 2023, by the California Institute of Technology. ALL RIGHTS RESERVED. United States Government Sponsorship acknowledged. Any commercial use must be negotiated with the Office of Technology Transfer at the California Institute of Technology.

This software may be subject to U.S. export control laws. By accepting this software, the user agrees to comply with all applicable U.S. export laws and regulations. User has the responsibility to obtain export licenses, or other export authority as may be required before exporting such information to foreign countries or providing access to foreign persons.
