"""
Runs ffmpeg commands to get an up-to-date list of supported file format extensions.
"""

from ffmpeg_cli import ffmpeg_cli

# default list of supported video file formats
# in case fetching current formats doesn't work and to ensure out of the box functionality
default_extensions = [
    'str', 'aa', 'aac', 'aax', 'ac3', 'acm', 'adf', 'adp', 'dtk', 'ads', 'ss2', 'adx', 'aea', 'afc', 'aix', 'al', 'apc',
    'ape', 'apl', 'mac', 'aptx', 'aptxhd', 'aqt', 'ast', 'obu', 'avi', 'avs', 'avr', 'bfstm', 'bcstm', 'binka',
    'bitpacked', 'bmv', 'bonk', 'brstm', 'avs', 'cdg', 'cdxl', 'xl', '302', 'daud', 'str', 'adp', 'dfpwm', 'dav', 'dss',
    'dts', 'dtshd', 'dv', 'dif', 'cdata', 'eac3', 'ec3', 'paf', 'fap', 'flm', 'flac', 'flv', 'fsb', 'fwse', 'genh',
    'gsm', 'hca', 'hevc', 'h265', '265', 'idf', 'ifv', 'cgi', 'ipu', 'sf', 'ircam', 'ivr', 'kux', 'laf', '669', 'amf',
    'ams', 'dbm', 'digi', 'dmf', 'dsm', 'dtm', 'far', 'gdm', 'ice', 'imf', 'it', 'j2b', 'm15', 'mdl', 'med', 'mmcmp',
    'mms', 'mo3', 'mod', 'mptm', 'mt2', 'mtm', 'nst', 'okt', 'plm', 'ppm', 'psm', 'pt36', 'ptm', 's3m', 'sfx', 'sfx2',
    'st26', 'stk', 'stm', 'stp', 'ult', 'umx', 'wow', 'xm', 'xpk', 'flv', 'dat', 'lvf', 'm4v', 'mkv', 'mk3d', 'mka',
    'mks', 'webm', 'mca', 'mcc', 'mjpg', 'mjpeg', 'mpo', 'j2k', 'mlp', 'mods', 'moflex', 'mov', 'mp4', 'm4a', '3gp',
    '3g2', 'mj2', 'psp', 'm4b', 'ism', 'ismv', 'isma', 'f4v', 'avif', 'mp2', 'mp3', 'm2a', 'mpa', 'mpc', 'mjpg', 'txt',
    'mpl2', 'sub', 'msf', 'mtaf', 'ul', 'musx', 'mvi', 'mxg', 'v', 'nist', 'sph', 'nsp', 'nut', 'obu', 'ogg', 'oma',
    'omg', 'aa3', 'pjs', 'pvf', 'yuv', 'cif', 'qcif', 'rgb', 'rt', 'rsd', 'rka', 'rsd', 'rso', 'sw', 'sb', 'smi',
    'sami', 'sbc', 'msbc', 'sbg', 'scc', 'sdns', 'sdr2', 'sds', 'sdx', 'ser', 'sga', 'shn', 'vb', 'son', 'imx', 'sln',
    'mjpg', 'stl', 'sub', 'sub', 'sup', 'svag', 'svs', 'tak', 'thd', 'tta', 'ans', 'art', 'asc', 'diz', 'ice', 'nfo',
    'txt', 'vt', 'ty', 'ty+', 'uw', 'ub', 'v210', 'yuv10', 'vag', 'vc1', 'rcv', 'viv', 'idx', 'vpk', 'txt', 'vqf',
    'vql', 'vqe', 'way', 'wa', 'vtt', 'wsd', 'xmd', 'xmv', 'xvag', 'yop', 'y4m'
]

# relevant file paths
extensions_file = r"extensions.txt"


def load_extensions():
    """return currently active extension list from txt file"""
    file = open(extensions_file, mode="r")

    extensions = list()

    for line in file:
        extensions.append(line.strip("\n"))

    return extensions


def use_default_extensions():
    """switch program to using premade list of extensions"""
    file = open(extensions_file, mode="w")

    for ext in default_extensions:
        file.write(ext + "\n")


def use_local_extensions():
    """switch to extension list from currently used ffmpeg version"""
    file = open(extensions_file, mode="w")
    local_extensions = get_single_file_formats()

    for ext in local_extensions:
        file.write(ext + "\n")


def get_demuxers():
    ffmpeg = ffmpeg_cli()
    command = ' -hide_banner -demuxers'

    output = ffmpeg.check_output(command).decode()

    # split at line beginning, remove header
    output = output.split(" D ")[1:]

    return output


def clean_demuxer_list():
    # create list of demuxers
    demuxers = get_demuxers()

    # isolate demuxer name in each line
    for i in range(len(demuxers)):
        # strip leading/trailing white space
        demuxers[i] = demuxers[i].strip()

        # get index of first space
        first_space = demuxers[i].find(" ")

        # delete everything from first space on
        demuxers[i] = demuxers[i][:first_space].strip()

    return demuxers


def get_full_demux_info():
    ffmpeg = ffmpeg_cli()
    demuxers = clean_demuxer_list()

    demuxer_list = list()

    for demuxer in demuxers:
        command = " -hide_banner -h demuxer={}".format(demuxer)

        demuxer_list.append(
            ffmpeg.check_output(command).decode()
        )

    return demuxer_list


def get_file_extensions():
    demuxers = get_full_demux_info()

    extensions_start = "extensions: "
    start_offset = len(extensions_start)
    extensions_end = "."

    # reduce strings in list to only extensions
    for i in range(len(demuxers)):
        # remove return and newline characters
        demuxers[i] = demuxers[i].replace("\r", "")
        demuxers[i] = demuxers[i].replace("\n", "")

        # find start of extension list
        start = demuxers[i].find(extensions_start)

        # find end of extension list
        end = demuxers[i].find(extensions_end)

        # isolate extensions
        demuxers[i] = demuxers[i][start:end]

        # remove description string
        demuxers[i] = demuxers[i][start_offset:]

    # remove empty list items
    for entry in reversed(demuxers):
        if entry == "":
            demuxers.remove(entry)

    return demuxers


def get_single_file_formats():
    extensions = get_file_extensions()

    # join into string with seperator
    extensions = ','.join(extensions)

    # separate again into list with each extension as single list entry
    extensions = extensions.split(",")

    return extensions
