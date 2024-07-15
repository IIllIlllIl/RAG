class MultiResolverMatch(object):
    def __init__(self, matches, exceptions, patterns_matched, path, route='', tried=None):
        self.matches = matches
        self.exceptions = exceptions
        self.patterns_matched = patterns_matched
        self.path = path
        self.route = route
        self.tried = tried

        # Attributes to emulate ResolverMatch
        self.kwargs = {}
        self.args = ()
        self.url_name = None
        self.app_names = []
        self.app_name = None
        self.namespaces = []

    @property
    def func(self):
        def multiview(request):
            for i, match in enumerate(self.matches):
                try:
                    return match.func(request, *match.args, **match.kwargs)
                except self.exceptions:
                    continue
            raise urlresolvers.Resolver404({'tried': self.patterns_matched, 'path': self.path})
        multiview.multi_resolver_match = self
        return multiview
