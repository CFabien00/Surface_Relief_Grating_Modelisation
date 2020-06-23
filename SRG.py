from math import pi


class surface_relief_grating:
    def __init__(self, filename):
        """Surface Relief Grating (SRG)
        Args:
            filename (str) -- filename of the stretched grating datas
        Attributes:
            nb_grating -- number of sinusoidal grating composing the SRG
            nb_strech  -- number of strech step during the experiment
            phase      -- estimated phase between each grating
            pitch      -- list of pithces of each grating at each strech step
            amplitude  -- list of light amplitudes value of each grating at each strech step
            angle      -- list of the angle from the stretch direction of each grating at each step of stretch
        """
        def add_data_line_in_list(lis, line):
            data_line = []
            for word in line.split():
                data_line.append(float(word))
            lis.append(data_line)

        self.pitch = []
        self.amplitude = []
        self.angle = []
        self.nb_grating = 0
        self.nb_strech = 0
        self.phase = 0.0
        self.data_file = ''
        self.data_file = filename

        with open(self.data_file, "r+") as file:
            for line_number, line in enumerate(file):
                if line_number == 0:
                    self.nb_grating = int(file.readline(1))
                    self.phase = pi/self.nb_grating
                if line_number == 1:
                    self.nb_strech = int(file.readline(1))
                if 1 < line_number <= (2 + self.nb_strech):
                    add_data_line_in_list(self.pitch, line)
                if (1 + self.nb_strech) < line_number <= (2 + 2*self.nb_strech):
                    add_data_line_in_list(self.amplitude, line)
                if (1 + 2*self.nb_strech) < line_number <= (2 + 3*self.nb_strech):
                    add_data_line_in_list(self.angle, line)

            self.pitch.pop(0)
            self.amplitude.pop(0)
            self.angle.pop(0)


if __name__ == "__main__":

    srg_3 = surface_relief_grating("data/3g.txt")

    print(f'Gratings : {srg_3.nb_grating}')
    print(f'Strech steps : {srg_3.nb_strech}')
    print(f'Phase : {srg_3.phase}')
    print(f'Pitch list : {srg_3.pitch}')
    print(f'Aamplitudes list : {srg_3.amplitude}')
    print(f'Angle list : {srg_3.angle}')
