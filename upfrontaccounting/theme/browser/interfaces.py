from zope.viewlet.interfaces import IViewletManager
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IPathBar(IViewletManager):
    """A viewlet manager that renders the path bar
    """

