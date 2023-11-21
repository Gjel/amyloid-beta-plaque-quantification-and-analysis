from argparse import ArgumentParser

def add_io_settings(parser: ArgumentParser):
    parser.add_argument('image', type=str,
                        help='The name of the vsi file that needs to be analysed. Omit .vsi in the name.')
    parser.add_argument('-sf', '--source_folder', required=True, type=str,
                        help='the folder in which the vsi file is located')
    parser.add_argument('-tf', '--target_folder', default='result/images', type=str,
                        help='The folder in which to place the resulting hdf5 file.')

def add_segmentation_settings(parser: ArgumentParser):
    parser.add_argument('-pss', '--patch_size_segmentation', default=1024, type=int,
                        help='The patch size in pixels used in the segmentation step (default=1024)')
    parser.add_argument('-df', '--downscale_factor', default=16, type=int,
                        help='The downsampling factor used for creating the grey matter segmentation (default=16)')
    parser.add_argument('-mp', '--model_path', default='models/2023-03-15-unet-16x-bs16-ps256-lr0.0001/2023-03-15-unet-16x-bs16-ps256-lr0.0001-e3v49.pt', type=str,
                        help='The path to the unet model trained for the segmentation task.')

def add_localisation_settings(parser: ArgumentParser):
    parser.add_argument('-psl', '--patch_size_localisation', default=4096, type=int,
                        help='The patch size in pixels used in the localisation step (default=4096)')
    parser.add_argument('-t', '--threshold', default=0.04, type=float,
                        help='The minimum threshold parameter for the localisation step. Range from 0 to 1 (default=0.04)')
    parser.add_argument('-ks', '--kernel_size', default=21, type=int,
                        help='The kernel size parameter in pixels for the localisation step (default=21)')
    parser.add_argument('-ms', '--minimum_size', default=10, type=float,
                        help='The minimum plaque size parameter in microns for the localisation step (default=10)')
