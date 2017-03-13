#!/usr/bin/env python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pdb
import datetime
from collections import namedtuple

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBmtTxrDfNLNbW6P5mzcxrpajZt_ByBdS0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

YTOptions = namedtuple('YTOptions', 'maxResults, channelId, publishedAfter')

class Aggregator(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)

    def get_current_datestring(self):
        current_timestamp=datetime.datetime.utcnow()
        today_timestamp=datetime.datetime(current_timestamp.year,current_timestamp.month,current_timestamp.day).isoformat('T')+"Z"
        return today_timestamp

    def retrive_youtube_updates(self, options):
        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = self.youtube.search().list(
            part="id,snippet",
            maxResults=options.maxResults,
            channelId=options.channelId,
            publishedAfter=options.publishedAfter
        ).execute()

        vinfos = {}

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                vname=search_result["snippet"]["title"].encode('utf-8')
                vid=search_result["id"]["videoId"]
                print "Video: {} {}".format(vname, vid)
                vinfos[vid]=vname
        return vinfos


if __name__ == "__main__":
    current_timestamp=datetime.datetime.utcnow()
    today_timestamp=datetime.datetime(current_timestamp.year,current_timestamp.month,current_timestamp.day).isoformat('T')+"Z"
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--maxResults", help="Max results", default=25)
    argparser.add_argument("--channelId", help="Channel Id", default='UCwWhs_6x42TyRM4Wstoq8HA')
    argparser.add_argument("--publishedAfter", help="Published After", default=today_timestamp)    
    args = argparser.parse_args()
    pdb.set_trace()
    aggr = Aggregator()
    aggr.retrive_youtube_updates(args)

    # try:
    # except HttpError, e:
    #     print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)        
