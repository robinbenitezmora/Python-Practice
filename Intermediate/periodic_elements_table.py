import csv, sys, re

elementsFile = open('elements.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elementsData = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = [
    'Atomic Number',
    'Element',
    'Symbol',
    'Atomic Weight',
    'Period',
    'Group',
    'Phase',
    'Most Stable Crystal',
    'Type',
    'Ionic Radius',
    'Atomic Radius',
    'Electronegativity',
    'First Ionization Potential',
    'Density',
    'Melting Point',
    'Boiling Point',
    'Isotopes',
    'Discoverer',
    'Year of Discovery',
    'Specific Heat Capacity',
    'Electron Configuration',
    'Display Row',
    'Display Column'
]

LONGEST_COLUMN = 0
for column in ALL_COLUMNS:
    if len(column) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(column)

def print_element_data(elementData):
    for i in range(len(ALL_COLUMNS)):
        print(f'{ALL_COLUMNS[i]:<{LONGEST_COLUMN}}: {elementData[i]}')

def get_element_data(element):
    for elementData in elementsData:
        if elementData[1].lower() == element.lower():
            return elementData
    return None

def get_periodic_table_data(periodicTableData, row, column):
    for elementData in periodicTableData:
        if elementData[22] == str(row) and elementData[23] == str(column):
            return elementData
    return None

def print_periodic_table_data(periodicTableData):
    for elementData in periodicTableData:
        print_element_data(elementData)
        print()

def get_periodic_table_data_by_element(element):
    elementData = get_element_data(element)
    if elementData is None:
        return None
    return get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22]))

def get_periodic_table_data_by_position(row, column):
    return get_periodic_table_data(elementsData, row, column)

def get_periodic_table_data_by_symbol(symbol):
    for elementData in elementsData:
        if elementData[2].lower() == symbol.lower():
            return get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22]))
    return None

def get_periodic_table_data_by_atomic_number(atomicNumber):
    for elementData in elementsData:
        if elementData[0] == atomicNumber:
            return get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22]))
    return None

def get_periodic_table_data_by_discoverer(discoverer):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_year_of_discovery(yearOfDiscovery):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[18] == yearOfDiscovery:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_phase(phase):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[6].lower() == phase.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_type(elementType):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[7].lower() == elementType.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_year_of_discovery(discoverer, yearOfDiscovery):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[18] == yearOfDiscovery:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_phase(discoverer, phase):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[6].lower() == phase.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_type(discoverer, elementType):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[7].lower() == elementType.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_year_of_discovery_and_phase(discoverer, yearOfDiscovery, phase):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[18] == yearOfDiscovery and elementData[6].lower() == phase.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_year_of_discovery_and_type(discoverer, yearOfDiscovery, elementType):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[18] == yearOfDiscovery and elementData[7].lower() == elementType.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_phase_and_type(discoverer, phase, elementType):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[6].lower() == phase.lower() and elementData[7].lower() == elementType.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_discoverer_and_year_of_discovery_and_phase_and_type(discoverer, yearOfDiscovery, phase, elementType):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[17].lower() == discoverer.lower() and elementData[18] == yearOfDiscovery and elementData[6].lower() == phase.lower() and elementData[7].lower() == elementType.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_atomic_weight(atomicWeight):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[3] == atomicWeight:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_period(period):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[21] == str(period):
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_group(group):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[22] == str(group):
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_ionic_radius(ionicRadius):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[9] == ionicRadius:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_atomic_radius(atomicRadius):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[10] == atomicRadius:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_electronegativity(electronegativity):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[11] == electronegativity:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_first_ionization_potential(firstIonizationPotential):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[12] == firstIonizationPotential:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_density(density):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[13] == density:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_melting_point(meltingPoint):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[14] == meltingPoint:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_boiling_point(boilingPoint):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[15] == boilingPoint:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_isotopes(isotopes):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[16] == isotopes:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_specific_heat_capacity(specificHeatCapacity):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[19] == specificHeatCapacity:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_electron_configuration(electronConfiguration):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[20].lower() == electronConfiguration.lower():
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row(displayRow):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_column(displayColumn):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[25] == displayColumn:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column(displayRow, displayColumn):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_range(displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_range(displayRowStart, displayRowEnd):
    periodicTableData = []
    for elementData in elementsData:
        if displayRowStart <= int(elementData[24]) <= displayRowEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_column_range(displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range(displayRow, displayColumn, displayRowStart, displayRowEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and displayRowStart <= int(elementData[24]) <= displayRowEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_column_range(displayRow, displayColumn, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[25] == displayColumn and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_row_range_and_display_column_range(displayRow, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_column_and_display_row_range_and_display_column_range(displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_range_and_display_column_range(displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData

def get_periodic_table_data_by_display_row_and_display_column_and_display_row_range_and_display_column_range_and_display_row_range_and_display_column_range(displayRow, displayColumn, displayRowStart, displayRowEnd, displayColumnStart, displayColumnEnd):
    periodicTableData = []
    for elementData in elementsData:
        if elementData[24] == displayRow and elementData[25] == displayColumn and displayRowStart <= int(elementData[24]) <= displayRowEnd and displayColumnStart <= int(elementData[25]) <= displayColumnEnd:
            periodicTableData.append(get_periodic_table_data(elementsData, int(elementData[21]), int(elementData[22])))
    return periodicTableData