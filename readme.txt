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
