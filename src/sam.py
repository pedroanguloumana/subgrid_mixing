import xarray as xr
from glob import glob
def load_2d_TKScaleOff():
    path = '/glade/u/home/pblossey/descratch/gSAM/RCE/TKScaleOff/OUT_2D/'
    files = sorted(glob(path+'*.nc'))
    ds = xr.concat([xr.open_dataset(f) for f in files], dim='time')
    return ds

def load_2d_TKScale0p2():
    path = '/glade/u/home/pblossey/descratch/gSAM/RCE/TKScale0p2/OUT_2D/'
    files = sorted(glob(path+'*_ab*.nc'))
    ds = xr.concat([xr.open_dataset(f) for f in files], dim='time')
    return ds