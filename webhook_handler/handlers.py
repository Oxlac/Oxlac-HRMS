# webhook_handler/handlers.py
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests
import json
import os

@receiver(post_save)
# Webhook triggered when a new candidate is created
def handle_model_update(sender, created, instance, **kwargs):
    if sender.__name__ == 'Candidate' and created: 
        print("hello"*100)
        # send a request to the webhook
        url = "https://discord.com/api/webhooks/1214916560590741564/lWDmGMRLd7cZ8Aa7-819ewdAPqUPgse6mRPGRDbtJmNom3EgSeXrKX13TODMasqYZ1fs"
        data = {
            "username": 'Oxlac HRMS',
            "avatar_url": "https://oxlac.com/favicon.png",
            "embeds": [
                {
                    "author": {
                        "name": "Oxlac HRMS",
                        "url": "https://oxlac.com",
                        "icon_url": "https://oxlac.com/favicon.png"
                    },
                    "title": "New Candidate has applied for position " + str(instance.job_position_id),
                    "url": "https://employee.oxlac.com/candidate-view/" + str(instance.recruitment_id)+"/",
                    "description": "Candidate Name: " + instance.name + "\n" + "Email: " + instance.email,
                }
            ]
        }
        # send the request
        try:
            temp = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
            print(temp.text)
        except Exception as e:
            print("Error in sending request to discord: ", e)
