from __future__ import print_function
import os
import fileinput

#################################################################################################
##############################Create Tables from Generator ##########################################
def pythonDocCreator(inFile,outFile):
    if os.path.getsize(inFile) > 0:
        # Grabs the header row for the table    
        with open(inFile,'r') as myfile:
            head = myfile.readlines()
        head = head[0].split(',')
        # Creates a list of the number of columns
        columns = len(head) - 1
        l = []
        while columns > -1:
            string = str(columns)
            l.append(string)
            columns = columns - 1
        # Sets the number of columns for the table 
        columns = len(head)
        with open(outFile,'a') as file:
            file.write('\ntable = document.add_table(rows=1, cols='+str(columns)+')\nhdr_cells = table.rows[0].cells\n')
        # Reverses the list above
        l = l[::-1]
        # Adds the header to the table
        columns = len(head) - 1
        x = 0
        while columns > -1:
            k = l[x]
            g = head[x]
            with open(outFile,'a') as file:
                file.write('hdr_cells['+str(k)+'].text = "'+g.rstrip()+'"\n')
            x  = x +1
            columns = columns -1
    
        with open(outFile,'a') as file:
            file.write('row_cells = table.add_row().cells\n')
                
        with open(inFile,'r') as myfile:
            entry = myfile.readlines()
            for line in entry[1:]:
                if len(line) > 1:
                    with open(outFile,'a') as file:
                        file.write('row_cells = table.add_row().cells\n')
                        line = line.split(',')
                        columns = len(head) - 1
                        x = 0
                        while columns > -1:
                            k = l[x]
                            g = head[x]
                            with open(outFile,'a') as file:
                                file .write('row_cells['+k+'].text = str("'+line[int(k)].rstrip()+'")\n')
                            x  = x +1
                            columns = columns -1
                else:
                    pass
    else:
        pass
#################################################################################################
##############################Create Opening/Closing Lines ##########################################
def createPython(outFile):
    with open(outFile,'w') as file:
        file .write('from docx import Document\nfrom docx.shared import Inches\n\ndocument = Document()\n\n')
def endPython(outFile):                 
    with open(outFile,'a') as file:
        file .write('\n\ndocument.add_page_break()\n\ndocument.save("C:/Daniel/techSpectoDoc/demo.docx")')
#################################################################################################
#################################Create Python Client Tech Spec######################################
createPython('templateBase.py')

with open('templateBase.py','a') as base:
    base.write('''document.add_heading("Overview", 1)
        
p = document.add_paragraph("")
p.add_run("Project Overview\\n").bold = True
p.add_run("PBS has deployed the Endeca IAP solution that provides search, Guided Navigation, and dynamic merchandising functionality on the pbs.org site.PBS engaged with Thanx Media Professional Services for guidance Finish(of the Data Foundry and pipeline processes for the creation of the indices that is utilized by the sites).  The user interface portion and control scripts for the application were developed by PBS to interact with the MDEX Engine through the Endeca Assembler API.")
p.add_run("\\n\\nAbout the Technical Specification Document\\n").bold = True
p.add_run("The purpose of this document is to outline the implementation details for the Endeca IAP instance reflecting the requirements defined through a Requirements Workshop and subsequently captured in the PBS Business Requirements document.  The Technical Specification document contains information about Endeca, index creation, custom scripts, and operational processes through control scripts and the Endeca Workbench.")
        
document.add_heading("Overview of Endeca Technology", 1)
        
p = document.add_paragraph("")
p.add_run("Endeca Architecture Overview\\n").bold = True
p.add_run("The basic Endeca Architecture consists of four (4) main parts as illustrated in the diagram: the Endeca Data Foundry (EDF), the Endeca MDEX Engine (MDEX), the Endeca Application Controller (EAC), and the Endeca API.")
        
document.add_picture("C:/Daniel/techSpectoDoc/template/architectureOverview.png", width=Inches(3.25))
        
p = document.add_paragraph("")
p.add_run("Endeca Data Foundry (EDF)\\n").bold = True
p.add_run("The EDF is an offline process that first reads in the source data and application specific configuration files.  Using the instructions outlined in the configuration files; the EDF transforms the raw data into structured data and indexes it.  The output of the EDF is a set of indices (binary and xml files) which are provided to the Endeca MDEX Engines.  This is typically a scheduled offline process that runs, and therefore happens independently of the MDEX Engines handling the runtime queries.")
p.add_run("\\n\\nEndeca MDEX Engine (MDEX)\\n").bold = True
p.add_run("The MDEX is an online server that listens on a specific port for HTTP requests, and responds by returning binary results.  Once a new set of indices is created from the EDF, the MDEX will load the indices into memory at process restart.  The MDEX is also stateless, with no concept of a session object for each user.  This allows multiple MDEX engines with the same set of indices to return the same results, allowing for easy scalability and redundancy behind a load balancer.")
p.add_run("\\n\\nEndeca Application Controller\\n").bold = True
p.add_run("The Endeca Application Controller consists of the Central Server and Agents.  The EAC is installed and runs on the primary Endeca server, creating a single interface for coordinating jobs across all machines.  Agents are installed on each Endeca server and are responsible for the actual work of an Endeca implementation.  Communication to these agents is performed through the EAC Central Server via eaccmd, a command line interface, or Workbench.")
p.add_run("\\n\\nEndeca API\\n").bold = True
p.add_run("The Endeca Presentation Layer Java API can be installed on any application server that supports Java.  The API is used to create and send the query to the MDEX Engine over HTTP.  It receives the response as a binary encoded result object and uses the appropriate methods and objects to display the information in the UI.  The query must be submitted to a pre-defined host and port.  If only one MDEX engine exists, the host and port of the MDEX engine should be configured at the UI level.  If multiple MDEX engines exist behind a load balancer, the host and port of the load balancer should be configured at the UI level. ")
p.add_run("\\n\\nImplementation Architecture\\n").bold = True
p.add_run("Architecture of the Endeca cluster will follow the Oracle Endeca best practice of Authoring/Live clusters. Authoring environments will be run with Live data, and will serve as the Endeca Workbench test platform. An overview of the environment can be found in section 16. ")
        
document.add_heading("Data Definition", 1)
        
p = document.add_paragraph("")
p.add_run("Data Sources\\n").bold = True
p.add_run("There are (4) main data types that make up the pbs.org site indices:")
document.add_paragraph("Records Feed: Provides information that will be used for search, search results, and navigational purposes throughout the site.", style="ListBullet")
document.add_paragraph("PS Record Data Feed: Provides program information that will also be used for search, search results, and navigational purposes throughout the site.", style="ListBullet")
document.add_paragraph("Forum Data Feed: Provides the category information that will be used to display category information and setup the Product Category hierarchy for navigation.", style="ListBullet")
document.add_paragraph("Search Rank Data Feed - Provides the category that will be used to display category information and setup the Product Category hierarchy for navigation.", style="ListBullet")
        
p = document.add_paragraph("")
p.add_run("\\n\\nCrawl Data\\n\\n").bold = True
        
p = document.add_paragraph("")
p.add_run("Partial Pipeline\\n").bold = True
p.add_run("There are (3) data files used to update the pbs.org site through the partial update process.")
document.add_paragraph("Recordupdate.xml: Contains the data which will update an existing record, selectively adding and removing dimension and property values. ", style="ListBullet")
document.add_paragraph("ecordadd.xml: Contains the data which will add an entirely new record with a set of property values to an existing index.", style="ListBullet")
document.add_paragraph("delete.txt: Contains the data which will remove a specific record from an existing index.", style="ListBullet")
        
p = document.add_paragraph("")
p.add_run("\\n\\nData Pre-processing\\n").bold = True
p.add_run("All data pre-processing is performed before the data is loaded into the E:/Endeca/apps/pbsconnect/data/ektron/full/ directory. Before the data is fed into the pipeline, Thanx has implemented several python scripts to clean and check the data. E:/Endeca/apps/pbs/")
        
table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Custom Scripts"
hdr_cells[1].text = "Operation"
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""
        
p = document.add_paragraph("")
p.add_run("\\nEXAMPLE: Thanx has implemented a custom thesaurus script createThesaurus.bat which converts the thesaurus entries to the Endeca required format and feeds it directly into the IFCR.")
p.add_run("\\n\\nEndeca IAP Data Structures\\n").bold = True
p.add_run("\\nProperties\\n").bold = True
p.add_run("The screenshot defines the properties to be created for this implementation.")

document.add_picture("C:/Daniel/techSpectoDoc/template/propertiesScreenshot.png", width=Inches(3.25))

p = document.add_paragraph("")
p.add_run("Dimensions\\n").bold = True
p.add_run("The table below defines the dimensions to be created for this implementation. The dimensions are dynamically generated from the PBS database and the Attribute dimensions list will change over time. Currently there are 27 dimensions defined and these match the list of attribute values defined in this section. Dimensions configuration is defined within the api_input configuration files, defined below. ")

document.add_picture("C:/Daniel/techSpectoDoc/template/dimensionsScreenshot.png", width=Inches(3.25))

p = document.add_paragraph("")
p.add_run("Dimension Groups\\n").bold = True
p.add_run("No dimension groups have been designated for configuration at this time.  Here is where the list of the groups and the dimensions can be defined:")\n''')

pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/dimensionGroups.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''p = document.add_paragraph("")
p.add_run("\\nRecord Filtering\\n").bold = True
p.add_run("Record filters allow an Endeca application to define subsets of the total record set and dynamically limit search and navigation results to these subsets. Record filters are applied before any search processing. The result is that the search query is performed as if the data set only contained records allowed by the record filter.\\n\\nRecord filters are applied when query is sent into an Endeca MDEX engine. Record filters are used for the site variable and repository, but are not required since this is a single site implementation. ")
p.add_run("\\n\\nFilter List\\n").bold = True
p.add_run("All dimension and properties can be filtered on. Dimensions are always filterable; the properties listed below are currently configured for filtering.\\n\\n")
p.add_run("Current Filterable Properties").bold = True\n''')
    
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/recordFilter.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nLanguage Configuration\\n").bold = True
p.add_run("\\nDimension Translations\\n").bold = True
p.add_run("No dimension translation is necessary at this time; all dimensions will appear in English.\\n")
p.add_run("\\nStemming\\n").bold = True
p.add_run("The stemming feature broadens search results to include word roots and word derivations. Stemming is supported for many languages. Endecas Developer Studio tool is used to configure stemming for an Endeca Application. From the menu choose edit>Stemming and select the appropriate language. There will only be one language selected per Endeca Application.")

document.add_picture("C:/Daniel/techSpectoDoc/template/stemming.png", width=Inches(2.25))

p = document.add_paragraph("")
p.add_run("Guided Navigation\\n").bold = True
p.add_run("Guided Navigation is enabled when dimensions are configured in Developer Studio.\\n\\n")
p.add_run("Attribute Navigation\\n").bold = True
p.add_run("Multiple attributes exist for every product item.  For this implementation, most of these attributes are auto-generated and auto-created to be available for refinements.\\n")
p.add_run("\\nPrecedence Rules").bold = True

table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Group"
hdr_cells[1].text = "Dimensions"
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""

p = document.add_paragraph("")
p.add_run("\\nCategory Matching\\n").bold = True
p.add_run("Dimension values are returned when a keyword search is performed.  These allow shortcut links to the selected navigation states.\\n\\nEnabling Dimension Search via Developer Studio for the dimensions above will automatically activate this feature.  The default match mode to use is\\n\\nMatchAll\\n\\nCurrently all of the dimensions except 'Programs' have been enabled for Dimension Search. \\n")
p.add_run("\\nKeyword Search\\n").bold = True
p.add_run("Search Interfaces\\n").bold = True
p.add_run("A search interface is a named collection of properties and dimensions, each of which is enabled for record search in Developer Studio.  A search interface may also contain an ordered collection of one or more ordering strategies.  When a user passes a search term (or terms) to a search interface, the Endeca IAP will search the term(s) against all the properties and dimensions listed in the search interface.\\nA search interface allows you to control record search behavior for groups of one or more properties or dimensions.  Some of the features that can be specified for a search interface include relevance ranking, matching across multiple properties and dimensions, keyword in context results, and partial match.\\n")
p.add_run("All Search Interface\\n").bold = True
p.add_run("The 'all' Search Interface is responsible for the initial search of records in the product catalog via a keyword search.  The records will be searched for matches against the properties defined below.\\n")''')
    
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/searchInterfaces.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nRelevance Ranking\\n").bold = True
p.add_run("Relevance ranking modules provide a level of control over the order in which search results are displayed to the end user of an Endeca IAP application.  Changes to relevance ranking configurations are an important part of on-going search and performance tuning and will continue post-launch.  This section describes the strategy for a retail catalog data set.  It assumes the following:\\n")
document.add_paragraph('The search mode is MatchAllPartial.  By using this mode, you ensure a users search would return a two-words-out-of-five match as well as a four-words-out-of-five match, just at a lower priority.  (For details, see the section 12.3.1: Match Mode).', style='ListBullet')
document.add_paragraph('The strategy is based on a search interface with members such as Name, Category, and Description, in that order.  The order is significant because a match on the first member ranks more highly than a cross-field match or match on the second or third member.\\n', style='ListBullet')
p.add_run("The table below defines the relevance ranking modules to be configured for the search interface. A static module is normally recommended as the final module, in this instance, PBS has added the date_sort_sixty_days as the static module in the 'All' search interface, and searchrank as the static module in the 'search_rank_topic' search interface.\\n")

table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Module Name"
hdr_cells[1].text = "Module Description"
row_cells = table.add_row().cells
row_cells[0].text = "NumFields"
row_cells[1].text = "NumFields has been added to match the current search strategy currently in place on PBS. Numfields ranks records based on the number of fields that match a query completely. "
row_cells = table.add_row().cells
row_cells[0].text = "NTerms"
row_cells[1].text = "Ensures in a multi-word search the more words that match the better.  For example, in a three-word query, results that match all three words will be ranked above results that match only two, which will be ranked above results that match only one."
row_cells = table.add_row().cells
row_cells[0].text = "MaxField"
row_cells[1].text = "Puts cross-field matches as high in priority as possible.  In other words, the more searchable fields that match the customer's search term, the better, as these results will have a higher priority in the results list."
row_cells = table.add_row().cells
row_cells[0].text = "Glom"
row_cells[1].text = "Decomposes cross-field matches, effectively breaking any ties resulting from MaxField.  Together, MaxField and Glom provide the proper ordering, depending upon what matched."
row_cells = table.add_row().cells
row_cells[0].text = "Phrase"
row_cells[1].text = "Considers results containing the user's query as an exact phrase, or a subset of the exact phrase more relevant than matches simply containing the user's search terms scattered throughout the text."

p = document.add_paragraph("")
p.add_run("\\nRecord Matching\\n").bold = True
p.add_run("It is important to give careful consideration to the possible search terms a user might enter in the context of the data being searched.  The features described below impact the way records are retrieved upon execution of a search query.\\n\\nThis section outlines the matching configurations to be used in the PBS implementation.\\n\\n")
p.add_run("Match Mode\\n").bold = True
p.add_run("Match modes control how many of the user's search terms within a multiple-term query are considered by the Endeca Navigation Engine.\\n\\nThe default search mode is MatchAllPartial.  This mode attempts to match all terms in a users search, and returns only those results if they are available.  If there are no records that match all the terms entered, those records that match at least a certain number of terms will be returned instead.  This allows the accuracy of MatchAll mode when applicable, but falls back to a broader MatchPartial mode when appropriate.\\n\\nThe MatchAllPartial search mode can be adjusted by setting the 'Match at least' and 'Omit at most' values for the search interface.  'Match at least' can be adjusted to broaden the search.  By default, this is set to two to help avoid false positive matches.  When set to one, meaning that at least one of the terms the user entered must match in a result, which would broaden the results.\\n\\n'Omit at most' can also be adjusted.  By default, this is set to two, also, to help avoid false positive matches.  This can be set to zero, meaning that any number of terms can be ignored from a given query.\\n\\n <CLIENT> has the following configured:")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Configuration"
row_cells = table.add_row().cells
row_cells[0].text = "Match at least 2 words"
row_cells = table.add_row().cells
row_cells[0].text = "Omit at most 8 words"

p = document.add_paragraph("")
p.add_run("\\nAuto-correct/Did You Mean\\n").bold = True
p.add_run("Auto-correct spelling correction operates by computing alternate spellings for user query terms, evaluating the likelihood that these alternate spellings are the best interpretation, and then using the best alternate spell-corrected query forms to return search results.\\n\\nFor example, a user might search for records containing the text 'frme'.  With spelling correction enabled, the Endeca MDEX Engine will return the expected results: those records containing the text 'frame'.\\n\\nThe auto-correct capability is enabled for this implementation.\\n\\nAuto-correct is enabled for this application.  If the original search criteria returns zero results, an auto-correction will be attempted.  If the auto-corrected term returns results, those results will be displayed.  A message 'No results were found for '[original term]' Results for '[corrected term]' are shown.' indicating the auto-corrected search terms will also be displayed.\\n\\nAuto-correct is enabled with a dgraph flag (below), which is set in the control scripts and/or the Manager Settings in Developer's Studio.\\n\\n--spl\\n\\n'Did You Mean' is related to auto-correct.  While auto-correct is engaged when no results are found for the current search, 'Did You Mean' is utilized when less than 5 results were found for the current search yet more results would be produced had the user searched for a term of similar spelling.  In this case, the results of the original search are returned and a link displaying 'Did you mean [DidYouMean term]?' which allows the user to view the results of the 'Did You Mean' term.\\n\\n'Did You Mean' is enabled with a dgraph flag (below), which is set in the control scripts and/or the Manager Settings in Developer's Studio.\\n\\n--dym\\n")
p.add_run("\\nThesaurus\\n").bold = True
p.add_run("The thesaurus feature provides the ability to configure rules for matching queries to text containing equivalent words or concepts.  The thesaurus is intended for specifying concept-level mappings between words and phrases.  Thesaurus configurations are an important part of on-going search tuning and will occur post-launch.\\n\\nThe thesaurus entries implemented are defined in the Requirements Definition documentation.\\n\\n")
p.add_run("\\nStemming\\n").bold = True
p.add_run("The stemming feature broadens search results to include word roots and word derivations.  Stemming is intended to allow words with a common root form (such as the singular and plural forms of nouns) to be considered interchangeable in search operations.  For example, search results for the word \\"lure\\" will include derivations such as \\"lur\\" and \\"lures,\\"while a search for \\"lures\\" will also include its word root \\"lure\\".\\n\\nStemming functionality utilizes a predefined set of word forms and is not configurable.  For this implementation, stemming will be enabled. \\n\\nStemming will need to be enabled for each Endeca application depending on the language. This is configured though Endeca's Developer Studio by selecting Edit > Stemming from the menu.")

document.add_picture("C:/Daniel/techSpectoDoc/template/stemming.png", width=Inches(2.25))

p = document.add_paragraph("")
p.add_run("\\nStop Words\\n").bold = True
p.add_run("\\nStop words are words set to be ignored by the Endeca MDEX Engine.  Typically, common words like \\"the\\" are included in the stop word list.  In addition, you might want to add terms that are prevalent in your data set.  For example, if your data consists of lists of books, you might want to add the word \\"book\\" itself to the stop word list, since a search on that word would return an impracticably large set of records.\\nFor the PBS implementation, no words are enabled as stop words. Additional stops words can be configured with Developer Studio in the \\"Search Configuration\\" section.\\n\\n")
p.add_run("Search Characters\\n").bold = True
p.add_run("Upper- and lower-case letters and the digits 0 to 9 are automatically included as valid search characters in your Endeca-enabled application.  However, in the case of other characters, such as certain punctuation characters, you can specify whether the character should be indexed along with alphanumeric characters in a token or instead treated as white space.\\n\\n")
p.add_run("Currently there are no additional search characters set up in the pipeline.\\n\\n")
p.add_run("Wildcard Search\\n").bold = True
p.add_run("Wildcard search allows substring matches to be considered when a query is executed, where the user may enter an asterisk (\\"*\\") operator as wildcard character.  For example, a search on 123* will return all items that contain 1234, 12367, 123A, etc.\\n\\n")
''')
 
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/wildcarding.txt","templateBase.py")
 
with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("Phrasing\\n").bold = True
p.add_run("Phrasing functionality allows words that should be considered as a group instead of as individual search terms to be configured accordingly.  If a user's search terms include one of these phrases, the phrase is identified and matches are only considered for those results containing the phrase, as opposed to containing the terms in any order and proximity.  For example, a search for \\"[SAMPLE PHRASE]\\" will return all records that contain the terms \\"[SAMPLE PHRASE]\\" in a single search field.\\n\\n")
p.add_run("Aggregate Records\\n").bold = True
p.add_run("By configuring aggregated records, the application is to display a group of multiple records as though it were a single record in the results list, based on the value of the rollup key.\\n\\nPBS does not currently have a property that can be used to aggregate records.\\n\\n")
p.add_run("Search Results and Display\\n").bold = True
p.add_run("In addition to the actual records returned by a search query, other elements that can impact the user's experience are also made available to the application rendering the results.  These include the ability to sort the results, highlighting blocks of text in the resulting records that contain the search term, as well as \\"Did You Mean\\" functionality.\\n\\nThis section outlines the display configurations used in the PBS Implementation.\\n\\n")
p.add_run("Did You Mean\\n").bold = True
p.add_run("\\"Did You Mean\\" functionality provides an application with the capability to provide the user with explicit alternative suggestions for a keyword search.  For example, if a user searches for \\"clump\\" in the PBS data, there will be one result.  The term \\"clamp\\" however, is much more prevalent (97 results).  When this feature is enabled, the MDEX Engine will respond with the one result for \\"clump\\" but will also suggest that \\"clamp\\" may be what the end-user actually intended.  If multiple suggestions are returned, they will be sorted and presented according to the closeness of the match.\\n\\nA threshold can be set where the system will look for alternate results close to what a customer is looking for.  The default threshold is 5 results, and this setting will not be changed for this implementation.  If the system finds an appropriate alternative that has more results than your initial search term, it will suggest it.  Once the user clicks on the \\"Did You Mean\\" term, product results are returned.\\n\\n")
p.add_run("Snippeting\\n").bold = True
p.add_run("The snippeting feature (also referred to as keyword in context) provides the ability to return an excerpt from a record--a snippet--to an application user who performs a record search query.  A snippet contains the search terms that the user provides along with a portion of the term's surrounding content to provide context.\\n\\n<CLIENT> has indicated that snippeting feature will be enabled for the body field.")
p.add_run("Sorting\\n").bold = True
p.add_run("Search results will be returned to the User Interface based upon relevance ranking.  The user will then be allowed to sort those results by the following:\\n")
''')
    
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/sorting.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''document.add_heading("Merchandising Workbench Configuration", 1)
               
p = document.add_paragraph("")
p.add_run("\\nTwo merchandising opportunities will be provided within the Endeca Workbench.\\n\\nBanners - this is a merchandising zone that allows the business user to add links to visual images, destination urls and/or html (for rotating banners).\\n\\nProduct spotlighting - this is a merchandising zone that allows the business user to select Programs, Tags, and Author to be highlighted within a special section on the page.\\n\\n")
p.add_run("Keyword Redirects\\n").bold = True
p.add_run("A keyword redirect is a search term-URL pair that defines where a user will be redirected to upon entering a search term.  For example, if the user searches for \\"shipping,\\" the number of records returned may be small (or the search will produce no results), so it may be more appropriate to automatically redirect the user to a page about shipping.\\n\\nCurrently there are no keyword redirects configured within the Developer Studio. Future additions should be added to the table below.\\n")

table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Search Term"
hdr_cells[1].text = "Redirect URL"
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""

p = document.add_paragraph("")
p.add_run("\\n\\nRule Groups\\n").bold = True
p.add_run("Rule Groups organize the large number of merchandising rules into smaller logical categories in order to allow multiple users to access the Endeca Workbench simultaneously.  Rule Groups can be aligned to a specific department, team, template or area of the page.\\n\\nThe default allowable rule groups for Guides search is listed below:\\n")

table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Rule Groups"
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells = table.add_row().cells
row_cells[0].text = ""

p = document.add_paragraph("")
p.add_run("\\n\\nCartridge Type\\n").bold = True
p.add_run("A cartridge is a defined area on a page that will contain Merchandising Rules.  The merchandising cartridges:\\n")

table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Name"
hdr_cells[1].text = "Max Records"
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""

p = document.add_paragraph("")
p.add_run("\\n\\nThe cartridges and the expected behavior need to be defined within the User Interface to properly render the supplemental content from a triggered rule.  Please see the section 10: \\"User Interface\\" for a reference that provides more details on this.\\n\\n")
p.add_run("Rules\\n").bold = True
p.add_run("Once cartridges have been configured, the merchandising rules themselves can be configured.  These rules can be created in Developer Studio, or by business users in the Workbench. \\n\\n")
p.add_run("Pipeline Configuration\\n").bold = True
p.add_run("The pipeline defines the import, conversion, and mapping of source data to Endeca IAP Properties and Dimensions.  PBS will have one pipeline indexing the product catalog. The pipeline is generated using the Endeca 3.1.1 Product Catalog Integration deployment template. No changes to default pipeline layout were made.\\n\\n")
p.add_run("Pipeline Diagram\\n").bold = True
p.add_run("Details of the pipeline diagram are outlined below.\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/pipeline.png", width=Inches(3.25))

p = document.add_paragraph("")
p.add_run("\\n\\nThe pipeline diagrams shown above will be leveraged to index content and product data. The content data will be read into a separate Endeca application.\\n\\n")
p.add_run("Pipeline Details\\n\\n").bold = True
p.add_run("Record Adapters\\n").bold = True
p.add_run("The table below describes the record adapters to be used for loading of the product data.  A record adapter is defined for each input source.\\n")
''')
    
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/recordAdapters.txt","templateBase.py")
  
with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nRecord Manipulators\\n").bold = True
p.add_run("No record manipulations of the source data are required in order to properly load the documents and extract the content.  At this time no record manipulators will be used.\\n")
''')

pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/recordManipulators.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nRecord Assemblers\\n").bold = True
p.add_run("The record assembler component will define the join between the various data extracts. No joins are necessary.\\n")
''')
    
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/recordAssembler.txt","templateBase.py")
   
with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nRecord Caches\\n").bold = True
p.add_run("The table below describes the record caches to be used for preparing data to join.  A record cache is defined for each data set that is joined to the main record set. Since no joins are needed, no record caches exist for this pipeline.\\n")
''')
    
pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/recordCache.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nProperty Mapper\\n").bold = True
p.add_run("The property mapper is responsible for mapping the source properties (from the data extracts themselves or created through a record manipulator) to Endeca IAP dimensions and properties.  The table below identifies the mappings that will be required.\\n\\nFull source data is needed in order to fill in this information.\\n")
''')

pythonDocCreator("C:/Daniel/techSpectoDoc/pipeline/tmp/propertyMapper.txt","templateBase.py")

with open('templateBase.py','a') as base:
    base.write('''\np = document.add_paragraph("")
p.add_run("\\nDimension Server\\n").bold = True
p.add_run("A standard dimension server will be used in this pipeline.\\n")

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Name"
hdr_cells[1].text = "Format"
hdr_cells[2].text = "URL"
row_cells = table.add_row().cells
row_cells[0].text = "DimensionServer"
row_cells[1].text = "XML"
row_cells[2].text = "../data/state/autogen_dimensions.xml.gz"

p = document.add_paragraph("")
p.add_run("\\nIndexer Adapter\\n").bold = True
p.add_run("A standard indexer adapter will be used in this pipeline.\\n")

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Name"
hdr_cells[1].text = "URL"
hdr_cells[2].text = "Output Prefix"
row_cells = table.add_row().cells
row_cells[0].text = "IndexerAdapter"
row_cells[1].text = "../forge_output/"
row_cells[2].text = "<CLIENT>"

p = document.add_paragraph("")
p.add_run("\\nUser Interface\\n").bold = True
p.add_run("The user interface of the PBS implementation will make use of Endeca Search, Guided Navigation, and Merchandising functionality.  The application look-and-feel will be based on PBS design.  PBS will use the Endeca Assembler API Java objects for querying information from the Endeca engine.\\n\\n")
p.add_run("Logging\\n").bold = True
p.add_run("Logging should be performed every time a meaningful query is made to the MDEX Engine, which includes queries performed for the results list and the record details page.  The logging API is separate from the navigation API.  The Log Server, which accepts logging requests, is independent of the MDEX Engine(s).\\n\\nThe Endeca logging queries should be made from the same application that will make the Endeca api calls. This should probably take place in the PBS user interface.\\n\\nThe \\"logserver\\" and \\"logport\\" values will be the same for all requests per Endeca Application. Each Endeca Application will have its own logging server.\\n\\nThe various parameters for logging can be designated within the User Interface.  The entries can include the following parameters:\\n")

table = document.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Name"
hdr_cells[1].text = "Values"
row_cells = table.add_row().cells
row_cells[0].text = "SESSION_ID"
row_cells[1].text = "Logging a session id allows the reporting engine to tie log entries to a session and report on per session statistics."
row_cells = table.add_row().cells
row_cells[0].text = "CONVERTED"
row_cells[1].text = "Set to \\"TRUE\\" when a record has been converted. Conversion means different things for different applications. For e-commerce applications, it usually means that the product has been ordered or added to a shopping cart. Only SESSION_ID and CONVERTED are needed for these log entries."
row_cells = table.add_row().cells
row_cells[0].text = "NUM_RECORDS"
row_cells[1].text = "The number of records returned."
row_cells = table.add_row().cells
row_cells[0].text = "TYPE"
row_cells[1].text = "S - Search only\\nN - Navigation only\\nSN - Search then Navigation\\nR - Record request\\nT - Root request (N=0)"
row_cells = table.add_row().cells
row_cells[0].text = "SEARCH_KEY"
row_cells[1].text = "The property or search interface searched against."
row_cells = table.add_row().cells
row_cells[0].text = "SEARCH_TERMS"
row_cells[1].text = "The search terms the user entered."
row_cells = table.add_row().cells
row_cells[0].text = "SEARCH_MODE"
row_cells[1].text = "MatchAllPartial or otherwise."
row_cells = table.add_row().cells
row_cells[0].text = "SORT_KEY"
row_cells[1].text = "Sort key used if sorting was applied."
row_cells = table.add_row().cells
row_cells[0].text = "DVALS"
row_cells[1].text = "A list of dimension values used for refinement. These values are usually logged as human readable strings, rather than DVAL_IDs."
row_cells = table.add_row().cells
row_cells[0].text = "DIMS"
row_cells[1].text = "A list of dimension names used for refinement."
row_cells = table.add_row().cells
row_cells[0].text = "NUMREFINEMENTS"
row_cells[1].text = "The number of refinements performed."
row_cells = table.add_row().cells
row_cells[0].text = "RECORD_NAMES"
row_cells[1].text = "The record names returned by the query."
row_cells = table.add_row().cells
row_cells[0].text = "DYM_TO"
row_cells[1].text = "Did You Mean terms triggered."
row_cells = table.add_row().cells
row_cells[0].text = "AUTOCORRECT_TO"
row_cells[1].text = "Auto-correction term triggered."
row_cells = table.add_row().cells
row_cells[0].text = "MERCH_RULES"
row_cells[1].text = "Merchandising rules that fired."
row_cells = table.add_row().cells
row_cells[0].text = "IN_MERCH"
row_cells[1].text = "Set to \\"1\\" if the record selected came from a merchandising result."
row_cells = table.add_row().cells
row_cells[0].text = "IN_DYM"
row_cells[1].text = "Set to \\"1\\" if the user clicked on a Did You Mean."
row_cells = table.add_row().cells
row_cells[0].text = "IN_DIM_SEARCH"
row_cells[1].text = "Set to \\"1\\" if the user clicked on a dimension search result."
row_cells = table.add_row().cells
row_cells[0].text = "PAGE_TIME"
row_cells[1].text = "Record the page render time in milliseconds.  Requires that the start time be recorded when the page begins loading."
row_cells = table.add_row().cells
row_cells[0].text = "ENE_TIME"
row_cells[1].text = "Record the ENE query time in milliseconds.  Requires that the start time be recorded before the Endeca query is called."
row_cells = table.add_row().cells
row_cells[0].text = ""
row_cells[1].text = ""

document.add_heading("Software Setup and Initial Configuration", 1)
p = document.add_paragraph("")
p.add_run("\\n\\nThis section provides the details on the physical infrastructure of the implementation, including the initial software setup and configuration of the application.\\n\\n")

p.add_run("Physical Environments").bold = True
p.add_run("\\nThe PBS implementation encompasses the server environments below.  Please refer to section 17.7: \\"Migration of Configuration Files between Environments\\" for details on migration of the Endeca configuration between environments.\\n\\nOverall design of the cluster will be the same for the Dev, Test and Production environments. The diagram below illustrates the overall design, and the installed Endeca software on each server.\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/environments.png", width=Inches(2.25))

p = document.add_paragraph("")
p.add_run("\\nData is exported from ATG through CAS to the Indexer. The index is built during the baseline process and is deployed out to the MDEX servers via EAC. Each MDEX server hosts one instance of the Live dgraph and only one server hosts the Authoring dgraph. All workbench changes are immediately deployed to Authoring, and are promoted to Live via the promote_content.bat script in the control directory. \\n\\n")

p.add_run("Development Environment\\n").bold = True
p.add_run("\\nThe dev environment is a single server environment providing the Data Foundry services, and MDEX Engine to serve query requests to the web/application servers in the PBS dev environment, the Endeca Workbench, and Logging / Report Generator server.  The server hostname is Endeca-DEV-01.\\n\\n")
document.add_paragraph(
    'Endeca-DEV-01', style='ListBullet'
)
p.add_run("\\n\\nTest Environment\\n").bold = True
p.add_run("The test environment is a single server environment providing the Data Foundry services, and MDEX Engine to serve query requests to the web/application servers in the PBS test environment, the Endeca Workbench, and Logging / Report Generator server.  The server hostname is Endeca-TEST-01.\\n")
document.add_paragraph(
    'Endeca-TEST-01', style='ListBullet'
)

p.add_run("\\n\\nProduction Environment\\n").bold = True
p.add_run("The production environment is a single (3) server environment providing the Data Foundry services, and MDEX Engine to serve query requests to the web/application servers in the PBS test environment, the Endeca Workbench, and Logging / Report Generator server.   The indexing server hostname is ENDECA-PROD-01.HQ.CORP.PBS.ORG.\\n\\n")
document.add_paragraph(
    'ENDECA-PROD-01.HQ.CORP.PBS.ORG', style='ListBullet'
)
document.add_paragraph(
    'ENDECA-PROD-02.HQ.CORP.PBS.ORG', style='ListBullet'
)
document.add_paragraph(
    'ENDECA-PROD-03.HQ.CORP.PBS.ORG', style='ListBullet'
)

p.add_run("\\n\\nSoftware Installation\\n").bold = True
p.add_run("Thanx Media performed the installation of the Endeca software on all servers under the E: partition.  The default installation directory for all environments will be:\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Directory"
row_cells = table.add_row().cells
row_cells[0].text = "E:/Endeca/"

p = document.add_paragraph("")
p.add_run("\\nPlease refer to the Endeca Installation Guide for details on installation of the Endeca software.\\n\\n")
p.add_run("Users and Permissions\\n").bold = True
p.add_run("Most of the Endeca software should be installed and all Endeca processes run as the \\"Administrator\\" user or equivalent. There may be permission issues during baseline updates if files are owned by different users.\\n\\nEach of the PBS servers running an Endeca process have user accounts created for the Thanx Media implementation team to provide access to all machines in all the Endeca environments.  Upon logging into that server, the Thanx Media users should have the same rights as the \\"Administrator\\" user to perform implementation related tasks.\\n\\nThe Thanx Media team has been given the \\"sys-endeca\\" user account with Administrator rights.\\n\\n")

p.add_run("Application Installation and Directory Structure\\n").bold = True
p.add_run("Each PBS application consists of all configuration XML and supporting documents, custom Control Scripts (defined below), shell scripts and, following data updates, MDEX index files and necessary directory structure to perform all implementation-specific tasks including data forge/indexing, MDEX Engine query responses, logging and report generation. \\n\\nThe PBS application will be deployed by Thanx to the following directory:\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Directory"
row_cells = table.add_row().cells
row_cells[0].text = "E:/Endeca/apps/pbs/"

p = document.add_paragraph("")
p.add_run("\\n\\nThe Endeca Deployment Template is a collection of operational components that provides a starting point for development and application deployment.  This template includes the complete directory structure required for deployment, including EAC scripts, configuration files, and batch files or shell scripts that wrap common script functionality.\\n\\nThe current Endeca Deployment Template is version PCI 3.1.1 and will be used for the PBS applications.\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Deployment Script Location"
row_cells = table.add_row().cells
row_cells[0].text = "E:/Endeca/ToolsAndFrameworks/3.1.1/deployment_template/bin/"

p = document.add_paragraph("")
p.add_run("\\n\\nFrom the execution of the Endeca Deployment template's deploy.bat script, the full directory structure used by the application on the primary server is: \\n\\n")

p.add_run("Workbench servers:\\n").bold = True
p.add_run("The default installation of the Endeca IAP software provides the necessary directory structure to power Workbench.  No additional directory structure required.\\n\\n")
p.add_run("Required Ports\\n").bold = True
p.add_run("The following TCP ports are required for ALL Endeca servers in ALL environments. The ports are non-standard and will not follow the Endeca default ports. Ports must be entered during installation of Platform Services, ToolsAndFrameworks (noted below) and during the application deployment. \\n")

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Port"
hdr_cells[1].text = "Process"
hdr_cells[2].text = "Purpose"
row_cells = table.add_row().cells
row_cells[0].text = "8888"
row_cells[1].text = "EAC Http Service"
row_cells[2].text = "Platform Services and EAC Port"
row_cells = table.add_row().cells
row_cells[0].text = "62911"
row_cells[1].text = "EAC Shutdown"
row_cells[2].text = "Port for EAC Shutdown"
row_cells = table.add_row().cells
row_cells[0].text = "62912"
row_cells[1].text = "EAC JCD"
row_cells[2].text = "EAC JCD Port"
row_cells = table.add_row().cells
row_cells[0].text = "8006"
row_cells[1].text = "Workbench "
row_cells[2].text = "Access Workbench Application"
row_cells = table.add_row().cells
row_cells[0].text = "8007"
row_cells[1].text = "Workbench Promotion"
row_cells[2].text = "Port used for promoting authoring to live"
row_cells = table.add_row().cells
row_cells[0].text = "62915"
row_cells[1].text = "CAS"
row_cells[2].text = "CAS Server Port"
row_cells = table.add_row().cells
row_cells[0].text = "62916"
row_cells[1].text = "CAS Shutdown"
row_cells[2].text = "Port for CAS Shutdown"
row_cells = table.add_row().cells
row_cells[0].text = "8446"
row_cells[1].text = "Workbench Redirect"
row_cells[2].text = "Port for Workbench Redirect"
row_cells = table.add_row().cells
row_cells[0].text = "16010"
row_cells[1].text = "Logserver"
row_cells[2].text = "Set port for logserver, logserver currently disabled, will need to be set below 32000 for operation. "
row_cells = table.add_row().cells
row_cells[0].text = "16000"
row_cells[1].text = "Live"
row_cells[2].text = "Live MDEX Port"
row_cells = table.add_row().cells
row_cells[0].text = "16002"
row_cells[1].text = "Authoring"
row_cells[2].text = "Authoring MDEX Port"
row_cells = table.add_row().cells
row_cells[0].text = "8084"
row_cells[1].text = "Workbench Shutdown"
row_cells[2].text = "Port for Workbench Shutdown"

p = document.add_paragraph("")
p.add_run("\\nWorkbench Port Configuration\\n").bold = True
p.add_run("Port configuration for Platform Services and the application are set through the install and deployment template, respectively. Port setting for the Workbench must be manually configured in the ToolsAndFrameworks conf directory. \\n\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Directory"
row_cells = table.add_row().cells
row_cells[0].text = "E:/Endeca/ToolsAndFrameworks/3.1.1/server/workspace/conf/"

p = document.add_paragraph("")
p.add_run("\\n\\nWithin the above directory, modify the webstudio and webstudio promotion ports in the webstudio.properties file as seen below:\\n\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/webstudioprops.png", width=Inches(3.25))

p = document.add_paragraph("")
p.add_run("\\n\\nAdditionally, within the server.xml file modify the SHUTDOWN port, and Connector ports. Connector port is the Webstudio port.\\n")


document.add_picture("C:/Daniel/techSpectoDoc/template/shutdownport.png", width=Inches(3.25))
document.add_picture("C:/Daniel/techSpectoDoc/template/connectorport.png", width=Inches(3.25))

p = document.add_paragraph("")
p.add_run("\\nA restart of the workbench is required after the following changes are made. \\n\\n")
p.add_run("Between-Environment Communication\\n").bold = True
p.add_run("Apart from the PBS developed process for migrating configurations between environments and transfer of source data extracts, there should be no necessity for communication between servers in separate environments. \\n\\nThe sole exception is if PBS wishes that the thesaurus and merchandising rule modifications made by business users on the Production Workbench server to be propagated to the TST or SIT environments.  If this is desired, an export of the site configuration can be created by executing the following script:\\n\\nE:/Endeca/apps/pbs/control/export_site.bat\\n\\nThis will create an XML file with all Workbench settings. This file can then be moved to the new environment and imported using the following script:\\n\\nE:/Endeca/apps/pbs/control/import_site.bat $filename --force\\n\\n")


p.add_run("Application Infrastructure Setup\\n").bold = True
p.add_run("This section details the configuration necessary for the web application. The production web application will be referred to as PBS.\\n\\nAt this point, the deployment template process should have been executed to create the application directory structure.  The components and processes defined in this section are described further in section 17: \\"System Components and Operations.\\"\\n\\nThe AppConfig.xml, LiveDgraphCluster.xml , and environment.properties file was modified in order to properly provision the authoring and live web applications.  Please refer to page 9 of the Deployment Template Usage Guide and the EAC Development Toolkit Usage Guide for additional details.\\n\\nIn order to properly partition and manage multiple components, it is important to configure each component to use specific ports and directories.\\n\\n")
p.add_run("Global variables\\n").bold = True
p.add_run("This section should require a few changes.  Ensure that the eac_hostname, eac_port variables has the correct value for the EAC Central Server, and add Authoring and Live MDEX host and ports. Configuration for TST environment listed below\\n\\n")

p.add_run("Environment.properties:\\n\\n").underline = True
p.add_run("EAC_PORT=8888\\nEAC_HOSTNAME=ENDECA-PROD-01\\n\\n#Dgraph settings\\nLiveMDEXHost PORT=16000\\nLiveMDEXHostA HOSTNAME= ENDECA-PROD-02\\nLiveMDEXHostB HOSTNAME= 10.168.44.28\\nLiveMDEXHostC HOSTNAME= 10.168.44.26\\n\\nAuthoringMDEXHost PORT=16002\\nAuthoringMDEXHost HOSTNAME= 10.168.44.26\\n\\n")
p.add_run("AppConfig.xml:\\n\\n").underline = True
#ADD PIC

p.add_run("Servers/Hosts\\n").bold = True
p.add_run("In order to manage the application across different environments, we will define host references to represent each server's role.\\n\\n\\"hostName\\" should represent a host or reachable IP address of the EAC agent.\\n\\nITLHost will contain the Forge and Dgidx components for the nightly process.\\n\\nDgraphA1[LiveMDEXHostA] will contain the primary Dgraph component.\\n\\nDgraphB1[LiveMDEXHostB] will contain the secondary Dgraph component.\\n\\nDgraphC1[LiveMDEXHostC] will contain the last Dgraph component.\\n\\nAuthoringDgraph will contain the authoring Dgraph component\\n\\nwebstudio will contain the Endeca Workbench component.\\n\\n")
p.add_run("Forge and Dgidx component\\n").bold = True
p.add_run("The Forge and Dgidx components for the Staging and Production applications were not altered. Configuration for these components are found in the DataIngest.xml\\n\\n")
p.add_run("Authroing Dgraph cluster component\\n").bold = True
p.add_run("Define a Dgraph cluster component that will be used in the authoring application.  Note that the id is unique in the file, and the reference is to the staging Dgraph component.\\n\\n")
p.add_run("AuthoringDgraphCluster.xml:\\n\\n").underline = True
#ADD PIC
p.add_run("Production Dgraph cluster component\\n").bold = True
p.add_run("Define a Dgraph cluster component that will be used in the production application.  Note that the id is unique in the file, and the references are to the production Dgraph components.\\n\\n")
p.add_run("AuthoringDgraphCluster.xml:\\n\\n").underline = True
#ADD PIC
p.add_run("Authoring Dgraph component\\n").bold = True
p.add_run("Define the Dgraph component that will be used in staging.  Note that the ids are unique in the file, and the host-id value is to the staging MDEXHost reference.\\n\\n")
#ADD PIC
p.add_run("Production Dgraph components\\n").bold = True
p.add_run("Define a Dgraph cluster component that will be used in the production application.  Note that the id is unique in the file, and the references are to the production Dgraph components.\\n\\n")
p.add_run("LiveDgraphCluster.xml: \\n\\n").underline = True
#ADD PIC
p.add_run("Authoring Dgraph component\\n").bold = True
p.add_run("Define the Dgraph component that will be used in staging.  Note that the ids are unique in the file, and the host-id value is to the staging MDEXHost reference.\\n\\n")
#ADD PIC
p.add_run("Production Dgraph components\\n").bold = True
p.add_run("Define the Dgraph components that will be used in production.  Note that the ids are unique in the file, and the host-id values are to the production MDEXHost, MDEXHost2 references.  In this setup it is acceptable to use the same port values since they will be on different physical machines.\\n\\n")
#ADD PIC
p.add_run("Baseline Update script for Production\\n").bold = True
p.add_run("Define the Baseline Update script that will be used for the nightly process. This script is found in the DataIngest.xml. \\n\\n")
#ADD PIC
p.add_run("ADD CUSTOM SCRIPTS HERE\\n").bold = True
p.add_run("CUSTOM SCRIPTS\\n\\n")
p.add_run("Application Provisioning\\n").bold = True
p.add_run("In order to provision the application you may use the ./control/initialize_services.bat script.  The AppConfig.xml file must be available in the ./config/script directory.\\n\\n")
p.add_run("Assembler API Configuration\\n").bold = True
p.add_run("First, edit the assembler.properties file located in at:\\n")
p.add_run("E:/Endeca/ToolsAndFrameworks/3.1.1/reference/pbs-service/WEB-INF/assembler.properties. All variables will need to be updated to match the configuration as noted in the above sections. For mdex host and port, please reference the load balancer port and host if configured. \\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/assembler.png", width=Inches(3.25))
p = document.add_paragraph("")
p.add_run("Next, to enable Web-service calls, if needed, we will update the assembler-context.xml file located in the same directory. First comment out the rollupKey property located in the navigationStateBuilder block:\\n\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/assemblercontext.png", width=Inches(3.25))
p = document.add_paragraph("")
p.add_run("Then, note the record spec (common.id) in the mdexResource block:\\n\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/mdexresource.png", width=Inches(3.25))
p = document.add_paragraph("")
p.add_run("Next, if needed, you can limit the properties returned in the ResultsList cartridge by adding or modifying the property names here:\\n\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/resultlist.png", width=Inches(3.25))
p = document.add_paragraph("")
p.add_run("When all of the values are commented out, all properties will return.\\n\\nFinally, add the service context file by creating a file called docen.xml in the E:/Endeca/ToolsAndFrameworks/3.1.1/erver/workspace/conf/Standalone/localhost directory. The file will contain the path from the url and the service path location as seen below: \\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/serverxml.png", width=Inches(3.25))
p = document.add_paragraph("")
p.add_run("Once setup, restart the Tools service, and verify you are receiving back xml/json from the following URLS:\\nhttp://10.168.44.26:8006/pbs-service/json/services/guidedsearch\\nhttp://10.168.44.26:8006/pbs-service/xml/services/guidedsearch\\n\\n")

document.add_heading("System Components and Operations", 1)
        
p = document.add_paragraph("")
p.add_run("\\n\\nThis section provides the details on the vital components and processes of the implementation. \\n\\n")
p.add_run("MDEX Engine Servers\\n").bold = True
p.add_run("The heart of the Endeca implementation is the MDEX Engine.  The MDEX Engine is the online process that responds to requests from PBS (via the Endeca API) by delivering guided navigation objects, keyword search results, refinement options, merchandising results, and other supporting information.  This response is interpreted by the PBS site, again through the Endeca API, for display of search results, refinement navigation elements and merchandising results.\\n\\nThe MDEX Engine can be expected to provide 25 operations per second.  PBS has two instances of the MDEX Engine spread out across two servers dedicated to serving search and navigation requests from the PBS servers.  The use of an HTTP load balancer to manage traffic between the web application servers and the MDEX Engine farm is recommended.\\n\\nNote: Since Endeca is installed on a shared server with other Endeca resources, performance testing should also take into account other application server load. \\n\\n")
p.add_run("Load Balancing MDEX Requests\\n").bold = True
p.add_run("An Endeca-based application relies upon the availability of an MDEX Engine to service user requests.  If that MDEX Engine should be unavailable, then the Endeca portion of the application will be unable to respond to queries.  The MDEX Engine might be unavailable or appear to be unavailable for any number of reasons, including hardware failure, an in-process update of the MDEX Engine's indices, or, in extreme cases, very high load on a given MDEX Engine.  In addition, this deployment entails two instances of the MDEX Engine spread out over two servers.  For these reasons, an HTTP load balancer is strongly recommended to manage traffic to the multiple Navigation Engines and to manage instances when an MDEX Engine is unavailable to serve requests.\\n\\nThe MDEX Engine functions very similarly to a web server in terms of network traffic.  It simply accepts HTTP requests on a specified port, and returns results to the caller.  This behavior allows for standard web load balancing techniques to be applied.\\n\\nPorts should be dedicated to communication between the load balancer and each MDEX Engine instance on each MDEX server.\\n\\nPBS has advised that there will be two instances for each product and content engine. \\n\\n")
p.add_run("Health Checks \\n").bold = True
p.add_run("Load balancers are also typically able to perform \\"health\\" status checks on the various MDEX Engine processes, by either making an HTTP request to the MDEX Engine's TCP port or by opening a connection to that port to ensure that the MDEX Engine is listening and alive.  The MDEX Engine's admin request is often used for this query (i.e., http://dgraphhost:16000/admin?op=ping).\\n\\nUpon failure of a health status check, the load balancer should be able to mark the port (process) as unavailable and remove it from the set of ports that it is directing load to (and preferably be able to alert on error - via a mechanism such as an SNMP trap).  Most load balancers will also support the ability to periodically attempt to recheck a port marked as unavailable to see if it is once again available.\\n\\n")
p.add_run("Backup Load Balancer\\n").bold = True
p.add_run("Endeca typically recommends implementing two hardware switches configured redundantly (either by network design or some other method).  This will ensure that the load balancer is not a single point of failure as well.\\n\\n")
p.add_run("Endeca Application Controller\\n").bold = True
p.add_run("The Endeca Application Controller (EAC) is the mechanism for performing data forging and indexing, index file distribution, data archiving, report generation, and other Endeca-related tasks in the production environment.  The EAC is comprised of two components: the Central Server and Agents.  The EAC provides your Endeca implementation with a reliable process execution and lightweight job management.\\n\\n")
p.add_run("Control Scripts\\n").bold = True
p.add_run("Control scripts are used to perform various tasks with an Endeca implementation.\\n\\nThese scripts are included with the Endeca Deployment Template after the bin/deploy.bat is run.\\n\\n")
p.add_run("Script Execution\\n").bold = True
p.add_run("Scheduled jobs are created on the primary Data Foundry server to initiate particular tasks according to the schedule below.  All the necessary tasks are captured in one script:\\n\\n")

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Script Name"
hdr_cells[1].text = "Function"
hdr_cells[2].text = "Schedule"
row_cells = table.add_row().cells
row_cells[0].text = "PBS Baseline Update"
row_cells[1].text = "Performs a full data update."
row_cells[2].text = "10:00PM on Saturday"
row_cells = table.add_row().cells
row_cells[0].text = "PBS Partial Updates"
row_cells[1].text = "Runs the partial update process."
row_cells[2].text = "9:30AM,11:30AM,1:30PM,3:30PM Daily"
row_cells = table.add_row().cells
row_cells[0].text = "PBS Thesaurus Update"
row_cells[1].text = "Updates the thesaurus.xml file"
row_cells[2].text = "11:00AM on Saturday"


p = document.add_paragraph("")
p.add_run("\\nAll scripts (including those referenced within the main script) reside in the following \\"control\\" directories on the Data Foundry server:\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Directory"
row_cells = table.add_row().cells
row_cells[0].text = "E:/Endeca/apps/pbs/control"

p = document.add_paragraph("")
p.add_run("Data Extracts\\n").bold = True
p.add_run("It is <CLIENT>'s responsibility to develop the process for producing the data extract used to populate the CAS record stores. \\n\\nRecord store data will reside in the following directories:\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Directory"
row_cells = table.add_row().cells
row_cells[0].text = "/lcl/$ENV/apps/edoc/endeca/CAS/workspace/state/DOCen_en_data"
row_cells = table.add_row().cells
row_cells[0].text = "/lcl/$ENV/apps/edoc/endeca/CAS/workspace/state/DOCen_en_dimvals"
row_cells = table.add_row().cells
row_cells[0].text = "/lcl/$ENV/apps/edoc/endeca/CAS/workspace/state/DOCen_en_prules"
row_cells = table.add_row().cells
row_cells[0].text = "/lcl/$ENV/apps/edoc/endeca/CAS/workspace/state/DOCen_en_schema"

p = document.add_paragraph("")
p.add_run("Data Updates\\n").bold = True
p.add_run("The PBS implementation will entail one type of update, the Baseline Update.  It is important to note all Data Update processes are fully automated and are initiated by the execution of the script described above. \\n\\n")
p.add_run("Baseline Update\\n").bold = True
p.add_run("A Baseline Update, or full data update, transforms all data in the provided extract files into Endeca index files for use by the MDEX Engine.\\n\\nIndex files from the previously run are not incorporated into the current update.  Therefore, the data extract files MUST include all PBS product and SKU data that is to be available for search queries.\\n\\nThe raw source data is transformed through an offline process called Forge.  The Forge process readies the source data for use by the Index process and produces a set of binary and supporting XML files.\\n\\nThe Index process then takes over and transforms the Forge output into binary index files for use by each instance of the MDEX Engine.  The integrity of the index files are tested by starting an instance of the MDEX Engine on the Data Foundry server.  Upon successful startup, the index files are then migrated to each instance of the MDEX Engine on all MDEX servers, as well as the MDEX Engine that serves Workbench requests on the Workbench server.  The migration process is described below.\\n\\n")
p.add_run("Index File Migration (Baseline Update)\\n").bold = True
p.add_run("The MDEX Engine derives its data from a collection of binary index files and supporting XML and other files.  These files are produced during the Data Update processes described above and copied from the Data Foundry server to each instance of the MDEX Engine.\\n\\nIt is assumed that firewalls or other restrictions will not prevent MDEX and Data Foundry servers in production from communicating with each other, nor prevent file transfer between production Endeca servers.\\n\\nThe following describes, step-by-step, the Index File Migration process for a MDEX Update:\\n\\n")
document.add_paragraph(
    'The Index files are transferred from the Data Foundry server into temporary directories created for each instance of the MDEX Engine on all MDEX Engine servers, as well as a backup directory on each server.  The backup directory is created so that during the subsequent Baseline Update, this set of Index files is available should difficulties during the migration process necessitate a rollback to the last valid Index.', style='ListNumber'
)
document.add_paragraph(
    'One by one, a command is issued to the MDEX Engine process to shutdown.  It is important to note that all requests currently in queue for that Engine after the command has been issued are served before the actual shutdown of the process occurs.', style='ListNumber'
)
document.add_paragraph(
    'The existing MDEX Engine data directory is deleted and the temporary directory data directory is renamed to serve as the current data directory.', style='ListNumber'
)
document.add_paragraph(
    'The MDEX request logs are then archived.', style='ListNumber'
)
document.add_paragraph(
    'The MDEX Engine is then started and is ready to serve requests.', style='ListNumber'
)
document.add_paragraph(
    'Steps 2-5 are repeated for each MDEX Engine.  The end result is minimal downtime for the MDEX Engine being updated while keeping a significant number of MDEX Engines online to continue to serve requests.', style='ListNumber'
)

p.add_run("\\n\\nWorkbench and Configuration Migration\\n").bold = True
p.add_run("The Endeca Workbench is a business tool allowing PBS personnel to make updates to merchandising business rules, thesaurus entries and other limited aspects of the MDEX configuration without the necessity for technical or development skills.\\n\\nThe Workbench operates within its own environment with its own instance of the MDEX Engine.  To ensure that business users are performing tasks on the current index and that their modifications to MDEX configurations are incorporated into production indices, the Baseline Update process must touch the Workbench environment.\\n\\n")
p.add_run("Incorporating Workbench Configuration Changes into Full Updates\\n").bold = True
p.add_run("After the Baseline Forge process, created dimensions and values are uploaded to the Workbench repository by performing the following functions:\\n")
document.add_paragraph(
    'After baseline is completed, cleans Workbench input directories.', style='ListNumber'
)
document.add_paragraph(
    'Copies the XML configuration files from the Workbench server to the DataFoundry server.', style='ListNumber'
)
document.add_paragraph(
    'Runs updateWsConfig to integrate changes into the repository. ', style='ListNumber'
)

p.add_run("\\n\\nLogging & Report Generation\\n").bold = True
p.add_run("The Logging server performs the task of receiving HTTP requests from the web application via the Endeca API and producing log entries for use by the Report Generator process to produce daily and weekly Endeca usage reports.  These reports are viewed via the Endeca Workbench.\\n\\nLog files are rolled on a nightly basis to maintain a reasonable log file size.  This process will occur at the completion of each nightly Baseline Update.\\n\\n")
p.add_run("Development Environment\\n").bold = True
p.add_run("Application Development will occur in the development environment and deployed directly to that environment.\\n\\nDevelopment occurs with the Developer Studio tool which should be installed on each developer's computer.  To facilitate ease of development, we recommended using PBS's current version control software (e.g. Visual SourceSafe, Subversion).\\n\\n")
p.add_run("Migration from Authoring Dgraph to Production Dgraphs\\n").bold = True
p.add_run("Within each environment, the Authoring environment serves as the staging area for changes to the Workbench. When workbench changes (such as redirects, thesaurus, and rule manager) are ready for promotion to the live environment, the following script can be executed from command line:\\n\\n")

table = document.add_table(rows=1, cols=1)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Directory"
row_cells = table.add_row().cells
row_cells[0].text = "E:/Endeca/apps/pbs/control/promote_content.bat"

p = document.add_paragraph("")
p.add_run("Or from within the Workbench admin console:\\n")

document.add_picture("C:/Daniel/techSpectoDoc/template/workbenchadmin.png", width=Inches(3.25))
''')

endPython("templateBase.py")
#################################################################################################
#####################################Create MS Word Doc##########################################
os.system('templateBase.py')
