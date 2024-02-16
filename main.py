from saxoncee import PySaxonProcessor

with PySaxonProcessor(license=True) as saxon_proc:
    print(saxon_proc.version)

    doc_builder = saxon_proc.new_document_builder()
    doc_builder.set_line_numbering(True)

    xdm_doc = doc_builder.parse_xml(xml_file_name='sample1.xml')

    xpath_processor = saxon_proc.new_xpath_processor()

    xpath_processor.set_context(xdm_item=xdm_doc)

    xpath_processor.declare_namespace('saxon', 'http://saxon.sf.net/')

    items = xpath_processor.evaluate('//item')

    for item in items:
        xpath_processor.set_context(xdm_item=item)
        print(item, xpath_processor.evaluate('saxon:line-number(.), saxon:column-number(.)'))