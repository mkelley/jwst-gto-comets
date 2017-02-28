#from glob import glob
import numpy as np
#import scipy.ndimage as nd
#import matplotlib.pyplot as plt
import astropy.units as u
#from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
import mskpy

# Put gas models into a form suitable for the JWST ETC
for f in ('gas/46p_jwst_miri100rp_20190515_radiance_0.5FWHM_sp_table.txt',
          'gas/46p_jwst_nirspec2700rp_20190515_radiance_0.1FWHM_sp_table.txt',
          'gas/46p_jwst_nirspecprism_20190515_radiance_0.1FWHM_sp_table.txt'):
    tab = ascii.read(f)
    wave = tab['col1']
    gas = tab['col6']
    for col in tab.colnames[6:]:
        gas += tab[col]

    with open(f.replace('table', 'cfg'), 'r') as inf:
        for line in inf:
            if 'GEOMETRY-DIAMETER-FOV' in line:
                rap = float(line.split('>')[1]) / 2
                break

    A = np.pi * rap**2 * (u.arcsec**2).to(u.sr)
    conv = A * u.Unit('W/(m2 um)').to(u.mJy, 1, u.spectral_density(wave * u.um))
    gas *= conv
    mskpy.write_table('46p-20190515-{}-gas-est.txt'.format(f.split('_')[2]),
                      Table(names=('wave', 'fluxd'), data=(wave, gas)),
                      {'origin': "GSFC Planetary Spectrum Generator, Villanueva et al."})

