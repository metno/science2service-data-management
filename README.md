# Science2Service data management

Welcome to the data management session!

## Preparations

Kickstart your own Python environment with the following commands.

1. Install `python3-venv` package if you don't have it from before.
    ```bash
    sudo apt-get install -y python3-venv
    ```
0. Create your Python virtual environment.
    ```bash
    python3 -m venv ~/v/dataman
    ```
0. Source your Python virtual environment. **PS!** Do this in every new terminal window you want to use this virtual environment.
    ```bash
    source ~/v/dataman/bin/activate
    ```
0. Upgrade pip package to latest version to avoid unnecessary errors during installation of requirements.
    ```bash
    pip3 install --upgrade pip
    ```
0. Install Python wheel package for downloading python pre-compiled libraries.
   ```bash
   pip3 install wheel
   ```
0. Clone this Git-repository.
    ```bash
    git clone https://github.com/metno/science2service-data-management.git
    ```
0. Enter the Git-repository.
    ```bash
    cd science2service-data-management
    ```
0. Install this workshops Python requirements in your own environment.
    ```bash
    pip3 install -r requirements.txt
    ```
0. Optional: install tools to easy look into your netcdf file:
    ```bash
    sudo apt-get install netcdf-bin
    ```
## Initial test of attributes in test dataset

Run py-mmd-tools on the dataset
```bash
python scripts/nc2mmd.py -i data/test-dataset.nc -o ./ -k
```

Should give you something like this:
```bash
WARNING:root:Using default values [ADC, METNCS] for the MMD collection field. Please, specify other collection(s) if this is wrong. Valid collections are provided in the MMD documentation (https://htmlpreview.github.io/?https://github.com/metno/mmd/blob/master/doc/mmd-specification.html#collection-keywords)
Traceback (most recent call last):
  File "scripts/nc2mmd.py", line 85, in <module>
    main(parser.parse_args())
  File "scripts/nc2mmd.py", line 79, in main
    checksum_calculation=args.checksum_calculation
  File "/home/trygveas/v/dataman/lib/python3.6/site-packages/py_mmd_tools/nc_to_mmd.py", line 1047, in to_mmd
    raise AttributeError('\n\t'+'\n\t'.join(self.missing_attributes['errors']))
AttributeError: 
	id is a required attribute.
	naming_authority is a required attribute.
	institution_short_name is a required attribute
	institution is a required attribute
	ACDD attribute date_created is required
	title is a required ACDD attribute
	summary is a required ACDD attribute
	time_coverage_start is a required ACDD attribute
	keywords_vocabulary is a required ACDD attribute
	keywords is a required ACDD attribute
	geospatial_lat_max is a required attribute
	geospatial_lat_min is a required attribute
	geospatial_lon_max is a required attribute
	geospatial_lon_min is a required attribute
	iso_topic_category is a required attribute
	spatial_representation is a required attribute
```

## Start filling in the needed discovery metadata

1. First generate an uuid and add this to your dataset
    ```bash
    python scripts/add-uuid.py data/test-dataset.nc
    ```

0. Run the check again
    ```bash
    python scripts/nc2mmd.py -i data/test-dataset.nc -o ./ -k
    ```
    Now the `id is a required attribute.` should be gone.

0. What about the rest?
    ```bash
    python scripts/add-other-needed-information.py data/test-dataset.nc
    ```

0. Run the check again:
    ```bash
    python scripts/nc2mmd.py -i data/test-dataset.nc -o ./ -k
    ```
    Now only a warning should be left. This is OK

0. Generate MMD xml file:
    ```bash
    python scripts/nc2mmd.py -i data/test-dataset.nc -o ./
    ```
    Should give you an MMD xml file `test-dataset.xml`

0. MMD xml file should looke like this:
    ```xml
    <mmd:mmd xmlns:mmd="http://www.met.no/schema/mmd" xmlns:gml="http://www.opengis.net/gml">
      <mmd:metadata_identifier>no.met:9ffb8513-3d76-48a2-8f32-a870b922a686</mmd:metadata_identifier>
      <mmd:title xml:lang="en">Direct Broadcast data processed in satellite swath to L1C.</mmd:title>
      <mmd:title xml:lang="no">Direktesendte satellittdata prosessert i satellittsveip til L1C.</mmd:title>
      <mmd:abstract xml:lang="en">Direct Broadcast data received at MET NORWAY Oslo. Processed by standard processing software to geolocated and calibrated values in satellite swath in received instrument resolution.</mmd:abstract>
      <mmd:abstract xml:lang="no">Direktesendte satellittdata mottatt ved Meteorologisk Institutt Oslo. Prosessert med standard prosesseringssoftware til geolokaliserte og kalibrerte verdier i satellitsveip i mottatt instrument oppløsning.</mmd:abstract>
      <mmd:metadata_status>Active</mmd:metadata_status>
      <mmd:dataset_production_status>Complete</mmd:dataset_production_status>
      <mmd:collection>ADC</mmd:collection>
      <mmd:collection>METNCS</mmd:collection>
      <mmd:last_metadata_update>
        <mmd:update>
          <mmd:datetime>2022-09-20T09:58:34Z</mmd:datetime>
          <mmd:type>Created</mmd:type>
        </mmd:update>
        <mmd:update>
          <mmd:datetime>2022-09-20T09:58:34Z</mmd:datetime>
          <mmd:type>Created</mmd:type>
        </mmd:update>
      </mmd:last_metadata_update>
      <mmd:temporal_extent>
        <mmd:start_date>2022-09-20T09:58:34.146771Z</mmd:start_date>
        <mmd:end_date>2022-09-20T12:03:34.146767Z</mmd:end_date>
      </mmd:temporal_extent>
      <mmd:temporal_extent>
        <mmd:start_date>2022-09-20T12:03:34.146767Z</mmd:start_date>
      </mmd:temporal_extent>
      <mmd:iso_topic_category>climatologyMeteorologyAtmosphere</mmd:iso_topic_category>
      <mmd:iso_topic_category>environment</mmd:iso_topic_category>
      <mmd:iso_topic_category>oceans</mmd:iso_topic_category>
      <mmd:keywords vocabulary="GCMDSK">
        <mmd:keyword>Earth Science &gt; Atmosphere &gt; Atmospheric radiation</mmd:keyword>
        <mmd:resource>https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords</mmd:resource>
        <mmd:separator></mmd:separator>
      </mmd:keywords>
      <mmd:keywords vocabulary="GCMDPROV">
        <mmd:keyword> Government Agencies-non-US &gt; Norway &gt; NO/MET &gt; Norwegian Meteorological Institute</mmd:keyword>
        <mmd:resource>https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/providers</mmd:resource>
        <mmd:separator></mmd:separator>
      </mmd:keywords>
      <mmd:keywords vocabulary="GCMDLOC">
        <mmd:keyword>Geographic Region &gt; Northern Hemisphere</mmd:keyword>
        <mmd:resource>https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/locations</mmd:resource>
        <mmd:separator></mmd:separator>
      </mmd:keywords>
      <mmd:keywords vocabulary="GEMET">
        <mmd:keyword>Meteorological geographical features</mmd:keyword>
        <mmd:keyword>Atmospheric conditions</mmd:keyword>
        <mmd:keyword>Oceanographic geographical features</mmd:keyword>
        <mmd:resource>http://inspire.ec.europa.eu/theme</mmd:resource>
        <mmd:separator></mmd:separator>
      </mmd:keywords>
      <mmd:keywords vocabulary="NORTHEMES">
        <mmd:keyword>Weather and climate</mmd:keyword>
        <mmd:resource>https://register.geonorge.no/subregister/metadata-kodelister/kartverket/nasjonal-temainndeling</mmd:resource>
        <mmd:separator></mmd:separator>
      </mmd:keywords>
      <mmd:geographic_extent>
        <mmd:rectangle srsName="EPSG:4326">
          <mmd:north>70.0</mmd:north>
          <mmd:south>60.0</mmd:south>
          <mmd:east>20</mmd:east>
          <mmd:west>-20</mmd:west>
        </mmd:rectangle>
      </mmd:geographic_extent>
      <mmd:dataset_language>en</mmd:dataset_language>
      <mmd:operational_status>Operational</mmd:operational_status>
      <mmd:access_constraint>Open</mmd:access_constraint>
      <mmd:use_constraint>
        <mmd:identifier>CC-BY-4.0</mmd:identifier>
        <mmd:resource>https://spdx.org/licenses/CC-BY-4.0</mmd:resource>
      </mmd:use_constraint>
      <mmd:personnel>
        <mmd:role>Investigator</mmd:role>
        <mmd:name>Norwegian Meteorological Institute</mmd:name>
        <mmd:email>post@met.no</mmd:email>
        <mmd:organisation>Norwegian Meteorological Institute</mmd:organisation>
      </mmd:personnel>
      <mmd:personnel>
        <mmd:role>Metadata author</mmd:role>
        <mmd:name>DIVISION FOR OBSERVATION QUALITY AND DATA PROCESSING</mmd:name>
        <mmd:email>post@met.no</mmd:email>
        <mmd:organisation>Norwegian Meteorological Institute</mmd:organisation>
      </mmd:personnel>
      <mmd:personnel>
        <mmd:role>Technical contact</mmd:role>
        <mmd:name>Norwegian Meteorological Institute</mmd:name>
        <mmd:email>post@met.no</mmd:email>
        <mmd:organisation>Norwegian Meteorological Institute</mmd:organisation>
      </mmd:personnel>
      <mmd:data_center>
        <mmd:data_center_name>
          <mmd:short_name>METNO</mmd:short_name>
          <mmd:long_name>Norwegian Meteorological Institute</mmd:long_name>
        </mmd:data_center_name>
        <mmd:data_center_url>met.no</mmd:data_center_url>
      </mmd:data_center>
      <mmd:storage_information>
        <mmd:file_name>test-dataset.nc</mmd:file_name>
        <mmd:file_location>data/test-dataset.nc</mmd:file_location>
        <mmd:file_format>NetCDF-CF</mmd:file_format>
        <mmd:file_size unit="MB">3.85</mmd:file_size>
        <mmd:checksum type=""></mmd:checksum>
      </mmd:storage_information>
      <mmd:project>
        <mmd:long_name>Govermental core service</mmd:long_name>
      </mmd:project>
      <mmd:spatial_representation>grid</mmd:spatial_representation>
      <mmd:dataset_citation>
        <mmd:author>Norwegian Meteorological Institute</mmd:author>
        <mmd:publication_date>2022-09-20T09:58:34Z</mmd:publication_date>
        <mmd:title>Direct Broadcast data processed in satellite swath to L1C.</mmd:title>
      </mmd:dataset_citation>
    </mmd:mmd>
    ```

0. Validate your MMD xml at the DMCI endpoint
    ```bash
    curl --data-binary @test-dataset.xml  https://dmci-dev.s-enda.k8s.met.no/v1/validate
    ```

    This will unfortunately fail. We are working on fixing this.
    The soulution now is to edit the second line in the MMD xml file and remove
    the prefix to the uuid `no.met:`

## Optional: setup a CSW test setup (beyond the scope of this course)

1. First you need to install vagrant and virtualbox. This is the first two points as described here
    ```http
    https://gitlab.met.no/it/kurs/ansible-workshop/-/blob/master/PREP.md
    ```
    If you get into trouble see trouble shooting further down at this page.

0. Clone repo
    ```bash
    git clone https://github.com/metno/vagrant-s-enda.git
    ```

0. Go to your directory and start vagrant:
    ```bash
    cd vagrant-s-enda
    vagrant up
    ```

0. Open a browser with the test CSW:
    ```http
    http://192.168.56.10/?mode=opensearch&service=CSW&version=2.0.2&request=GetRecords&elementsetname=full&typenames=csw:Record&resulttype=results
    ```

0. Send your MMD file to the CSW catalog via the DMCI:
    ```bash
    curl --data-binary @test-dataset.xml http://192.168.56.10:8000/v1/insert
    ```



<!---
vim: set spell spelllang=en:
-->
