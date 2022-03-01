from backend.src.migration.data_extractor import extract_csv, extract_data

CSV_HEADER_PATH = '../testdata/data_header.csv'
CSV_PATH = '../testdata/data.csv'
CSV_RESULT = [['A',
               '2',
               'A',
               '',
               'KOSZAROWA (SZPITAL) - Koszarowa - Berenta',
               '3',
               '35',
               '2022-02-05',
               '2999-01-01']]
FIELD_NAMES = 'route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_type2_id,valid_from,valid_until'


class TestCSVExtract:

    def test_extract(self):
        assert extract_csv(CSV_PATH) == CSV_RESULT

    def test_extract_header(self):
        assert extract_csv(CSV_HEADER_PATH, has_header=True) == CSV_RESULT


class TestExtract:

    def test_extract(self):
        assert extract_data(CSV_PATH) == CSV_RESULT
