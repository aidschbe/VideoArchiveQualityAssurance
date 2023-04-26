"""
Class to provide ffmpeg command line functions.
"""
import subprocess


class ffmpeg_cli:
    # relevant file paths
    ffmpeg_default = r".\src\ffmpeg\bin\ffmpeg.exe"
    ffmpeg = r".\src\ffmpeg\bin\ffmpeg.exe"

    def check_output(self, command):
        return subprocess.check_output(self.ffmpeg + command, shell=True)

    # TODO: allow user to set ffmpeg_cli.py.exe other than default shipped version
    # TODO: save user choice permanently somewhere (ini file?)
    # TODO: check if exists, otherwise use default and/or provide error
    # TODO: check if actually ffmpeg exe, for security reasons
    # TODO: don't use global, remove default-ffmpeg_cli.py variable
    def set_ffmpeg_path(filepath):
        global ffmpeg
        ffmpeg = filepath
