with open('templateBase','w') as base:
    base.write('p = document.add_paragraph("")')
    base.write('p.add_run("Record Filtering\n").bold = True')
    base.write('p.add_run("Record filters allow an Endeca application to define subsets of the total record set and dynamically limit search and navigation results to these subsets. Record filters are applied before any search processing. The result is that the search query is performed as if the data set only contained records allowed by the record filter.\n\nRecord filters are applied when query is sent into an Endeca MDEX engine. Record filters are used for the site variable and repository, but are not required since this is a single site implementation. ")')
    base.write('p.add_run("\n\nFilter List \n").bold = True')
    base.write('p.add_run("All dimension and properties can be filtered on. Dimensions are always filterable; the properties listed below are currently configured for filtering.\n\n")')
    base.write('p.add_run("Current Filterable Properties\n").bold = True')
