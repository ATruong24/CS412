'''
Description: Models for Voter data
Author: Anthony Truong
Date: Fall 2026
'''

from django.db import models

class Voter(models.Model):
    '''
    Store the data for one registered voter in Newton
    '''

    last_name = models.TextField()
    first_name = models.TextField()

    street_number = models.TextField()
    street_name = models.TextField()
    apartment_number = models.TextField(blank=True)
    zip_code = models.TextField()

    date_of_birth = models.DateField()
    date_of_registration = models.DateField()

    party_affiliation = models.CharField(max_length=2)
    precinct_number = models.TextField()

    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()

    voter_score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of the voter'''
        return (f'{self.first_name} {self.last_name}, 'f'{self.street_number} {self.street_name} ' f'({self.party_affiliation}, score {self.voter_score})')

def load_data():
    '''Load Voter data from CSV File into DjangoDB'''

    Voter.objects.all().delete()

    
    filename = '/Users/atruong/Downloads/newton_voters.csv'
    f = open(filename)
    f.readline()

    for line in f:
        fields = line.strip().split(',')
        try:
            # create voter from this CSV row
            voter = Voter(
                last_name=fields[1],
                first_name=fields[2],
                street_number=fields[3],
                street_name=fields[4],
                apartment_number=fields[5],
                zip_code=fields[6],
                date_of_birth=fields[7],
                date_of_registration=fields[8],
                party_affiliation=fields[9].strip(),
                precinct_number=fields[10],
                v20state=(fields[11] == 'TRUE'),
                v21town=(fields[12] == 'TRUE'),
                v21primary=(fields[13] == 'TRUE'),
                v22general=(fields[14] == 'TRUE'),
                v23town=(fields[15] == 'TRUE'),
                voter_score=int(fields[16]),
            )
            voter.save() 

        except Exception as e:
            print(f'Skipped: {fields} ({e})')

    f.close()
    print(f'Created {Voter.objects.count()} Voters.')