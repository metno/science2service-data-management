#!/usr/bin/env python

from datetime import datetime, timedelta, timezone
import sys
import netCDF4 as nc
from uuid import uuid4

with nc.Dataset(sys.argv[1], "a") as f:
    f.id = str(uuid4())
    
    f.collection = 'METNCS'

    f.title = 'Direct Broadcast data processed in satellite swath to L1C.'
    f.title_lang = 'en'
    f.title_no = 'Direktesendte satellittdata prosessert i satellittsveip til L1C.'

    # MMD abstract, ACDD summary
    f.summary = 'Direct Broadcast data received at MET NORWAY Oslo. '
    f.summary += 'Processed by standard processing software to geolocated '
    f.summary += 'and calibrated values in satellite swath in received instrument resolution.'
    f.summary_lang = 'en'
    f.summary_no = 'Direktesendte satellittdata mottatt ved Meteorologisk Institutt Oslo. '
    f.summary_no += 'Prosessert med standard prosesseringssoftware til geolokaliserte og kalibrerte verdier '
    f.summary_no += 'i satellitsveip i mottatt instrument oppløsning.'
    # MMD temporal_extent,start_date, ACDD time_coverage_start

    f.processing_level = 'Operational'
    # MMD use_constraint_identifier, ACDD license
    f.license = 'CC-BY-4.0'
    f.license_resource = 'https://spdx.org/licenses/CC-BY-4.0'

    # MMD personnel, ACDD creator
    f.creator_type = 'institution'
    f.creator_role = 'Investigator'
    f.creator_name = 'Norwegian Meteorological Institute'
    f.creator_email = 'post@met.no'
    f.creator_url = 'met.no'
    f.creator_institution = 'Norwegian Meteorological Institute'

    f.contributor_name = "DIVISION FOR OBSERVATION QUALITY AND DATA PROCESSING,Norwegian Meteorological Institute"
    f.contributor_role = "Metadata author,Technical contact"
    f.contributor_email = "post@met.no,post@met.no"
    f.contributor_institution = "Norwegian Meteorological Institute,Norwegian Meteorological Institute"
    f.contributor_type = "institution,institution"
    f.contributor_url = "met.no,met.no"

    f.publisher_institution = 'MET NORWAY'
    f.publisher_country = 'NORWAY'
    f.publisher_email = 'post@met.no'
    f.publisher_name = 'DIVISION FOR OBSERVATION QUALITY AND DATA PROCESSING'
    f.publisher_url = 'met.no'
    f.keywords = 'GCMDSK:Earth Science > Atmosphere > Atmospheric radiation, '
    f.keywords += 'GCMDLOC:Geographic Region > Northern Hemisphere, '
    f.keywords += 'GCMDPROV: Government Agencies-non-US > Norway > NO/MET > Norwegian Meteorological Institute, '
    f.keywords += 'GEMET:Meteorological geographical features, GEMET:Atmospheric conditions, '
    f.keywords += 'GEMET:Oceanographic geographical features, NORTHEMES:Weather and climate'
    f.keywords_vocabulary = 'GCMDSK:GCMD Science Keywords:https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords, '
    f.keywords_vocabulary += 'GCMDPROV:GCMD Providers:https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/providers, '
    f.keywords_vocabulary += 'GCMDLOC:GCMD Locations:https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/locations, '
    f.keywords_vocabulary += 'GEMET:INSPIRE themes:http://inspire.ec.europa.eu/theme, '
    f.keywords_vocabulary += 'NORTHEMES:GeoNorge Themes:https://register.geonorge.no/subregister/metadata-kodelister/kartverket/nasjonal-temainndeling'
    f.keywords_resource = 'GCMD:https://gcmdservices.gsfc.nasa.gov/static/kms/, GEMET:http://inspire.ec.europa.eu/theme, '
    f.keywords_resource += 'NORTHEMES:https://register.geonorge.no/subregister/metadata-kodelister/kartverket/nasjonal-temainndeling'

    f.institution = 'Norwegian Meteorological Institute'
    f.institution_short_name = 'METNO'
    f.project = 'Govermental core service'

    # MMD mandatory not in ACDD
    f.metadata_status = 'Active'
    f.dataset_production_status = 'Complete'
    f.iso_topic_category = 'climatologyMeteorologyAtmosphere,environment,oceans'

    f.access_constraint = 'Open'
    f.spatial_representation = 'grid'

    f.naming_authority = 'no.met'

    right_now = datetime.now()
    f.time_coverage_start = '{:%Y-%m-%dT%H:%M:%S.%f}Z'.format(datetime.now(tz=timezone.utc))
    f.time_coverage_end = '{:%Y-%m-%dT%H:%M:%S.%f}Z'.format(right_now + timedelta(minutes=5))
    
    f.ancillary_timeliness = 'NRT'

    f.date_created = '{:%Y-%m-%dT%H:%M:%S}Z'.format(datetime.now(tz=timezone.utc))

    f.date_metadata_modified = '{:%Y-%m-%dT%H:%M:%S}Z'.format(datetime.now(tz=timezone.utc))
    f.date_metadata_modified_type = 'Created'

    # f.related_dataset_relation_type = 'parent'
    # f.related_dataset_id = parent_uuid

    f.Conventions = 'CF-1.7, ACDD-1.3'

    f.geospatial_lat_min = 60.0
    f.geospatial_lat_max = 70.0
    f.geospatial_lon_min = -20
    f.geospatial_lon_max = 20

