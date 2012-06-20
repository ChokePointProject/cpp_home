import string
import logging
import json
from django.conf import settings
from django.shortcuts import render_to_response
from home.models import Country,Region,RegionCountry

logger = logging.getLogger('django')

def root(request):
    return render_to_response('index.html', {'settings':settings})

def about(request):
    return render_to_response('about.html', {'settings':settings})

def countries(request):
    section_list = {}
    country_list = Country.objects.all().order_by('name')
    for country in country_list:
        initial = country.name[0].lower()
        if not initial in section_list:
            section_list[initial] = []
        section_list[initial].append(country)
    return render_to_response('country/index.html', {
                                                     'settings':settings,
                                                     'countries': country_list, 
                                                     'sections':sorted(section_list.iteritems()), 
                                                     'initials':sorted(section_list.keys())
                                                     })


def regions(request):
    section_list = {}
    for cr in RegionCountry.objects.all():
        region = cr.region.name
        if not region in section_list:
            section_list[region] = []
        section_list[region].append(cr.country)
    return render_to_response('region/index.html', {
                                                    'settings':settings,
                                                    'sections':sorted(section_list.iteritems()), 
                                                    })

def country(request, country_id):
    country = Country.objects.get(id=country_id)
    transparency = country.incidents.filter(type__in=[17,18]).order_by('-ts')[:20]
    incidents = country.incidents.all().order_by('-ts')[:20]
    features = []
    for incident in incidents:
        rec = {'id':incident.id,'properties':{'html':incident.descr},'geometry':{'type':'Point','coordinates':[incident.lon,incident.lat]}}
        features.append(rec)
    return render_to_response('country/view.html', {
                                                    'settings':settings,
                                                    'country': country,
                                                    'incidents': incidents,
                                                    'incident_count': incidents.count(),
                                                    'transparency_incidents': transparency,
                                                    'transparency_incident_count': transparency.count(),
                                                    'features_json': json.dumps(features)
                                                    })
