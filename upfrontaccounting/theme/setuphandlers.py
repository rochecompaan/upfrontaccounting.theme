from Products.CMFCore.utils import getToolByName

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('upfrontaccounting.theme_various.txt') is None:
        return

    # Add additional setup code here

    site = context.getSite()
    for id in ('Members', 'news', 'events', 'front-page'):
        if id in site.objectIds():
            site.manage_delObjects(ids=id)

    fc = getToolByName(site, 'portal_form_controller')
    # redirect to parent after editing for the content types below
    for type_name in ('Ledger', 'CustomerLedger', 'SupplierLedger',
        'CashBook'):
        fc.addFormAction('validate_integrity', 'success',
            type_name, None, 'redirect_to', 'string:../view')
