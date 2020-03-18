from dataflows import Flow, load, dump_to_path, dump_to_zip, printer, add_metadata
from dataflows import sort_rows, filter_rows, find_replace, delete_fields, set_type, validate, unpivot




def listings_csv():
    flow = Flow(
        # Load inputs
        load('http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2020-02-14/visualisations/listings.csv', format='csv', ),
        # Process them (if necessary)
        # Save the results
        add_metadata(name='listings_csv', title='''listings.csv'''),
        printer(),
        dump_to_path('listings_csv'),
    )
    flow.process()


if __name__ == '__main__':
    listings_csv()