"""
Class to provide ffmpeg command line functions.
"""
import subprocess


class ffmpeg_cli:
    # exe file paths
    ffmpeg_folder = r".\src\ffmpeg"
    ffmpeg = ffmpeg_folder + r"\bin\ffmpeg.exe"
    ffprobe = ffmpeg_folder + r"\bin\ffprobe.exe"

    def check_output(self, command):
        """
        Exectues command line function for ffmpeg.exe and returns results.
        :param command: command line parameters
        :return: Output as bytes-object (use .decode() to convert to string if needed
        """
        return subprocess.check_output(self.ffmpeg + command, shell=True)

    def probe(self, file):
        """

        :param file:
        :return:
        """
        command = r'-v error -hide_banner -print_format json -show_streams -show_format '
        result = subprocess.check_output(self.ffprobe + command + file, shell=True)
        return result

    # TODO: allow user to set ffmpeg_cli.py.exe other than default shipped version
    # TODO: save user choice permanently somewhere (ini file?)
    # TODO: check if exists, otherwise use default and/or provide error
    # TODO: check if actually ffmpeg exe, for security reasons
    def set_ffmpeg_path(filepath):
        global ffmpeg
        ffmpeg = filepath
