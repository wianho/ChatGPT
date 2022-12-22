{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import DaVinciResolveScript as resolve\
\
# Connect to DaVinci Resolve\
resolve.Connect()\
\
# Get the current project\
project = resolve.GetCurrentProject()\
\
# Import the video file\
video_path = '/path/to/video.mp4'\
imported_media = project.GetMediaPool().ImportFile(video_path)\
\
# Create a new timeline\
timeline = project.CreateTimeline("My Timeline")\
\
# Add the video to the timeline\
video_track = timeline.GetVideoTrackAt(0)\
clip = video_track.CreateClip(imported_media)\
clip.SetTimelineIn(0)\
clip.SetTimelineOut(imported_media.GetDuration())\
\
# Save the project\
project.Save()\
\
# Disconnect from DaVinci Resolve\
resolve.Disconnect()\
}