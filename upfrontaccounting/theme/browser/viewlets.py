from zope.component import getUtility

from zope.app.publisher.interfaces.browser import IBrowserMenu

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.common import SearchBoxViewlet as \
    SearchBoxViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet as \
    GlobalSectionsViewletBase
from plone.app.layout.viewlets.common import SiteActionsViewlet as \
    SiteActionsViewletBase
from plone.app.contentmenu.menu import FactoriesSubMenuItem

class SearchBoxViewlet(SearchBoxViewletBase):
    index = ViewPageTemplateFile('searchbox.pt')

class GlobalSectionsViewlet(GlobalSectionsViewletBase):
    index = ViewPageTemplateFile('sections.pt')

class SiteActionsViewlet(SiteActionsViewletBase):
    index = ViewPageTemplateFile('site_actions.pt')

class FolderFactoriesMenu(ViewletBase):
    """ A viewlet that only shows the folder factories menu and not the
        whole content menu.
    """
    index = ViewPageTemplateFile('contentmenu.pt')

    def available(self):
        return True

    def menu(self):
        menu = FactoriesSubMenuItem(self.context, self.request)
        submenu = getUtility(IBrowserMenu, name='plone_contentmenu_factory')
        items = submenu.getMenuItems(self.context, self.request)
        items.reverse()
        result = [
            {'action': menu.action,
             'extra': menu.extra,
             'icon': False,
             'description': menu.description,
             'selected': menu.selected,
             'submenu': items,
             'title': menu.title}
        ]
        return result
