from datetime import datetime

MEETUPS = []
RSVPS = []


class Meetup(object):
    '''this class defines a blueprint of a meetup record'''
    def __init__(self):
        self.count = len(MEETUPS)
    def create_meetup(self, **kwargs):
        '''this function creates a meetup record in the api'''
        meetup = {
            "id":self.count+1,
            "topic":kwargs['topic'],
            "created_on":datetime.now(),
            "happening_on":kwargs['happening_on'],
            "location":kwargs['location'],
            "images":kwargs['images'],
            "tags":kwargs['tags']
        }
        MEETUPS.append(meetup)
        return meetup

    
    def get_meetup(meetup_id):
        '''this function fetches on meetup record 
        and returns it or returns an error if it is not found
         '''
        meetups = MEETUPS
        
        meetup_ = [meetup for meetup in meetups if meetup["id"] == meetup_id]
        if len(meetup_)!= 0:
            return meetup_[0]
        else:
            return "error"
   
    def get_all_meetups():
        meetups = MEETUPS
        '''function to get all the meetups'''
        return meetups
      

class Rsvp(object):
    def rsvp_meetup(**kwargs):
        '''this function allow user to RSVP for a meetup'''
        rsvp = {
            "id":kwargs["id"],
            "meetup":kwargs["meetup"],
            "user":kwargs["user"],
            "response":kwargs["response"]
        }
        return rsvp
    def get_rsvp(id):
        '''this function gets a single rsvp record '''
        rsvps = RSVPS
        rsvp = [r for r in rsvps if r["id"]==id]
        if len(rsvp) > 0:
            return rsvp[0]
        else:
            return "error"