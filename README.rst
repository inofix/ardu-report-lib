ardu-report-lib
===============

.. image:: https://travis-ci.org/zwischenloesung/ardu-report-lib.svg?branch=master
       :target: https://travis-ci.org/zwischenloesung/ardu-report-lib

Python library to report back the sensor data from, e.g., our arduino(s).

See https://github.com/zwischenloesung/ardu-report for a CLI using it.

Dependencies, Requirements
--------------------------

 * Unix/Linux

 * Python 2.7, 3.3, 3.4, 3.5

  - see requirements.txt for the dependencies


TODOs
-----

 * Upload to PyPI


Basic Idea
----------

There is a central data store that holds the data. It accepts JSON as input and returns JSON. Both in- and
output JSON can be specified by a JSON Schema (see below).

One or more reader threads can be connected to one or more serial lines to collect the data from the
microcontroller connected to the actual sensors. Whenever data is sent over the wire, it is then stored
in the data store object described above.

A third reporter object can then be told to report the data on a regular basis to some URL.


Usage
-----

Import and Setup
~~~~~~~~~~~~~~~~
See https://github.com/zwischenloesung/ardu-report for a concrete example implementation.

Import the classes::

    from libardurep import datastore, datareporter, serialreader

Create the objects (example)::

    store = datastore.DataStore()
    url = 'file:///tmp/example'
    reporter = datareporter.DataReporter(store, url)
    rounds = 10
    device = '/dev/ttyACM0'
    baudrate = 9600
    reader = serialreader.SerialReader(device, baudrate, store, rounds)


Does It Make Sense for Your Project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we really only
need some sort of identifier and a value,
for a valid sensor datum, it is quite trivial to accept
a wide range of input JSON as provided by the sensor infrastructure
and to be able to transform
it to some output JSON as needed by your display infrastructure.

There is a meta schema definition in the 'schema' folder that
describes the valid schemas. Any such valid schema can be provided
to the data store object to describe the JSON expected to
come from the sensor infrastructure and equally for the JSON
that is desired as output. Load the custom schema on DataStore
creation like::

    datastore.DataStore(input_schema, input_meta_schema, output_schema, output_meta_schema)

The 'example' folder contains JSON file that
validates against the schema and the tests/test\_json.py has
a test run for both the input.json against the schema and the
schema against the meta-schema.. Furthermore there is an
extended-input.json that validates against an example
customized schema (extended-input-schema.json), with itself
still validates against the meta-schema.json.


Example Data for Python Processing
----------------------------------

INPUT: JSON from the (e.g.) arduino over the serial line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two examples under the 'examples' folder.

The simple 'input.json'
shows two example measurements.
The "id" and "value" entries in the object are
mandatory. The "unit" and "threshold" are recognized
(and interpreted for the text form output to stdout, see the datastore
code for details).

Note that no timestamp joins the data. Often there is no
clock source available to the dump sensor controller. The timestamp
is added in the output below though. If a timestamp is available
in the input though, it can still be passed on of course.

See the 'extended-input.json' for an example with
more enries and custom naming.


OUTPUT: Target JSON from the (e.g.) raspberry pi for the use in e.g. a web app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data is appended to a file ("file://") as
a continuing list of JSON objects containing sensor value entries or
sent as a complete JSON array to a web server ("http://" / "https://")
as a POST request. Alternatively the data is just printed in
text form to stdout.

Example JSON output can be found under the examples folder:

 * output.json - default

 * custom-output.json - if an output JSON scheme is defined, the
   entries can be translated. The output JSON must validate against
   the meta schema..

