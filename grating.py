from math import (pi, cos, sin)


DATA_SHIFT = 2


class SinusoidalGrating:
    def __init__(self, pitch, amplitude, angle):
        """Gratings define by pitches, amplitudes and an angle from observation line.

        Args:
            pitch (float): distance between two sinusoidal summit.
            amplitude (float): light amplitude of the first diffracted order.
            angle (float): angle betwen the line -1/+1 order and the horizontal plane.
        Attributes:
            pitch (float)     : distance between summit of sinusoïdale grating.
            amplitude (float) : amplitude of the sinusoïd.
            angle (float)     : orientation from the x axe.

        """
        self.pitch = pitch
        self.amplitude = amplitude
        self.angle = angle

    def get_surface(self, dimension=10, step=0.1):
        """Return surface of the area (dimension x dimension)
        composed by the sinusoidal grating.

        Args:
            dimension (int, optional): dimension of the wanted area. Defaults to 10.
            step (float, optional): resolution of this surface. Defaults to 0.1.

        Returns:
            list of float : list of amplidude list[x][y]=z.

        """
        nb_point = int(dimension/step)
        surface = [[0]*nb_point for i in range(nb_point)]
        for x in range(nb_point):
            for y in range(nb_point):
                surface[x][y] = (self.amplitude *
                                 (((x * step) * cos(self.angle) +
                                   (y * step) * sin(self.angle)) /
                                     self.pitch))
        return surface


class SurfaceReliefGrating:
    def __init__(self, filename):
        """SurfaceGrating (SRG) define by a list of gratings (composed of pitches,
        amplitudes and angle) through different step of stretching.

        Args:
            filename (str) : filename of the stretched grating datas.
        Attributes:
            nb_grating (int)  : number of sinusoidal grating composing the SRG.
            nb_strech (int)   : number of strech step during the experiment.
            phase (float)     : estimated phase between each grating.
            pitch (float)     : list of pithces of each grating at each strech step.
            amplitude (float) : list of light amplitudes value of each grating at each strech step.
            angle (float)     : list of the angle from the stretch direction of each grating
                                at each step of stretch.
        Methods:
            get_list_of_grating(self, stretch)
            get_stretched_surface(self, stretching=1, dimension=5, step=0.5)

        """

        self.pitches = []
        self.amplitudes = []
        self.angles = []
        self.phase = 0.0
        self.nb_grating = 0
        self.nb_strech = 0
        self.data_file = filename

        with open(self.data_file, "r+") as file:

            def add_data_line_in_list(lis, line):
                data_line = []
                for word in line.split():
                    data_line.append(float(word))
                lis.append(data_line)

            for line_nb, line in enumerate(file):
                if line_nb == 0:
                    self.nb_grating = int(file.readline(1))
                    self.phase = pi/self.nb_grating
                if line_nb == 1:
                    self.nb_strech = int(file.readline(1))
                if 1 < line_nb <= (DATA_SHIFT + self.nb_strech):
                    add_data_line_in_list(self.pitches, line)
                if (1 + self.nb_strech) < line_nb <= (DATA_SHIFT * (1 + self.nb_strech)):
                    add_data_line_in_list(self.amplitudes, line)
                if (1 + DATA_SHIFT*self.nb_strech) < line_nb <= (DATA_SHIFT * (1 + self.nb_strech) + self.nb_strech):
                    add_data_line_in_list(self.angles, line)

            self.pitches.pop(0)
            self.amplitudes.pop(0)
            self.angles.pop(0)

    def get_list_of_grating(self, stretch):
        """Return a list of all gratings composing the SRG.

        Args:
            stretch (int): correspond to the desired stretch step to analyse.

        Returns:
            list: list of gratings (class Gratings).

        """
        if 0 < stretch < self.nb_stretch:
            return None

        gratings_list = []
        for g in range(self.nb_grating):
            grating_caracteristic = SinusoidalGrating(
                self.pitches[g][stretch],
                self.amplitudes[g][stretch],
                self.angles[g][stretch])
            gratings_list.append(grating_caracteristic)
        return gratings_list

    def get_stretched_surface(self, stretching=1, dimension=5, step=0.1):
        """Return surface of the area (dimension x dimension)
        composed by one ore more sinusoidal grating.

        Args:
            stretching (int): stretching step to analyse. Defaults to 1.
            dimension (int, optional): dimension of the wanted area. Defaults to 5.
            step (float, optional): resolution of this surface. Defaults to 0.5.

        Returns:
            list of float : list of amplidude list[x][y]=z.

        """
        if 0 < stretching < self.nb_stretch:
            return None

        grating_list = self.get_list_of_grating(stretch=stretching)
        nb_point = int(dimension/step)
        surface = [[0]*nb_point for i in range(nb_point)]
        for g in range(self.nb_grating):
            for x in range(nb_point):
                for y in range(nb_point):
                    surface[x][y] += (grating_list[g].amplitude *
                                      (self.phase +
                                       ((x * step) * cos(grating_list[g].angle) +
                                        (y * step) * sin(grating_list[g].angle)) /
                                       grating_list[g].pitch))
        return surface


if __name__ == "__main__":

    srg_3 = SurfaceReliefGrating("data/3g.txt")

    print(f'Gratings :\n {srg_3.nb_grating}')
    print(f'Strech steps :\n {srg_3.nb_strech}')
    print(f'Phase :\n {srg_3.phase}')
    print(f'Pitch list :\n {srg_3.pitches}')
    print(f'Aamplitudes list :\n {srg_3.amplitudes}')
    print(f'Angle list :\n {srg_3.angles}')

    stretch = 0
    surface = srg_3.get_stretched_surface(
        stretching=stretch, dimension=1, step=0.1)
    print(f'Surface (stretch = {stretch}) :\n {surface}')
    #print(len(surface))
    #print(len(surface[1]))
