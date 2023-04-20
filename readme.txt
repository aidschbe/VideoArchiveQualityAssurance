Based on an old data model I made at university, this project is an attempt to create software that
finds all videofiles in a given directory (and its subdirectories), probes them for metadata
and uses that metadata to look for qualitative shortcomings.
(eg low resolution, old container format, missing data stream names, missing language tags, etc)

Working:
- fetching list of supported extensions from ffmpeg
-

TODO:
 - ffmpeg class
 - try mediainfo and other alternatives
 - user interface
 - make separate list of non-video/non-supported files (may be relevant for the QA evaluation, old formats, external subs, etc)

Disclaimer:
- this software uses code of http://ffmpeg.org licensed under the http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
- this software uses libraries from the FFmpeg project under the LGPLv2.1
- this software uses FFmpeg under the LGPLv2.1
- I do not own FFmpeg, all information on it can be found here: http://ffmpeg.org