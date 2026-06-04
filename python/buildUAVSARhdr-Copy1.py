#! /usr/bin/env python


''' Author: Nathan Thomas
Email: nmt8@aber.ac.uk
Date: 23/08/2014
Version: 1.0
THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''



import os.path
import argparse
    

def genHDRfromTXT(annFile, dataFile, pol):
    # Specify the format type
    format = 'GRD'

    # Initialize a dictionary to hold header parameters
    headerPar = {}

    # Extract the base name of the annotation file without the extension
    fileBaseName = os.path.splitext(os.path.basename(annFile))[0]
    headerPar['fileBaseName'] = fileBaseName

    # Open the annotation file and read its contents
    with open(annFile, 'r') as hdrFile:
        for line in hdrFile:
            # Extract and store the upper left latitude coordinate
            if 'grd_mag.row_addr' in line:
                headerPar['ULlatCord'] = line.split()[3]
                print('UPPER LEFT LAT =', headerPar['ULlatCord'])
            # Extract and store the upper left longitude coordinate
            elif 'grd_mag.col_addr' in line:
                headerPar['ULlongCord'] = line.split()[3]
                print('UPPER LEFT LONG =', headerPar['ULlongCord'])
            # Extract and store the number of samples if the format is 'GRD'
            elif 'grd_pwr.set_rows' in line and format == 'GRD':
                headerPar['GRDSamples'] = line.split()[3]
                print('SAMPLES =', headerPar['GRDSamples'])
            # Extract and store the number of lines if the format is 'GRD'
            elif 'grd_pwr.set_cols' in line and format == 'GRD':
                headerPar['GRDLines'] = line.split()[3]
                print('LINES =', headerPar['GRDLines'])
            # Extract and store the latitude pixel size if the format is 'GRD'
            elif 'grd_mag.row_mult' in line and format == 'GRD':
                headerPar['GRDlatPixel'] = abs(float(line.split()[3].split(';')[0]))
                print('PIXEL LAT SIZE =', headerPar['GRDlatPixel'])
            # Extract and store the longitude pixel size if the format is 'GRD'
            elif 'grd_mag.col_mult' in line and format == 'GRD':
                headerPar['GRDlongPixel'] = abs(float(line.split()[3].split(';')[0]))
                print('PIXEL LONG SIZE =', headerPar['GRDlongPixel'])

    # Map the polarization to the appropriate data type
    dataType_map = {
        'HHHV': 6,
        'HHVV': 6,
        'HVVV': 6,
        'HHHH': 4,
        'HVHV': 4,
        'VVVV': 4
    }

    # Assign the data type based on the polarization
    headerPar['dataType'] = dataType_map.get(pol, 4)
    print('DATATYPE =', headerPar['dataType'])

    # Construct the filename for the output HDR file
    hdr_filename = f"{dataFile}.hdr"
    print('Writing output HDR file...')

    # Create the ENVI HDR content using the header parameters
    enviHDR_content = f"""ENVI
description = {{{headerPar['fileBaseName']}}}
samples = {headerPar['GRDLines']}
lines = {headerPar['GRDSamples']}
bands = 1
header offset = 0
file type = ENVI Standard
data type = {headerPar['dataType']}
interleave = bsq
sensor type = Unknown
byte order = 0
map info = {{Geographic Lat/Lon, 1.5, 1.5, {headerPar['ULlongCord']}, {headerPar['ULlatCord']}, {headerPar['GRDlongPixel']}, {headerPar['GRDlatPixel']}, WGS-84, units=Degrees}}
coordinate system string = {{GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.017453292519943295]]}}
wavelength units = Unknown\n"""

    # Write the ENVI HDR content to the output file
    with open(hdr_filename, 'w') as enviHDRFile:
        enviHDRFile.write(enviHDR_content)

    print('Output HDR file =', hdr_filename)
    print('\nThank you for using UAVSAR.py\n')



def main():
    print("UAVSAR.py is written by Nathan Thomas (nmt8@aber.ac.uk, @Nmt28) of the Aberystwyth University Earth Observation and Ecosystems Dynamics Laboratory (@AU_EarthObs) as part of a visiting research program at NASA JPL\nUse '-h' for help and required input parameters\n")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Specify the input UAVSAR ann file")
    parser.add_argument("-r", "--uavsar", type=str, help="Specify the input UAVSAR radar file")
    parser.add_argument("-p", "--polarization", type=str, help="Specify the input UAVSAR polarization in UPPERCASE (i.e HHHV)")
    args = parser.parse_args()

    if '.txt' in str(args.input):
        pass
    else:
        print("INPUT UAVSAR ANN FILE MUST BE '.TXT'")
        os._exit(1)
    if args.input == None:
        print("SPECIFY IINPUT TXT FILE")
        os._exit(1)
    elif args.uavsar == None:
        print("SPECIFY INPUT UAVSAR FILE")
        os._exit(1)
    elif args.polarization == None:
        print("SPECIFY UAVSAR IMAGE POLARIZATION (i.e. 'HHHV')")
        os._exit(1)


    genHDRfromTXT(args)


if __name__ == "__main__":
    main()

