from __future__ import print_function

import datetime
from distutils import core
import os.path
from time import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import httplib2
import os

from apiclient import discovery
from oauth2client import tools

import sometimeahead

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def createEvent(summary = 'Event', location = 'location', description = 'description', startTime = 1, endTime = -1, attendees = 'null', reminders = '30'):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if endTime == -1:
        endTime = startTime + 1
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Create a calendar event
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': sometimeahead.main(startTime),
                'timeZone': 'Europe/Stockholm',
            },
            'end': {
                'dateTime': sometimeahead.main(endTime),
                'timeZone': 'Europe/Stockholm',
            },
            'attendees': [],
            'reminders': {
                'useDefault': False
            },
        }
        if attendees != 'null':
            attendeearray = attendees.split(' ')
            i = 0
            for item in attendeearray:
                attendeedict = {
                    'email': attendeearray[i]
                }
                event['attendees'].append(attendeedict)
                i = i + 1

        if reminders != 'null':
            overridearray = reminders.split(' ')
            overridemetadict = {
                'overrides': []
            }
            i = 0
            for item in overridearray:
                overridedict = {
                    'method': 'popup',
                    'minutes': overridearray[i]
                }
                overridemetadict['overrides'].append(overridedict)
            event['reminders'].update(overridemetadict)
        
        print(event)

        service = build('calendar', 'v3', credentials=creds)

        event = service.events().insert(calendarId='primary', body=event).execute()
        return 'Event created: %s' % (event.get('htmlLink'))
        # service = build('calendar', 'v3', credentials=creds)

        # # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        # events_result = service.events().list(calendarId='primary', timeMin=now,
        #                                       maxResults=10, singleEvents=True,
        #                                       orderBy='startTime').execute()
        # events = events_result.get('items', [])

        # if not events:
        #     print('No upcoming events found.')
        #     return

        # # Prints the start and name of the next 10 events
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    createEvent()