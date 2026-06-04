#! /usr/bin/env python


''' Author: Nathan Thomas
Email: nmt8@aber.ac.uk
Date: 23/08/2014
Version: 1.0
THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''

import os.path
import sys
import glob
import argparse


def genHDRfromANN(args):
    format = 'GRD'

    # Set up dictionary to hold header parameters
    headerPar = {}

    file = args.input
    fileBaseName = os.path.split(file)[-1]
    fileBaseName = fileBaseName.replace('.ann', '')
    headerPar['fileBaseName'] = fileBaseName
    headerPar['grdName'] = args.uavsar
    annFile = open(file, 'r')
    for line in annFile:
        if 'grd_mag.row_addr' in line:
            ULlatCord = line.split()[3]
            print('UPPER LEFT LAT = ', ULlatCord)
            headerPar['ULlatCord'] = ULlatCord
        elif 'grd_mag.col_addr' in line:
            ULlongCord = line.split()[3]
            print('UPPER LEFT LONG = ', ULlongCord)
            headerPar['ULlongCord'] = ULlongCord
    annFile.close()

    if format == 'GRD':
        annFile = open(file, 'r')
        for line in annFile:
            if 'grd_mag.set_rows' in line:
                GRDSamples = line.split()[3]
                print('SAMPLES =', GRDSamples)
                headerPar['GRDSamples'] = GRDSamples
            elif 'grd_mag.set_cols' in line:
                GRDLines = line.split()[3]
                print('Lines =', GRDLines)
                headerPar['GRDLines'] = GRDLines
            elif 'grd_mag.row_mult' in line:
                GRDlatPixel = abs(float(line.split()[3].split(';')[0]))
                print('PIXEL LAT SIZE = ', GRDlatPixel)
                headerPar['GRDlatPixel'] = GRDlatPixel
            elif 'grd_mag.col_mult' in line:
                GRDlongPixel = abs(float(line.split()[3].split(';')[0]))
                print('PIXEL LONG SIZE = ', GRDlongPixel)
                headerPar['GRDlongPixel'] = GRDlongPixel

    # ASSIGN NUMER OF LINES AND SAMPLES BASED UPON FILE TYPE
    # print('Reading lines...')
    if format == 'GRD':
        lines = GRDLines
        samples = GRDSamples
        if args.polarization in ['HHHV', 'HHVV', 'HVVV', 'int']:
            dataType = 6
        elif args.polarization in ['HHHH', 'HVHV', 'VVVV', 'amp1', 'amp2', 'cor', 'unw', 'hgt']:
            dataType = 4

        print('DATATYPE = ', dataType)
        headerPar['dataType'] = dataType

    if args.input.endswith('.ann'):
        file = args.uavsar + '.hdr'
        print('Writing output HDR file...')
        enviHDRFile = open(file, 'w')
        enviHDR = '''ENVI
description = {{UAVSAR georeferenced data {grdName}}}
samples = {GRDLines}
lines = {GRDSamples}
bands = 1
header offset = 0
file type = ENVI Standard
data type = {dataType}
interleave = bsq
sensor type = Unknown
byte order = 0
map info = {{Geographic Lat/Lon, 1.5, 1.5, {ULlongCord}, {ULlatCord}, {GRDlongPixel}, {GRDlatPixel}, WGS-84, units=Degrees}}
coordinate system string = {{GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.017453292519943295]]}}
wavelength units = Unknown\n'''.format(**headerPar)
        enviHDRFile.write(enviHDR)
        enviHDRFile.close()
        print('Output HDR file =', file)

    print('\nThank you for using UAVSAR.py\n')


def main():
    print(
        "UAVSAR.py is written by Nathan Thomas (nmt8@aber.ac.uk, @Nmt28) of the Aberystwyth University Earth Observation and Ecosystems Dynamics Laboratory (@AU_EarthObs) as part of a visiting research program at NASA JPL\nUse '-h' for help and required input parameters\n")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Specify the input UAVSAR ann file")
    parser.add_argument("-r", "--uavsar", type=str, help="Specify the input UAVSAR radar file")
    parser.add_argument("-p", "--polarization", type=str,
                        help="Specify the input UAVSAR polarization in UPPERCASE (i.e HHHV)")
    args = parser.parse_args()

    if '.ann' in str(args.input):
        pass
    else:
        print("INPUT UAVSAR ANN FILE MUST BE '.ann'")
        os._exit(1)
    if args.input == None:
        print("SPECIFY INPUT ANN FILE")
        os._exit(1)
    elif args.uavsar == None:
        print("SPECIFY INPUT UAVSAR FILE")
        os._exit(1)
    elif args.polarization == None:
        print("SPECIFY UAVSAR IMAGE POLARIZATION (i.e. 'HHHV')")
        os._exit(1)

    genHDRfromANN(args)


if __name__ == "__main__":
    main()


