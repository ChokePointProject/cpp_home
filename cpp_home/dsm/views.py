import string
import logging
import json
from django.conf import settings
from django.shortcuts import render_to_response
from home.models import Country,Region,RegionCountry

logger = logging.getLogger('django')

def root(request):
    return render_to_response('dsm/index.html', {'settings':settings})

def about(request):
    return render_to_response('dsm/about.html', {'settings':settings})

def country(request, country_id):
    country = Country.objects.get(id=country_id)
    transparency = country.incidents.filter(type__in=[17,18]).order_by('-ts')[:20]
    incidents = country.incidents.all().order_by('-ts')[:20]
    features = []
    for incident in incidents:
        rec = {'id':incident.id,'properties':{'html':incident.descr},'geometry':{'type':'Point','coordinates':[incident.lon,incident.lat]}}
        features.append(rec)
    return render_to_response('dsm/country.html', {
                                                    'settings':settings,
                                                    'country': country,
                                                    'incidents': incidents,
                                                    'incident_count': incidents.count(),
                                                    'transparency_incidents': transparency,
                                                    'transparency_incident_count': transparency.count(),
                                                    'features_json': json.dumps(features)
                                                    })
