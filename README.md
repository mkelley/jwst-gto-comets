# jwst-gto-comets
Comet observation design for a JWST GTO program.

Science Lead: Mike Kelley, UMD

JWST GTO Principal Investigator: Heidi Hammel, AURA

## Spectral mapping of a comet coma
Goal: To excercise JWSTs spectral mapping capabilities at a comet.

Target: 46P/Wirtanen

Science team: Chick Woodward (UMN), Silvia Protopapa (UMD)

|Instrument|Mode              |Goals|Notes|
|----------|------------------|-----|-----|
|NIRSpec   |IFU, Prism (R~100)|Detect continuum at SNR~100|Dust, potential ice, major gas species.|
|NIRSpec   |IFU, R~2700       |At least map water and CO2, detect other gasses|Water, CO2, CO, CH4, C2H6, C2H2, CH3OH, H2CO|
|MIRI      |LRS, R~100        |Detect continuum at SNR~100|Long-slit mode, spectral map for water band, dust|

Gas lines modeled by the [Planetary Spectrum Generator](http://ssed.gsfc.nasa.gov/psg/)

## Detection of water in the coma of a main-belt comet
Goal: To test the cometary nature of MBCs.

Target: 313P/Gibbs

Science team: Henry Hsieh (PSI), Dennis Bodewits (UMD)

|Instrument|Mode              |Notes                            |
|----------|------------------|---------------------------------|
|NIRSpec   |Fixed-slit, R~2700|1.8 to 3.1 μm for water band|
|NIRCam    |SWC+LWC           |F200W and F277W for context imaging|
