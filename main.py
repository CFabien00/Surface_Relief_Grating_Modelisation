from grating import *

srg_3 = SurfaceReliefGrating("data/3g.txt")

print(f'Gratings :\n {srg_3.nb_grating}')
print(f'Strech steps :\n {srg_3.nb_strech}')
print(f'Phase :\n {srg_3.phase}')
print(f'Pitch list :\n {srg_3.pitches}')
print(f'Aamplitudes list :\n {srg_3.amplitudes}')
print(f'Angle list :\n {srg_3.angles}')

stretch = 0
surface = srg_3.get_stretched_surface(
    stretching=stretch, dimension=10, step=1)
print(f'Surface (stretch = {stretch}) :\n {surface}')
